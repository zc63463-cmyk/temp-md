---
title: "第03章 Fourier级数的收敛性 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第03章 Fourier级数的收敛性"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
date: 2026-04-23
cssclasses:
  - wide-page
---

> [!abstract]
> 本章主线（去重版）：先在 $L^2(\mathbb T)$ 的 Hilbert 空间框架中用正交投影“解决收敛”（Bessel/Parseval/均方收敛），再在点态层面直面 Dirichlet 核的奇异振荡，解释为什么逐点收敛需要额外局部正则性（BV/分段光滑），并与第02章的 Cesàro/Abel（好核）求和法形成对照。
>
^overview

## 0. 导航（本章权威条目与承接）
- 章节汇总（已存在）：[[第03章 Fourier级数的收敛性 — 章节汇总]]
- 节笔记（本轮范围）：[[3.1 Fourier级数的均方收敛]]｜[[3.2 逐点收敛]]｜[[3.3 练习]]｜[[3.4 问题]]
- 本章 cards（高优先级；去重版入口）：
  - 定理（3.1/3.2）：[[THM-Bessel不等式（L2）]]、[[THM-Parseval恒等式（圆周Plancherel）]]、[[THM-Fourier部分和的L2均方收敛（S_N f→f）]]、[[THM-Dirichlet点态收敛定理（BV_分段光滑）]]
  - 公式/对象/方法（3.1/3.2）：[[FML-L2内积（圆周归一化）]]、[[FML-Fourier系数与部分和（定义）]]、[[FML-Dirichlet核闭式（sin比）]]、[[MTH-对称化（偶核→左右平均）]]、[[OBJ-有界变差（BV）在Dirichlet收敛中的角色]]
  - 练习/问题（3.3/3.4，本轮新增/更新）：[[THM-ℓ2空间完备性（Hilbert）]]、[[THM-Wirtinger–Poincaré不等式（周期_均值为0）]]、[[THM-导数在L2则Fourier级数绝对收敛]]、[[FML-共轭Dirichlet核闭式]]、[[EST-共轭Dirichlet核L1对数估计]]、[[THM-Euler型恒等式（cot求和）]]、[[FML-ζ(2m) 与 Bernoulli 数]]、[[FML-Bernoulli多项式 Fourier 展开]]

> [!note] 去重策略声明（全库）
> - 第03章（3.1–3.4）作为“收敛口径 + 训练题真源”权威条目：$L^2$ 正交展开（均方收敛/Parseval）、点态收敛门槛（Dirichlet 核 + BV）、以及练习/问题中的标准估计与经典恒等式推导。
> - 第02章（尤其 2.3/2.4/2.5）作为“核/卷积/好核/求和法权威条目”：遇到同一结论/定义/估计时，优先回链第02章真源 block-id，避免重复维护。
> - cards 只转引真源 block-id；证明/公式的可维护真源固定在节笔记（或第02章权威条目）中。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 3.1 Bessel 不等式：[[3.1 Fourier级数的均方收敛#^pf-3-1-bessel]]
> - 3.1 Parseval 恒等式：[[3.1 Fourier级数的均方收敛#^pf-3-1-parseval]]
> - 3.1 $L^2$ 均方收敛（$S_N f\to f$）：[[3.1 Fourier级数的均方收敛#^pf-3-1-l2-convergence]]
> - 3.2 Dirichlet 点态收敛定理（BV/分段光滑）：[[3.2 逐点收敛#^pf-3-2-dirichlet-convergence]]
> - 3.3 $\ell^2$ 完备性：[[3.3 练习#^pf-3-3-02]]
> - 3.3 Wirtinger–Poincaré：[[3.3 练习#^pf-3-3-11]]
> - 3.3 $f'\in L^2$ 推绝对收敛：[[3.3 练习#^pf-3-3-14]]
> - 3.4 共轭 Dirichlet 核闭式：[[3.4 问题#^pf-3-4-01a]]
> - 3.4 共轭 Dirichlet 核 $L^1$ 对数估计：[[3.4 问题#^pf-3-4-01b]]
> - 3.4 Euler 型求和恒等式（cot）：[[3.4 问题#^pf-3-4-03b]]
> - 3.4 $\zeta(2m)$ 与 Bernoulli 数：[[3.4 问题#^pf-3-4-04c]]
> - 3.4 Bernoulli 多项式 Fourier 展开：[[3.4 问题#^pf-3-4-05e]]
>
# 1. 本章主线（3.1 → 3.2）
1) 3.1 先选“最稳的收敛概念”：在 $L^2$ 中，指数系是正交系，Fourier 系数是投影坐标；于是 Bessel/Parseval/均方收敛都是 Hilbert 空间结构性结论。  
2) 3.2 再面对“最直观也最难的收敛概念”：逐点收敛。此时部分和 $S_N f$ 的核是 Dirichlet 核，具有奇异性与强振荡；点态极限是否存在取决于函数的局部正则性（BV/分段光滑）能否压住振荡积分。  
3) 与第02章对照：Cesàro/Abel 对应 Fejér/Poisson 好核（非负、质量集中、$L^1$ 有界）→ 收敛更稳健；Dirichlet 核不满足好核性质 → 需要更强假设。

> [!warning] 易混淆点（章级入口）
> - Bessel（$\le$）到 Parseval（$=$）的门槛是“完备性/稠密性”，不是代数技巧。
> - $S_N$ 在 3.1 中是正交投影（最佳均方逼近），并不等价于“平滑平均”；因此 $L^2$ 收敛与点态收敛之间存在本质鸿沟。
> - 跳点处取平均是偶核对称化的结构必然，不是人为规定。
> - BV/分段光滑的作用是把误差项转成可控的振荡积分，从而使用 Dirichlet 判别/分部积分得到趋零。
> - “连续 ⇒ 部分和点态收敛”是错误命题：存在连续函数使 Fourier 部分和在某点发散；正确层级是 Carleson/Hunt 的“几乎处处收敛”（$L^p, p>1$）。
> - Cesàro/Abel 更稳是因为换了“核”：好核绕开了 Dirichlet 核的非正/振荡/$L^1$ 增长困境。
>
# 2. 外部参考（用于“补充理解/易混淆点”callout 的权威来源）
- Mikko Salo, *Fourier analysis: Lecture notes, Fall 2024*（含 $L^2$ Fourier series 与 pointwise convergence 章节）  
  https://users.jyu.fi/~salomi/teaching/fa_2024/Fourier_lectures_2024.pdf （访问：2026-04-23）
- Michael Gressman (UPenn), *Advanced Analysis: Convergence of Partial Sums*（Dirichlet kernel 性质与点态收敛推导）  
  https://www2.math.upenn.edu/~gressman/analysis/08b-convergence.html （访问：2026-04-23）
- Michael Gressman (UPenn), *Advanced Analysis: Summability Methods*（与 Cesàro/Abel 的对照）  
  https://www2.math.upenn.edu/~gressman/analysis/08b-summability.html （访问：2026-04-23）
- Naoki Saito (UC Davis), *A Brief History of the Convergence of the Fourier Series*（du Bois-Reymond 反例与 Carleson/Hunt 层级）  
  https://www.math.ucdavis.edu/~saito/courses/ACHA.suppl/fs.pdf （访问：2026-04-23）
- T. W. Körner, *A First Look at Fourier Analysis*（“为何会有收敛问题”的直觉与对照）  
  http://www.dpmms.cam.ac.uk/~twk10/Prince.pdf （访问：2026-04-23）
- NIST DLMF（Bernoulli numbers/polynomials 与相关公式；可长期引用）  
  https://dlmf.nist.gov/24.2 （访问：2026-04-23）  
  https://dlmf.nist.gov/24.8 （访问：2026-04-23）  
  https://dlmf.nist.gov/25.6 （访问：2026-04-23）
- Eremenko（补充理解：留数法推导 Bernoulli/ζ 关系的短讲义）  
  https://www.math.purdue.edu/~eremenko/dvi/bernoulli.pdf （访问：2026-04-23）
