# 论文公式与伪代码审核报告

## 审核日期
2026-05-03

## 审核范围
- 论文章节：background.tex, pipeline.tex, experiment.tex
- 代码库：D:\软件\对抗性防御\对抗性防御-1\03.代码

---

## 一、公式正确性审核

### 1.1 背景章节公式 (background.tex)

| 公式编号 | 公式内容 | 状态 | 说明 |
|---------|---------|------|------|
| (3.1) | 卷积操作定义 | ✅ 正确 | 标准卷积公式 |
| (3.2) | ReLU激活函数 | ✅ 正确 | $\\text{ReLU}(x) = \\max(0, x)$ |
| (3.3) | 最大池化操作 | ✅ 正确 | 标准池化公式 |
| (3.4) | 交叉熵损失 | ✅ 正确 | 标准交叉熵定义 |
| (3.5) | 对抗样本定义 | ✅ 正确 | 符合文献定义 |
| (3.6) | FGSM攻击 | ✅ 正确 | $\\mathbf{x}' = \\mathbf{x} + \\varepsilon \\cdot \\text{sign}(\\nabla_{\\mathbf{x}} \\mathcal{L})$ |
| (3.7) | PGD攻击迭代公式 | ✅ 正确 | 投影梯度下降标准形式 |
| (3.8) | C&W攻击目标函数 | ✅ 正确 | $\\min_{\\boldsymbol{\\delta}} \\|\\boldsymbol{\\delta}\\|_2 + c \\cdot g(\\mathbf{x} + \\boldsymbol{\\delta})$ |
| (3.9) | 对抗性训练min-max问题 | ✅ 正确 | Madry等人提出的标准形式 |
| (3.10) | 原始梯度显著性图 | ✅ 正确 | $\\mathbf{S}(\\mathbf{x}) = \\left| \\frac{\\partial f_c(\\mathbf{x})}{\\partial \\mathbf{x}} \\right|$ |
| (3.11) | 积分梯度归因 | ✅ 正确 | Sundararajan等人原始定义 |
| (3.12) | 积分梯度Riemann近似 | ✅ 正确 | 离散化近似公式 |

### 1.2 方法章节公式 (pipeline.tex)

| 公式编号 | 公式内容 | 状态 | 说明 |
|---------|---------|------|------|
| (4.1) | 经验风险最小化 | ✅ 正确 | 标准训练目标 |
| (4.2) | 梯度显著性图 | ✅ 正确 | $S(x, y) = \\left| \\frac{\\partial f_y(x)}{\\partial x} \\right|$ |
| (4.3) | 邻域显著性聚合 | ✅ 正确 | 卷积求和策略 |
| (4.4) | 卷积实现 | ✅ 正确 | Conv2d等价形式 |
| (4.5) | Top-K位置选取 | ✅ 正确 | 峰值选取策略 |
| (4.6) | 掩码膨胀 | ✅ 正确 | 方形区域置1 |
| (4.7) | 遮蔽施加公式 | ✅ 正确 | $x' = x \\odot (1 - M) + c \\cdot M$ |
| (4.8) | 积分梯度归因 | ✅ 正确 | 路径积分形式 |
| (4.9) | 对抗性训练目标 | ✅ 正确 | SOAT训练目标 |
| (4.10) | 混合攻击选择 | ✅ 正确 | 概率混合公式 |
| (4.11) | PGD更新规则 | ✅ 正确 | 投影操作定义 |

### 1.3 实验章节公式 (experiment.tex)

| 公式编号 | 公式内容 | 状态 | 说明 |
|---------|---------|------|------|
| (5.1) | 数据归一化 | ✅ 正确 | MNIST标准化 |
| (5.2) | 干净准确率 | ✅ 正确 | 标准准确率定义 |
| (5.3) | 对抗准确率 | ✅ 正确 | 对抗样本准确率 |
| (5.4) | 攻击成功率 | ✅ 正确 | ASR = 1 - AdvAcc |
| (5.5) | 归因集中度 | ✅ 正确 | Top-9像素占比 |

**公式审核结论：所有公式均正确，与标准文献定义一致。**

---

## 二、伪代码与代码实现对比审核

### 2.1 算法1：梯度显著性图计算 (alg:saliency)

| 伪代码行 | 伪代码内容 | 代码实现 | 状态 |
|---------|-----------|---------|------|
| 1 | 启用输入梯度追踪：$x.\\text{requires\\_grad} \\leftarrow \\text{True}$ | `x.detach().requires_grad_(True)` | ✅ 一致 |
| 2 | 前向传播：$\\text{output} \\leftarrow f_{\\theta}(x)$ | `output = model(x)` | ✅ 一致 |
| 3 | 提取目标类别得分：$\\text{scores} \\leftarrow \\text{output}[y]$ | `scores = output.gather(1, y.view(-1, 1))` | ✅ 一致 |
| 4 | 反向传播计算梯度 | `torch.autograd.grad(scores, x, ...)` | ✅ 一致 |
| 5 | 取绝对值：$S \\leftarrow \\left| \\partial\\text{scores}/\\partial x \\right|$ | `return saliency_map.abs()` | ✅ 一致 |

**代码位置：** `occlusion_attack.py:14-29`

**结论：** 伪代码与代码实现完全一致。

---

### 2.2 算法2：固定原始梯度显著性图 (alg:fixed_attack)

| 伪代码步骤 | 代码实现 | 状态 | 备注 |
|-----------|---------|------|------|
| 显著性计算：$S \\leftarrow \\left|\\partial f_Y(X)/\\partial X\\right|$ | `compute_saliency()` 调用 | ✅ 一致 | 使用算法1 |
| 邻域聚合：Conv2d with $\\mathbf{1}_{k\\times k}$ | `nn.Conv2d(1, 1, kernel_size=...)` | ✅ 一致 | occlusion_attack.py:72-77 |
| Top-K位置选取 | `torch.topk(out_sum_flat, self.top_k, dim=1)` | ✅ 一致 | occlusion_attack.py:83 |
| 掩码膨胀 | 循环设置mask为1 | ✅ 一致 | occlusion_attack.py:87-95 |
| 施加遮蔽：$X \\odot (1-M) + c \\cdot M$ | `(1 - mask) * x.detach() + mask * occlu` | ✅ 一致 | occlusion_attack.py:100 |
| 像素截断：$\\mathrm{clamp}(X', 0, 1)$ | `torch.clamp(..., 0, 1)` | ✅ 一致 | occlusion_attack.py:100 |

**代码位置：** `occlusion_attack.py:32-102` (SaliencyOcclusionAttack类)

**结论：** 伪代码与代码实现完全一致。

---

### 2.3 算法3：自适应原始梯度显著性图 (alg:adaptive_attack)

| 伪代码步骤 | 代码实现 | 状态 | 备注 |
|-----------|---------|------|------|
| 显著性计算 | `compute_saliency()` | ✅ 一致 | 算法1 |
| 按显著性降序排序 | `torch.sort(attr_flat, dim=1, descending=True)` | ✅ 一致 | occlusion_attack.py:146 |
| 预计算累积掩码 | 嵌套循环构建nr2mask字典 | ✅ 一致 | occlusion_attack.py:149-175 |
| 渐进遮蔽与早停 | n/r循环+sample2perturb判断 | ✅ 一致 | occlusion_attack.py:185-203 |

**⚠️ 发现一处细节差异：**

| 项目 | 论文伪代码 | 代码实现 | 说明 |
|-----|-----------|---------|------|
| 迭代顺序 | 先遍历$n$再遍历$r$ (第10-13行) | 先遍历$n$再遍历$r$ | ✅ 实际一致 |
| 掩码索引 | `mask(n,r)` | `nr2mask[f'{n}_{r}']` | ✅ 等价 |
| 边界处理 | $\\lfloor k/2 \\rfloor$ | `r`直接作为半径 | ⚠️ 论文公式(4.6)使用$\\lfloor k/2 \\rfloor$，但代码中$R$直接作为半径 |

**重要说明：**
- 论文中kernel_size=3对应半径$\\lfloor 3/2 \\rfloor = 1$
- 代码中直接设置$R=3$表示半径为3像素（实际遮蔽块大小为$2R+1=7$）
- 这导致论文中"kernel_size=3"与代码中"R=3"的实际遮蔽面积差异：
  - 论文：$3\\times3=9$像素
  - 代码：$7\\times7=49$像素

**建议：** 论文中应明确区分"kernel_size"和"radius"的概念，或在代码中使用`kernel_size = 2*R+1`保持一致。

---

### 2.4 算法4：基于遮蔽攻击的对抗性训练 (alg:soat)

| 伪代码步骤 | 代码实现 | 状态 | 备注 |
|-----------|---------|------|------|
| 切换至eval模式 | `self.model.eval()` | ✅ 一致 | adversarial_training.py:54 |
| 生成对抗样本 | `self.adversary((x, y))` | ✅ 一致 | adversarial_training.py:55 |
| 切换至train模式 | `self.model.train()` | ✅ 一致 | adversarial_training.py:58 |
| 前向传播 | `self.model(x_adv)` | ✅ 一致 | adversarial_training.py:59 |
| 计算损失 | `F.cross_entropy(output, y)` | ✅ 一致 | 损失计算 |
| 反向传播更新 | 由调用者完成 | ✅ 一致 | 伪代码省略了具体优化器调用 |

**代码位置：** `adversarial_training.py:38-61` (OcclusionAdversarialTraining类)

**结论：** 伪代码与代码实现完全一致。

---

### 2.5 算法5：混合对抗性训练 (alg:mat)

| 伪代码步骤 | 代码实现 | 状态 | 备注 |
|-----------|---------|------|------|
| 采样 $u \\sim \\mathrm{Uniform}(0, 1)$ | 需要检查具体实现 | ⚠️ 待验证 | 未找到MAT直接实现 |
| 条件判断 $u < p$ | 需要检查具体实现 | ⚠️ 待验证 | 未找到MAT直接实现 |
| 遮蔽攻击分支 | `OcclusionAdversarialTraining` | ✅ 存在 | adversarial_training.py:38 |
| PGD攻击分支 | `AdversarialTraining` | ✅ 存在 | adversarial_training.py:7 |

**⚠️ 重要发现：**

在代码库中**未找到**混合对抗性训练(MAT)的直接实现。具体表现为：

1. `adversarial_training.py` 中实现了独立的`AdversarialTraining`和`OcclusionAdversarialTraining`类
2. 但没有实现算法5中描述的以概率$p$随机选择攻击类型的混合训练类
3. 需要通过外部训练循环手动实现混合逻辑

**建议：** 应在`adversarial_training.py`中补充`MixedAdversarialTraining`类的实现，封装算法5的完整逻辑。

---

## 三、其他发现

### 3.1 代码中存在但论文未提及的实现细节

1. **Loss-based vs Score-based梯度计算**
   - 代码文件：`occlusion_attack_fixed.py`
   - 实现了两种梯度计算方式：
     - `compute_saliency_score_based()`: 原始实现（与论文一致）
     - `compute_saliency_loss_based()`: 修复版（使用CrossEntropyLoss梯度）
   - 论文仅描述了Score-based版本

2. **IG-based攻击变体**
   - 代码实现了多种IG-based攻击类：
     - `OcclusionAttack`: 基础IG固定遮蔽
     - `AdaptiveOcclusionAttack`: IG自适应遮蔽
     - `IGFixedOcclusionAttack`: Inequality项目迁移版本
     - `AdaptiveIGOcclusionAttack`: Inequality自适应版本
     - `InequalityIGOcclusionAttack`: 完全复刻Inequality项目
   - 论文仅统一描述为"基于梯度积分的遮蔽攻击"

3. **多种PGD攻击变体**
   - `LinfPGD`: L∞范数PGD（论文使用）
   - `L2PGD`: L2范数PGD（论文未提及）
   - `FGSM`: 快速梯度符号法（论文提及）
   - `CWAttack`: C&W攻击（论文提及）
   - `MSDAttack`: 多尺度多样性攻击（论文未提及）

### 3.2 参数对应关系

| 论文参数 | 代码参数 | 对应关系 |
|---------|---------|---------|
| top\_$k$ | `top_k` | ✅ 直接对应 |
| kernel\_size | `kernel_size` | ✅ 直接对应 |
| $N$ | `N` | ✅ 直接对应 |
| $R$ | `R` | ⚠️ 论文半径=kernel_size/2，代码R直接为半径 |
| $c$ | `occlu_color` / `c` | ✅ 直接对应 |
| PGD $\\varepsilon$ | `eps` | ✅ 直接对应 |
| PGD step\_size | `step_size` | ✅ 直接对应 |
| PGD iterations | `step` | ⚠️ 论文20步，代码默认10步 |

---

## 四、审核结论

### 4.1 公式正确性
**状态：✅ 全部正确**

所有数学公式均与标准文献定义一致，推导正确，符号规范。

### 4.2 伪代码与代码一致性
**状态：⚠️ 基本一致，存在 minor issues**

| 算法 | 一致性 | 问题 |
|-----|-------|------|
| 算法1 (梯度显著性图) | ✅ 完全一致 | 无 |
| 算法2 (固定遮蔽攻击) | ✅ 完全一致 | 无 |
| 算法3 (自适应遮蔽攻击) | ⚠️ 基本一致 | R与kernel_size概念差异 |
| 算法4 (SOAT) | ✅ 完全一致 | 无 |
| 算法5 (MAT) | ❌ 缺失实现 | 代码中无直接对应类 |

### 4.3 建议修改项

1. **论文pipeline.tex第84行附近：** 明确区分kernel_size和radius概念
   - 建议添加注释："kernel_size=3对应radius=1"

2. **adversarial_training.py：** 添加MixedAdversarialTraining类
   - 封装算法5的完整逻辑
   - 实现概率选择遮蔽/PGD攻击

3. **论文第4.2.3节：** 明确说明PGD迭代次数
   - 实验章节表4.1写的是20步
   - 代码中LinfPGD默认是10步

---

## 五、详细对比表

### 5.1 核心攻击类对应关系

| 论文名称 | 代码类名 | 文件位置 | 状态 |
|---------|---------|---------|------|
| 固定原始梯度显著性图 | `SaliencyOcclusionAttack` | occlusion_attack.py:32 | ✅ |
| 自适应原始梯度显著性图 | `AdaptiveSaliencyOcclusionAttack` | occlusion_attack.py:105 | ✅ |
| 固定积分梯度归因遮蔽 | `OcclusionAttack` | occlusion_attack.py:207 | ✅ |
| 自适应积分梯度归因遮蔽 | `AdaptiveOcclusionAttack` | occlusion_attack.py:269 | ✅ |
| PGD攻击 | `LinfPGD` | pgd.py:49 | ✅ |
| FGSM攻击 | `FGSM` | pgd.py:176 | ✅ |
| C&W攻击 | `CWAttack` | pgd.py:211 | ✅ |

### 5.2 训练类对应关系

| 论文名称 | 代码类名 | 文件位置 | 状态 |
|---------|---------|---------|------|
| 基于遮蔽攻击的对抗性训练 | `OcclusionAdversarialTraining` | adversarial_training.py:38 | ✅ |
| 自适应遮蔽对抗性训练 | `AdaptiveOcclusionAdversarialTraining` | adversarial_training.py:64 | ✅ |
| PGD对抗性训练 | `AdversarialTraining` | adversarial_training.py:7 | ✅ |
| FGSM对抗性训练 | `FGSMAdversarialTraining` | adversarial_training.py:116 | ✅ |
| 混合对抗性训练 | ❌ 缺失 | - | ❌ |

---

**审核完成**

审核人：Claude Code
日期：2026-05-03
