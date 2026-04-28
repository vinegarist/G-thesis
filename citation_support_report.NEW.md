# 引用支撑性（摘要级）核查报告

- 生成时间：2026-04-28 13:23:43
- Bib 文件：nkthesis.bib
- 扫描 TeX 文件数：8
- 联网校验：是

## 重要说明

- 本报告只做"摘要级"自动核对：把你论文中引用处的段落，与可公开获取的摘要/页面文本做关键词一致性比对。
- "一致性高/中/低"仅表示"主题相关性"的启发式强弱，不能替代逐段阅读原文；尤其当论文段落为中文而摘要为英文时，自动分数会偏保守。
- 建议优先人工复核"一致性=低"以及"不确定"的引用点。

## 总览

- 引用点总数（按 cite 命令逐次计数）：62
- 成功获取摘要的条目数：15
- 未获取摘要的条目数：11
- 标记为一致性=低的引用点：16
- 标记为不确定的引用点：38

## 逐条核查（按 Bib key）

### `brown2017adversarialpatch` — Adversarial patch (2017)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1712.09665
- 证据 HTTP：200
- 摘要（节选）：
  - We present a method to create universal, robust, targeted adversarial image patches in the real world. The patches are universal because they can be used to attack any scene, robust because they work under a wide variety of transformations, and targeted because they can cause a classifier to output any target class. These adversarial patches can be printed, added to any scene, photographed, and presented to image classifiers; even when the patches are small, they cause the classifiers to ignore the other items in the scene and report a chosen target class. To reproduce the results from the paper, our code is available at https://github.com/tensorflow/cleverhans/tree/master/examples/adversarial_patch
- 可访问链接（用于人工核对）：
  - arXiv: https://arxiv.org/abs/1712.09665
- 论文中引用位置：2 处
  - introduction.tex:33  (cite)
    - 一致性：中 — 主题可能相关，但摘要关键词重合一般；建议人工核对具体结论
    - 关键词重合：adversarial, patch
    - 分数：J(title)=0.250; J(abstract)=0.034
    - 引用行：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑 …
    - 段落（节选）：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。
  - background.tex:142  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：adversarial, patch
    - 分数：J(title)=0.333; J(abstract)=0.035
    - 引用行：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志 …
    - 段落（节选）：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志上粘贴特定图案，成功使自动驾驶系统的视觉识别模型产生严重误判，揭示了此类攻击在安全关键领域的现实威胁性。

### `carlini2017cw` — Towards evaluating the robustness of neural networks (2017)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/sp.2017.49
  - URL(来自Crossref): https://doi.org/10.1109/sp.2017.49
- 论文中引用位置：2 处
  - background.tex:130  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：Carlini和Wagner提出的C\&W攻击\cite{carlini2017cw}将对抗样本生成转化为连续优化问题，通过最小化以下目标函数来寻找扰动幅度尽可能小的高置信度对抗样本：
    - 段落（节选）：Carlini和Wagner提出的C\&W攻击\cite{carlini2017cw}将对抗样本生成转化为连续优化问题，通过最小化以下目标函数来寻找扰动幅度尽可能小的高置信度对抗样本：
  - experiment.tex:89  (cite)
    - 一致性：不确定 — 未获取摘要且标题重合较少，建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：C\&W \cite{carlini2017cw}
    - 段落（节选）：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini2017cw} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次，$\kappa=50$ …

### `cohen2019certified` — Certified adversarial robustness via randomized smoothing (2019)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1902.02918
- 证据 HTTP：200
- 摘要（节选）：
  - We show how to turn any classifier that classifies well under Gaussian noise into a new classifier that is certifiably robust to adversarial perturbations under the $\ell_2$ norm. This "randomized smoothing" technique has been proposed recently in the literature, but existing guarantees are loose. We prove a tight robustness guarantee in $\ell_2$ norm for smoothing with Gaussian noise. We use randomized smoothing to obtain an ImageNet classifier with e.g. a certified top-1 accuracy of 49% under adversarial perturbations with $\ell_2$ norm less than 0.5 (=127/255). No certified defense has been shown feasible on ImageNet except for smoothing. On smaller-scale datasets where competing approaches to certified $\ell_2$ robustness are viable, smoothing delivers higher certified accuracies. Our strong empirical results suggest that randomized smoothing is a promising direction for future res …
- 可访问链接（用于人工核对）：
  - arXiv(来自API): https://arxiv.org/abs/1902.02918
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：certified, defense
    - 分数：J(title)=0.083; J(abstract)=0.025
    - 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …
    - 段落（节选）：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `croce2020autoattack` — Reliable evaluation of adversarial robustness with an ensemble of attacks (2020)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/2003.01690
- 证据 HTTP：200
- 摘要（节选）：
  - The field of defense strategies against adversarial attacks has significantly grown over the last years, but progress is hampered as the evaluation of adversarial defenses is often insufficient and thus gives a wrong impression of robustness. Many promising defenses could be broken later on, making it difficult to identify the state-of-the-art. Frequent pitfalls in the evaluation are improper tuning of hyperparameters of the attacks, gradient obfuscation or masking. In this paper we first propose two extensions of the PGD-attack overcoming failures due to suboptimal step size and problems of the objective function. We then combine our novel attacks with two complementary existing ones to form a parameter-free, computationally affordable and user-independent ensemble of attacks to test adversarial robustness. We apply our ensemble to over 50 models from papers published at recent top ma …
- 可访问链接（用于人工核对）：
  - arXiv(来自API): https://arxiv.org/abs/2003.01690
- 论文中引用位置：1 处
  - introduction.tex:31  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：pgd
    - 分数：J(title)=0.000; J(abstract)=0.009
    - 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …
    - 段落（节选）：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。

### `duan2023inequality` — Inequality phenomenon in $L_\infty$ adversarial training, and its unrealized threats (2023)

- 证据来源：OpenReview
- 证据链接：https://openreview.net/forum?id=4t9q35BxGr
- 证据 HTTP：200
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=4t9q35BxGr
- 论文中引用位置：4 处
  - introduction.tex:81  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：4) 对所提方法进行了系统的实验评估。在MNIST数据集上对九种防御策略（涵盖显著性归因与积分梯度归因两类遮蔽训练）在七类攻击下进行了对比测试，分析了遮蔽参数对攻击效果的影响。实验验证了原始梯度显著性遮蔽攻击与梯度攻击在混合训练模型上呈现抵消效应\cite{duan2023inequality}。
    - 段落（节选）：4) 对所提方法进行了系统的实验评估。在MNIST数据集上对九种防御策略（涵盖显著性归因与积分梯度归因两类遮蔽训练）在七类攻击下进行了对比测试，分析了遮蔽参数对攻击效果的影响。实验验证了原始梯度显著性遮蔽攻击与梯度攻击在混合训练模型上呈现抵消效应\cite{duan2023inequality}。
  - experiment.tex:525  (cite)
    - 一致性：中 — 仅能对齐标题/关键词（未获取摘要），建议人工核对
    - 关键词重合：inequality, infty
    - 分数：J(title)=0.143; J(abstract)=0.000
    - 引用行：Duan等人\cite{duan2023inequality}指出，$L_\infty$ 对抗性训练会导致模型决策依赖发生"特征不均等"（feature inequality）现象，即少数像素的归因显著放大，模型对显著像素的依赖性增强。该现象意味着遮蔽攻击与梯度类对抗性训练可能存在\textbf{相互抵消趋势}：针对遮蔽攻击，遮蔽对抗训练的鲁棒性高于标准模型，而梯度对抗训练 (PGD-AT、FGSM-AT) 反而低于（或与标准模型持 …
    - 段落（节选）：Duan等人\cite{duan2023inequality}指出，$L_\infty$ 对抗性训练会导致模型决策依赖发生"特征不均等"（feature inequality）现象，即少数像素的归因显著放大，模型对显著像素的依赖性增强。该现象意味着遮蔽攻击与梯度类对抗性训练可能存在\textbf{相互抵消趋势}：针对遮蔽攻击，遮蔽对抗训练的鲁棒性高于标准模型，而梯度对抗训练 (PGD-AT、FGSM-AT) 反而低于（或与标准模型持平）；针对梯度类攻击，规律完全相反。本文实验中这一现象在原始归因下得到了清晰体现，但在 积分梯度归因 归因下未呈现。具体数据汇总于表~\ref{tab:cancel}。
  - experiment.tex:529  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：inequality, infty
    - 分数：J(title)=0.182; J(abstract)=0.000
    - 引用行：对于原始梯度遮蔽攻击，PGD-AT的防御准确率（固定$k$=9: 70.11\%）略低于Standard（71.19\%），自适应显著性遮蔽下亦然（PGD-AT: 30.12\% vs. Standard: 34.33\%），表明PGD对抗性训练不仅未能提升对显著性遮蔽的防御，反而使模型略微更加脆弱。这一“抵消效应”与Duan等人\cite{duan2023inequality}发现的$L_\infty$对抗性训练导致特征归因不均等 …
    - 段落（节选）：对于原始梯度遮蔽攻击，PGD-AT的防御准确率（固定$k$=9: 70.11\%）略低于Standard（71.19\%），自适应显著性遮蔽下亦然（PGD-AT: 30.12\% vs. Standard: 34.33\%），表明PGD对抗性训练不仅未能提升对显著性遮蔽的防御，反而使模型略微更加脆弱。这一“抵消效应”与Duan等人\cite{duan2023inequality}发现的$L_\infty$对抗性训练导致特征归因不均等（inequality）现象一致：PGD-AT迫使模型将决策依据集中于极少数像素，一旦这些像素被遮蔽，模型即丧失判别能力。
  - experiment.tex:580  (cite)
    - 一致性：中 — 仅能对齐标题/关键词（未获取摘要），建议人工核对
    - 关键词重合：inequality, infty
    - 分数：J(title)=0.154; J(abstract)=0.000
    - 引用行：\textbf{PGD-AT 使原始梯度归因显著集中（2.47倍）。}标准模型上 原始梯度归因相对分散（集中度0.064），而 PGD-AT 训练后 原始梯度归因集中度跃升至 0.157，与 Duan 等人\cite{duan2023inequality}发现的“$L_\infty$对抗性训练导致特征归因不均等（inequality）”现象一致。此时 PGD-AT 模型将决策依赖压缩到极少数像素，一旦这些像素被准确遮蔽，模型即丧失判 …
    - 段落（节选）：\textbf{PGD-AT 使原始梯度归因显著集中（2.47倍）。}标准模型上 原始梯度归因相对分散（集中度0.064），而 PGD-AT 训练后 原始梯度归因集中度跃升至 0.157，与 Duan 等人\cite{duan2023inequality}发现的“$L_\infty$对抗性训练导致特征归因不均等（inequality）”现象一致。此时 PGD-AT 模型将决策依赖压缩到极少数像素，一旦这些像素被准确遮蔽，模型即丧失判别能力，因此 PGD-AT 对原始梯度显著性图的防御能力反而略低于 Standard（70.11\% vs.\ 71.19\%）。

### `eykholt2018robust` — Robust physical-world attacks on deep learning models (2018)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/cvpr.2018.00175
  - URL(来自Crossref): https://doi.org/10.1109/cvpr.2018.00175
- 论文中引用位置：3 处
  - introduction.tex:20  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术 …
    - 段落（节选）：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术的可信部署具有重要意义。
  - introduction.tex:33  (cite)
    - 一致性：不确定 — 未获取摘要且标题重合较少，建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑 …
    - 段落（节选）：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。
  - background.tex:142  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志 …
    - 段落（节选）：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志上粘贴特定图案，成功使自动驾驶系统的视觉识别模型产生严重误判，揭示了此类攻击在安全关键领域的现实威胁性。

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1412.6572
- 证据 HTTP：200
- 摘要（节选）：
  - Several machine learning models, including neural networks, consistently misclassify adversarial examples---inputs formed by applying small but intentionally worst-case perturbations to examples from the dataset, such that the perturbed input results in the model outputting an incorrect answer with high confidence. Early attempts at explaining this phenomenon focused on nonlinearity and overfitting. We argue instead that the primary cause of neural networks' vulnerability to adversarial perturbation is their linear nature. This explanation is supported by new quantitative results while giving the first explanation of the most intriguing fact about them: their generalization across architectures and training sets. Moreover, this view yields a simple and fast method of generating adversarial examples. Using this approach to provide examples for adversarial training, we reduce the test se …
- 可访问链接（用于人工核对）：
  - arXiv: https://arxiv.org/abs/1412.6572
- 论文中引用位置：5 处
  - introduction.tex:31  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …
    - 段落（节选）：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。
  - background.tex:110  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：fast, method
    - 分数：J(title)=0.000; J(abstract)=0.024
    - 引用行：快速梯度符号法（Fast Gradient Sign Method，FGSM）由Goodfellow等人提出\cite{goodfellow2015fgsm}，是最具代表性的单步对抗攻击方法。FGSM利用损失函数关于输入的梯度方向构造对抗扰动，其生成公式为：
    - 段落（节选）：快速梯度符号法（Fast Gradient Sign Method，FGSM）由Goodfellow等人提出\cite{goodfellow2015fgsm}，是最具代表性的单步对抗攻击方法。FGSM利用损失函数关于输入的梯度方向构造对抗扰动，其生成公式为：
  - pipeline.tex:245  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
    - 段落（节选）：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
  - experiment.tex:83  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：FGSM \cite{goodfellow2015fgsm}
    - 段落（节选）：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini2017cw} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次，$\kappa=50$ …
  - experiment.tex:117  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：\item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。
    - 段落（节选）：\begin{enumerate} \item \textbf{Standard}：标准训练，无对抗扰动，仅使用干净样本训练，作为性能基线。 \item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。 \item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。 \item \textbf{Adaptive-Saliency-AT}：基于自适应原始梯度显著性图（$N=5$，$R=3$）的对抗性训练，训练时每轮对最显著区域施加自适应遮蔽。 \item \textbf{Mix-AT(Adaptive-Saliency+PGD)}：混合对抗性训练，以自适应原始梯度显著性图与PGD攻击共同训练，平衡遮蔽防御与梯度防御。 \item \textbf{Fi …

### `he2016resnet` — Deep residual learning for image recognition (2016)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/cvpr.2016.90
  - URL(来自Crossref): https://doi.org/10.1109/cvpr.2016.90
- 论文中引用位置：1 处
  - introduction.tex:9  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
    - 段落（节选）：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。

### `hinton2006deep` — A fast learning algorithm for deep belief nets (2006)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1162/neco.2006.18.7.1527
  - URL(来自Crossref): https://doi.org/10.1162/neco.2006.18.7.1527
- 论文中引用位置：1 处
  - introduction.tex:5  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …
    - 段落（节选）：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\cite{szegedy2014intriguing}。

### `kingma2015adam` — Adam: A method for stochastic optimization (2015)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1412.6980
- 证据 HTTP：200
- 摘要（节选）：
  - We introduce Adam, an algorithm for first-order gradient-based optimization of stochastic objective functions, based on adaptive estimates of lower-order moments. The method is straightforward to implement, is computationally efficient, has little memory requirements, is invariant to diagonal rescaling of the gradients, and is well suited for problems that are large in terms of data and/or parameters. The method is also appropriate for non-stationary objectives and problems with very noisy and/or sparse gradients. The hyper-parameters have intuitive interpretations and typically require little tuning. Some connections to related algorithms, on which Adam was inspired, are discussed. We also analyze the theoretical convergence properties of the algorithm and provide a regret bound on the convergence rate that is comparable to the best known results under the online convex optimization f …
- 可访问链接（用于人工核对）：
  - arXiv: https://arxiv.org/abs/1412.6980
- 论文中引用位置：3 处
  - background.tex:82  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：adam
    - 分数：J(title)=0.143; J(abstract)=0.011
    - 引用行：在优化算法方面，本文采用Adam优化器\cite{kingma2015adam}训练网络参数。Adam结合了动量（Momentum）和自适应学习率（RMSProp）的优势，对梯度的一阶矩和二阶矩分别进行指数移动平均估计，在不同任务和网络结构上均表现出良好的收敛性和鲁棒性，是深度学习训练中应用最为广泛的优化算法之一。
    - 段落（节选）：在优化算法方面，本文采用Adam优化器\cite{kingma2015adam}训练网络参数。Adam结合了动量（Momentum）和自适应学习率（RMSProp）的优势，对梯度的一阶矩和二阶矩分别进行指数移动平均估计，在不同任务和网络结构上均表现出良好的收敛性和鲁棒性，是深度学习训练中应用最为广泛的优化算法之一。
  - experiment.tex:24  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：adam
    - 分数：J(title)=0.053; J(abstract)=0.010
    - 引用行：优化器 & Adam \cite{kingma2015adam} \\
    - 段落（节选）：本文实验在如表~\ref{tab:env}~所示的软硬件环境下完成。 \begin{table}[htbp] \centering \caption{实验软硬件环境配置} \label{tab:env} \begin{tabular}{ll} \toprule \textbf{配置项} & \textbf{配置内容} \\ \midrule 操作系统 & Windows 11 \\ 编程语言 & Python 3.10 \\ 深度学习框架 & PyTorch 2.7.1 \\ CUDA版本 & CUDA 11.8 \\ 优化器 & Adam \cite{kingma2015adam} \\ \bottomrule \end{tabular} \end{table}
  - experiment.tex:128  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：adam
    - 分数：J(title)=0.167; J(abstract)=0.011
    - 引用行：所有策略均在相同的训练设置下进行：训练轮数50个epoch，使用Adam优化器\cite{kingma2015adam}，学习率调度一致，以确保比较的公平性。
    - 段落（节选）：所有策略均在相同的训练设置下进行：训练轮数50个epoch，使用Adam优化器\cite{kingma2015adam}，学习率调度一致，以确保比较的公平性。

### `kokhlikyan2020captum` — Captum: A unified and generic model interpretability library for {PyTorch} (2020)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/2009.07896
- 证据 HTTP：200
- 摘要（节选）：
  - In this paper we introduce a novel, unified, open-source model interpretability library for PyTorch [12]. The library contains generic implementations of a number of gradient and perturbation-based attribution algorithms, also known as feature, neuron and layer importance algorithms, as well as a set of evaluation metrics for these algorithms. It can be used for both classification and non-classification models including graph-structured models built on Neural Networks (NN). In this paper we give a high-level overview of supported attribution algorithms and show how to perform memory-efficient and scalable computations. We emphasize that the three main characteristics of the library are multimodality, extensibility and ease of use. Multimodality supports different modality of inputs such as image, text, audio or video. Extensibility allows adding new algorithms and features. The librar …
- 可访问链接（用于人工核对）：
  - arXiv(来自API): https://arxiv.org/abs/2009.07896
- 论文中引用位置：1 处
  - pipeline.tex:207  (cite)
    - 一致性：中 — 主题可能相关，但摘要关键词重合一般；建议人工核对具体结论
    - 关键词重合：captum, text, top
    - 分数：J(title)=0.059; J(abstract)=0.031
    - 引用行：具体而言，\textbf{固定 积分梯度归因 遮蔽攻击}的流程为：首先使用 Captum 库\cite{kokhlikyan2020captum}的 IntegratedGradients 模块（$n_{\text{steps}}=50$）计算每个像素的 积分梯度归因 归因值，随后对归因图执行与梯度显著性图相同的邻域聚合（式\eqref{eq:conv_sum}）、Top-$K$ 选取与掩码膨胀操作，最终生成遮蔽对抗样本。\text …
    - 段落（节选）：具体而言，\textbf{固定 积分梯度归因 遮蔽攻击}的流程为：首先使用 Captum 库\cite{kokhlikyan2020captum}的 IntegratedGradients 模块（$n_{\text{steps}}=50$）计算每个像素的 积分梯度归因 归因值，随后对归因图执行与梯度显著性图相同的邻域聚合（式\eqref{eq:conv_sum}）、Top-$K$ 选取与掩码膨胀操作，最终生成遮蔽对抗样本。\textbf{自适应 积分梯度归因 遮蔽攻击}则在归因计算替换为 积分梯度归因 的基础上，沿用自适应原始梯度显著性图（算法\ref{alg:adaptive_attack}）的逐样本提前终止与二维渐进搜索机制，实现基于 积分梯度归因 归因的自适应遮蔽。

### `krizhevsky2012imagenet` — ImageNet classification with deep convolutional neural networks (2012)

- 证据来源：NeurIPS Proceedings
- 证据链接：https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- 证据 HTTP：200
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- 论文中引用位置：2 处
  - introduction.tex:9  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
    - 段落（节选）：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
  - background.tex:11  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：convolutional, neural
    - 分数：J(title)=0.200; J(abstract)=0.000
    - 引用行：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。
    - 段落（节选）：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `kurakin2017adversarial` — Adversarial examples in the physical world (2017)

- 证据来源：arXiv(search score=0.98)
- 证据链接：https://arxiv.org/abs/1607.02533
- 证据 HTTP：200
- 摘要（节选）：
  - Most existing machine learning classifiers are highly vulnerable to adversarial examples. An adversarial example is a sample of input data which has been modified very slightly in a way that is intended to cause a machine learning classifier to misclassify it. In many cases, these modifications can be so subtle that a human observer does not even notice the modification at all, yet the classifier still makes a mistake. Adversarial examples pose security concerns because they could be used to perform an attack on machine learning systems, even if the adversary has no access to the underlying model. Up to now, all previous work have assumed a threat model in which the adversary can feed data directly into the machine learning classifier. This is not always the case for systems operating in the physical world, for example those which are using signals from cameras and other sensors as an …
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=S1OufnIlx
- 论文中引用位置：1 处
  - introduction.tex:20  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术 …
    - 段落（节选）：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术的可信部署具有重要意义。

### `lecun1998lenet` — Gradient-based learning applied to document recognition (1998)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/5.726791
  - URL(来自Crossref): https://doi.org/10.1109/5.726791
- 论文中引用位置：2 处
  - background.tex:41  (cite)
    - 一致性：不确定 — 未获取摘要且标题重合较少，建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：LeNet-5是由LeCun等人提出的经典卷积神经网络架构\cite{lecun1998lenet}，最初用于手写数字识别任务，是现代CNN架构的重要先驱，其网络结构如图\ref{fig:lenet5}
    - 段落（节选）：LeNet-5是由LeCun等人提出的经典卷积神经网络架构\cite{lecun1998lenet}，最初用于手写数字识别任务，是现代CNN架构的重要先驱，其网络结构如图\ref{fig:lenet5} 所示。 \begin{figure}[htbp] \centering \includegraphics[width=0.9\textwidth]{figures/lenet5.png} \caption{LeNet-5网络结构示意图} \label{fig:lenet5} \end{figure}
  - experiment.tex:41  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：本文以改进后的LeNet-5~\cite{lecun1998lenet}作为基础分类网络，网络结构详见~\ref{chpt:background}~表~\ref{tab:lenet5}。该网络在标准训练（无对抗扰动）下于MNIST测试集上可达99.0\%的干净准确率，表明基础模型具有充分的分类能力，为后续对抗性训练实验提供了可靠的性能基线。所有防御策略均选用相同的网络架构进行训练，仅在训练目标上加以区分，从而保证对比实验的公平性。
    - 段落（节选）：本文以改进后的LeNet-5~\cite{lecun1998lenet}作为基础分类网络，网络结构详见~\ref{chpt:background}~表~\ref{tab:lenet5}。该网络在标准训练（无对抗扰动）下于MNIST测试集上可达99.0\%的干净准确率，表明基础模型具有充分的分类能力，为后续对抗性训练实验提供了可靠的性能基线。所有防御策略均选用相同的网络架构进行训练，仅在训练目标上加以区分，从而保证对比实验的公平性。

### `lecun2010mnist` — MNIST handwritten digit database (2010)

- 证据来源：URL
- 证据链接：http://yann.lecun.com/exdb/mnist/
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - URL(启发式): http://yann.lecun.com/exdb/mnist/
- 论文中引用位置：1 处
  - experiment.tex:31  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：mnist
    - 分数：J(title)=0.111; J(abstract)=0.000
    - 引用行：本文采用MNIST手写数字数据集\cite{lecun2010mnist}作为目标数据集。MNIST是计算机视觉与对抗鲁棒性研究领域最经典的基准数据集之一，其主要特征如下：训练集包含60,000张样本，测试集包含10,000张样本；每个样本的图像分辨率为$28 \times 28$像素，单通道灰度图；标签覆盖0至9共10个数字类别；像素值归一化采用均值0.1307、标准差0.3081的标准化处理，即：
    - 段落（节选）：本文采用MNIST手写数字数据集\cite{lecun2010mnist}作为目标数据集。MNIST是计算机视觉与对抗鲁棒性研究领域最经典的基准数据集之一，其主要特征如下：训练集包含60,000张样本，测试集包含10,000张样本；每个样本的图像分辨率为$28 \times 28$像素，单通道灰度图；标签覆盖0至9共10个数字类别；像素值归一化采用均值0.1307、标准差0.3081的标准化处理，即：

### `lecun2015deeplearning` — Deep learning (2015)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1038/nature14539
  - URL(来自Crossref): https://doi.org/10.1038/nature14539
- 论文中引用位置：3 处
  - introduction.tex:5  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …
    - 段落（节选）：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\cite{szegedy2014intriguing}。
  - introduction.tex:9  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
    - 段落（节选）：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
  - background.tex:11  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。
    - 段落（节选）：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)

- 证据来源：arXiv(search score=0.98)
- 证据链接：https://arxiv.org/abs/1706.06083
- 证据 HTTP：200
- 摘要（节选）：
  - Recent work has demonstrated that deep neural networks are vulnerable to adversarial examples---inputs that are almost indistinguishable from natural data and yet classified incorrectly by the network. In fact, some of the latest findings suggest that the existence of adversarial attacks may be an inherent weakness of deep learning models. To address this problem, we study the adversarial robustness of neural networks through the lens of robust optimization. This approach provides us with a broad and unifying view on much of the prior work on this topic. Its principled nature also enables us to identify methods for both training and attacking neural networks that are reliable and, in a certain sense, universal. In particular, they specify a concrete security guarantee that would protect against any adversary. These methods let us train networks with significantly improved resistance to …
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=rJzIBfZAb
- 论文中引用位置：11 处
  - introduction.tex:22  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：面对对抗样本的挑战，学术界提出了多种防御思路，其中对抗性训练\cite{madry2018pgd}被广泛认为是目前最有效的防御范式。该方法使用对抗性样本进行训练，使得模型增强对扰动的鲁棒性。
    - 段落（节选）：面对对抗样本的挑战，学术界提出了多种防御思路，其中对抗性训练\cite{madry2018pgd}被广泛认为是目前最有效的防御范式。该方法使用对抗性样本进行训练，使得模型增强对扰动的鲁棒性。
  - introduction.tex:31  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性 …
    - 段落（节选）：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。
  - introduction.tex:39  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型 …
    - 段落（节选）：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:120  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：投影梯度下降攻击（Projected Gradient Descent，PGD）由Madry等人提出\cite{madry2018pgd}，是FGSM的多步迭代扩展，也是目前最为重要的对抗攻击基准之一。PGD在 $\varepsilon$-球约束集内反复执行梯度上升步骤，并在每步之后将扰动投影回约束集：
    - 段落（节选）：投影梯度下降攻击（Projected Gradient Descent，PGD）由Madry等人提出\cite{madry2018pgd}，是FGSM的多步迭代扩展，也是目前最为重要的对抗攻击基准之一。PGD在 $\varepsilon$-球约束集内反复执行梯度上升步骤，并在每步之后将扰动投影回约束集：
  - background.tex:152  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：对抗性训练的优化目标可形式化为一个min-max鞍点优化问题\cite{madry2018pgd}：
    - 段落（节选）：对抗性训练的优化目标可形式化为一个min-max鞍点优化问题\cite{madry2018pgd}：
  - background.tex:164  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：Madry等人从鞍点优化角度对该框架进行了理论分析，并证明使用PGD攻击近似求解内层最大化问题，能够有效提升模型的 $L_\infty$ 鲁棒性\cite{madry2018pgd}。
    - 段落（节选）：Madry等人从鞍点优化角度对该框架进行了理论分析，并证明使用PGD攻击近似求解内层最大化问题，能够有效提升模型的 $L_\infty$ 鲁棒性\cite{madry2018pgd}。
  - pipeline.tex:22  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：\item \textbf{对抗性训练}：将遮蔽攻击生成的对抗样本引入训练循环，并进一步提出混合对抗性训练策略，将遮蔽攻击与 PGD 攻击\cite{madry2018pgd}相结合，提升模型对多类型攻击的泛化防御能力。
    - 段落（节选）：\begin{enumerate} \item \textbf{关键区域定位}：利用特征归因图定位模型决策的关键像素区域，生成二值掩码 $M$。 \item \textbf{遮蔽攻击生成}：在关键区域定位的基础上，分别设计固定原始梯度显著性图与自适应原始梯度显著性图，前者适用于批量高效攻击，后者以最小代价实现逐样本自适应攻击。 \item \textbf{对抗性训练}：将遮蔽攻击生成的对抗样本引入训练循环，并进一步提出混合对抗性训练策略，将遮蔽攻击与 PGD 攻击\cite{madry2018pgd}相结合，提升模型对多类型攻击的泛化防御能力。 \end{enumerate}
  - pipeline.tex:245  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
    - 段落（节选）：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
  - experiment.tex:86  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：PGD \cite{madry2018pgd}
    - 段落（节选）：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini2017cw} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次，$\kappa=50$ …
  - experiment.tex:116  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：\item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。
    - 段落（节选）：\begin{enumerate} \item \textbf{Standard}：标准训练，无对抗扰动，仅使用干净样本训练，作为性能基线。 \item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。 \item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。 \item \textbf{Adaptive-Saliency-AT}：基于自适应原始梯度显著性图（$N=5$，$R=3$）的对抗性训练，训练时每轮对最显著区域施加自适应遮蔽。 \item \textbf{Mix-AT(Adaptive-Saliency+PGD)}：混合对抗性训练，以自适应原始梯度显著性图与PGD攻击共同训练，平衡遮蔽防御与梯度防御。 \item \textbf{Fi …
  - experiment.tex:533  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：这一差异的原因可能在于梯度掩蔽（gradient masking）\cite{madry2018pgd}对两种归因方法的影响不同。在评估对抗训练模型的遮蔽鲁棒性时，应同时使用多种归因方法进行攻击，以避免因单一归因方法受梯度掩蔽干扰而高估模型的真实防御能力。
    - 段落（节选）：这一差异的原因可能在于梯度掩蔽（gradient masking）\cite{madry2018pgd}对两种归因方法的影响不同。在评估对抗训练模型的遮蔽鲁棒性时，应同时使用多种归因方法进行攻击，以避免因单一归因方法受梯度掩蔽干扰而高估模型的真实防御能力。

### `muller2019labelsmoothing` — When does label smoothing help? (2019)

- 证据来源：arXiv(search score=1.00)
- 证据链接：https://arxiv.org/abs/1906.02629
- 证据 HTTP：200
- 摘要（节选）：
  - The generalization and learning speed of a multi-class neural network can often be significantly improved by using soft targets that are a weighted average of the hard targets and the uniform distribution over labels. Smoothing the labels in this way prevents the network from becoming over-confident and label smoothing has been used in many state-of-the-art models, including image classification, language translation and speech recognition. Despite its widespread use, label smoothing is still poorly understood. Here we show empirically that in addition to improving generalization, label smoothing improves model calibration which can significantly improve beam-search. However, we also observe that if a teacher network is trained with label smoothing, knowledge distillation into a student network is much less effective. To explain these observations, we visualize how label smoothing chan …
- 可访问链接（用于人工核对）：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2019/hash/f1748d6b0fd9d439f71450117eba2725-Abstract.html
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …
    - 段落（节选）：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `papernot2016distillation` — Distillation as a defense to adversarial perturbations against deep neural networks (2016)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/sp.2016.41
  - URL(来自Crossref): https://doi.org/10.1109/sp.2016.41
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 一致性：不确定 — 未获取摘要且标题重合较少，建议重点核对
    - 关键词重合：defense
    - 分数：J(title)=0.067; J(abstract)=0.000
    - 引用行：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M …
    - 段落（节选）：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `selvaraju2017gradcam` — Grad-CAM: Visual explanations from deep networks via gradient-based localization (2017)

- 证据来源：(none)
- 摘要：未获取
- 可访问链接（用于人工核对）：
  - DOI(来自Crossref): https://doi.org/10.1109/iccv.2017.74
  - URL(来自Crossref): https://doi.org/10.1109/iccv.2017.74
- 论文中引用位置：1 处
  - introduction.tex:49  (cite)
    - 一致性：中 — 仅能对齐标题/关键词（未获取摘要），建议人工核对
    - 关键词重合：cam, grad, gradient
    - 分数：J(title)=0.158; J(abstract)=0.000
    - 引用行：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sunda …
    - 段落（节选）：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射（Grad-CAM）\cite{selvaraju2017gradcam}利用卷积特征图的梯度生成类别区分性热力图，能够 …

### `shafahi2019free` — Adversarial training for free! (2019)

- 证据来源：arXiv(search score=1.00)
- 证据链接：https://arxiv.org/abs/1904.12843
- 证据 HTTP：200
- 摘要（节选）：
  - Adversarial training, in which a network is trained on adversarial examples, is one of the few defenses against adversarial attacks that withstands strong attacks. Unfortunately, the high cost of generating strong adversarial examples makes standard adversarial training impractical on large-scale problems like ImageNet. We present an algorithm that eliminates the overhead cost of generating adversarial examples by recycling the gradient information computed when updating model parameters. Our "free" adversarial training algorithm achieves comparable robustness to PGD adversarial training on the CIFAR-10 and CIFAR-100 datasets at negligible additional cost compared to natural training, and can be 7 to 30 times faster than other strong adversarial training methods. Using a single workstation with 4 P100 GPUs and 2 days of runtime, we can train a robust model for the large-scale ImageNet …
- 可访问链接（用于人工核对）：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2019/hash/7503cfacd12053d309b6bed5c89de212-Abstract.html
- 论文中引用位置：2 处
  - introduction.tex:39  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：free, pgd
    - 分数：J(title)=0.083; J(abstract)=0.024
    - 引用行：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型 …
    - 段落（节选）：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:172  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：free
    - 分数：J(title)=0.111; J(abstract)=0.025
    - 引用行：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。
    - 段落（节选）：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

### `simonyan2014saliency` — Deep inside convolutional networks: Visualising image classification models and saliency maps (2014)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1312.6034
- 证据 HTTP：200
- 摘要（节选）：
  - This paper addresses the visualisation of image classification models, learnt using deep Convolutional Networks (ConvNets). We consider two visualisation techniques, based on computing the gradient of the class score with respect to the input image. The first one generates an image, which maximises the class score [Erhan et al., 2009], thus visualising the notion of the class, captured by a ConvNet. The second technique computes a class saliency map, specific to a given image and class. We show that such maps can be employed for weakly supervised object segmentation using classification ConvNets. Finally, we establish the connection between the gradient-based ConvNet visualisation methods and deconvolutional networks [Zeiler et al., 2013].
- 可访问链接（用于人工核对）：
  - arXiv: https://arxiv.org/abs/1312.6034
- 论文中引用位置：3 处
  - introduction.tex:49  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：gradient, saliency
    - 分数：J(title)=0.045; J(abstract)=0.029
    - 引用行：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sunda …
    - 段落（节选）：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射（Grad-CAM）\cite{selvaraju2017gradcam}利用卷积特征图的梯度生成类别区分性热力图，能够 …
  - background.tex:190  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：saliency
    - 分数：J(title)=0.067; J(abstract)=0.049
    - 引用行：原始梯度显著性图（Vanilla Gradient Saliency Map）由Simonyan等人提出\cite{simonyan2014saliency}，是最基础也最直观的特征归因方法。其核心思想是：模型预测对某一输入像素的梯度绝对值越大，说明该像素对预测结果的影响越大，即该像素越"显著"。
    - 段落（节选）：原始梯度显著性图（Vanilla Gradient Saliency Map）由Simonyan等人提出\cite{simonyan2014saliency}，是最基础也最直观的特征归因方法。其核心思想是：模型预测对某一输入像素的梯度绝对值越大，说明该像素对预测结果的影响越大，即该像素越"显著"。
  - pipeline.tex:32  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：saliency
    - 分数：J(title)=0.053; J(abstract)=0.015
    - 引用行：原始梯度显著性图由 Simonyan 等人\cite{simonyan2014saliency}提出，其核心思想是利用模型对输入的一阶梯度信息衡量每个像素对预测结果的重要程度。给定分类模型 $f_{\theta}$、输入图像 $x \in \mathbb{R}^{C \times H \times W}$ 及真实类别 $y$，梯度显著性图定义为：
    - 段落（节选）：原始梯度显著性图由 Simonyan 等人\cite{simonyan2014saliency}提出，其核心思想是利用模型对输入的一阶梯度信息衡量每个像素对预测结果的重要程度。给定分类模型 $f_{\theta}$、输入图像 $x \in \mathbb{R}^{C \times H \times W}$ 及真实类别 $y$，梯度显著性图定义为： \begin{equation} S(x, y) = \left| \frac{\partial f_y(x)}{\partial x} \right| \label{eq:saliency} \end{equation} 其中 $f_y(x)$ 表示模型对类别 $y$ 的输出得分（logit），$|\cdot|$ 表示逐元素取绝对值。显著性值越高的像素，其微小变化对模型输出的影响越大，因此被视为模型决策的关键特征。

### `sundararajan2017ig` — Axiomatic attribution for deep networks (2017)

- 证据来源：arXiv
- 证据链接：https://arxiv.org/abs/1703.01365
- 证据 HTTP：200
- 摘要（节选）：
  - We study the problem of attributing the prediction of a deep network to its input features, a problem previously studied by several other works. We identify two fundamental axioms---Sensitivity and Implementation Invariance that attribution methods ought to satisfy. We show that they are not satisfied by most known attribution methods, which we consider to be a fundamental weakness of those methods. We use the axioms to guide the design of a new attribution method called Integrated Gradients. Our method requires no modification to the original network and is extremely simple to implement; it just needs a few calls to the standard gradient operator. We apply this method to a couple of image models, a couple of text models and a chemistry model, demonstrating its ability to debug networks, to extract rules from a network, and to enable users to engage with models better.
- 可访问链接（用于人工核对）：
  - arXiv(来自API): https://arxiv.org/abs/1703.01365
- 论文中引用位置：3 处
  - introduction.tex:49  (cite)
    - 一致性：中 — 主题可能相关，但摘要关键词重合一般；建议人工核对具体结论
    - 关键词重合：gradient, gradients, integrated
    - 分数：J(title)=0.000; J(abstract)=0.037
    - 引用行：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sunda …
    - 段落（节选）：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射（Grad-CAM）\cite{selvaraju2017gradcam}利用卷积特征图的梯度生成类别区分性热力图，能够 …
  - background.tex:204  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：gradients, integrated
    - 分数：J(title)=0.000; J(abstract)=0.028
    - 引用行：梯度积分（Integrated Gradients，积分梯度归因）由Sundararajan等人提出\cite{sundararajan2017ig}，是一种在理论上更为严格的特征归因方法。积分梯度归因的核心思想是沿从基线输入 $\mathbf{x}^{(0)}$（通常为全零图像）到目标输入 $\mathbf{x}$ 的路径上对梯度进行积分，从而计算每个特征对预测变化的累积贡献：
    - 段落（节选）：梯度积分（Integrated Gradients，积分梯度归因）由Sundararajan等人提出\cite{sundararajan2017ig}，是一种在理论上更为严格的特征归因方法。积分梯度归因的核心思想是沿从基线输入 $\mathbf{x}^{(0)}$（通常为全零图像）到目标输入 $\mathbf{x}$ 的路径上对梯度进行积分，从而计算每个特征对预测变化的累积贡献：
  - pipeline.tex:91  (cite)
    - 一致性：中 — 主题可能相关，但摘要关键词重合一般；建议人工核对具体结论
    - 关键词重合：gradients, integrated, text
    - 分数：J(title)=0.000; J(abstract)=0.037
    - 引用行：梯度积分（Integrated Gradients，积分梯度归因）\cite{sundararajan2017ig}是一种理论性质更完备的特征归因方法，其通过从基准图像 $x_0$（通常为全黑图像）到输入 $x$ 的路径积分计算归因值：
    - 段落（节选）：梯度积分（Integrated Gradients，积分梯度归因）\cite{sundararajan2017ig}是一种理论性质更完备的特征归因方法，其通过从基准图像 $x_0$（通常为全黑图像）到输入 $x$ 的路径积分计算归因值： \begin{equation} \text{积分梯度归因}_i(x, y) = (x_i - x_{0,i}) \cdot \int_0^1 \frac{\partial f_y(x_0 + \alpha(x - x_0))}{\partial x_i} \,\mathrm{d}\alpha \end{equation} 在实践中，积分通过 Riemann 近似以 $n_{\text{steps}}=50$ 步离散化，需要 50 次前向与反向传播，且依赖 Captum 等外部归因库。

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)

- 证据来源：arXiv(search score=0.98)
- 证据链接：https://arxiv.org/abs/1312.6199
- 证据 HTTP：200
- 摘要（节选）：
  - Deep neural networks are highly expressive models that have recently achieved state of the art performance on speech and visual recognition tasks. While their expressiveness is the reason they succeed, it also causes them to learn uninterpretable solutions that could have counter-intuitive properties. In this paper we report two such properties. First, we find that there is no distinction between individual high level units and random linear combinations of high level units, according to various methods of unit analysis. It suggests that it is the space, rather than the individual units, that contains of the semantic information in the high layers of neural networks. Second, we find that deep neural networks learn input-output mappings that are fairly discontinuous to a significant extend. We can cause the network to misclassify an image by applying a certain imperceptible perturbation …
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=kklr_MTHMRQjG
- 论文中引用位置：4 处
  - introduction.tex:5  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …
    - 段落（节选）：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\cite{szegedy2014intriguing}。
  - introduction.tex:5  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的 …
    - 段落（节选）：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\cite{szegedy2014intriguing}。
  - introduction.tex:11  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：然而，2014年Szegedy等人的开创性研究首次揭示了深度神经网络中普遍存在的对抗样本现象\cite{szegedy2014intriguing}：通过在原始输入图像上叠加人眼几乎无法察觉的微小扰动，便可以使分类能力极强的深度模型以极高置信度输出完全错误的预测结果。如图\ref{fig:adversarial_example}所示，原始图像经过细微扰动处理后得到对抗样本。对于人眼观察者而言，两幅图像视觉上完全一致，均呈现"熊猫"的 …
    - 段落（节选）：然而，2014年Szegedy等人的开创性研究首次揭示了深度神经网络中普遍存在的对抗样本现象\cite{szegedy2014intriguing}：通过在原始输入图像上叠加人眼几乎无法察觉的微小扰动，便可以使分类能力极强的深度模型以极高置信度输出完全错误的预测结果。如图\ref{fig:adversarial_example}所示，原始图像经过细微扰动处理后得到对抗样本。对于人眼观察者而言，两幅图像视觉上完全一致，均呈现"熊猫"的形象。然而深度神经网络的判断却截然不同：模型对原始输入能够正确分类，却对对抗样本给出了99.3\%置信度的"长臂猿"这一错误预测。
  - background.tex:88  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：（无）
    - 分数：J(title)=0.000; J(abstract)=0.000
    - 引用行：对抗样本（Adversarial Examples）是指在原始输入样本 $\mathbf{x}$ 的基础上，通过添加人眼难以察觉的微小扰动 $\boldsymbol{\delta}$，生成一个能够欺骗深度神经网络产生错误预测的输入 $\mathbf{x}' = \mathbf{x} + \boldsymbol{\delta}$。Szegedy等人在2014年首次系统性地发现并研究了这一现象\cite{szegedy2014intri …
    - 段落（节选）：对抗样本（Adversarial Examples）是指在原始输入样本 $\mathbf{x}$ 的基础上，通过添加人眼难以察觉的微小扰动 $\boldsymbol{\delta}$，生成一个能够欺骗深度神经网络产生错误预测的输入 $\mathbf{x}' = \mathbf{x} + \boldsymbol{\delta}$。Szegedy等人在2014年首次系统性地发现并研究了这一现象\cite{szegedy2014intriguing}，指出即便是在分类任务上表现优异的深度神经网络，也对精心设计的微小输入扰动极为敏感。

### `tramer2018ensemble` — Ensemble adversarial training: Attacks and defenses (2018)

- 证据来源：arXiv(search score=0.98)
- 证据链接：https://arxiv.org/abs/1705.07204
- 证据 HTTP：200
- 摘要（节选）：
  - Adversarial examples are perturbed inputs designed to fool machine learning models. Adversarial training injects such examples into training data to increase robustness. To scale this technique to large datasets, perturbations are crafted using fast single-step methods that maximize a linear approximation of the model's loss. We show that this form of adversarial training converges to a degenerate global minimum, wherein small curvature artifacts near the data points obfuscate a linear approximation of the loss. The model thus learns to generate weak perturbations, rather than defend against strong ones. As a result, we find that adversarial training remains vulnerable to black-box attacks, where we transfer perturbations computed on undefended models, as well as to a powerful novel single-step attack that escapes the non-smooth vicinity of the input data via a small random step. We fu …
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=rkZvSe-RZ
- 论文中引用位置：1 处
  - introduction.tex:33  (cite)
    - 一致性：低 — 摘要关键词重合很少（可能不对应此处论述），建议重点核对
    - 关键词重合：adversarial
    - 分数：J(title)=0.083; J(abstract)=0.009
    - 引用行：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑 …
    - 段落（节选）：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。

### `wong2020fast` — Fast is better than free: Revisiting adversarial training (2020)

- 证据来源：arXiv(search score=1.00)
- 证据链接：https://arxiv.org/abs/2001.03994
- 证据 HTTP：200
- 摘要（节选）：
  - Adversarial training, a method for learning robust deep networks, is typically assumed to be more expensive than traditional training due to the necessity of constructing adversarial examples via a first-order method like projected gradient decent (PGD). In this paper, we make the surprising discovery that it is possible to train empirically robust models using a much weaker and cheaper adversary, an approach that was previously believed to be ineffective, rendering the method no more costly than standard training in practice. Specifically, we show that adversarial training with the fast gradient sign method (FGSM), when combined with random initialization, is as effective as PGD-based training but has significantly lower cost. Furthermore we show that FGSM adversarial training can be further accelerated by using standard techniques for efficient training of deep networks, allowing us …
- 可访问链接（用于人工核对）：
  - OpenReview(来自API): https://openreview.net/forum?id=BJx040EFvH
- 论文中引用位置：2 处
  - introduction.tex:39  (cite)
    - 一致性：中 — 主题可能相关，但摘要关键词重合一般；建议人工核对具体结论
    - 关键词重合：fast, fgsm, free, pgd
    - 分数：J(title)=0.133; J(abstract)=0.033
    - 引用行：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型 …
    - 段落（节选）：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:172  (cite)
    - 一致性：不确定 — 上下文英文关键词较少，自动比对不稳定
    - 关键词重合：free
    - 分数：J(title)=0.077; J(abstract)=0.025
    - 引用行：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。
    - 段落（节选）：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

