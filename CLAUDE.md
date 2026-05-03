# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是南开大学本科生毕业论文 LaTeX 模板，基于 NKThesis 宏包。项目使用 XeLaTeX 编译，支持中文排版，采用 biblatex 管理参考文献。

## 编译命令

### 完整编译（推荐）
```bash
make compile
```
该命令执行：xelatex -> biber -> xelatex -> xelatex，共编译4遍以确保交叉引用和参考文献正确。

### 使用脚本编译
```bash
# Linux/macOS
./build.sh

# Windows
build.bat
```

### 手动编译
```bash
xelatex -synctex=1 main
biber main
xelatex -synctex=1 main
xelatex -synctex=1 main
```

### 清理辅助文件
```bash
make clean        # 删除 PDF 和主要辅助文件
rm *.aux *.out *.blg *.toc *.bbl *.bcf  # 删除所有辅助文件
```

## 项目结构

### 核心文件
- **main.tex** - 主文件，包含文档设置、宏包引用、章节包含控制 (`
includeonly`)
- **NKThesis.sty** - 南开大学学位论文格式宏包，定义样式和字体
- **nkthesis.bib** - 参考文献数据库 (BibTeX 格式)
- **nkthesis.bbx/cbx** - biblatex 样式文件

### 章节文件
通过 `
includeonly` 在 main.tex 中控制编译哪些章节：
- abstract.tex - 摘要
- introduction.tex - 引言
- background.tex - 相关工作/背景
- pipeline.tex - 方法/实现
- experiment.tex - 实验
- conclusion.tex - 结论
- acknowledgements.tex - 致谢
- references.tex - 参考文献列表

### 资源目录
- **fonts/** - 字体文件
- **figures/** - 图片文件 (支持 PDF, PNG, JPG, EPS)
- **docs/** - 文档和说明
- **tools/** - 辅助工具脚本

## 重要配置

### 论文信息设置
在 main.tex 中通过 `
NKTsetup` 设置论文元信息：
```latex

data{论文题目(中文), 论文题目(英文), 学号, 姓名, 年级, 专业, 系别, 学院, 指导教师, 论文完成时间}
```

### 编译方式选择
- **推荐**: XeLaTeX (UTF-8 编码，自动处理中英文间距)
- 备选: pdfLaTeX (需使用 CJK 包，不推荐)

切换编译方式前必须删除 *.toc 和 *.aux 文件。

### 参考文献管理
使用 biblatex 宏包管理参考文献：
- 引用命令: `
cite{key}`, `
upcite{key}` (上标引用)
- 样式: nkthesis (自定义)
- 处理工具: biber (不是 bibtex)

## 工具脚本

### 参考文献审计工具
```bash
python tools/reference_audit.py --output reference_verification_report.md
```
功能：
- 检查引用的文献是否存在
- 验证 DOI/URL/arXiv 链接可访问性
- 生成引用位置报告

## 开发注意事项

1. **章节开发**: 编辑单个章节后，可在 `
includeonly` 中只保留该章节以加快编译速度
2. **图片格式**: 推荐使用 PDF 格式图片以获得最佳兼容性
3. **字体**: 使用宋体、黑体、楷体、仿宋四种中文字体，通过 NKThesis.sty 自动配置
4. **定理环境**: 预定义了定理、引理、推论、命题、定义、例等环境
5. **算法**: 使用 algorithm + algpseudocode 宏包，已汉化输入/输出标签

## 参考资源

- 模板说明文档: manual.tex
- 在线文档: docs/index.md
- 项目主页: https://github.com/Tr0py/NKU-thesis-template-2020
- Overleaf 模板: 可在 Overleaf 中搜索 "NKU-thesis-template-2020"
