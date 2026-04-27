#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reference audit for LaTeX + BibTeX projects.

Goals:
- Verify that every cited key exists in the .bib file
- List where each key is cited (file/line + surrounding context)
- Try to resolve each reference to an external identifier/link (DOI/URL/arXiv)
- Optionally validate existence via Crossref/URL reachability

This script intentionally avoids third‑party dependencies.

Usage (from repo root):
  python tools/reference_audit.py --output reference_verification_report.md

Network:
- Uses Crossref REST API where possible.
- Uses plain URL reachability checks (GET) with short timeouts.
"""

from __future__ import annotations

import argparse
import dataclasses
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


@dataclass
class BibEntry:
    entry_type: str
    key: str
    fields: Dict[str, str]
    raw: str


@dataclass
class CiteOccurrence:
    tex_path: Path
    line_no: int  # 1-based
    command: str
    keys: List[str]
    line_text: str
    context: str


@dataclass
class VerificationResult:
    # High-level
    status: str  # ok | maybe | fail | skipped
    summary: str

    # Links
    doi: Optional[str] = None
    doi_url: Optional[str] = None
    url: Optional[str] = None
    url_source: Optional[str] = None  # bib | heuristic
    arxiv_id: Optional[str] = None
    arxiv_url: Optional[str] = None
    arxiv_source: Optional[str] = None  # bib | api

    # Crossref matching
    crossref_matched: bool = False
    crossref_score: Optional[float] = None
    crossref_doi: Optional[str] = None
    crossref_url: Optional[str] = None
    crossref_title: Optional[str] = None
    crossref_year: Optional[int] = None

    # Reachability
    url_http_status: Optional[int] = None
    doi_crossref_http_status: Optional[int] = None
    arxiv_http_status: Optional[int] = None

    # Diagnostics
    error: Optional[str] = None


ARXIV_ID_RE = re.compile(r"(?:arXiv\s*:\s*|arXiv\s+preprint\s+arXiv\s*:\s*)(?P<id>\d{4}\.\d{4,5})(?:v\d+)?", re.积分梯度归因NORECASE)
ARXIV_ID_SIMPLE_RE = re.compile(r"\b(?P<id>\d{4}\.\d{4,5})(?:v\d+)?\b")

CITE_CMD_RE = re.compile(
    r"\\(?P<cmd>[A-Za-z]*cite[A-Za-z]*|upcite|nocite)"  # command
    r"\s*(?:\[[^\]]*\]\s*)*"  # optional args (0..n)
    r"\{(?P<keys>[^}]*)\}",  # keys
)

# Matching thresholds
CROSSREF_OK_SCORE = 0.84
CROSSREF_MAYBE_SCORE = 0.75
ARXIV_OK_SCORE = 0.88


def strip_tex_comment(line: str) -> str:
    r"""Remove TeX comments (%) while preserving escaped \%."""
    out_chars: List[str] = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "%":
            # if escaped with backslash, keep it
            if i > 0 and line[i - 1] == "\\":
                out_chars.append(ch)
                i += 1
                continue
            break
        out_chars.append(ch)
        i += 1
    return "".join(out_chars)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_title(text: str) -> str:
    # remove math, braces, and common LaTeX escapes
    text = re.sub(r"\$[^$]*\$", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    text = text.replace("\\&", " and ")
    text = re.sub(r"\\[A-Za-z]+\s*", " ", text)  # commands
    text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    return normalize_whitespace(text.lower())


def normalize_container(text: str) -> str:
    text = re.sub(r"\$[^$]*\$", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\\[A-Za-z]+\s*", " ", text)
    text = re.sub(r"[^A-Za-z0-9]+", " ", text)
    return normalize_whitespace(text.lower())


def fold_to_ascii(text: str) -> str:
    if not text:
        return ""
    return "".join(
        ch for ch in unicodedata.normalize("NFKD", text) if not unicodedata.combining(ch)
    )


def normalize_name_token(text: str) -> str:
    # Make author matching robust across BibTeX LaTeX escapes and Unicode (e.g., Müller).
    text = fold_to_ascii(text)
    normalized = normalize_title(text)
    return normalized.replace(" ", "")


def get_bib_year(entry: BibEntry) -> Optional[int]:
    try:
        y = int((entry.fields.get("year") or "").strip())
        return y
    except Exception:
        return None


def get_bib_container(entry: BibEntry) -> Optional[str]:
    # Prefer journal if present; else booktitle.
    journal = (entry.fields.get("journal") or "").strip()
    booktitle = (entry.fields.get("booktitle") or "").strip()
    if journal and "arxiv" not in journal.lower():
        return journal
    if booktitle:
        return booktitle
    return None


def looks_like_preprint_venue(entry: BibEntry) -> bool:
    journal = (entry.fields.get("journal") or "").lower()
    booktitle = (entry.fields.get("booktitle") or "").lower()
    if "arxiv" in journal:
        return True
    # Common venues that frequently have arXiv versions and may lack DOI.
    if "iclr" in booktitle or "learning representations" in booktitle:
        return True
    if "neurips" in booktitle or "neural information processing systems" in booktitle:
        return True
    if "icml" in booktitle or "machine learning" in booktitle:
        return True
    return False


def looks_like_openreview_venue(entry: BibEntry) -> bool:
    """Heuristic for venues commonly hosted on OpenReview (e.g., ICLR)."""
    journal = (entry.fields.get("journal") or "").lower()
    booktitle = (entry.fields.get("booktitle") or "").lower()
    if "openreview" in journal or "openreview" in booktitle:
        return True
    if "iclr" in booktitle or "learning representations" in booktitle:
        return True
    return False


def looks_like_neurips_venue(entry: BibEntry) -> bool:
    booktitle = (entry.fields.get("booktitle") or "").lower()
    return ("neurips" in booktitle) or ("nips" in booktitle) or ("neural information processing systems" in booktitle)


def parse_bibtex(path: Path) -> Dict[str, BibEntry]:
    text = path.read_text(encoding="utf-8")
    entries: Dict[str, BibEntry] = {}

    i = 0
    n = len(text)

    def skip_ws(idx: int) -> int:
        while idx < n and text[idx].isspace():
            idx += 1
        return idx

    while True:
        at = text.find("@", i)
        if at == -1:
            break
        i = at + 1
        i = skip_ws(i)

        # entry type
        m = re.match(r"[A-Za-z]+", text[i:])
        if not m:
            continue
        entry_type = m.group(0).lower()
        i += len(m.group(0))
        i = skip_ws(i)
        if i >= n or text[i] not in "{(":
            continue
        open_delim = text[i]
        close_delim = "}" if open_delim == "{" else ")"
        i += 1

        # key
        i = skip_ws(i)
        key_start = i
        while i < n and text[i] not in ",\n\r":
            i += 1
        key = text[key_start:i].strip()
        if not key:
            continue

        # move past comma
        comma = text.find(",", i)
        if comma == -1:
            continue
        i = comma + 1

        # parse until close_delim at depth 0
        fields: Dict[str, str] = {}
        raw_start = at
        depth = 1
        body_start = i
        while i < n and depth > 0:
            ch = text[i]
            if ch == open_delim:
                depth += 1
            elif ch == close_delim:
                depth -= 1
            i += 1
        raw_end = i
        raw_block = text[raw_start:raw_end]
        body = text[body_start:raw_end - 1]  # exclude closing delim

        # field parsing within body
        j = 0
        bn = len(body)

        def body_skip(idx: int) -> int:
            while idx < bn and body[idx].isspace():
                idx += 1
            return idx

        while j < bn:
            j = body_skip(j)
            # consume leading commas
            while j < bn and body[j] == ",":
                j += 1
                j = body_skip(j)
            if j >= bn:
                break

            # field name
            name_match = re.match(r"[A-Za-z][A-Za-z0-9_-]*", body[j:])
            if not name_match:
                break
            field_name = name_match.group(0).lower()
            j += len(name_match.group(0))
            j = body_skip(j)
            if j >= bn or body[j] != "=":
                break
            j += 1
            j = body_skip(j)
            if j >= bn:
                break

            # value
            if body[j] == "{":
                depth2 = 1
                j += 1
                val_start = j
                while j < bn and depth2 > 0:
                    if body[j] == "{":
                        depth2 += 1
                    elif body[j] == "}":
                        depth2 -= 1
                    j += 1
                val = body[val_start:j - 1]
            elif body[j] == '"':
                j += 1
                val_start = j
                while j < bn:
                    if body[j] == '"' and body[j - 1] != "\\":
                        break
                    j += 1
                val = body[val_start:j]
                j += 1  # closing quote
            else:
                val_start = j
                while j < bn and body[j] not in ",\n\r":
                    j += 1
                val = body[val_start:j]

            fields[field_name] = normalize_whitespace(val)

        entries[key] = BibEntry(entry_type=entry_type, key=key, fields=fields, raw=raw_block)

    return entries


def parse_included_tex_files(main_tex: Path) -> List[Path]:
    # Look for \include{foo} and \input{foo}
    text = main_tex.read_text(encoding="utf-8")
    includes = []
    for cmd in ("include", "input"):
        for m in re.finditer(r"\\" + cmd + r"\{([^}]+)\}", text):
            name = m.group(1).strip()
            if not name:
                continue
            if name.endswith(".tex"):
                path = main_tex.parent / name
            else:
                path = main_tex.parent / f"{name}.tex"
            includes.append(path)

    # de-dup while preserving order
    seen: set[Path] = set()
    ordered: List[Path] = []
    for p in includes:
        if p not in seen:
            seen.add(p)
            ordered.append(p)
    return ordered


def find_citations_in_tex(tex_path: Path) -> List[CiteOccurrence]:
    lines = tex_path.read_text(encoding="utf-8").splitlines()
    occurrences: List[CiteOccurrence] = []

    for idx, raw_line in enumerate(lines):
        line_no = idx + 1
        line = strip_tex_comment(raw_line)
        for m in CITE_CMD_RE.finditer(line):
            cmd = m.group("cmd")
            keys_raw = m.group("keys")
            keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
            if not keys:
                continue

            # Context: whole paragraph (between blank lines)
            start = idx
            while start > 0 and lines[start - 1].strip() != "":
                start -= 1
            end = idx
            while end + 1 < len(lines) and lines[end + 1].strip() != "":
                end += 1

            para_lines = [strip_tex_comment(l).strip() for l in lines[start : end + 1]]
            context = normalize_whitespace(" ".join([l for l in para_lines if l]))

            line_text = normalize_whitespace(line.strip())

            occurrences.append(
                CiteOccurrence(
                    tex_path=tex_path,
                    line_no=line_no,
                    command=cmd,
                    keys=keys,
                    line_text=line_text,
                    context=context,
                )
            )

    return occurrences


def extract_arxiv_id(entry: BibEntry) -> Optional[str]:
    # explicit fields
    for field_name in ("eprint", "arxiv", "arxivid"):
        val = entry.fields.get(field_name)
        if not val:
            continue
        m = ARXIV_ID_SIMPLE_RE.search(val)
        if m:
            return m.group("id")

    # from journal/note/howpublished
    for field_name in ("journal", "note", "howpublished"):
        val = entry.fields.get(field_name)
        if not val:
            continue
        m = ARXIV_ID_RE.search(val)
        if m:
            return m.group("id")
        m2 = re.search(r"arXiv\s*:\s*(\d{4}\.\d{4,5})", val, re.积分梯度归因NORECASE)
        if m2:
            return m2.group(1)
    return None


def heuristic_url(entry: BibEntry) -> Optional[str]:
    """Best-effort URL suggestions for references that often lack DOI/URL in BibTeX."""
    key = entry.key.lower()
    title = (entry.fields.get("title") or "").lower()
    if key == "lecun2010mnist" or ("mnist" in title and "digit" in title):
        # Common canonical page for MNIST dataset.
        return "http://yann.lecun.com/exdb/mnist/"
    return None


def http_get(
    url: str,
    *,
    timeout: float = 12.0,
    headers: Optional[Dict[str, str]] = None,
    max_bytes: Optional[int] = 8192,
) -> Tuple[Optional[int], Optional[bytes], Optional[str]]:
    hdrs = {
        "User-Agent": "G-thesis-reference-audit/1.0",
        "Accept": "*/*",
    }
    if headers:
        hdrs.update(headers)

    req = urllib.request.Request(url, headers=hdrs, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", None)
            data = resp.read() if max_bytes is None else resp.read(max_bytes)
            return int(status) if status is not None else 200, data, None
    except urllib.error.HTTPError as e:
        # even for 404 etc, return status
        try:
            data = e.read(1024)
        except Exception:
            data = None
        return int(e.code), data, f"HTTPError: {e}"
    except Exception as e:
        return None, None, f"{type(e).__name__}: {e}"


def http_get_json(url: str, *, timeout: float = 12.0) -> Tuple[Optional[int], Optional[dict], Optional[str]]:
    # Crossref responses can exceed 8KB; read a larger capped payload.
    status, data, err = http_get(
        url,
        timeout=timeout,
        headers={"Accept": "application/json"},
        max_bytes=2_000_000,
    )
    if status is None or data is None:
        return status, None, err
    try:
        return status, json.loads(data.decode("utf-8", errors="replace")), err
    except Exception as e:
        return status, None, f"json decode failed: {type(e).__name__}: {e}" + (f" ({err})" if err else "")


def title_similarity(a: str, b: str) -> float:
    na = normalize_title(a)
    nb = normalize_title(b)
    if not na or not nb:
        return 0.0
    return SequenceMatcher(None, na, nb).ratio()


def parse_first_author_family(author_field: str) -> Optional[str]:
    # BibTeX often uses: "Last, First and Last2, First2"
    authors = [a.strip() for a in author_field.split(" and ") if a.strip()]
    if not authors:
        return None
    first = authors[0]
    if "," in first:
        family = first.split(",", 1)[0].strip()
        return family.lower() or None
    parts = first.split()
    return (parts[-1].lower() if parts else None)


def crossref_best_match(entry: BibEntry, *, rows: int = 5) -> Tuple[Optional[dict], Optional[float], Optional[str]]:
    title = entry.fields.get("title")
    if not title:
        return None, None, "missing title"

    bib_year = get_bib_year(entry)
    bib_author_family_raw = (
        parse_first_author_family(entry.fields.get("author", "")) if entry.fields.get("author") else None
    )
    bib_author_family = normalize_name_token(bib_author_family_raw) if bib_author_family_raw else None
    bib_container = get_bib_container(entry)

    select = "DOI,URL,title,author,issued,created,published-print,published-online,container-title"

    def fetch_items(params: Dict[str, str]) -> Tuple[List[dict], Optional[str]]:
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        status, data, err = http_get_json(url)
        if status != 200 or not data:
            return [], err or f"crossref http status {status}"
        items = (data.get("message") or {}).get("items") or []
        return list(items), None

    base: Dict[str, str] = {
        "query.title": title,
        "rows": str(rows),
        "select": select,
    }
    if bib_author_family:
        base["query.author"] = bib_author_family
    if bib_container:
        base["query.container-title"] = bib_container
    if bib_year:
        base["filter"] = f"from-pub-date:{bib_year-1}-01-01,until-pub-date:{bib_year+1}-12-31"

    # Try stricter queries first, then relax.
    attempts: List[Dict[str, str]] = [dict(base)]
    if "query.container-title" in base:
        p = dict(base)
        p.pop("query.container-title", None)
        attempts.append(p)
    if "query.author" in base:
        p = dict(base)
        p.pop("query.author", None)
        attempts.append(p)
    if "filter" in base:
        p = dict(base)
        p.pop("filter", None)
        attempts.append(p)

    items: List[dict] = []
    last_err: Optional[str] = None
    for params in attempts:
        items, last_err = fetch_items(params)
        if items:
            break
    if not items:
        return None, None, last_err or "no items"

    best_item = None
    best_score = -1.0

    for item in items:
        item_titles = item.get("title") or []
        item_title = item_titles[0] if item_titles else ""
        ts = title_similarity(title, item_title)

        # year
        item_year = None
        for yr_field in ("published-print", "published-online", "issued", "created"):
            parts = ((item.get(yr_field) or {}).get("date-parts") or [])
            if parts and parts[0] and isinstance(parts[0][0], int):
                item_year = int(parts[0][0])
                break
        year_score = 0.0
        if bib_year and item_year:
            diff = abs(bib_year - item_year)
            if diff == 0:
                year_score = 1.0
            elif diff == 1:
                year_score = 0.7
            elif diff == 2:
                year_score = 0.4
            else:
                year_score = 0.0

        # first author family
        author_score = 0.0
        if bib_author_family:
            cr_authors = item.get("author") or []
            if cr_authors:
                cr_family_raw = (cr_authors[0].get("family") or "").strip()
                cr_family = normalize_name_token(cr_family_raw)
                if cr_family and cr_family == bib_author_family:
                    author_score = 1.0

        # container title (journal / proceedings)
        container_score = 0.0
        if bib_container:
            item_containers = item.get("container-title") or []
            item_container = item_containers[0] if item_containers else ""
            nb = normalize_container(bib_container)
            ni = normalize_container(item_container)
            if nb and ni:
                if nb in ni or ni in nb:
                    container_score = 1.0
                else:
                    container_score = SequenceMatcher(None, nb, ni).ratio()

        score = 0.60 * ts + 0.22 * year_score + 0.10 * author_score + 0.08 * container_score
        if score > best_score:
            best_score = score
            best_item = item

    return best_item, best_score if best_item is not None else None, None


def arxiv_best_match(entry: BibEntry, *, max_results: int = 10) -> Tuple[Optional[str], Optional[float], Optional[str]]:
    """Resolve an arXiv id by searching arXiv API with title (+ optional author).

    Returns: (arxiv_id, score, error)
    """
    title = entry.fields.get("title")
    if not title:
        return None, None, "missing title"

    bib_author_family_raw = (
        parse_first_author_family(entry.fields.get("author", "")) if entry.fields.get("author") else None
    )
    bib_author_family = normalize_name_token(bib_author_family_raw) if bib_author_family_raw else None
    bib_year = get_bib_year(entry)

    # Build search queries using a cleaned title (avoid LaTeX/math breaking arXiv search).
    cleaned_title = normalize_title(title)
    words = cleaned_title.split() if cleaned_title else []
    phrase = " ".join(words[:16]) if words else cleaned_title
    phrase = (phrase or "").strip() or title
    phrase = phrase.replace('"', " ")  # avoid breaking quotes in query
    phrase = normalize_whitespace(phrase)

    stopwords = {
        "a",
        "an",
        "the",
        "and",
        "or",
        "of",
        "in",
        "on",
        "for",
        "with",
        "to",
        "via",
        "from",
        "under",
        "into",
        "at",
        "by",
        "as",
        "is",
        "are",
        "be",
        "its",
        "their",
        "our",
        "your",
        "we",
        "us",
        "they",
        "this",
        "that",
    }

    def build_and_query(prefix: str, *, max_terms: int = 8) -> Optional[str]:
        terms: List[str] = []
        seen: set[str] = set()
        for w in words:
            if not w:
                continue
            if w in stopwords:
                continue
            if len(w) <= 2:
                continue
            if w.isdigit():
                continue
            if w in seen:
                continue
            seen.add(w)
            terms.append(f"{prefix}:{w}")
            if len(terms) >= max_terms:
                break
        # Require a few terms; otherwise too broad.
        if len(terms) < 3:
            return None
        return " AND ".join(terms)

    and_ti = build_and_query("ti")
    and_all = build_and_query("all")

    queries: List[str] = []
    if bib_author_family:
        queries.append(f'ti:"{phrase}" AND au:{bib_author_family}')
    queries.append(f'ti:"{phrase}"')
    queries.append(f'all:"{phrase}"')

    # Fallback: token-AND queries are much less brittle than exact phrases.
    # Example: AutoAttack title variants often break phrase queries.
    if and_ti and bib_author_family:
        queries.append(f"{and_ti} AND au:{bib_author_family}")
    if and_ti:
        queries.append(and_ti)
    if and_all and bib_author_family:
        queries.append(f"{and_all} AND au:{bib_author_family}")
    if and_all:
        queries.append(and_all)

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    best_id: Optional[str] = None
    best_score = -1.0
    last_err: Optional[str] = None

    for qi, q in enumerate(queries):
        if qi > 0:
            time.sleep(0.05)
        params = {
            "search_query": q,
            "start": "0",
            "max_results": str(max_results),
        }
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        st, data, err = http_get(url, headers={"Accept": "application/atom+xml"}, max_bytes=2_000_000)
        if st != 200 or not data:
            last_err = err or f"arXiv http status {st}"
            continue

        try:
            root = ET.fromstring(data)
        except Exception as e:
            last_err = f"arXiv xml parse failed: {type(e).__name__}: {e}"
            continue

        for ent in root.findall("atom:entry", ns):
            ent_title = (ent.findtext("atom:title", default="", namespaces=ns) or "").strip()
            ent_id_url = (ent.findtext("atom:id", default="", namespaces=ns) or "").strip()
            ent_published = (ent.findtext("atom:published", default="", namespaces=ns) or "").strip()

            if "/abs/" not in ent_id_url:
                continue
            arxiv_id = ent_id_url.split("/abs/", 1)[1].strip().rstrip("/")
            arxiv_id = re.sub(r"v\d+$", "", arxiv_id)

            ts = title_similarity(title, ent_title)

            author_score = 0.0
            if bib_author_family:
                for a in ent.findall("atom:author", ns):
                    nm = (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
                    if not nm:
                        continue
                    fam_guess = nm.split()[-1] if nm.split() else nm
                    fam = normalize_name_token(fam_guess)
                    if fam and fam == bib_author_family:
                        author_score = 1.0
                        break

            year_score = 0.0
            if bib_year and len(ent_published) >= 4 and ent_published[:4].isdigit():
                pub_year = int(ent_published[:4])
                diff = abs(bib_year - pub_year)
                if diff == 0:
                    year_score = 1.0
                elif diff == 1:
                    year_score = 0.6

            score = 0.85 * ts + 0.10 * author_score + 0.05 * year_score
            if score > best_score:
                best_score = score
                best_id = arxiv_id

        if best_id is not None and best_score >= ARXIV_OK_SCORE:
            break

    if best_id is None:
        return None, None, last_err or "no arXiv match"
    return best_id, float(best_score), None


def openreview_best_match(entry: BibEntry, *, limit: int = 10) -> Tuple[Optional[str], Optional[float], Optional[str]]:
    """Resolve an OpenReview forum id by searching OpenReview's public notes/search endpoint.

    Returns: (forum_id, score, error)
    """
    title = entry.fields.get("title")
    if not title:
        return None, None, "missing title"

    bib_author_family_raw = (
        parse_first_author_family(entry.fields.get("author", "")) if entry.fields.get("author") else None
    )
    bib_author_family = normalize_name_token(bib_author_family_raw) if bib_author_family_raw else None

    params = {
        "term": title,
        "limit": str(limit),
    }
    url = "https://api.openreview.net/notes/search?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    st, data, err = http_get_json(url)
    if st != 200 or not data:
        return None, None, err or f"openreview http status {st}"

    notes = data.get("notes") or []
    if not notes:
        return None, None, "no openreview match"

    best_forum: Optional[str] = None
    best_score = -1.0

    for note in notes:
        content = note.get("content") or {}
        note_title = (content.get("title") or "").strip()
        if not note_title:
            continue

        ts = title_similarity(title, note_title)

        author_score = 0.0
        if bib_author_family:
            authors = content.get("authors") or []
            for a in authors:
                if not isinstance(a, str):
                    continue
                nm = a.strip()
                if not nm:
                    continue
                fam_guess = nm.split()[-1] if nm.split() else nm
                fam = normalize_name_token(fam_guess)
                if fam and fam == bib_author_family:
                    author_score = 1.0
                    break

        score = 0.85 * ts + 0.15 * author_score
        if score > best_score:
            best_score = score
            best_forum = (note.get("forum") or note.get("id") or "").strip() or None

    if not best_forum:
        return None, None, "no openreview match"
    return best_forum, float(best_score), None


def resolve_neurips_proceedings_url(entry: BibEntry) -> Tuple[Optional[str], Optional[str]]:
    """Try to resolve a NeurIPS proceedings abstract URL by scraping the year index page."""
    title = entry.fields.get("title")
    if not title:
        return None, "missing title"
    year = get_bib_year(entry)
    if not year:
        return None, "missing year"

    index_url = f"https://proceedings.neurips.cc/paper/{year}"
    st, data, err = http_get(index_url, headers={"Accept": "text/html"}, max_bytes=2_000_000)
    if st != 200 or not data:
        return None, err or f"neurips http status {st}"

    page_html = data.decode("utf-8", errors="replace")
    target = normalize_title(title)
    if not target:
        return None, "empty normalized title"

    best_href: Optional[str] = None
    best_score = -1.0

    # Keep parsing simple and dependency-free.
    anchor_re = re.compile(r"<a[^>]*href=(?:\"|')(?P<href>[^\"']+)(?:\"|')[^>]*>(?P<text>[^<]+)</a>", re.积分梯度归因NORECASE)
    for m in anchor_re.finditer(page_html):
        href = (m.group("href") or "").strip()
        text = html.unescape((m.group("text") or "").strip())
        if not href or not text:
            continue
        ts = title_similarity(title, text)
        if ts > best_score:
            best_score = ts
            best_href = href

    if not best_href or best_score < 0.90:
        return None, "no neurips proceedings match"

    abs_url = urllib.parse.urljoin("https://proceedings.neurips.cc", best_href)
    return abs_url, None


def verify_entry(entry: BibEntry, *, network: bool, polite_delay_s: float = 0.15) -> VerificationResult:
    doi = entry.fields.get("doi") or entry.fields.get("DOI")
    doi = doi.strip() if isinstance(doi, str) and doi.strip() else None
    url = entry.fields.get("url") or entry.fields.get("URL")
    url = url.strip() if isinstance(url, str) and url.strip() else None

    url_source: Optional[str] = "bib" if url else None
    if not url:
        hurl = heuristic_url(entry)
        if hurl:
            url = hurl
            url_source = "heuristic"

    arxiv_id = extract_arxiv_id(entry)
    arxiv_source: Optional[str] = "bib" if arxiv_id else None
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None
    doi_url = f"https://doi.org/{doi}" if doi else None

    vr = VerificationResult(
        status="skipped" if not network else "fail",
        summary="未联网校验" if not network else "尚未获得可验证的外部链接",
        doi=doi,
        doi_url=doi_url,
        url=url,
        url_source=url_source,
        arxiv_id=arxiv_id,
        arxiv_url=arxiv_url,
        arxiv_source=arxiv_source,
    )

    if not network:
        return vr

    verified_ok = False

    # 1) If DOI present, validate via Crossref works/<doi>
    if doi:
        time.sleep(polite_delay_s)
        cr_url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
        st, data, err = http_get_json(cr_url)
        vr.doi_crossref_http_status = st
        if st == 200 and data and (data.get("status") == "ok"):
            msg = data.get("message") or {}
            vr.crossref_matched = True
            vr.crossref_doi = msg.get("DOI")
            vr.crossref_url = msg.get("URL")
            titles = msg.get("title") or []
            vr.crossref_title = titles[0] if titles else None
            parts = ((msg.get("issued") or {}).get("date-parts") or [])
            if parts and parts[0] and isinstance(parts[0][0], int):
                vr.crossref_year = int(parts[0][0])
            verified_ok = True
            vr.summary = "Crossref DOI 记录存在"
        else:
            if err:
                vr.error = err

    # 2) arXiv reachability (if arXiv id already known)
    if vr.arxiv_url:
        time.sleep(polite_delay_s)
        st, _data, err = http_get(vr.arxiv_url)
        vr.arxiv_http_status = st
        if st and 200 <= st < 400:
            verified_ok = True
            if vr.summary == "尚未获得可验证的外部链接":
                vr.summary = "arXiv 页面可访问"
        else:
            if err and not vr.error:
                vr.error = err

    # 2.5) Venue-specific URL resolution (OpenReview / NeurIPS proceedings) when no URL is present.
    if (not verified_ok) and (not vr.url):
        # OpenReview (e.g., ICLR) often has the canonical public record even without arXiv/DOI.
        if looks_like_openreview_venue(entry):
            time.sleep(polite_delay_s)
            forum, oscore, oerr = openreview_best_match(entry)
            if forum and oscore is not None and oscore >= 0.92:
                vr.url = f"https://openreview.net/forum?id={forum}"
                vr.url_source = "openreview"
            elif oerr and not vr.error:
                vr.error = oerr

        # NeurIPS proceedings can be parsed deterministically by year + title.
        if (not vr.url) and looks_like_neurips_venue(entry):
            time.sleep(polite_delay_s)
            purl, perr = resolve_neurips_proceedings_url(entry)
            if purl:
                vr.url = purl
                vr.url_source = "neurips"
            elif perr and not vr.error:
                vr.error = perr

    # 3) URL reachability (if provided or heuristic)
    if vr.url:
        time.sleep(polite_delay_s)
        st, _data, err = http_get(vr.url)
        vr.url_http_status = st
        if st and 200 <= st < 400:
            verified_ok = True
            if vr.summary == "尚未获得可验证的外部链接":
                vr.summary = "URL 可访问"
        else:
            if err and not vr.error:
                vr.error = err

    # 4) If it looks like a preprint/conference entry and we still don't have any verified link, try arXiv API search.
    # This avoids cluttering the report with "no arXiv match" when we already verified via OpenReview/proceedings.
    if (not verified_ok) and (not vr.arxiv_id) and looks_like_preprint_venue(entry):
        time.sleep(polite_delay_s)
        aid, ascore, aerr = arxiv_best_match(entry)
        if aid and ascore is not None and ascore >= ARXIV_OK_SCORE:
            vr.arxiv_id = aid
            vr.arxiv_url = f"https://arxiv.org/abs/{aid}"
            vr.arxiv_source = "api"
            time.sleep(polite_delay_s)
            st, _data, err = http_get(vr.arxiv_url)
            vr.arxiv_http_status = st
            if st and 200 <= st < 400:
                verified_ok = True
                if vr.summary == "尚未获得可验证的外部链接":
                    vr.summary = f"arXiv（API 匹配 score={ascore:.2f}）页面可访问"
            elif err and not vr.error:
                vr.error = err
        elif aerr and not vr.error:
            vr.error = aerr

    # 5) Crossref title match (only when needed)
    # Avoid injecting misleading DOIs when we already verified via arXiv for preprint-like venues.
    should_try_crossref = not vr.crossref_matched and (not (looks_like_preprint_venue(entry) and verified_ok))
    if should_try_crossref:
        time.sleep(polite_delay_s)
        item, score, err = crossref_best_match(entry)
        if item and score is not None:
            vr.crossref_matched = True
            vr.crossref_score = float(score)
            vr.crossref_doi = item.get("DOI")
            vr.crossref_url = item.get("URL")
            titles = item.get("title") or []
            vr.crossref_title = titles[0] if titles else None

            item_year = None
            for yr_field in ("published-print", "published-online", "issued", "created"):
                parts = ((item.get(yr_field) or {}).get("date-parts") or [])
                if parts and parts[0] and isinstance(parts[0][0], int):
                    item_year = int(parts[0][0])
                    break
            vr.crossref_year = item_year

            if score >= CROSSREF_OK_SCORE and vr.summary == "尚未获得可验证的外部链接":
                vr.summary = f"Crossref 匹配成功（score={score:.2f}）"
                verified_ok = True
            elif (not verified_ok) and score >= CROSSREF_MAYBE_SCORE:
                vr.summary = f"Crossref 可能匹配（score={score:.2f}）"
            elif (not verified_ok):
                vr.summary = f"Crossref 匹配置信度低（score={score:.2f}）"
        else:
            if err and not vr.error:
                vr.error = err

    # Final status
    if verified_ok:
        vr.status = "ok"
    else:
        # If we found some candidate info (Crossref matched) but couldn't verify reachability, keep maybe.
        if vr.crossref_matched and vr.crossref_score is not None and vr.crossref_score >= CROSSREF_MAYBE_SCORE:
            vr.status = "maybe"
        else:
            vr.status = "fail"
            if vr.summary == "尚未获得可验证的外部链接":
                vr.summary = "未找到可验证的外部记录（Crossref/URL/arXiv）"

    return vr


def md_escape(text: str) -> str:
    # minimal escaping
    return text.replace("\n", " ")


def truncate_text(text: str, *, max_len: int) -> str:
    if len(text) <= max_len:
        return text
    if max_len <= 1:
        return "…"
    # keep a little more headroom to avoid breaking words too often
    cut = max(0, max_len - 2)
    return text[:cut].rstrip() + " …"


def strip_html_tags(text: str) -> str:
    # best-effort HTML to plain text without third-party deps
    if not text:
        return ""
    s = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.积分梯度归因NORECASE | re.DOTALL)
    s = re.sub(r"<style\b[^>]*>.*?</style>", " ", s, flags=re.积分梯度归因NORECASE | re.DOTALL)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return normalize_whitespace(s)


def normalize_for_tokens(text: str) -> str:
    if not text:
        return ""
    # Keep LaTeX command names as tokens (e.g., \infty -> infty)
    s = text.replace("\\&", " and ")
    s = s.replace("$", " ")
    s = s.replace("{", " ").replace("}", " ")
    s = re.sub(r"\\([A-Za-z]+)", r" \1 ", s)
    s = re.sub(r"[^A-Za-z0-9]+", " ", s)
    return normalize_whitespace(s.lower())


SUPPORT_STOPWORDS = {
    # English
    "a",
    "an",
    "the",
    "and",
    "or",
    "of",
    "in",
    "on",
    "for",
    "with",
    "to",
    "via",
    "from",
    "under",
    "into",
    "at",
    "by",
    "as",
    "is",
    "are",
    "be",
    "its",
    "their",
    "our",
    "your",
    "we",
    "us",
    "they",
    "this",
    "that",
    "these",
    "those",
    "et",
    "al",
    # common LaTeX-ish / thesis noise
    "cite",
    "nocite",
    "upcite",
    "eqref",
    "ref",
    "label",
    "begin",
    "end",
    "textbf",
    "textit",
    "mathrm",
    "mathbf",
    "mathcal",
    "mathbb",
    "left",
    "right",
}


def tokenize_support(text: str) -> List[str]:
    norm = normalize_for_tokens(text)
    if not norm:
        return []
    toks = []
    for w in norm.split():
        if len(w) < 3:
            continue
        if w in SUPPORT_STOPWORDS:
            continue
        toks.append(w)
    return toks


def jaccard(set_a: set[str], set_b: set[str]) -> float:
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return float(inter) / float(union) if union else 0.0


@dataclass
class Evidence:
    source: str
    url: Optional[str]
    title: Optional[str]
    abstract: Optional[str]
    http_status: Optional[int] = None
    error: Optional[str] = None


def fetch_arxiv_evidence(arxiv_id: str) -> Evidence:
    params = {
        "id_list": arxiv_id,
        "max_results": "1",
    }
    api_url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    st, data, err = http_get(api_url, headers={"Accept": "application/atom+xml"}, max_bytes=2_000_000)
    if st != 200 or not data:
        return Evidence(
            source="arXiv",
            url=f"https://arxiv.org/abs/{arxiv_id}",
            title=None,
            abstract=None,
            http_status=st,
            error=err or f"arXiv http status {st}",
        )

    try:
        root = ET.fromstring(data)
    except Exception as e:
        return Evidence(
            source="arXiv",
            url=f"https://arxiv.org/abs/{arxiv_id}",
            title=None,
            abstract=None,
            http_status=st,
            error=f"arXiv xml parse failed: {type(e).__name__}: {e}",
        )

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    ent = root.find("atom:entry", ns)
    if ent is None:
        return Evidence(
            source="arXiv",
            url=f"https://arxiv.org/abs/{arxiv_id}",
            title=None,
            abstract=None,
            http_status=st,
            error="arXiv: no entry",
        )

    title = normalize_whitespace((ent.findtext("atom:title", default="", namespaces=ns) or "").strip()) or None
    abstract = normalize_whitespace((ent.findtext("atom:summary", default="", namespaces=ns) or "").strip()) or None
    return Evidence(
        source="arXiv",
        url=f"https://arxiv.org/abs/{arxiv_id}",
        title=title,
        abstract=abstract,
        http_status=st,
        error=None,
    )


def unwrap_openreview_field(val: object) -> Optional[str]:
    if val is None:
        return None
    if isinstance(val, str):
        return val.strip() or None
    if isinstance(val, list):
        items = [str(x).strip() for x in val if str(x).strip()]
        return normalize_whitespace(" ".join(items)) or None
    if isinstance(val, dict):
        # OpenReview sometimes returns {"value": "..."}
        if "value" in val and isinstance(val["value"], str):
            return val["value"].strip() or None
        if "values" in val and isinstance(val["values"], list):
            items = [str(x).strip() for x in val["values"] if str(x).strip()]
            return normalize_whitespace(" ".join(items)) or None
    return None


def fetch_openreview_evidence(forum_id: str) -> Evidence:
    params = {
        "forum": forum_id,
        "limit": "1",
    }
    api_url = "https://api.openreview.net/notes?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    st, data, err = http_get_json(api_url)
    if st != 200 or not data:
        return Evidence(
            source="OpenReview",
            url=f"https://openreview.net/forum?id={forum_id}",
            title=None,
            abstract=None,
            http_status=st,
            error=err or f"openreview http status {st}",
        )

    notes = data.get("notes") or []
    if not notes:
        return Evidence(
            source="OpenReview",
            url=f"https://openreview.net/forum?id={forum_id}",
            title=None,
            abstract=None,
            http_status=st,
            error="openreview: no notes",
        )

    content = (notes[0].get("content") or {})
    title = unwrap_openreview_field(content.get("title"))
    abstract = unwrap_openreview_field(content.get("abstract"))
    return Evidence(
        source="OpenReview",
        url=f"https://openreview.net/forum?id={forum_id}",
        title=title,
        abstract=abstract,
        http_status=st,
        error=None,
    )


def fetch_neurips_evidence(proceedings_url: str) -> Evidence:
    st, data, err = http_get(proceedings_url, headers={"Accept": "text/html"}, max_bytes=2_000_000)
    if st != 200 or not data:
        return Evidence(
            source="NeurIPS Proceedings",
            url=proceedings_url,
            title=None,
            abstract=None,
            http_status=st,
            error=err or f"neurips http status {st}",
        )

    page = data.decode("utf-8", errors="replace")

    # Title
    title = None
    mt = re.search(r"<title>(?P<t>.*?)</title>", page, flags=re.积分梯度归因NORECASE | re.DOTALL)
    if mt:
        title = strip_html_tags(mt.group("t"))

    abstract = None
    # Common pattern: <h4>Abstract</h4><p>...</p>
    m1 = re.search(
        r"<h4[^>]*>\s*Abstract\s*</h4>\s*<p[^>]*>(?P<a>.*?)</p>",
        page,
        flags=re.积分梯度归因NORECASE | re.DOTALL,
    )
    if m1:
        abstract = strip_html_tags(m1.group("a"))
    if not abstract:
        # Fallback: meta description
        m2 = re.search(
            r"<meta[^>]+name=(?:\"|')description(?:\"|')[^>]+content=(?:\"|')(?P<a>.*?)(?:\"|')",
            page,
            flags=re.积分梯度归因NORECASE | re.DOTALL,
        )
        if m2:
            abstract = strip_html_tags(m2.group("a"))

    abstract = normalize_whitespace(abstract) if abstract else None
    title = normalize_whitespace(title) if title else None

    return Evidence(
        source="NeurIPS Proceedings",
        url=proceedings_url,
        title=title,
        abstract=abstract,
        http_status=st,
        error=None,
    )


def fetch_crossref_evidence(doi: str) -> Evidence:
    api_url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    st, data, err = http_get_json(api_url)
    if st != 200 or not data or (data.get("status") != "ok"):
        return Evidence(
            source="Crossref",
            url=f"https://doi.org/{doi}",
            title=None,
            abstract=None,
            http_status=st,
            error=err or f"crossref http status {st}",
        )

    msg = data.get("message") or {}
    titles = msg.get("title") or []
    title = titles[0] if titles else None
    abstract = msg.get("abstract")
    if isinstance(abstract, str):
        abstract = strip_html_tags(abstract)
    else:
        abstract = None

    return Evidence(
        source="Crossref",
        url=f"https://doi.org/{doi}",
        title=normalize_whitespace(title) if title else None,
        abstract=normalize_whitespace(abstract) if abstract else None,
        http_status=st,
        error=None,
    )


def forum_id_from_openreview_url(url: str) -> Optional[str]:
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        return None
    qs = urllib.parse.parse_qs(parsed.query or "")
    fid = (qs.get("id") or qs.get("forum") or [None])[0]
    return fid.strip() if isinstance(fid, str) and fid.strip() else None


def fetch_best_evidence(entry: BibEntry, vr: VerificationResult, *, polite_delay_s: float) -> Evidence:
    # Priority: arXiv > OpenReview > NeurIPS proceedings > Crossref (DOI)
    if vr.arxiv_id:
        time.sleep(polite_delay_s)
        return fetch_arxiv_evidence(vr.arxiv_id)

    if vr.url and vr.url_source == "openreview":
        forum_id = forum_id_from_openreview_url(vr.url)
        if forum_id:
            time.sleep(polite_delay_s)
            return fetch_openreview_evidence(forum_id)

    if vr.url and vr.url_source == "neurips":
        time.sleep(polite_delay_s)
        return fetch_neurips_evidence(vr.url)

    if vr.doi:
        time.sleep(polite_delay_s)
        return fetch_crossref_evidence(vr.doi)

    # Fallback: URL exists but abstract unknown
    if vr.url:
        return Evidence(source="URL", url=vr.url, title=entry.fields.get("title"), abstract=None)
    return Evidence(source="(none)", url=None, title=entry.fields.get("title"), abstract=None)


def classify_support(
    *,
    context: str,
    ref_title: str,
    evidence_abstract: Optional[str],
) -> Tuple[str, str, List[str], float, float]:
    """Return (level, reason, common_tokens, jaccard_title, jaccard_abs).

    Level is a conservative heuristic: 高/中/低/不确定.
    """
    ctx_tokens = set(tokenize_support(context))
    title_tokens = set(tokenize_support(ref_title))
    abs_tokens = set(tokenize_support(evidence_abstract or ""))

    common_title = ctx_tokens & title_tokens
    common_abs = ctx_tokens & abs_tokens

    jt = jaccard(ctx_tokens, title_tokens)
    ja = jaccard(ctx_tokens, abs_tokens) if abs_tokens else 0.0

    # If the thesis context contains too few Latin tokens, automated matching is unreliable.
    if len(ctx_tokens) < 8:
        common = sorted(common_title or common_abs)
        return "不确定", "上下文英文关键词较少，自动比对不稳定", common[:12], jt, ja

    if not abs_tokens:
        if len(common_title) >= 3 or jt >= 0.10:
            common = sorted(common_title)
            return "中", "仅能对齐标题/关键词（未获取摘要），建议人工核对", common[:12], jt, ja
        common = sorted(common_title)
        return "不确定", "未获取摘要且标题重合较少，建议重点核对", common[:12], jt, ja

    # With abstract
    if len(common_abs) >= 6 or ja >= 0.08:
        common = sorted(common_abs)
        return "高", "上下文与摘要关键词重合较多（主题一致性较高）", common[:12], jt, ja
    if len(common_abs) >= 3 or len(common_title) >= 3 or jt >= 0.10:
        common = sorted(common_abs if common_abs else common_title)
        return "中", "主题可能相关，但摘要关键词重合一般；建议人工核对具体结论", common[:12], jt, ja
    common = sorted(common_abs if common_abs else common_title)
    return "低", "摘要关键词重合很少（可能不对应此处论述），建议重点核对", common[:12], jt, ja


def write_support_report(
    *,
    root: Path,
    out_path: Path,
    bib_path: Path,
    tex_files: List[Path],
    entries: Dict[str, BibEntry],
    verifications: Dict[str, VerificationResult],
    key_to_occ: Dict[str, List[CiteOccurrence]],
    network: bool,
    polite_delay_s: float,
) -> None:
    rel = lambda p: p.relative_to(root).as_posix()

    # Fetch evidence once per key
    evidence_by_key: Dict[str, Evidence] = {}
    for key, entry in entries.items():
        vr = verifications.get(key)
        if not vr or (not network):
            evidence_by_key[key] = Evidence(source="(no-network)", url=None, title=entry.fields.get("title"), abstract=None)
            continue
        evidence_by_key[key] = fetch_best_evidence(entry, vr, polite_delay_s=polite_delay_s)

    # Build stats
    total_occ = sum(len(v) for v in key_to_occ.values())
    abstract_ok = sum(1 for ev in evidence_by_key.values() if ev.abstract)
    abstract_missing = len(entries) - abstract_ok

    flagged_low = 0
    flagged_uncertain = 0
    for key, occs in key_to_occ.items():
        entry = entries.get(key)
        if not entry:
            continue
        ev = evidence_by_key.get(key)
        if not ev:
            continue
        for o in occs:
            lvl, _reason, _common, _jt, _ja = classify_support(
                context=o.context,
                ref_title=(entry.fields.get("title") or ""),
                evidence_abstract=ev.abstract,
            )
            if lvl == "低":
                flagged_low += 1
            elif lvl == "不确定":
                flagged_uncertain += 1

    lines: List[str] = []
    lines.append("# 引用支撑性（摘要级）核查报告")
    lines.append("")
    lines.append(f"- 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- Bib 文件：{rel(bib_path)}")
    lines.append(f"- 扫描 TeX 文件数：{len(tex_files)}")
    lines.append(f"- 联网校验：{'否（--no-network）' if not network else '是'}")
    lines.append("")
    lines.append("## 重要说明")
    lines.append("")
    lines.append("- 本报告只做\"摘要级\"自动核对：把你论文中引用处的段落，与可公开获取的摘要/页面文本做关键词一致性比对。")
    lines.append("- \"一致性高/中/低\"仅表示\"主题相关性\"的启发式强弱，不能替代逐段阅读原文；尤其当论文段落为中文而摘要为英文时，自动分数会偏保守。")
    lines.append("- 建议优先人工复核\"一致性=低\"以及\"不确定\"的引用点。")
    lines.append("")

    lines.append("## 总览")
    lines.append("")
    lines.append(f"- 引用点总数（按 cite 命令逐次计数）：{total_occ}")
    lines.append(f"- 成功获取摘要的条目数：{abstract_ok}")
    lines.append(f"- 未获取摘要的条目数：{abstract_missing}")
    lines.append(f"- 标记为一致性=低的引用点：{flagged_low}")
    lines.append(f"- 标记为不确定的引用点：{flagged_uncertain}")
    lines.append("")

    lines.append("## 逐条核查（按 Bib key）")
    lines.append("")

    for key in sorted(entries.keys()):
        entry = entries[key]
        vr = verifications.get(key)
        ev = evidence_by_key.get(key)

        title = entry.fields.get("title", "")
        year = entry.fields.get("year", "")

        lines.append(f"### `{key}` — {md_escape(title)} ({year})")
        lines.append("")
        if ev:
            lines.append(f"- 证据来源：{ev.source}")
            if ev.url:
                lines.append(f"- 证据链接：{ev.url}")
            if ev.http_status is not None:
                lines.append(f"- 证据 HTTP：{ev.http_status}")
            if ev.error:
                lines.append(f"- 证据抓取提示：{md_escape(ev.error)}")

            if ev.abstract:
                snippet = truncate_text(ev.abstract, max_len=900)
                lines.append("- 摘要（节选）：")
                lines.append(f"  - {md_escape(snippet)}")
            else:
                lines.append("- 摘要：未获取")

        # Also include the verified links to help manual checking.
        if vr:
            links = format_links(vr)
            if links:
                lines.append("- 可访问链接（用于人工核对）：")
                for lk in links:
                    lines.append(f"  - {lk}")

        occs = key_to_occ.get(key, [])
        lines.append(f"- 论文中引用位置：{len(occs)} 处")
        if not occs:
            lines.append("")
            continue

        for o in occs:
            lvl, reason, common, jt, ja = classify_support(
                context=o.context,
                ref_title=title,
                evidence_abstract=(ev.abstract if ev else None),
            )
            lines.append(f"  - {rel(o.tex_path)}:{o.line_no}  ({o.command})")
            lines.append(f"    - 一致性：{lvl} — {md_escape(reason)}")
            lines.append(f"    - 关键词重合：{', '.join(common) if common else '（无）'}")
            lines.append(f"    - 分数：J(title)={jt:.3f}; J(abstract)={ja:.3f}")
            lines.append(f"    - 引用行：{md_escape(truncate_text(o.line_text, max_len=220))}")
            lines.append(f"    - 段落（节选）：{md_escape(truncate_text(o.context, max_len=420))}")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_links(vr: VerificationResult) -> List[str]:
    links: List[str] = []
    if vr.doi_url:
        links.append(f"DOI: {vr.doi_url}")
    # Only surface Crossref-derived links when confidence is high.
    crossref_trusted = vr.crossref_matched and (
        vr.crossref_score is None or (vr.crossref_score is not None and vr.crossref_score >= CROSSREF_OK_SCORE)
    )
    if crossref_trusted and vr.crossref_doi and not vr.doi_url:
        links.append(f"DOI(来自Crossref): https://doi.org/{vr.crossref_doi}")

    if vr.url:
        if vr.url_source == "openreview":
            links.append(f"OpenReview(来自API): {vr.url}")
        elif vr.url_source == "neurips":
            links.append(f"NeurIPS Proceedings(自动解析): {vr.url}")
        else:
            label = "URL" if (vr.url_source != "heuristic") else "URL(启发式)"
            links.append(f"{label}: {vr.url}")
    if crossref_trusted and vr.crossref_url and (not vr.url):
        links.append(f"URL(来自Crossref): {vr.crossref_url}")

    if vr.arxiv_url:
        label = "arXiv" if (vr.arxiv_source != "api") else "arXiv(来自API)"
        links.append(f"{label}: {vr.arxiv_url}")
    return links


def main(argv: Sequence[str]) -> int:
    ap = argparse.ArgumentParser(description="Audit BibTeX references and LaTeX citations.")
    ap.add_argument("--root", default=".", help="Project root (default: .)")
    ap.add_argument("--bib", default="nkthesis.bib", help="BibTeX file (default: nkthesis.bib)")
    ap.add_argument("--main-tex", default="main.tex", help="Main TeX file to find included chapters (default: main.tex)")
    ap.add_argument("--output", default="reference_verification_report.md", help="Output markdown report path")
    ap.add_argument(
        "--support-report",
        default=None,
        help="Optional: write an additional markdown report to heuristically check whether each citation context is supported by publicly available abstracts/pages",
    )
    ap.add_argument("--include-all-tex", action="store_true", help="Scan all .tex under root (instead of only files included by main.tex)")
    ap.add_argument("--include-manual", action="store_true", help="Include manual.tex when scanning all .tex")
    ap.add_argument("--no-network", action="store_true", help="Skip all network checks")
    ap.add_argument("--delay", type=float, default=0.15, help="Polite delay between network requests (seconds)")

    args = ap.parse_args(list(argv))

    root = Path(args.root).resolve()
    bib_path = (root / args.bib).resolve()
    main_tex = (root / args.main_tex).resolve()
    out_path = (root / args.output).resolve()
    support_out_path = (root / args.support_report).resolve() if args.support_report else None

    if not bib_path.exists():
        print(f"ERROR: bib file not found: {bib_path}", file=sys.stderr)
        return 2

    entries = parse_bibtex(bib_path)

    # Determine which tex files to scan
    tex_files: List[Path]
    if args.include_all_tex:
        tex_files = sorted(root.glob("**/*.tex"))
        if not args.include_manual:
            tex_files = [p for p in tex_files if p.name.lower() != "manual.tex"]
    else:
        if not main_tex.exists():
            print(f"ERROR: main tex file not found: {main_tex}", file=sys.stderr)
            return 2
        tex_files = [p for p in parse_included_tex_files(main_tex) if p.exists()]

    all_occurrences: List[CiteOccurrence] = []
    for tex in tex_files:
        try:
            all_occurrences.extend(find_citations_in_tex(tex))
        except UnicodeDecodeError:
            # best-effort fallback
            all_occurrences.extend(find_citations_in_tex(Path(str(tex))))

    # Build cite-key mapping
    key_to_occ: Dict[str, List[CiteOccurrence]] = {}
    cited_keys: List[str] = []
    for occ in all_occurrences:
        for k in occ.keys:
            cited_keys.append(k)
            key_to_occ.setdefault(k, []).append(occ)

    cited_set = set(cited_keys)
    bib_keys = set(entries.keys())

    missing_in_bib = sorted(cited_set - bib_keys)
    unused_in_tex = sorted(bib_keys - cited_set)

    # Verify each bib entry (only those cited, but also list unused)
    network = not args.no_network

    verifications: Dict[str, VerificationResult] = {}
    for key in sorted(entries.keys()):
        vr = verify_entry(entries[key], network=network, polite_delay_s=float(args.delay))
        verifications[key] = vr

    # Write report (existence + link verification)
    rel = lambda p: p.relative_to(root).as_posix()

    lines: List[str] = []
    lines.append("# 参考文献与引用核查报告")
    lines.append("")
    lines.append(f"- 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- Bib 文件：{rel(bib_path)}")
    lines.append(f"- 扫描 TeX 文件数：{len(tex_files)}")
    lines.append(f"- 联网校验：{'否（--no-network）' if not network else '是'}")
    lines.append("")

    lines.append("## 总览")
    lines.append("")
    lines.append(f"- Bib 条目数：{len(entries)}")
    lines.append(f"- 论文中出现的 cite key 数（去重）：{len(cited_set)}")
    lines.append(f"- cite 总次数（含重复）：{len(cited_keys)}")
    lines.append(f"- 缺失的 cite key（TeX 中出现但 Bib 中不存在）：{len(missing_in_bib)}")
    lines.append(f"- 未被引用的 Bib 条目（Bib 中存在但 TeX 未引用）：{len(unused_in_tex)}")
    lines.append("")

    if missing_in_bib:
        lines.append("### 缺失 cite key")
        lines.append("")
        for k in missing_in_bib:
            occs = key_to_occ.get(k, [])
            if occs:
                o = occs[0]
                lines.append(f"- `{k}` 首次出现于 {rel(o.tex_path)}:{o.line_no}")
            else:
                lines.append(f"- `{k}`")
        lines.append("")

    if unused_in_tex:
        lines.append("### 未被引用的 Bib 条目")
        lines.append("")
        for k in unused_in_tex:
            title = entries[k].fields.get("title", "")
            year = entries[k].fields.get("year", "")
            lines.append(f"- `{k}` ({year}) {title}")
        lines.append("")

    lines.append("## 逐条核查")
    lines.append("")

    for key in sorted(entries.keys()):
        entry = entries[key]
        vr = verifications[key]
        title = entry.fields.get("title", "")
        year = entry.fields.get("year", "")

        lines.append(f"### `{key}` — {md_escape(title)} ({year})")
        lines.append("")
        lines.append(f"- 类型：@{entry.entry_type}")
        if entry.fields.get("author"):
            lines.append(f"- 作者：{md_escape(entry.fields['author'])}")
        if entry.fields.get("journal"):
            lines.append(f"- 期刊/出处：{md_escape(entry.fields['journal'])}")
        if entry.fields.get("booktitle"):
            lines.append(f"- 会议/出处：{md_escape(entry.fields['booktitle'])}")

        # Links
        links = format_links(vr)
        if links:
            lines.append("- 链接：")
            for lk in links:
                lines.append(f"  - {lk}")

        # Verification summary
        lines.append(f"- 存在性校验：{vr.status} — {vr.summary}")
        if vr.crossref_matched:
            extra = []
            if vr.crossref_title:
                extra.append(f"title={vr.crossref_title}")
            if vr.crossref_year:
                extra.append(f"year={vr.crossref_year}")
            if vr.crossref_doi:
                extra.append(f"DOI={vr.crossref_doi}")
            if vr.crossref_score is not None:
                extra.append(f"score={vr.crossref_score:.2f}")
            if extra:
                lines.append(f"- Crossref：{'; '.join(extra)}")

        if vr.doi_crossref_http_status is not None:
            lines.append(f"- DOI→Crossref HTTP：{vr.doi_crossref_http_status}")
        if vr.arxiv_http_status is not None:
            lines.append(f"- arXiv HTTP：{vr.arxiv_http_status}")
        if vr.url_http_status is not None:
            lines.append(f"- URL HTTP：{vr.url_http_status}")
        if vr.error:
            lines.append(f"- 错误/提示：{md_escape(vr.error)}")

        # Citation occurrences
        occs = key_to_occ.get(key, [])
        lines.append(f"- 论文中引用位置：{len(occs)} 处")
        if occs:
            for o in occs:
                lines.append(f"  - {rel(o.tex_path)}:{o.line_no}  ({o.command})")
                lines.append(f"    - 上下文：{md_escape(truncate_text(o.context, max_len=360))}")
        else:
            lines.append("  - （未在扫描的 TeX 文件中发现引用）")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote report: {out_path}")

    if support_out_path is not None:
        write_support_report(
            root=root,
            out_path=support_out_path,
            bib_path=bib_path,
            tex_files=tex_files,
            entries=entries,
            verifications=verifications,
            key_to_occ=key_to_occ,
            network=network,
            polite_delay_s=float(args.delay),
        )
        print(f"Wrote support report: {support_out_path}")

    # Exit code: 0 ok; 1 if any missing keys
    return 1 if missing_in_bib else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
