#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re

# 读取notebook
nb_path = r'D:\软件\对抗性防御\对抗性防御-1\03.代码\15. Saliency遮蔽攻击对抗性训练 copy.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Notebook共有 {len(nb['cells'])} 个单元\n")

# 搜索包含训练循环的代码单元
found = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])

        # 查找训练循环
        if 'def ' in source and ('train' in source or 'epoch' in source):
            # 检查是否同时包含occlusion和pgd相关代码
            has_occlusion = 'occlusion' in source.lower() or 'Occlusion' in source
            has_pgd = 'pgd' in source.lower() or 'PGD' in source or 'LinfPGD' in source
            has_mixed = 'mixed' in source.lower() or 'mix' in source.lower() or 'random' in source.lower()
            has_prob = '0.5' in source or 'probability' in source.lower() or 'p=' in source

            score = 0
            if has_occlusion: score += 1
            if has_pgd: score += 2
            if has_mixed: score += 3
            if has_prob: score += 3

            if score >= 3:
                found.append((i, score, has_occlusion, has_pgd, has_mixed, has_prob, source))

# 按相关性排序
found.sort(key=lambda x: -x[1])

print(f"找到 {len(found)} 个相关训练函数\n")
print("="*80)

for idx, (i, score, occ, pgd, mixed, prob, source) in enumerate(found[:5]):
    print(f"\n=== Cell {i} (得分: {score}) ===")
    print(f"包含Occlusion: {occ}, 包含PGD: {pgd}, 包含Mixed: {mixed}, 包含概率: {prob}")
    print("-"*60)
    # 打印源代码
    lines = source.split('\n')
    for line in lines:
        print(line)
    print("="*80)

# 如果没有找到，尝试更宽松的搜索
if not found:
    print("\n未找到匹配的训练函数，尝试搜索所有包含'train'的函数...\n")
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if 'def train' in source or ('for epoch' in source and 'train' in source):
                print(f"\n=== Cell {i} ===")
                lines = source.split('\n')
                for line in lines[:50]:  # 只打印前50行
                    print(line)
                if len(lines) > 50:
                    print(f"... (还有 {len(lines)-50} 行)")
                print("="*80)
