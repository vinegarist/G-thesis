# 引用点优先人工核对清单（从支撑性报告提取）

- 生成时间：2026-04-28 13:24:30
- 来源报告：citation_support_report.md
- 低：16；不确定：38（总提取记录：62）

说明：本清单只做“优先级索引”，最终是否支撑以阅读全文为准。

## 一致性=低（16）

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：background.tex:120 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：投影梯度下降攻击（Projected Gradient Descent，PGD）由Madry等人提出\cite{madry2018pgd}，是FGSM的多步迭代扩展，也是目前最为重要的对抗攻击基准之一。PGD在 $\varepsilon$-球约束集内反复执行梯度上升步骤，并在每步之后将扰动投影回约束集：

### `kingma2015adam` — Adam: A method for stochastic optimization (2015)
- 位置：experiment.tex:24 (cite)
- 证据链接：https://arxiv.org/abs/1412.6980
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：优化器 & Adam \cite{kingma2015adam} \\

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)
- 位置：experiment.tex:83 (cite)
- 证据链接：https://arxiv.org/abs/1412.6572
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：FGSM \cite{goodfellow2015fgsm}

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：experiment.tex:86 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：PGD \cite{madry2018pgd}

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：experiment.tex:116 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：\item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)
- 位置：experiment.tex:117 (cite)
- 证据链接：https://arxiv.org/abs/1412.6572
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：\item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。

### `croce2020autoattack` — Reliable evaluation of adversarial robustness with an ensemble of attacks (2020)
- 位置：introduction.tex:31 (cite)
- 证据链接：https://arxiv.org/abs/2003.01690
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)
- 位置：introduction.tex:31 (cite)
- 证据链接：https://arxiv.org/abs/1412.6572
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：introduction.tex:31 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …

### `tramer2018ensemble` — Ensemble adversarial training: Attacks and defenses (2018)
- 位置：introduction.tex:33 (cite)
- 证据链接：https://arxiv.org/abs/1705.07204
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑 …

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：introduction.tex:39 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型 …

### `shafahi2019free` — Adversarial training for free! (2019)
- 位置：introduction.tex:39 (cite)
- 证据链接：https://arxiv.org/abs/1904.12843
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型 …

### `cohen2019certified` — Certified adversarial robustness via randomized smoothing (2019)
- 位置：introduction.tex:41 (cite)
- 证据链接：https://arxiv.org/abs/1902.02918
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …

### `muller2019labelsmoothing` — When does label smoothing help? (2019)
- 位置：introduction.tex:41 (cite)
- 证据链接：https://arxiv.org/abs/1906.02629
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …

### `simonyan2014saliency` — Deep inside convolutional networks: Visualising image classification models and saliency maps (2014)
- 位置：introduction.tex:49 (cite)
- 证据链接：https://arxiv.org/abs/1312.6034
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sunda …

### `simonyan2014saliency` — Deep inside convolutional networks: Visualising image classification models and saliency maps (2014)
- 位置：pipeline.tex:32 (cite)
- 证据链接：https://arxiv.org/abs/1312.6034
- 机器判定：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
- 引用行：原始梯度显著性图由 Simonyan 等人\cite{simonyan2014saliency}提出，其核心思想是利用模型对输入的一阶梯度信息衡量每个像素对预测结果的重要程度。给定分类模型 $f_{\theta}$、输入图像 $x \in \mathbb{R}^{C \times H \times W}$ 及真实类别 $y$，梯度显著性图定义为：

## 一致性=不确定（38）

### `krizhevsky2012imagenet` — ImageNet classification with deep convolutional neural networks (2012)
- 位置：background.tex:11 (cite)
- 证据链接：https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `lecun2015deeplearning` — Deep learning (2015)
- 位置：background.tex:11 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `lecun1998lenet` — Gradient-based learning applied to document recognition (1998)
- 位置：background.tex:41 (cite)
- 机器判定：不确定 — 未获取摘要且标题重合较少，建议重点核对
- 引用行：LeNet-5是由LeCun等人提出的经典卷积神经网络架构\cite{lecun1998lenet}，最初用于手写数字识别任务，是现代CNN架构的重要先驱，其网络结构如图\ref{fig:lenet5}

### `kingma2015adam` — Adam: A method for stochastic optimization (2015)
- 位置：background.tex:82 (cite)
- 证据链接：https://arxiv.org/abs/1412.6980
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：在优化算法方面，本文采用Adam优化器\cite{kingma2015adam}训练网络参数。Adam结合了动量（Momentum）和自适应学习率（RMSProp）的优势，对梯度的一阶矩和二阶矩分别进行指数移动平均估计，在不同任务和网络结构上均表现出良好的收敛性和鲁棒性，是深度学习训练中应用最为广泛的优化算法之一。

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)
- 位置：background.tex:88 (cite)
- 证据链接：https://arxiv.org/abs/1312.6199
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：对抗样本（Adversarial Examples）是指在原始输入样本 $\mathbf{x}$ 的基础上，通过添加人眼难以察觉的微小扰动 $\boldsymbol{\delta}$，生成一个能够欺骗深度神经网络产生错误预测的输入 $\mathbf{x}' = \mathbf{x} + \boldsymbol{\delta}$。Szegedy等人在2014年首次系统性地发现并研究了这一现象\cite{szegedy2014intri …

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)
- 位置：background.tex:110 (cite)
- 证据链接：https://arxiv.org/abs/1412.6572
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：快速梯度符号法（Fast Gradient Sign Method，FGSM）由Goodfellow等人提出\cite{goodfellow2015fgsm}，是最具代表性的单步对抗攻击方法。FGSM利用损失函数关于输入的梯度方向构造对抗扰动，其生成公式为：

### `carlini2017cw` — Towards evaluating the robustness of neural networks (2017)
- 位置：background.tex:130 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：Carlini和Wagner提出的C\&W攻击\cite{carlini2017cw}将对抗样本生成转化为连续优化问题，通过最小化以下目标函数来寻找扰动幅度尽可能小的高置信度对抗样本：

### `brown2017adversarialpatch` — Adversarial patch (2017)
- 位置：background.tex:142 (cite)
- 证据链接：https://arxiv.org/abs/1712.09665
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志 …

### `eykholt2018robust` — Robust physical-world attacks on deep learning models (2018)
- 位置：background.tex:142 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志 …

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：background.tex:152 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：对抗性训练的优化目标可形式化为一个min-max鞍点优化问题\cite{madry2018pgd}：

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：background.tex:164 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：Madry等人从鞍点优化角度对该框架进行了理论分析，并证明使用PGD攻击近似求解内层最大化问题，能够有效提升模型的 $L_\infty$ 鲁棒性\cite{madry2018pgd}。

### `shafahi2019free` — Adversarial training for free! (2019)
- 位置：background.tex:172 (cite)
- 证据链接：https://arxiv.org/abs/1904.12843
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

### `wong2020fast` — Fast is better than free: Revisiting adversarial training (2020)
- 位置：background.tex:172 (cite)
- 证据链接：https://arxiv.org/abs/2001.03994
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

### `simonyan2014saliency` — Deep inside convolutional networks: Visualising image classification models and saliency maps (2014)
- 位置：background.tex:190 (cite)
- 证据链接：https://arxiv.org/abs/1312.6034
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：原始梯度显著性图（Vanilla Gradient Saliency Map）由Simonyan等人提出\cite{simonyan2014saliency}，是最基础也最直观的特征归因方法。其核心思想是：模型预测对某一输入像素的梯度绝对值越大，说明该像素对预测结果的影响越大，即该像素越"显著"。

### `sundararajan2017ig` — Axiomatic attribution for deep networks (2017)
- 位置：background.tex:204 (cite)
- 证据链接：https://arxiv.org/abs/1703.01365
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：梯度积分（Integrated Gradients，积分梯度归因）由Sundararajan等人提出\cite{sundararajan2017ig}，是一种在理论上更为严格的特征归因方法。积分梯度归因的核心思想是沿从基线输入 $\mathbf{x}^{(0)}$（通常为全零图像）到目标输入 $\mathbf{x}$ 的路径上对梯度进行积分，从而计算每个特征对预测变化的累积贡献：

### `lecun2010mnist` — MNIST handwritten digit database (2010)
- 位置：experiment.tex:31 (cite)
- 证据链接：http://yann.lecun.com/exdb/mnist/
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：本文采用MNIST手写数字数据集\cite{lecun2010mnist}作为目标数据集。MNIST是计算机视觉与对抗鲁棒性研究领域最经典的基准数据集之一，其主要特征如下：训练集包含60,000张样本，测试集包含10,000张样本；每个样本的图像分辨率为$28 \times 28$像素，单通道灰度图；标签覆盖0至9共10个数字类别；像素值归一化采用均值0.1307、标准差0.3081的标准化处理，即：

### `lecun1998lenet` — Gradient-based learning applied to document recognition (1998)
- 位置：experiment.tex:41 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：本文以改进后的LeNet-5~\cite{lecun1998lenet}作为基础分类网络，网络结构详见~\ref{chpt:background}~表~\ref{tab:lenet5}。该网络在标准训练（无对抗扰动）下于MNIST测试集上可达99.0\%的干净准确率，表明基础模型具有充分的分类能力，为后续对抗性训练实验提供了可靠的性能基线。所有防御策略均选用相同的网络架构进行训练，仅在训练目标上加以区分，从而保证对比实验的公平性。

### `carlini2017cw` — Towards evaluating the robustness of neural networks (2017)
- 位置：experiment.tex:89 (cite)
- 机器判定：不确定 — 未获取摘要且标题重合较少，建议重点核对
- 引用行：C\&W \cite{carlini2017cw}

### `kingma2015adam` — Adam: A method for stochastic optimization (2015)
- 位置：experiment.tex:128 (cite)
- 证据链接：https://arxiv.org/abs/1412.6980
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：所有策略均在相同的训练设置下进行：训练轮数50个epoch，使用Adam优化器\cite{kingma2015adam}，学习率调度一致，以确保比较的公平性。

### `duan2023inequality` — Inequality phenomenon in $L_\infty$ adversarial training, and its unrealized threats (2023)
- 位置：experiment.tex:529 (cite)
- 证据链接：https://openreview.net/forum?id=4t9q35BxGr
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：对于原始梯度遮蔽攻击，PGD-AT的防御准确率（固定$k$=9: 70.11\%）略低于Standard（71.19\%），自适应显著性遮蔽下亦然（PGD-AT: 30.12\% vs. Standard: 34.33\%），表明PGD对抗性训练不仅未能提升对显著性遮蔽的防御，反而使模型略微更加脆弱。这一“抵消效应”与Duan等人\cite{duan2023inequality}发现的$L_\infty$对抗性训练导致特征归因不均等 …

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：experiment.tex:533 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：这一差异的原因可能在于梯度掩蔽（gradient masking）\cite{madry2018pgd}对两种归因方法的影响不同。在评估对抗训练模型的遮蔽鲁棒性时，应同时使用多种归因方法进行攻击，以避免因单一归因方法受梯度掩蔽干扰而高估模型的真实防御能力。

### `hinton2006deep` — A fast learning algorithm for deep belief nets (2006)
- 位置：introduction.tex:5 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …

### `lecun2015deeplearning` — Deep learning (2015)
- 位置：introduction.tex:5 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)
- 位置：introduction.tex:5 (cite)
- 证据链接：https://arxiv.org/abs/1312.6199
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)
- 位置：introduction.tex:5 (cite)
- 证据链接：https://arxiv.org/abs/1312.6199
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …

### `he2016resnet` — Deep residual learning for image recognition (2016)
- 位置：introduction.tex:9 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。

### `krizhevsky2012imagenet` — ImageNet classification with deep convolutional neural networks (2012)
- 位置：introduction.tex:9 (cite)
- 证据链接：https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。

### `lecun2015deeplearning` — Deep learning (2015)
- 位置：introduction.tex:9 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)
- 位置：introduction.tex:11 (cite)
- 证据链接：https://arxiv.org/abs/1312.6199
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：然而，2014年Szegedy等人的开创性研究首次揭示了深度神经网络中普遍存在的对抗样本现象\cite{szegedy2014intriguing}：通过在原始输入图像上叠加人眼几乎无法察觉的微小扰动，便可以使分类能力极强的深度模型以极高置信度输出完全错误的预测结果。如图\ref{fig:adversarial_example}所示，原始图像经过细微扰动处理后得到对抗样本。对于人眼观察者而言，两幅图像视觉上完全一致，均呈现"熊猫"的 …

### `eykholt2018robust` — Robust physical-world attacks on deep learning models (2018)
- 位置：introduction.tex:20 (cite)
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术 …

### `kurakin2017adversarial` — Adversarial examples in the physical world (2017)
- 位置：introduction.tex:20 (cite)
- 证据链接：https://arxiv.org/abs/1607.02533
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术 …

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：introduction.tex:22 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：面对对抗样本的挑战，学术界提出了多种防御思路，其中对抗性训练\cite{madry2018pgd}被广泛认为是目前最有效的防御范式。该方法使用对抗性样本进行训练，使得模型增强对扰动的鲁棒性。

### `eykholt2018robust` — Robust physical-world attacks on deep learning models (2018)
- 位置：introduction.tex:33 (cite)
- 机器判定：不确定 — 未获取摘要且标题重合较少，建议重点核对
- 引用行：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑 …

### `papernot2016distillation` — Distillation as a defense to adversarial perturbations against deep neural networks (2016)
- 位置：introduction.tex:41 (cite)
- 机器判定：不确定 — 未获取摘要且标题重合较少，建议重点核对
- 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …

### `duan2023inequality` — Inequality phenomenon in $L_\infty$ adversarial training, and its unrealized threats (2023)
- 位置：introduction.tex:81 (cite)
- 证据链接：https://openreview.net/forum?id=4t9q35BxGr
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：4) 对所提方法进行了系统的实验评估。在MNIST数据集上对九种防御策略（涵盖显著性归因与积分梯度归因两类遮蔽训练）在七类攻击下进行了对比测试，分析了遮蔽参数对攻击效果的影响。实验验证了原始梯度显著性遮蔽攻击与梯度攻击在混合训练模型上呈现抵消效应\cite{duan2023inequality}。

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：pipeline.tex:22 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：\item \textbf{对抗性训练}：将遮蔽攻击生成的对抗样本引入训练循环，并进一步提出混合对抗性训练策略，将遮蔽攻击与 PGD 攻击\cite{madry2018pgd}相结合，提升模型对多类型攻击的泛化防御能力。

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)
- 位置：pipeline.tex:245 (cite)
- 证据链接：https://arxiv.org/abs/1412.6572
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)
- 位置：pipeline.tex:245 (cite)
- 证据链接：https://arxiv.org/abs/1706.06083
- 机器判定：不确定 — 上下文英文关键词较少，自动比对不稳定
- 引用行：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
