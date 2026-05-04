---
title: "MTH-用正交性计算有限和（Fourier trick）"
type: card
card_type: method
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.1–7.2"
tags:
  - 傅里叶分析/cards
  - method
  - finite-fourier
  - orthogonality
  - estimate
---

> [!abstract]
> 把“难求和/难计数”改写成“频域点乘/能量估计”，再用 Cauchy–Schwarz 或频域结构得到界。

# 可调用口径
- 把目标量写成内积或卷积点值（例如 $\sum f\overline g$ 或 $(f*g)(0)$）。
- 用 Plancherel 或卷积定理翻译到频域：$\sum f\overline g=(1/N)\sum \widehat f\,\overline{\widehat g}$，或 $(f*g)\widehat{\ }=\widehat f\widehat g$。
- 在频域做估计：用 Cauchy–Schwarz、支撑大小、或逐点界。
- 再反译回原问题（时域/计数意义）。

# 真源（勿在本卡重复维护）
![[7.1 Z_N上的Fourier分析#^mth-7-1-fourier-trick]]

