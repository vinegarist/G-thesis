# 论文审稿与参考文献核验报告

- 审核对象：`D:\软件\南开大学论文模板2026`
- 审核时间：2026-04-26
- 审核范围：实际参与编译的 `abstract.tex`、`introduction.tex`、`background.tex`、`pipeline.tex`、`experiment.tex`、`conclusion.tex`、`nkthesis.bib`
- 排除项：`manual.tex` 为模板示例文件，不参与论文正文编译

## 一、总体结论

这篇论文的主体结构完整，参考文献条目总体可检索，正文 `\cite` 与 `nkthesis.bib` 的 key 也能一一对应；未发现“正文引用了不存在的 bib key”或“bib 中缺条目”的硬错误。

但目前存在 5 类需要优先修正的问题：

1. **逻辑判断方向错误**：将“白盒攻击显著强于迁移攻击”的现象解释为“梯度掩蔽”，这在对抗鲁棒性文献中通常是反方向的。
2. **引用内容不匹配**：至少有一处把“物理世界对抗样本”文献写成了“医学影像误诊”证据。
3. **参考文献元数据错误**：`duan2023inequality` 的作者写错；`kokhlikyan2020captum` 的作者列表不准确。
4. **实验表格数值错误**：`experiment.tex` 中迁移攻击表的白盒 PGD/C&W 数值与现有核验报告不一致。
5. **因果推断过强**：从有限可视化和 4 个样本的集中度统计，直接推出 “IG 系统性偏离真正关键像素”，证据不足。

## 二、优先级最高的问题

### 1. 梯度掩蔽的定义与结论用了反

- 位置：`experiment.tex:692`
- 原文核心意思：把“白盒攻击下准确率很低、迁移攻击下准确率很高”定义为梯度掩蔽。
- 问题：这不是典型的“梯度掩蔽/obfuscated gradients”证据。更常见的可疑信号是 **白盒一阶攻击异常失效、黑盒/迁移或无梯度攻击反而更强**。而你这里的数据是：
  - 白盒 PGD：`4.63%`（正文表中）/ `4.78%`（已核验原始数据）
  - 迁移 PGD：`93.98%`
- 这更像“白盒攻击远强于迁移攻击”的正常现象，不能直接反推存在梯度掩蔽。
- 受影响位置：
  - `experiment.tex:677`
  - `experiment.tex:683`
  - `experiment.tex:692`
  - `experiment.tex:696`
  - `experiment.tex:710`
  - `experiment.tex:732`
- 修改建议：把“已发现梯度掩蔽”改成“存在可疑现象但证据不足，需要用 AutoAttack、无梯度攻击、BPDA/EOT 或 loss landscape 检查进一步验证”。

### 2. “不能仅凭白盒准确率得出该模型对梯度攻击极度脆弱”这一结论不成立

- 位置：`experiment.tex:696`
- 问题：如果白盒 PGD 准确率只有 `4.78%`，那么对于“白盒 PGD 威胁模型”这一命题，模型就是极度脆弱。迁移攻击弱，只能说明“替代模型生成的攻击不够贴合目标模型”，不能推翻白盒脆弱性本身。
- 建议改写为：
  - “该模型对白盒梯度攻击显著脆弱；但其黑盒迁移鲁棒性较高，二者差异值得进一步分析。”

### 3. `Kurakin 2017` 被错误地当成“医学影像误诊”证据

- 位置：`introduction.tex:20`
- 原文：`医学影像诊断系统中的微弱扰动则可能导致严重误诊\cite{kurakin2017adversarial}`
- 问题：`Kurakin et al., Adversarial examples in the physical world` 讨论的是物理世界对抗样本，不是医学影像诊断。
- 结论：这是**引文内容不对应**，应更换为真正讨论医学影像对抗攻击/误诊风险的论文，或删除该句。

### 4. `duan2023inequality` 文献作者写错

- 位置：`nkthesis.bib:198`
- 现有写法作者：`Rui Duan and Hu, Jinfeng and Li, Renhao and Chen, Tianyuan and Liang, Hao and Cao, Jiancheng and Ye, Jingzhi`
- 核验结果：该题名真实存在，但 OpenReview/DBLP 上的作者为：
  - `Ranjie Duan`
  - `Yuefeng Chen`
  - `Yao Zhu`
  - `Xiaojun Jia`
  - `Rong Zhang`
  - `Hui Xue`
- 结论：这是**参考文献元数据错误**，且该文在正文中被多次用作理论支撑，必须修正。

### 5. 迁移攻击表中的两个数值与已存在核验报告不一致

- 位置：`experiment.tex:671`
- 正文当前写法：
  - 白盒 PGD：`4.63%`
  - 白盒 C&W：`5.76%`
- 与 `data_verification_report.md` 的核验结果不一致：
  - 白盒 PGD 应为 `4.78%`
  - 白盒 C&W 应为 `5.73%`
- 这会进一步影响 `experiment.tex:677`、`683` 等对差值的描述。

## 三、中等优先级问题

### 1. 对 IG 失效机理的因果推断过强

- 位置：
  - `experiment.tex:519`
  - `experiment.tex:551`
- 问题：论文当前表述把“PGD-AT 下 IG 攻击效果下降”直接解释为“IG 归因系统性偏离真正关键像素”。但支撑证据主要是：
  - 少量可视化
  - 4 个样本的集中度统计
- 这些证据只能支持“存在这种可能性”或“观察到与此一致的现象”，还不足以支撑“系统性偏离”的强因果结论。
- 建议措辞降级为：
  - “提示 IG 归因可能受梯度结构变化影响而失真”
  - “该机制仍需更大样本量与更严格诊断实验验证”

### 2. “与 Duan 等人的理论一致”这类表述用得过满

- 位置：
  - `experiment.tex:515`
  - `experiment.tex:549`
  - `experiment.tex:564`
  - `experiment.tex:585`
- 问题：Duan 那篇文章讨论的是 `L_\infty` adversarial training 下的 feature inequality 与被 occlusion/perturbation 攻击的脆弱性。你文中将其直接扩展为“相互抵消趋势”的理论基础，属于**合理联想**，但不是原文已经严格证明的命题。
- 建议把“与理论一致”改为“与其观察到的现象相符”或“受到其结论启发”。

### 3. `MNIST` 条目更像数据集网页，不是正式论文

- 位置：`nkthesis.bib` 中 `lecun2010mnist`
- 结论：条目真实存在，但本质上是网页/数据集入口，不是标准期刊/会议论文。
- 建议：如果学校格式允许，可以保留为在线资源；否则建议注明 URL 与访问日期，或改为更规范的数据集引用格式。

### 4. `Captum` 条目的作者列表不准确

- 位置：`nkthesis.bib` 中 `kokhlikyan2020captum`
- 当前 bib 与公开记录相比，至少存在以下问题：
  - `Natalia Kliushkina` 被写成 `Natalia Kliber`
  - 作者列表缺少 `Carlos Araya`、`Siqi Yan`
- 结论：论文存在，但 BibTeX 元数据应修正。

## 四、正文引用与 BibTeX 键一致性检查

实际参与编译的章节中，正文使用的 26 个 `cite key` 全都能在 `nkthesis.bib` 中找到对应条目，未发现：

- “正文引用 key 不存在”
- “文献表缺条目”
- “正文章节使用了模板 `manual.tex` 的示例引用”

## 五、逐条参考文献真实性核验

说明：

- `状态=真实` 表示可检索到对应论文/数据集/网页。
- `引用准确性` 分为 `准确`、`基本准确`、`有误需改`。
- “标准引用建议”用于替换或校正当前 bib 信息。

| key | 论文中当前条目是否真实存在 | 引用准确性 | 核验链接 | 标准引用建议 |
|---|---|---|---|---|
| `hinton2006deep` | 真实 | 准确 | https://direct.mit.edu/neco/article/18/7/1527/7054/A-Fast-Learning-Algorithm-for-Deep-Belief-Nets | Hinton, G. E., Osindero, S., & Teh, Y.-W. (2006). A fast learning algorithm for deep belief nets. *Neural Computation, 18*(7), 1527-1554. |
| `szegedy2014intriguing` | 真实 | 基本准确 | https://arxiv.org/abs/1312.6199 | Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2014). Intriguing properties of neural networks. *ICLR 2014*. |
| `goodfellow2015fgsm` | 真实 | 基本准确 | https://arxiv.org/abs/1412.6572 | Goodfellow, I. J., Shlens, J., & Szegedy, C. (2015). Explaining and harnessing adversarial examples. *ICLR 2015*. |
| `madry2018pgd` | 真实 | 准确 | https://openreview.net/forum?id=rJzIBfZAb | Madry, A., Makelov, A., Schmidt, L., Tsipras, D., & Vladu, A. (2018). Towards deep learning models resistant to adversarial attacks. *ICLR 2018*. |
| `carlini2017cw` | 真实 | 准确 | https://ieeexplore.ieee.org/document/7958570 | Carlini, N., & Wagner, D. (2017). Towards evaluating the robustness of neural networks. *IEEE Symposium on Security and Privacy*, 39-57. |
| `croce2020autoattack` | 真实 | 基本准确 | https://proceedings.mlr.press/v119/croce20b.html | Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML 2020*, 2206-2216. |
| `simonyan2014saliency` | 真实 | 基本准确 | https://arxiv.org/abs/1312.6034 | Simonyan, K., Vedaldi, A., & Zisserman, A. (2014). Deep inside convolutional networks: Visualising image classification models and saliency maps. *ICLR Workshop 2014 / arXiv:1312.6034*. |
| `sundararajan2017ig` | 真实 | 准确 | https://proceedings.mlr.press/v70/sundararajan17a.html | Sundararajan, M., Taly, A., & Yan, Q. (2017). Axiomatic attribution for deep networks. *ICML 2017*, 3319-3328. |
| `selvaraju2017gradcam` | 真实 | 准确 | https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html | Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. *ICCV 2017*, 618-626. |
| `lecun1998lenet` | 真实 | 准确 | https://ieeexplore.ieee.org/document/726791 | LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proceedings of the IEEE, 86*(11), 2278-2324. |
| `shafahi2019free` | 真实 | 准确 | https://proceedings.neurips.cc/paper/2019/hash/7503cfacd12053d309b6bed5c89de212-Abstract.html | Shafahi, A., Najibi, M., Ghiasi, A., Xu, Z., Dickerson, J., Studer, C., Davis, L. S., Taylor, G., & Goldstein, T. (2019). Adversarial training for free! *NeurIPS 2019*, 3358-3369. |
| `wong2020fast` | 真实 | 准确 | https://openreview.net/forum?id=BJx040EFvH | Wong, E., Rice, L., & Kolter, J. Z. (2020). Fast is better than free: Revisiting adversarial training. *ICLR 2020*. |
| `brown2017adversarialpatch` | 真实 | 基本准确 | https://arxiv.org/abs/1712.09665 | Brown, T. B., Mane, D., Roy, A., Abadi, M., & Gilmer, J. (2017). Adversarial patch. *arXiv:1712.09665*. |
| `papernot2016distillation` | 真实 | 准确 | https://ieeexplore.ieee.org/document/7546538 | Papernot, N., McDaniel, P., Wu, X., Jha, S., & Swami, A. (2016). Distillation as a defense to adversarial perturbations against deep neural networks. *IEEE Symposium on Security and Privacy*, 582-597. |
| `cohen2019certified` | 真实 | 准确 | https://proceedings.mlr.press/v97/cohen19c.html | Cohen, J. M., Rosenfeld, E., & Kolter, J. Z. (2019). Certified adversarial robustness via randomized smoothing. *ICML 2019*, 1310-1320. |
| `kingma2015adam` | 真实 | 基本准确 | https://arxiv.org/abs/1412.6980 | Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. *ICLR 2015 / arXiv:1412.6980*. |
| `lecun2015deeplearning` | 真实 | 准确 | https://www.nature.com/articles/nature14539 | LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature, 521*(7553), 436-444. |
| `krizhevsky2012imagenet` | 真实 | 准确 | https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html | Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *NeurIPS 2012*, 1097-1105. |
| `he2016resnet` | 真实 | 准确 | https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html | He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. *CVPR 2016*, 770-778. |
| `kurakin2017adversarial` | 真实 | **正文使用场景错误** | https://arxiv.org/abs/1607.02533 | Kurakin, A., Goodfellow, I., & Bengio, S. (2017). Adversarial examples in the physical world. *ICLR Workshop 2017 / arXiv:1607.02533*. |
| `eykholt2018robust` | 真实 | 准确 | https://openaccess.thecvf.com/content_cvpr_2018/html/Eykholt_Robust_Physical-World_Attacks_CVPR_2018_paper.html | Eykholt, K., Evtimov, I., Fernandes, E., Li, B., Rahmati, A., Xiao, C., Prakash, A., Kohno, T., & Song, D. (2018). Robust physical-world attacks on deep learning models. *CVPR 2018*, 1625-1634. |
| `tramer2018ensemble` | 真实 | 准确 | https://openreview.net/forum?id=rkZvSe-RZ | Tramèr, F., Kurakin, A., Papernot, N., Goodfellow, I., Boneh, D., & McDaniel, P. (2018). Ensemble adversarial training: Attacks and defenses. *ICLR 2018*. |
| `muller2019labelsmoothing` | 真实 | 准确 | https://proceedings.neurips.cc/paper/2019/hash/f1748d6b0fd9d439f71450117eba2725-Abstract.html | Müller, R., Kornblith, S., & Hinton, G. E. (2019). When does label smoothing help? *NeurIPS 2019*, 4694-4703. |
| `lecun2010mnist` | 真实 | **资源类型需注明** | http://yann.lecun.com/exdb/mnist/ | LeCun, Y., Cortes, C., & Burges, C. J. C. *MNIST handwritten digit database*. Online resource: http://yann.lecun.com/exdb/mnist/ |
| `kokhlikyan2020captum` | 真实 | **作者信息有误需改** | https://arxiv.org/abs/2009.07896 | Kokhlikyan, N., Miglani, V., Martin, M., Wang, E., Alsallakh, B., Reynolds, J., Melnikov, A., Kliushkina, N., Araya, C., Yan, S., & Reblitz-Richardson, O. (2020). Captum: A unified and generic model interpretability library for PyTorch. *CoRR, abs/2009.07896*. |
| `duan2023inequality` | 真实 | **作者信息有误需改** | https://openreview.net/forum?id=4t9q35BxGr | Duan, R., Chen, Y., Zhu, Y., Jia, X., Zhang, R., & Xue, H. (2023). Inequality phenomenon in $l_{\infty}$-adversarial training, and its unrealized threats. *ICLR 2023*. |

## 六、建议的最小修订清单

1. 修正 `nkthesis.bib` 中 `duan2023inequality` 和 `kokhlikyan2020captum` 的作者信息。
2. 修正 `experiment.tex:671` 表中的 `4.63 -> 4.78`、`5.76 -> 5.73`。
3. 删除或替换 `introduction.tex:20` 中 `kurakin2017adversarial` 对“医学影像误诊”的引用。
4. 将所有“已经证明存在梯度掩蔽”的表述降级为“存在可疑现象，需要进一步验证”。
5. 将“不能仅凭白盒准确率得出该模型对梯度攻击极度脆弱”的结论改为“对白盒梯度攻击脆弱，但黑盒迁移攻击效果较弱，两者差异需要进一步解释”。
6. 将“IG 系统性偏离真正关键像素”的断言改为更谨慎的经验性表述。

## 七、核验依据

- 本地文件：
  - `main.tex`
  - `introduction.tex`
  - `background.tex`
  - `pipeline.tex`
  - `experiment.tex`
  - `nkthesis.bib`
  - `data_verification_report.md`
- 在线核验来源：
  - OpenReview
  - PMLR
  - CVF Open Access
  - IEEE Xplore
  - Nature
  - arXiv
  - Yann LeCun MNIST 页面
  - DBLP
