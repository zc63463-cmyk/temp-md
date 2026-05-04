---
title: "OBJ-Riemann可积（上和_下和）"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.1"
tags:
  - 傅里叶分析/cards
  - object
  - integration
  - riemann
---

> [!abstract]
> Riemann 可积性的主角不是“原函数”，而是“上和/下和能否被分割压到任意小差距”。这一定义天然适配 Fourier 分析中的“换序/极限交换”合法性检查：先把问题变成对 $U(P,f)-L(P,f)$ 的控制。

# 可调用口径
- 上和 $U(P,f)$/下和 $L(P,f)$ 是“对每个小区间取最坏值再加权”的积分近似。
- $f$ 可积 $\Leftrightarrow$ 对任意 $\varepsilon$ 存在分割使 $U-L<\varepsilon$。
- 积分值被定义为所有上和的下确界（等于所有下和的上确界）。

# 真源（勿在本卡重复维护）
![[9.1 Riemann可积函数的定义#^def-9-1-upper-lower-sums]]
![[9.1 Riemann可积函数的定义#^def-9-1-riemann-integrable]]
![[9.1 Riemann可积函数的定义#^def-9-1-integral-value]]

