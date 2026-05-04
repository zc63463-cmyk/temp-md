---
title: "FML-U-L差=局部振荡加权和"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第09章 9.1"
tags:
  - 傅里叶分析/cards
  - formula
  - integration
  - riemann
---

> [!abstract]
> Riemann 可积性最可操作的公式：上/下和差是各子区间振荡的加权和。所有“把坏点贡献压小”的证明，都在控制这条公式右边。

# 可调用口径
- 对分割 $P$ 的子区间 $I$，记 $\omega_I=\sup_I f-\inf_I f$，则
  $$U(P,f)-L(P,f)=\sum_{I\in P}\omega_I\,|I|.$$
- 典型用途：将 $U-L$ 分成“坏区间贡献 + 好区间贡献”，分别估计并压到任意小。

# 真源（勿在本卡重复维护）
![[9.1 Riemann可积函数的定义#^fml-9-1-gap-decomposition]]

