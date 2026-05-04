---
title: "THM-Z_N上Plancherel（Parseval）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - finite-fourier
  - Z_N
  - Plancherel
  - Parseval
---

> [!abstract]
> 离散能量恒等式：时域平方和与频域平方和只差一个固定比例（由归一化决定）。

# 可调用口径
- 这是“有限维正交展开”的能量守恒公式；用于把估计搬到频域做。
- 常见用法：配合 Cauchy–Schwarz 得到指数和/卷积量的上界（Fourier trick）。
- 关键条件：与反演/定义使用同一套归一化常数；本卡按节笔记约定。
- 误区：不要把它误记成 $\sum|f|^2=\sum|\hat f|^2$；是否等距取决于是否把 $1/N$ 放进前向变换。

# 真源（勿在本卡重复维护）
![[7.1 Z_N上的Fourier分析#^thm-7-1-plancherel]]
![[7.1 Z_N上的Fourier分析#^pf-7-1-plancherel]]

