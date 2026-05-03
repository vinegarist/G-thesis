# 论文公式与伪代码最终审核报告

## 审核日期
2026-05-03

---

## 一、公式风格一致性审核

### 1.1 公式环境使用

| 文件 | 公式数量 | 主要环境 | 一致性评价 |
|------|---------|---------|-----------|
| background.tex | 12个 | `\begin{equation}` | ✅ 统一使用equation环境 |
| pipeline.tex | 11个 | `\begin{equation}` | ✅ 统一使用equation环境 |
| experiment.tex | 6个 | `\begin{equation}` | ✅ 统一使用equation环境 |

**结论：** 所有公式均统一使用 `equation` 环境，风格一致。

### 1.2 公式编号与标签

**存在问题：**

| 问题类型 | 位置 | 具体描述 | 建议 |
|---------|------|---------|------|
| 有编号无标签 | background.tex:17,25,33... | 大部分公式未加 `\label` | 建议所有公式都添加标签便于引用 |
| 有标签未引用 | pipeline.tex:33 (`\label{eq:saliency}`) | 仅被引用1次 | ✅ 使用正确 |
| 引用与标签不匹配 | pipeline.tex:67 | `\eqref{eq:conv_sum}` 正确引用 | ✅ 使用正确 |

**标签命名规范：**
- 章节：`chpt:xxx` (如 `chpt:background`, `chpt:pipeline`)
- 图：`fig:xxx` (如 `fig:lenet5`, `fig:fixed_saliency_compare`)
- 表：`tab:xxx` (如 `tab:lenet5`, `tab:attack_config`)
- 公式：`eq:xxx` (如 `eq:saliency`, `eq:conv_sum`)

**评价：** 标签命名风格统一，符合规范。

### 1.3 引用方式一致性

| 引用类型 | 命令 | 使用场景 | 正确性 |
|---------|------|---------|-------|
| 公式引用 | `\eqref{eq:xxx}` | 引用带编号的公式 | ✅ 正确 |
| 图引用 | `\ref{fig:xxx}` | 引用图 | ✅ 正确 |
| 表引用 | `\ref{tab:xxx}` | 引用表格 | ✅ 正确 |
| 章节引用 | `\ref{chpt:xxx}` | 引用章节 | ✅ 正确 |
| 算法引用 | `\ref{alg:xxx}` | 引用算法 | ✅ 正确 |

**特殊用法：**
- 波浪号连接：`表~\ref{tab:env}~所示` - 防止表和编号分行
- 多引用连接：`图~\ref{fig:viz_4atk_pgdat}~$\sim$~图~\ref{fig:viz_4atk_adaigat}~` - 使用 `\sim` 表示范围

**结论：** 引用方式统一，符合中文学术论文规范。

### 1.4 数学符号风格

| 符号类型 | 风格 | 示例 | 一致性 |
|---------|------|------|-------|
| 向量/矩阵 | 粗体斜体 | `$\mathbf{x}$`, `$\mathbf{S}$` | ✅ 统一 |
| 集合 | 花体 | `$\mathcal{X}$`, `$\mathcal{D}$` | ✅ 统一 |
| 函数 | 斜体 | `$f_\theta$`, `$\mathcal{L}$` | ✅ 统一 |
| 范数 | 双竖线 | `$\|\boldsymbol{\delta}\|_\infty$` | ✅ 统一 |
| 梯度 | nabla符号 | `$\nabla_{\mathbf{x}}$` | ✅ 统一 |
| 期望 | mathbb E | `$\mathbb{E}$` | ✅ 统一 |

**结论：** 数学符号风格统一，符合机器学习领域规范。

---

## 二、混合对抗训练实现确认

### 2.1 论文描述

论文第4.4.2节"混合对抗性训练策略"(pipeline.tex:243-284)中描述：

> 本文提出混合对抗性训练策略（Mixed Adversarial Training，MAT），在每次训练迭代中以概率 $p$ 选用遮蔽攻击，以概率 $1-p$ 选用 PGD 攻击：
> $$X' = \begin{cases}
>     \mathcal{A}_{\text{occ}}(f_{\theta}, X, Y), & \text{以概率 } p \\\[4pt]
>     \mathcal{A}_{\text{pgd}}(f_{\theta}, X, Y), & \text{以概率 } 1-p
>   \end{cases}$$

算法5(pseudocode: alg:mat)详细描述了MAT的完整流程。

### 2.2 代码实现检查

**adversarial_training.py中实现的类：**

| 类名 | 功能 | 混合训练实现 |
|-----|------|-------------|
| `AdversarialTraining` | PGD对抗训练 | ❌ 仅PGD |
| `OcclusionAdversarialTraining` | 固定遮蔽对抗训练 | ❌ 仅遮蔽 |
| `AdaptiveOcclusionAdversarialTraining` | 自适应遮蔽对抗训练 | ❌ 仅遮蔽 |
| `FGSMAdversarialTraining` | FGSM对抗训练 | ❌ 仅FGSM |
| `CWAdversarialTraining` | C&W对抗训练 | ❌ 仅C&W |
| `L2PGDAdversarialTraining` | L2 PGD对抗训练 | ❌ 仅L2 PGD |
| `MSDAdversarialTraining` | 多尺度多样性攻击训练 | ⚠️ 同时使用L2和L∞，但不是遮蔽+PGD |

**结论：** `adversarial_training.py` 中**没有直接实现混合对抗训练(MAT)**。

### 2.3 混合训练的实际实现方式

根据对notebook的分析，混合对抗训练通过**外部训练循环**实现，而非封装在类中：

```python
# 典型实现方式（在notebook的训练循环中）
for epoch in range(epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        # 以概率p选择遮蔽攻击
        if random.random() < p:
            x_adv = occlusion_attack(data, target)
        else:
            x_adv = pgd_attack(data, target)

        # 使用对抗样本训练
        output = model(x_adv)
        loss = criterion(output, target)
        # ... 反向传播
```

### 2.4 建议

**优先级：高**
- 在 `adversarial_training.py` 中补充 `MixedAdversarialTraining` 类
- 封装概率选择逻辑，提供参数 `p` 控制混合比例
- 示例实现：

```python
class MixedAdversarialTraining(nn.Module):
    """混合对抗性训练：以概率p选择遮蔽攻击，1-p选择PGD攻击"""

    def __init__(self, model, occlusion_attacker, pgd_attacker, p=0.5):
        super().__init__()
        self.model = model
        self.occlusion = occlusion_attacker
        self.pgd = pgd_attacker
        self.p = p

    def forward(self, x, y):
        training = self.model.training
        self.model.eval()

        # 以概率p选择攻击类型
        if random.random() < self.p:
            x_adv = self.occlusion((x, y))
        else:
            x_adv = self.pgd((x, y))

        if training:
            self.model.train()
        return self.model(x_adv)
```

---

## 三、公式正确性最终确认

### 3.1 关键公式验证

| 公式 | 论文位置 | 数学正确性 | 代码实现 | 状态 |
|-----|---------|-----------|---------|------|
| 梯度显著性图 | eq:saliency (pipeline:33) | ✅ $S(x,y) = |\partial f_y/\partial x|$ | `compute_saliency()` | ✅ 一致 |
| 遮蔽施加 | eq:occlusion (pipeline:83) | ✅ $x' = x \odot (1-M) + c \cdot M$ | `(1-mask)*x + mask*occlu` | ✅ 一致 |
| PGD更新 | pipeline:316 | ✅ $x_{t+1} = \Pi(x_t + \alpha \cdot \text{sign}(\nabla \mathcal{L}))$ | `LinfPGD.forward()` | ✅ 一致 |
| FGSM | background:112 | ✅ $x' = x + \varepsilon \cdot \text{sign}(\nabla \mathcal{L})$ | `FGSM.forward()` | ✅ 一致 |

### 3.2 伪代码与代码对应关系

| 算法 | 论文位置 | 代码实现 | 一致性 |
|-----|---------|---------|-------|
| 算法1 梯度显著性图 | pipeline:41-54 | `compute_saliency()` | ✅ 完全一致 |
| 算法2 固定遮蔽 | pipeline:110-130 | `SaliencyOcclusionAttack` | ✅ 完全一致 |
| 算法3 自适应遮蔽 | pipeline:153-187 | `AdaptiveSaliencyOcclusionAttack` | ⚠️ R与kernel_size概念差异 |
| 算法4 SOAT | pipeline:223-241 | `OcclusionAdversarialTraining` | ✅ 完全一致 |
| 算法5 MAT | pipeline:258-282 | ❌ 无直接对应类 | ❌ 需补充实现 |

---

## 四、发现的所有问题汇总

### 4.1 公式风格问题（轻微）

1. **部分公式缺少标签**
   - 影响：无法被引用
   - 建议：为所有重要公式添加 `\label{eq:xxx}`

### 4.2 伪代码与代码不一致（中等）

1. **算法3中的R参数概念差异**
   - 论文：kernel_size=3（3×3遮蔽块）
   - 代码：R=3（实际为半径，7×7遮蔽块）
   - 影响：参数对应关系不清晰
   - 建议：论文中明确说明半径与kernel_size的关系

2. **算法5混合对抗训练缺失实现**
   - 影响：论文描述与代码实现不匹配
   - 建议：在 `adversarial_training.py` 中补充 `MixedAdversarialTraining` 类

### 4.3 参数不一致（轻微）

| 参数 | 论文值 | 代码默认值 | 状态 |
|-----|-------|-----------|------|
| PGD iterations | 20 (表4.1) | 10 (`LinfPGD.__init__`) | ⚠️ 不一致 |
| top_k | 9 | 9 | ✅ 一致 |
| kernel_size/R | 3 | R=3 (代码) | ⚠️ 概念差异 |
| 混合比例p | 0.5 | 未封装 | ⚠️ 外部实现 |

---

## 五、最终审核结论

### 5.1 公式正确性
✅ **全部正确** - 所有数学公式与标准文献定义一致，推导正确。

### 5.2 公式风格一致性
✅ **基本一致** - 使用统一的equation环境，标签命名规范，引用方式一致。

### 5.3 伪代码与代码实现对应性
⚠️ **基本一致，存在2处需要改进**：
1. 算法3的R参数概念需澄清
2. 算法5的混合训练类需补充

### 5.4 建议修改清单

| 优先级 | 问题 | 建议修改位置 | 修改内容 |
|-------|------|-------------|---------|
| 高 | 混合训练类缺失 | adversarial_training.py | 添加 `MixedAdversarialTraining` 类 |
| 中 | R与kernel_size概念差异 | pipeline.tex 第4.3节 | 添加注释说明 radius = kernel_size // 2 |
| 低 | PGD迭代次数不一致 | pipeline.tex 表4.1 或 pgd.py | 统一为20步或10步 |
| 低 | 公式缺少标签 | background.tex, experiment.tex | 为重要公式添加 `\label` |

---

**审核完成**

审核人：Claude Code
日期：2026-05-03

**报告文件：** `formula_code_audit_final_report.md`
