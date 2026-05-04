---
title: "MTH-截断+尾部控制实现无界域换序"
type: card
card_type: method
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.3"
tags:
  - 傅里叶分析/cards
  - method
  - integration
  - improper-integral
  - fubini
---

> [!abstract]
> 在 $R^d$ 上做换序/卷积型积分时，常见错误是“直接交换”而忽略无穷远。正确模板是：先在有界域 $Q_N$ 上使用 9.2 的换序，再让 $N\to\infty$，用尾部估计证明截断极限是 Cauchy，从而合法地把换序推广到全空间。

# 可调用口径
- Step A（截断）：先证明在 $Q_N$ 上的等式/换序成立。
- Step B（尾部）：估计 $|I_M-I_N|\le \int_{|x|\ge N} |f(x)|dx$ 并证明其 $\to 0$。
- Step C（放极限）：把 $N\to\infty$ 的极限放入等式两侧，得到全空间版本。

# 真源（勿在本卡重复维护）
![[9.3 反常积分 R_d上的积分#^pf-9-3-existence]]
![[9.3 反常积分 R_d上的积分#^pf-9-3-fubini-slow]]
![[9.3 反常积分 R_d上的积分#^pf-9-3-convolution-swap]]

