---
title: "FML-共轭Dirichlet核闭式"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.4"
tags:
  - 傅里叶分析/cards
  - formula
  - Dirichlet核
  - 共轭核
  - 振荡
---

> [!abstract]
> 共轭 Dirichlet 核（Hilbert 变换型核）把“奇对称的部分和”写成显式三角比值，是对数估计与反例构造的起点。
>
>
# 可调用口径
- **对象**：$\widetilde D_N(x)=\sum_{|n|\le N}\mathrm{sgn}(n)e^{inx}$（$\mathrm{sgn}(0)=0$）。
- **闭式**：可化为 $\widetilde D_N(x)=\frac{\cos(x/2)-\cos((N+1/2)x)}{\sin(x/2)}$。
- **意义**：分母带来 $x=0$ 奇异性，分子带来频率随 $N$ 增大的振荡；二者叠加导致 $L^1$ 只呈对数控制。
- **常用用途**：用于证明相关算子在某些范数下的增长（如 $\log N$），以及构造“不是 Fourier 级数”的反例链条。
- **对照**：与 Dirichlet 核/Fejér 核相比，共轭核更偏“奇核/主值型”结构。

# 真源（勿在本卡重复维护）
![[3.4 问题#^pf-3-4-01a]]

# 关联
- [[EST-共轭Dirichlet核L1对数估计]]
- [[THM-Dirichlet点态收敛定理（BV_分段光滑）]]

