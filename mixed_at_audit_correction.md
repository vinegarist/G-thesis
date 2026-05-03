# 混合对抗训练审核修正报告

## 重要发现

经过仔细重新检查代码，我发现了混合对抗训练的实现。之前的审核结论有误，特此更正。

---

## 一、混合对抗训练实现确认

### 1.1 实现位置

**文件**: `15. Saliency遮蔽攻击对抗性训练 copy.ipynb`
**单元格**: Cell 37
**类名**: `AdaptiveSaliencyPgdMixedAT`

### 1.2 完整代码实现

```python
class AdaptiveSaliencyPgdMixedAT(nn.Module):
    """自适应Saliency遮蔽攻击 + PGD 混合对抗性训练

    每个batch中按比例混合两种攻击：
    - 自适应Saliency遮蔽攻击: 渐进式遮蔽，保留语义
    - PGD (L∞): 基于梯度的迭代攻击
    """

    def __init__(
        self,
        model,
        N=5,
        R=3,
        c=0.0,
        eps=0.1,
        pgd_step=20,
        pgd_step_size=0.025,
        random_start=True,
        occlu_ratio=0.5,  # 遮蔽攻击比例
        criterion=F.cross_entropy,
    ):
        super().__init__()
        self.model = model
        self.occlu_ratio = occlu_ratio

        # 自适应Saliency遮蔽攻击
        self.occlusion = AdaptiveSaliencyOcclusionAttack(
            model, N=N, R=R, c=c
        )
        # PGD攻击
        self.pgd = LinfPGD(
            net=model,
            eps=eps,
            step_size=pgd_step_size,
            step=pgd_step,
            random_start=random_start,
            criterion=criterion,
        )

    def forward(self, x, y=None):
        if y is None:
            return self.model(x)

        training = self.model.training
        # 对抗样本生成阶段固定为eval模式
        self.model.eval()

        bs = x.size(0)
        k = int(bs * self.occlu_ratio)  # 计算遮蔽攻击样本数

        if k <= 0:
            # 全部使用PGD
            x_mix = self.pgd((x, y))
        elif k >= bs:
            # 全部使用遮蔽攻击
            x_mix = self.occlusion((x, y))
        else:
            # 混合：前k个用遮蔽攻击，其余用PGD
            x_adv_occl = self.occlusion((x, y))
            x_adv_pgd = self.pgd((x, y))

            x_mix = x_adv_pgd.clone()
            x_mix[:k] = x_adv_occl[:k]  # 前k个替换为遮蔽攻击

        # 恢复训练模式
        if training:
            self.model.train()

        return self.model(x_mix)
```

---

## 二、论文描述 vs 代码实现对比

### 2.1 论文描述（算法5）

```
算法5：混合对抗性训练（MAT）
...
7: 采样 u ~ Uniform(0, 1)
8: if u < p then
9:   X' ← A_occ(f_θ, X, Y)
10:  // 遮蔽攻击分支
11: else
12:   X' ← A_pgd(f_θ, X, Y)
13:  // PGD 攻击分支
14: end if
```

**描述含义**:
> "在每次训练迭代中以概率 p 选用遮蔽攻击，以概率 1-p 选用 PGD 攻击"

**实现方式**: **按样本随机选择** - 每个样本独立以概率p选择攻击类型

### 2.2 代码实现

```python
bs = x.size(0)
k = int(bs * self.occlu_ratio)  # 例如 bs=256, ratio=0.5 → k=128

# 混合：前k个用遮蔽攻击，其余用PGD
x_adv_occl = self.occlusion((x, y))  # 整个批次生成遮蔽对抗样本
x_adv_pgd = self.pgd((x, y))          # 整个批次生成PGD对抗样本

x_mix = x_adv_pgd.clone()
x_mix[:k] = x_adv_occl[:k]  # 前k个用遮蔽，后(bs-k)个用PGD
```

**实现方式**: **按比例切分批次** - 整个批次中前k个固定用遮蔽，后(bs-k)个固定用PGD

### 2.3 关键差异

| 特性 | 论文描述 | 代码实现 | 差异程度 |
|-----|---------|---------|---------|
| 选择方式 | 按样本随机选择 | 按批次位置切分 | ⚠️ 不同 |
| 期望比例 | p=0.5 | occlu_ratio=0.5 | ✅ 相同 |
| 随机性 | 每样本独立随机 | 固定前k个遮蔽 | 🔴 不同 |
| 攻击生成 | 仅生成选定类型的对抗样本 | 两种攻击都生成，然后切分 | 🔴 不同 |

**核心区别**:
- **论文**: 随机性体现在"每个样本有p概率被选中用遮蔽攻击"
- **代码**: 固定性体现在"批次中前occlu_ratio比例用遮蔽，其余用PGD"

### 2.4 实际影响

虽然期望上都是50%遮蔽+50%PGD，但实现方式有重要差异：

1. **随机性差异**:
   - 论文：每个epoch中每个样本的攻击类型随机变化
   - 代码：同一位置的样本始终使用相同攻击类型（前k个总是遮蔽）

2. **计算效率差异**:
   - 论文：只需生成选定类型的对抗样本
   - 代码：两种攻击都对整个批次生成，然后切分（计算量翻倍）

3. **训练动态差异**:
   - 论文：样本级别随机，更均匀
   - 代码：批次级别固定，可能导致某些样本始终用同一种攻击

---

## 三、建议

### 3.1 论文修改建议

**选项1**: 修改论文描述以匹配代码实现
> 建议修改为："在每个训练批次中，按固定比例 p 将批次切分为两部分，前 p 比例的样本使用遮蔽攻击，其余使用 PGD 攻击"

**选项2**: 修改代码实现以匹配论文描述
```python
# 论文描述的实现方式
import random

if random.random() < self.p:
    x_mix = self.occlusion((x, y))
else:
    x_mix = self.pgd((x, y))
```

### 3.2 推荐修改代码

当前实现虽然功能正确，但存在不必要的计算浪费（两种攻击都对整个批次生成）。建议优化为：

```python
# 优化的实现（符合论文描述且更高效）
def forward(self, x, y=None):
    if y is None:
        return self.model(x)

    training = self.model.training
    self.model.eval()

    # 随机决定是否使用遮蔽攻击
    if random.random() < self.occlu_ratio:
        x_mix = self.occlusion((x, y))
    else:
        x_mix = self.pgd((x, y))

    if training:
        self.model.train()

    return self.model(x_mix)
```

---

## 四、审核结论修正

### 原结论
❌ "adversarial_training.py 中**没有** MixedAdversarialTraining 类"

### 修正结论
✅ **混合对抗训练已实现**，位于notebook的 `AdaptiveSaliencyPgdMixedAT` 类

### 新问题
⚠️ **实现方式与论文描述不一致**:
- 论文：按样本概率随机选择
- 代码：按批次比例固定切分

---

## 五、总结

| 检查项 | 原结论 | 修正结论 |
|-------|-------|---------|
| 混合训练是否存在 | ❌ 不存在 | ✅ 存在 (`AdaptiveSaliencyPgdMixedAT`) |
| 实现位置 | - | `15. Saliency遮蔽攻击对抗性训练 copy.ipynb` Cell 37 |
| 与论文一致性 | - | ⚠️ 实现方式不同（随机选择 vs 比例切分） |
| 参数对应 | - | `occlu_ratio=0.5` 对应论文 `p=0.5` |

**诚挚致歉**: 初次审核时未仔细检查notebook文件，导致遗漏了重要实现。感谢指出，已重新 thorough 审核。

---

审核人：Claude Code
日期：2026-05-03
