---
title: "THM-Lebesgue判别（Riemann可积⇔不连续点零测）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - integration
  - riemann
  - null-set
---

> [!abstract]
> 有界函数 Riemann 可积的充要条件：它的不连续点集是零测集。这是“Riemann 框架里能忽略坏点”的核心闸门，也是后续换序/极限交换时最常用的合法性接口。

# 可调用口径
- 若 $D(f)$ 零测，则可用开区间把坏点覆盖到任意小总长度；在补集上用一致连续把振荡压小，从而 $U-L<\varepsilon$。
- 反向：若 $f$ 可积，则对任意 $\varepsilon$，集合 $\{c:\mathrm{osc}(f,c)\ge \varepsilon\}$ 零测，故 $D(f)$ 零测。

# 真源（勿在本卡重复维护）
![[9.1 Riemann可积函数的定义#^thm-9-1-lebesgue-criterion]]
![[9.1 Riemann可积函数的定义#^pf-9-1-lebesgue-criterion]]

