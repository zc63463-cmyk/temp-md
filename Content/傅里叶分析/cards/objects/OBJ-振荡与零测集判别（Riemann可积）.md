---
title: "OBJ-振荡与零测集判别（Riemann可积）"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.1"
tags:
  - 傅里叶分析/cards
  - object
  - integration
  - oscillation
  - null-set
---

> [!abstract]
> 振荡 $\mathrm{osc}(f,c)$ 把“连续/不连续”变成可量化对象，并允许把可积性判别写成集合论条件：Riemann 可积 $\Leftrightarrow$ 不连续点是零测集。这是“看懂但不会用”最常卡住的接口：如何把坏点信息转成上/下和差的估计。

# 可调用口径
- $\mathrm{osc}(f,c)=0 \Leftrightarrow f$ 在 $c$ 连续。
- $A_\varepsilon=\{c:\mathrm{osc}(f,c)\ge \varepsilon\}$ 是闭集；不连续点集 $D(f)=\bigcup_{m\ge 1}A_{1/m}$。
- 若能用开区间把 $D(f)$ 覆盖到任意小总长度，就能把这些区间对 $U-L$ 的贡献压到任意小。

# 真源（勿在本卡重复维护）
![[9.1 Riemann可积函数的定义#^def-9-1-oscillation]]
![[9.1 Riemann可积函数的定义#^thm-9-1-lebesgue-criterion]]
![[9.1 Riemann可积函数的定义#^pf-9-1-lebesgue-criterion]]

