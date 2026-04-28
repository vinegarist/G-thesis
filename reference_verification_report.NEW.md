# 参考文献与引用核查报告

- 生成时间：2026-04-28 13:23:20
- Bib 文件：nkthesis.bib
- 扫描 TeX 文件数：8
- 联网校验：是

## 总览

- Bib 条目数：26
- 论文中出现的 cite key 数（去重）：26
- cite 总次数（含重复）：62
- 缺失的 cite key（TeX 中出现但 Bib 中不存在）：0
- 未被引用的 Bib 条目（Bib 中存在但 TeX 未引用）：0

## 逐条核查

### `brown2017adversarialpatch` — Adversarial patch (2017)

- 类型：@article
- 作者：Brown, Tom B. and Man{\'e}, Dandelion and Roy, Aurko and Abadi, Mart{\'\i}n and Gilmer, Justin
- 期刊/出处：arXiv preprint arXiv:1712.09665
- 链接：
  - arXiv: https://arxiv.org/abs/1712.09665
- 存在性校验：ok — arXiv 页面可访问
- arXiv HTTP：200
- 论文中引用位置：2 处
  - introduction.tex:33  (cite)
    - 上下文：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。
  - background.tex:142  (cite)
    - 上下文：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志上粘贴特定图案，成功使自动驾驶系统的视觉识别模型产生严重误判，揭示了此类攻击在安全关键领域的现实威胁性。

### `carlini2017cw` — Towards evaluating the robustness of neural networks (2017)

- 类型：@inproceedings
- 作者：Carlini, Nicholas and Wagner, David
- 会议/出处：IEEE Symposium on Security and Privacy (SP)
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/sp.2017.49
  - URL(来自Crossref): https://doi.org/10.1109/sp.2017.49
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Towards Evaluating the Robustness of Neural Networks; year=2017; DOI=10.1109/sp.2017.49; score=1.00
- 论文中引用位置：2 处
  - background.tex:130  (cite)
    - 上下文：Carlini和Wagner提出的C\&W攻击\cite{carlini2017cw}将对抗样本生成转化为连续优化问题，通过最小化以下目标函数来寻找扰动幅度尽可能小的高置信度对抗样本：
  - experiment.tex:89  (cite)
    - 上下文：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini …

### `cohen2019certified` — Certified adversarial robustness via randomized smoothing (2019)

- 类型：@inproceedings
- 作者：Cohen, Jeremy M. and Rosenfeld, Elan and Kolter, J. Zico
- 会议/出处：International Conference on Machine Learning (ICML)
- 链接：
  - arXiv(来自API): https://arxiv.org/abs/1902.02918
- 存在性校验：ok — arXiv（API 匹配 score=1.00）页面可访问
- arXiv HTTP：200
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 上下文：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `croce2020autoattack` — Reliable evaluation of adversarial robustness with an ensemble of attacks (2020)

- 类型：@inproceedings
- 作者：Croce, Francesco and Hein, Matthias
- 会议/出处：International Conference on Machine Learning (ICML)
- 链接：
  - arXiv(来自API): https://arxiv.org/abs/2003.01690
- 存在性校验：ok — arXiv（API 匹配 score=0.88）页面可访问
- arXiv HTTP：200
- 论文中引用位置：1 处
  - introduction.tex:31  (cite)
    - 上下文：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。

### `duan2023inequality` — Inequality phenomenon in $L_\infty$ adversarial training, and its unrealized threats (2023)

- 类型：@inproceedings
- 作者：Duan, Rui and Hu, Jinfeng and Li, Renhao and Chen, Tianyuan and Liang, Hao and Cao, Jiancheng and Ye, Jingzhi
- 会议/出处：International Conference on Learning Representations (ICLR)
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=4t9q35BxGr
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：4 处
  - introduction.tex:81  (cite)
    - 上下文：4) 对所提方法进行了系统的实验评估。在MNIST数据集上对九种防御策略（涵盖显著性归因与积分梯度归因两类遮蔽训练）在七类攻击下进行了对比测试，分析了遮蔽参数对攻击效果的影响。实验验证了原始梯度显著性遮蔽攻击与梯度攻击在混合训练模型上呈现抵消效应\cite{duan2023inequality}。
  - experiment.tex:525  (cite)
    - 上下文：Duan等人\cite{duan2023inequality}指出，$L_\infty$ 对抗性训练会导致模型决策依赖发生"特征不均等"（feature inequality）现象，即少数像素的归因显著放大，模型对显著像素的依赖性增强。该现象意味着遮蔽攻击与梯度类对抗性训练可能存在\textbf{相互抵消趋势}：针对遮蔽攻击，遮蔽对抗训练的鲁棒性高于标准模型，而梯度对抗训练 (PGD-AT、FGSM-AT) 反而低于（或与标准模型持平）；针对梯度类攻击，规律完全相反。本文实验中这一现象在原始归因下得到了清晰体现，但在 积分梯度归因 归因下未呈现。具体数据汇总于表~\ref{tab:cancel}。
  - experiment.tex:529  (cite)
    - 上下文：对于原始梯度遮蔽攻击，PGD-AT的防御准确率（固定$k$=9: 70.11\%）略低于Standard（71.19\%），自适应显著性遮蔽下亦然（PGD-AT: 30.12\% vs. Standard: 34.33\%），表明PGD对抗性训练不仅未能提升对显著性遮蔽的防御，反而使模型略微更加脆弱。这一“抵消效应”与Duan等人\cite{duan2023inequality}发现的$L_\infty$对抗性训练导致特征归因不均等（inequality）现象一致：PGD-AT迫使模型将决策依据集中于极少数像素，一旦这些像素被遮蔽，模型即丧失判别能力。
  - experiment.tex:580  (cite)
    - 上下文：\textbf{PGD-AT 使原始梯度归因显著集中（2.47倍）。}标准模型上 原始梯度归因相对分散（集中度0.064），而 PGD-AT 训练后 原始梯度归因集中度跃升至 0.157，与 Duan 等人\cite{duan2023inequality}发现的“$L_\infty$对抗性训练导致特征归因不均等（inequality）”现象一致。此时 PGD-AT 模型将决策依赖压缩到极少数像素，一旦这些像素被准确遮蔽，模型即丧失判别能力，因此 PGD-AT 对原始梯度显著性图的防御能力反而略低于 Standard（70.11\% vs.\ 71.19\%）。

### `eykholt2018robust` — Robust physical-world attacks on deep learning models (2018)

- 类型：@inproceedings
- 作者：Eykholt, Kevin and Evtimov, Ivan and Fernandes, Earlence and Li, Bo and Rahmati, Amir and Xiao, Chaowei and Prakash, Atul and Kohno, Tadayoshi and Song, Dawn
- 会议/出处：IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/cvpr.2018.00175
  - URL(来自Crossref): https://doi.org/10.1109/cvpr.2018.00175
- 存在性校验：ok — Crossref 匹配成功（score=0.87）
- Crossref：title=Robust Physical-World Attacks on Deep Learning Visual Classification; year=2018; DOI=10.1109/cvpr.2018.00175; score=0.87
- 论文中引用位置：3 处
  - introduction.tex:20  (cite)
    - 上下文：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术的可信部署具有重要意义。
  - introduction.tex:33  (cite)
    - 上下文：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。
  - background.tex:142  (cite)
    - 上下文：基于遮蔽的对抗攻击与物理世界中的真实威胁场景高度契合。Brown等人提出的对抗性贴片（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像中放置一块可打印的对抗性图案，无论贴片放置在何位置，均能使分类器产生目标误分类，且该方法在物理打印环境下仍具有可迁移性。Eykholt等人\cite{eykholt2018robust}进一步将遮蔽攻击应用于道路标志识别场景，通过在停车标志上粘贴特定图案，成功使自动驾驶系统的视觉识别模型产生严重误判，揭示了此类攻击在安全关键领域的现实威胁性。

### `goodfellow2015fgsm` — Explaining and harnessing adversarial examples (2015)

- 类型：@article
- 作者：Goodfellow, Ian J. and Shlens, Jonathon and Szegedy, Christian
- 期刊/出处：arXiv preprint arXiv:1412.6572
- 链接：
  - arXiv: https://arxiv.org/abs/1412.6572
- 存在性校验：ok — arXiv 页面可访问
- arXiv HTTP：200
- 论文中引用位置：5 处
  - introduction.tex:31  (cite)
    - 上下文：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。
  - background.tex:110  (cite)
    - 上下文：快速梯度符号法（Fast Gradient Sign Method，FGSM）由Goodfellow等人提出\cite{goodfellow2015fgsm}，是最具代表性的单步对抗攻击方法。FGSM利用损失函数关于输入的梯度方向构造对抗扰动，其生成公式为：
  - pipeline.tex:245  (cite)
    - 上下文：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
  - experiment.tex:83  (cite)
    - 上下文：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini …
  - experiment.tex:117  (cite)
    - 上下文：\begin{enumerate} \item \textbf{Standard}：标准训练，无对抗扰动，仅使用干净样本训练，作为性能基线。 \item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。 \item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。 \item \textbf{Adaptive-Saliency-AT}：基于自适应原始梯度显著性图（$N=5$，$R=3$）的对抗性训练，训练时每轮对最显著区域施加自适应遮蔽。 \item \textbf{Mix-AT(Adaptive-Saliency+PGD)}： …

### `he2016resnet` — Deep residual learning for image recognition (2016)

- 类型：@inproceedings
- 作者：He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian
- 会议/出处：IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/cvpr.2016.90
  - URL(来自Crossref): https://doi.org/10.1109/cvpr.2016.90
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Deep Residual Learning for Image Recognition; year=2016; DOI=10.1109/cvpr.2016.90; score=1.00
- 论文中引用位置：1 处
  - introduction.tex:9  (cite)
    - 上下文：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。

### `hinton2006deep` — A fast learning algorithm for deep belief nets (2006)

- 类型：@article
- 作者：Hinton, Geoffrey E. and Osindero, Simon and Teh, Yee-Whye
- 期刊/出处：Neural Computation
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1162/neco.2006.18.7.1527
  - URL(来自Crossref): https://doi.org/10.1162/neco.2006.18.7.1527
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=A Fast Learning Algorithm for Deep Belief Nets; year=2006; DOI=10.1162/neco.2006.18.7.1527; score=1.00
- 论文中引用位置：1 处
  - introduction.tex:5  (cite)
    - 上下文：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\c …

### `kingma2015adam` — Adam: A method for stochastic optimization (2015)

- 类型：@article
- 作者：Kingma, Diederik P. and Ba, Jimmy
- 期刊/出处：arXiv preprint arXiv:1412.6980
- 链接：
  - arXiv: https://arxiv.org/abs/1412.6980
- 存在性校验：ok — arXiv 页面可访问
- arXiv HTTP：200
- 论文中引用位置：3 处
  - background.tex:82  (cite)
    - 上下文：在优化算法方面，本文采用Adam优化器\cite{kingma2015adam}训练网络参数。Adam结合了动量（Momentum）和自适应学习率（RMSProp）的优势，对梯度的一阶矩和二阶矩分别进行指数移动平均估计，在不同任务和网络结构上均表现出良好的收敛性和鲁棒性，是深度学习训练中应用最为广泛的优化算法之一。
  - experiment.tex:24  (cite)
    - 上下文：本文实验在如表~\ref{tab:env}~所示的软硬件环境下完成。 \begin{table}[htbp] \centering \caption{实验软硬件环境配置} \label{tab:env} \begin{tabular}{ll} \toprule \textbf{配置项} & \textbf{配置内容} \\ \midrule 操作系统 & Windows 11 \\ 编程语言 & Python 3.10 \\ 深度学习框架 & PyTorch 2.7.1 \\ CUDA版本 & CUDA 11.8 \\ 优化器 & Adam \cite{kingma2015adam} \\ \bottomrule \end{tabular} \end{table}
  - experiment.tex:128  (cite)
    - 上下文：所有策略均在相同的训练设置下进行：训练轮数50个epoch，使用Adam优化器\cite{kingma2015adam}，学习率调度一致，以确保比较的公平性。

### `kokhlikyan2020captum` — Captum: A unified and generic model interpretability library for {PyTorch} (2020)

- 类型：@inproceedings
- 作者：Kokhlikyan, Narine and Miglani, Vivek and Martin, Miguel and Wang, Edward and Alsallakh, Bilal and Reynolds, Jonathan and Melnikov, Alexander and Kliber, Natalia and Fan, Carlos and Stepka, Dilber and Reblitz-Richardson, Orion
- 会议/出处：ICML Workshop on Human Interpretability in Machine Learning
- 链接：
  - arXiv(来自API): https://arxiv.org/abs/2009.07896
- 存在性校验：ok — arXiv（API 匹配 score=1.00）页面可访问
- arXiv HTTP：200
- 论文中引用位置：1 处
  - pipeline.tex:207  (cite)
    - 上下文：具体而言，\textbf{固定 积分梯度归因 遮蔽攻击}的流程为：首先使用 Captum 库\cite{kokhlikyan2020captum}的 IntegratedGradients 模块（$n_{\text{steps}}=50$）计算每个像素的 积分梯度归因 归因值，随后对归因图执行与梯度显著性图相同的邻域聚合（式\eqref{eq:conv_sum}）、Top-$K$ 选取与掩码膨胀操作，最终生成遮蔽对抗样本。\textbf{自适应 积分梯度归因 遮蔽攻击}则在归因计算替换为 积分梯度归因 的基础上，沿用自适应原始梯度显著性图（算法\ref{alg:adaptive_attack}）的逐样本提前终止与二维渐进搜索机制，实现基于 积分梯度归因 归因的自适应遮蔽。

### `krizhevsky2012imagenet` — ImageNet classification with deep convolutional neural networks (2012)

- 类型：@inproceedings
- 作者：Krizhevsky, Alex and Sutskever, Ilya and Hinton, Geoffrey E.
- 会议/出处：Advances in Neural Information Processing Systems (NeurIPS)
- 链接：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：2 处
  - introduction.tex:9  (cite)
    - 上下文：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
  - background.tex:11  (cite)
    - 上下文：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `kurakin2017adversarial` — Adversarial examples in the physical world (2017)

- 类型：@inproceedings
- 作者：Kurakin, Alexey and Goodfellow, Ian and Bengio, Samy
- 会议/出处：International Conference on Learning Representations (ICLR) Workshop
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=S1OufnIlx
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：1 处
  - introduction.tex:20  (cite)
    - 上下文：这一发现动摇了深度学习系统可靠性高的固有印象，凸显了其固有的脆弱性。后续研究进一步表明，对抗样本的威胁已从数字仿真环境扩展至现实物理世界：Eykholt等人验证了在交通标志上施加特定扰动可诱导自动驾驶系统做出错误决策\cite{eykholt2018robust}，医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}。这些安全问题表明，开展深度模型对抗鲁棒性研究对于实现人工智能技术的可信部署具有重要意义。

### `lecun1998lenet` — Gradient-based learning applied to document recognition (1998)

- 类型：@article
- 作者：LeCun, Yann and Bottou, L{\'e}on and Bengio, Yoshua and Haffner, Patrick
- 期刊/出处：Proceedings of the IEEE
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/5.726791
  - URL(来自Crossref): https://doi.org/10.1109/5.726791
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Gradient-based learning applied to document recognition; year=1998; DOI=10.1109/5.726791; score=1.00
- 论文中引用位置：2 处
  - background.tex:41  (cite)
    - 上下文：LeNet-5是由LeCun等人提出的经典卷积神经网络架构\cite{lecun1998lenet}，最初用于手写数字识别任务，是现代CNN架构的重要先驱，其网络结构如图\ref{fig:lenet5} 所示。 \begin{figure}[htbp] \centering \includegraphics[width=0.9\textwidth]{figures/lenet5.png} \caption{LeNet-5网络结构示意图} \label{fig:lenet5} \end{figure}
  - experiment.tex:41  (cite)
    - 上下文：本文以改进后的LeNet-5~\cite{lecun1998lenet}作为基础分类网络，网络结构详见~\ref{chpt:background}~表~\ref{tab:lenet5}。该网络在标准训练（无对抗扰动）下于MNIST测试集上可达99.0\%的干净准确率，表明基础模型具有充分的分类能力，为后续对抗性训练实验提供了可靠的性能基线。所有防御策略均选用相同的网络架构进行训练，仅在训练目标上加以区分，从而保证对比实验的公平性。

### `lecun2010mnist` — MNIST handwritten digit database (2010)

- 类型：@article
- 作者：LeCun, Yann and Cortes, Corinna and Burges, Christopher J. C.
- 期刊/出处：ATT Labs [Online]
- 链接：
  - URL(启发式): http://yann.lecun.com/exdb/mnist/
- 存在性校验：ok — URL 可访问
- Crossref：title=NGO Database; year=2011; DOI=10.5860/choice.49-1239; score=0.49
- URL HTTP：200
- 论文中引用位置：1 处
  - experiment.tex:31  (cite)
    - 上下文：本文采用MNIST手写数字数据集\cite{lecun2010mnist}作为目标数据集。MNIST是计算机视觉与对抗鲁棒性研究领域最经典的基准数据集之一，其主要特征如下：训练集包含60,000张样本，测试集包含10,000张样本；每个样本的图像分辨率为$28 \times 28$像素，单通道灰度图；标签覆盖0至9共10个数字类别；像素值归一化采用均值0.1307、标准差0.3081的标准化处理，即：

### `lecun2015deeplearning` — Deep learning (2015)

- 类型：@article
- 作者：LeCun, Yann and Bengio, Yoshua and Hinton, Geoffrey
- 期刊/出处：Nature
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1038/nature14539
  - URL(来自Crossref): https://doi.org/10.1038/nature14539
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Deep learning; year=2015; DOI=10.1038/nature14539; score=1.00
- 论文中引用位置：3 处
  - introduction.tex:5  (cite)
    - 上下文：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\c …
  - introduction.tex:9  (cite)
    - 上下文：近年来，深度学习技术在计算机视觉领域取得了举世瞩目的突破性进展\cite{lecun2015deeplearning}。以卷积神经网络为代表的深度模型在图像分类、目标检测、语义分割等核心任务上的表现已全面超越传统方法，甚至在部分基准测试中达到乃至超越人类水平\cite{krizhevsky2012imagenet,he2016resnet}。深度学习模型深刻改变着各行各业的技术格局。
  - background.tex:11  (cite)
    - 上下文：卷积神经网络（Convolutional Neural Network，CNN）是深度学习领域最具影响力的模型架构之一，在图像分类、目标检测、语义分割等计算机视觉任务中取得了突破性进展\cite{lecun2015deeplearning,krizhevsky2012imagenet}。与传统的全连接神经网络相比，卷积神经网络通过局部连接和权重共享机制，极大地降低了参数量，同时利用卷积核自动提取图像的局部空间特征，具有平移不变性。

### `madry2018pgd` — Towards deep learning models resistant to adversarial attacks (2018)

- 类型：@inproceedings
- 作者：Madry, Aleksander and Makelov, Aleksandar and Schmidt, Ludwig and Tsipras, Dimitris and Vladu, Adrian
- 会议/出处：International Conference on Learning Representations (ICLR)
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=rJzIBfZAb
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：11 处
  - introduction.tex:22  (cite)
    - 上下文：面对对抗样本的挑战，学术界提出了多种防御思路，其中对抗性训练\cite{madry2018pgd}被广泛认为是目前最有效的防御范式。该方法使用对抗性样本进行训练，使得模型增强对扰动的鲁棒性。
  - introduction.tex:31  (cite)
    - 上下文：在基于梯度的白盒攻击方面，Goodfellow等人提出的快速梯度符号法（FGSM）\cite{goodfellow2015fgsm}是最早的高效攻击算法之一，通过沿损失函数梯度方向施加一步扰动实现攻击，计算代价低但攻击成功率有限。Madry等人将攻击问题形式化为约束优化问题，提出的投影梯度下降攻击（PGD）\cite{madry2018pgd}通过多步迭代逼近最优对抗扰动，被公认为Lp范数约束下最强的一阶攻击方法，至今仍是对抗鲁棒性研究的基准参照。Croce与Hein提出的AutoAttack\cite{croce2020autoattack}将多种互补攻击策略集成为标准化评估框架，有效规避了单一攻击方法评估的局限性，已成为对抗鲁棒性基准评测的通行标准。
  - introduction.tex:39  (cite)
    - 上下文：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:120  (cite)
    - 上下文：投影梯度下降攻击（Projected Gradient Descent，PGD）由Madry等人提出\cite{madry2018pgd}，是FGSM的多步迭代扩展，也是目前最为重要的对抗攻击基准之一。PGD在 $\varepsilon$-球约束集内反复执行梯度上升步骤，并在每步之后将扰动投影回约束集：
  - background.tex:152  (cite)
    - 上下文：对抗性训练的优化目标可形式化为一个min-max鞍点优化问题\cite{madry2018pgd}：
  - background.tex:164  (cite)
    - 上下文：Madry等人从鞍点优化角度对该框架进行了理论分析，并证明使用PGD攻击近似求解内层最大化问题，能够有效提升模型的 $L_\infty$ 鲁棒性\cite{madry2018pgd}。
  - pipeline.tex:22  (cite)
    - 上下文：\begin{enumerate} \item \textbf{关键区域定位}：利用特征归因图定位模型决策的关键像素区域，生成二值掩码 $M$。 \item \textbf{遮蔽攻击生成}：在关键区域定位的基础上，分别设计固定原始梯度显著性图与自适应原始梯度显著性图，前者适用于批量高效攻击，后者以最小代价实现逐样本自适应攻击。 \item \textbf{对抗性训练}：将遮蔽攻击生成的对抗样本引入训练循环，并进一步提出混合对抗性训练策略，将遮蔽攻击与 PGD 攻击\cite{madry2018pgd}相结合，提升模型对多类型攻击的泛化防御能力。 \end{enumerate}
  - pipeline.tex:245  (cite)
    - 上下文：基于遮蔽攻击的对抗性训练能够有效提升模型对遮蔽类攻击的防御能力，但由于训练时仅使用遮蔽攻击样本，模型可能在抵御梯度类攻击（如 FGSM\cite{goodfellow2015fgsm}、PGD\cite{madry2018pgd}）方面出现退化。这一现象源于对抗性训练的\textbf{攻击类型特异性}：模型倾向于拟合训练时所见攻击的扰动分布，对训练时未见的攻击类型泛化能力有限。
  - experiment.tex:86  (cite)
    - 上下文：\begin{table}[htbp] \centering \caption{攻击方法参数配置} \label{tab:attack_config} \begin{tabular}{lp{3cm}p{5.5cm}} \toprule \textbf{攻击方法} & \textbf{关键参数} & \textbf{参数说明} \\ \midrule FGSM \cite{goodfellow2015fgsm} & $\varepsilon = 0.1$ & 单步梯度符号攻击，扰动在$L_\infty$球内 \\ PGD \cite{madry2018pgd} & $\varepsilon=0.1$，$\alpha=0.025$，迭代20次 & 多步投影梯度下降攻击 \\ C\&W \cite{carlini …
  - experiment.tex:116  (cite)
    - 上下文：\begin{enumerate} \item \textbf{Standard}：标准训练，无对抗扰动，仅使用干净样本训练，作为性能基线。 \item \textbf{PGD-AT}：基于PGD对抗样本的对抗性训练\cite{madry2018pgd}，代表梯度类攻击防御的主流范式。 \item \textbf{FGSM-AT}：基于FGSM对抗样本的对抗性训练\cite{goodfellow2015fgsm}，计算开销较小的梯度防御方法。 \item \textbf{Adaptive-Saliency-AT}：基于自适应原始梯度显著性图（$N=5$，$R=3$）的对抗性训练，训练时每轮对最显著区域施加自适应遮蔽。 \item \textbf{Mix-AT(Adaptive-Saliency+PGD)}： …
  - experiment.tex:533  (cite)
    - 上下文：这一差异的原因可能在于梯度掩蔽（gradient masking）\cite{madry2018pgd}对两种归因方法的影响不同。在评估对抗训练模型的遮蔽鲁棒性时，应同时使用多种归因方法进行攻击，以避免因单一归因方法受梯度掩蔽干扰而高估模型的真实防御能力。

### `muller2019labelsmoothing` — When does label smoothing help? (2019)

- 类型：@inproceedings
- 作者：M{\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.
- 会议/出处：Advances in Neural Information Processing Systems (NeurIPS)
- 链接：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2019/hash/f1748d6b0fd9d439f71450117eba2725-Abstract.html
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 上下文：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `papernot2016distillation` — Distillation as a defense to adversarial perturbations against deep neural networks (2016)

- 类型：@inproceedings
- 作者：Papernot, Nicolas and McDaniel, Patrick and Wu, Xi and Jha, Somesh and Swami, Ananthram
- 会议/出处：IEEE Symposium on Security and Privacy (SP)
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/sp.2016.41
  - URL(来自Crossref): https://doi.org/10.1109/sp.2016.41
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Distillation as a Defense to Adversarial Perturbations Against Deep Neural Networks; year=2016; DOI=10.1109/sp.2016.41; score=1.00
- 论文中引用位置：1 处
  - introduction.tex:41  (cite)
    - 上下文：在其他防御路径方面，Papernot等人提出的防御蒸馏方法\cite{papernot2016distillation}通过知识蒸馏平滑模型的输出分布，降低对梯度信息的敏感性以缓解梯度攻击的威胁。Cohen等人提出的随机平滑认证防御（Certified Defense）\cite{cohen2019certified}通过对输入施加高斯噪声并统计预测分布，为模型鲁棒性提供可证明的理论保证，是目前为数不多具有严格理论背书的防御方法。M\"{u}ller等人研究了标签平滑正则化在对抗鲁棒性提升中的作用\cite{muller2019labelsmoothing}，证明了正则化手段对模型泛化鲁棒性的积极影响。

### `selvaraju2017gradcam` — Grad-CAM: Visual explanations from deep networks via gradient-based localization (2017)

- 类型：@inproceedings
- 作者：Selvaraju, Ramprasaath R. and Cogswell, Michael and Das, Abhishek and Vedantam, Ramakrishna and Parikh, Devi and Batra, Dhruv
- 会议/出处：IEEE International Conference on Computer Vision (ICCV)
- 链接：
  - DOI(来自Crossref): https://doi.org/10.1109/iccv.2017.74
  - URL(来自Crossref): https://doi.org/10.1109/iccv.2017.74
- 存在性校验：ok — Crossref 匹配成功（score=1.00）
- Crossref：title=Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization; year=2017; DOI=10.1109/iccv.2017.74; score=1.00
- 论文中引用位置：1 处
  - introduction.tex:49  (cite)
    - 上下文：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射 …

### `shafahi2019free` — Adversarial training for free! (2019)

- 类型：@inproceedings
- 作者：Shafahi, Ali and Najibi, Mahyar and Ghiasi, Amin and Xu, Zheng and Dickerson, John and Studer, Christoph and Davis, Larry S. and Taylor, Gavin and Goldstein, Tom
- 会议/出处：Advances in Neural Information Processing Systems (NeurIPS)
- 链接：
  - NeurIPS Proceedings(自动解析): https://proceedings.neurips.cc/paper_files/paper/2019/hash/7503cfacd12053d309b6bed5c89de212-Abstract.html
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：2 处
  - introduction.tex:39  (cite)
    - 上下文：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:172  (cite)
    - 上下文：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

### `simonyan2014saliency` — Deep inside convolutional networks: Visualising image classification models and saliency maps (2014)

- 类型：@article
- 作者：Simonyan, Karen and Vedaldi, Andrea and Zisserman, Andrew
- 期刊/出处：arXiv preprint arXiv:1312.6034
- 链接：
  - arXiv: https://arxiv.org/abs/1312.6034
- 存在性校验：ok — arXiv 页面可访问
- arXiv HTTP：200
- 论文中引用位置：3 处
  - introduction.tex:49  (cite)
    - 上下文：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射 …
  - background.tex:190  (cite)
    - 上下文：原始梯度显著性图（Vanilla Gradient Saliency Map）由Simonyan等人提出\cite{simonyan2014saliency}，是最基础也最直观的特征归因方法。其核心思想是：模型预测对某一输入像素的梯度绝对值越大，说明该像素对预测结果的影响越大，即该像素越"显著"。
  - pipeline.tex:32  (cite)
    - 上下文：原始梯度显著性图由 Simonyan 等人\cite{simonyan2014saliency}提出，其核心思想是利用模型对输入的一阶梯度信息衡量每个像素对预测结果的重要程度。给定分类模型 $f_{\theta}$、输入图像 $x \in \mathbb{R}^{C \times H \times W}$ 及真实类别 $y$，梯度显著性图定义为： \begin{equation} S(x, y) = \left| \frac{\partial f_y(x)}{\partial x} \right| \label{eq:saliency} \end{equation} 其中 $f_y(x)$ 表示模型对类别 $y$ 的输出得分（logit），$|\cdot|$ 表示逐元素取绝对值。显著性值越高的像素，其微小变 …

### `sundararajan2017ig` — Axiomatic attribution for deep networks (2017)

- 类型：@inproceedings
- 作者：Sundararajan, Mukund and Taly, Ankur and Yan, Qiqi
- 会议/出处：International Conference on Machine Learning (ICML)
- 链接：
  - arXiv(来自API): https://arxiv.org/abs/1703.01365
- 存在性校验：ok — arXiv（API 匹配 score=1.00）页面可访问
- arXiv HTTP：200
- 论文中引用位置：3 处
  - introduction.tex:49  (cite)
    - 上下文：原始梯度显著性图（Vanilla Gradient Saliency）由Simonyan等人率先提出\cite{simonyan2014saliency}，其核心思想是将网络输出对输入的梯度绝对值作为各像素重要性的度量。该方法计算简洁，仅需一次反向传播即可获得全图的重要性评分，是计算效率最高的特征归因方法之一。Sundararajan等人提出的梯度积分（Integrated Gradients, 积分梯度归因）\cite{sundararajan2017ig}在梯度显著性图的基础上引入了公理化约束，通过沿基线到输入的路径对梯度进行积分，满足灵敏性与实现不变性等理论性质，归因精度显著优于原始梯度方法，但代价是需要多次前向与反向传播，计算开销远高于原始梯度显著性图。Selvaraju等人提出的梯度加权类激活映射 …
  - background.tex:204  (cite)
    - 上下文：梯度积分（Integrated Gradients，积分梯度归因）由Sundararajan等人提出\cite{sundararajan2017ig}，是一种在理论上更为严格的特征归因方法。积分梯度归因的核心思想是沿从基线输入 $\mathbf{x}^{(0)}$（通常为全零图像）到目标输入 $\mathbf{x}$ 的路径上对梯度进行积分，从而计算每个特征对预测变化的累积贡献：
  - pipeline.tex:91  (cite)
    - 上下文：梯度积分（Integrated Gradients，积分梯度归因）\cite{sundararajan2017ig}是一种理论性质更完备的特征归因方法，其通过从基准图像 $x_0$（通常为全黑图像）到输入 $x$ 的路径积分计算归因值： \begin{equation} \text{积分梯度归因}_i(x, y) = (x_i - x_{0,i}) \cdot \int_0^1 \frac{\partial f_y(x_0 + \alpha(x - x_0))}{\partial x_i} \,\mathrm{d}\alpha \end{equation} 在实践中，积分通过 Riemann 近似以 $n_{\text{steps}}=50$ 步离散化，需要 50 次前向与反向传播，且依赖 Captum 等 …

### `szegedy2014intriguing` — Intriguing properties of neural networks (2014)

- 类型：@inproceedings
- 作者：Szegedy, Christian and Zaremba, Wojciech and Sutskever, Ilya and Bruna, Joan and Erhan, Dumitru and Goodfellow, Ian and Fergus, Rob
- 会议/出处：International Conference on Learning Representations (ICLR)
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=kklr_MTHMRQjG
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：4 处
  - introduction.tex:5  (cite)
    - 上下文：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\c …
  - introduction.tex:5  (cite)
    - 上下文：人工智能的研究历史可追溯至二十世纪中叶，该领域经历了多次高潮与低谷。在2006年，Hinton等人提出的深度学习方法\cite{hinton2006deep}引发了新一轮研究热潮。深度学习之所以能够推动人工智能技术实现质的飞跃，关键在于其在视觉感知、语言理解等复杂任务上展现出的卓越能力，部分场景下甚至超越了人类表现\cite{lecun2015deeplearning}。然而，这一看似强大的技术体系却存在一个致命弱点：对对抗性样本的高度敏感。对抗性样本通过在原始数据上叠加精心设计的细微扰动，可使深度神经网络产生置信度极高但完全错误的判断\cite{szegedy2014intriguing}。Szegedy等人于2014年的实证研究表明，包括当时最先进深度神经网络在内的多种机器学习模型均难以抵御此类攻击\c …
  - introduction.tex:11  (cite)
    - 上下文：然而，2014年Szegedy等人的开创性研究首次揭示了深度神经网络中普遍存在的对抗样本现象\cite{szegedy2014intriguing}：通过在原始输入图像上叠加人眼几乎无法察觉的微小扰动，便可以使分类能力极强的深度模型以极高置信度输出完全错误的预测结果。如图\ref{fig:adversarial_example}所示，原始图像经过细微扰动处理后得到对抗样本。对于人眼观察者而言，两幅图像视觉上完全一致，均呈现"熊猫"的形象。然而深度神经网络的判断却截然不同：模型对原始输入能够正确分类，却对对抗样本给出了99.3\%置信度的"长臂猿"这一错误预测。
  - background.tex:88  (cite)
    - 上下文：对抗样本（Adversarial Examples）是指在原始输入样本 $\mathbf{x}$ 的基础上，通过添加人眼难以察觉的微小扰动 $\boldsymbol{\delta}$，生成一个能够欺骗深度神经网络产生错误预测的输入 $\mathbf{x}' = \mathbf{x} + \boldsymbol{\delta}$。Szegedy等人在2014年首次系统性地发现并研究了这一现象\cite{szegedy2014intriguing}，指出即便是在分类任务上表现优异的深度神经网络，也对精心设计的微小输入扰动极为敏感。

### `tramer2018ensemble` — Ensemble adversarial training: Attacks and defenses (2018)

- 类型：@inproceedings
- 作者：Tram{\`e}r, Florian and Kurakin, Alexey and Papernot, Nicolas and Goodfellow, Ian and Boneh, Dan and McDaniel, Patrick
- 会议/出处：International Conference on Learning Representations (ICLR)
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=rkZvSe-RZ
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：1 处
  - introduction.tex:33  (cite)
    - 上下文：在更贴近物理世界的攻击方面，Brown等人提出的对抗补丁攻击（Adversarial Patch）\cite{brown2017adversarialpatch}通过在图像的局部矩形区域叠加显著可见的对抗图案实现攻击，对遮蔽类攻击场景具有直接的启示意义。Eykholt等人进一步证明，在交通标志上物理粘贴特定图案可稳定欺骗自动驾驶视觉系统\cite{eykholt2018robust}，将对抗攻击的威胁从数字仿真推向真实部署场景。在黑盒攻击方面，Tram\`{e}r等人揭示了对抗样本的跨模型可迁移性\cite{tramer2018ensemble}，表明在代理模型上生成的对抗扰动可有效迁移至未知目标模型，从而实现无需访问目标模型梯度的黑盒攻击，大幅降低了现实攻击的实施门槛。

### `wong2020fast` — Fast is better than free: Revisiting adversarial training (2020)

- 类型：@inproceedings
- 作者：Wong, Eric and Rice, Leslie and Kolter, J. Zico
- 会议/出处：International Conference on Learning Representations (ICLR)
- 链接：
  - OpenReview(来自API): https://openreview.net/forum?id=BJx040EFvH
- 存在性校验：ok — URL 可访问
- URL HTTP：200
- 论文中引用位置：2 处
  - introduction.tex:39  (cite)
    - 上下文：对抗性训练是目前被广泛认可的最有效防御方法。Madry等人提出的标准对抗性训练（PGD-AT）\cite{madry2018pgd}在每轮训练迭代中以PGD生成的对抗样本替换干净样本进行训练，显著提升了模型对梯度攻击的鲁棒性，奠定了对抗性训练的基础范式。然而，PGD-AT的计算开销巨大，制约了其在大规模任务上的应用。Shafahi等人提出的Free-AT\cite{shafahi2019free}通过"免费"复用梯度信息同步更新模型参数与对抗扰动，将训练代价降低至与标准训练相近的水平。Wong等人提出的Fast-AT\cite{wong2020fast}采用随机初始化的FGSM攻击替代多步PGD，在损失较小的精度代价下大幅缩短了训练时间。
  - background.tex:172  (cite)
    - 上下文：为降低对抗性训练的计算开销，Wong等人提出了基于随机初始化FGSM的快速对抗性训练方法（FGSM-AT）\cite{wong2020fast}，通过单步FGSM攻击代替多步PGD生成对抗样本，将训练成本降低至接近标准训练的水平；Shafahi等人提出的Free对抗性训练\cite{shafahi2019free}则通过在单次前向-反向传播中同时更新扰动参数和模型参数，进一步提高了训练效率，在保持较好鲁棒性的同时大幅削减了计算成本。

