---
title: "FML-有限群卷积定理（卷积_点乘）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.1"
tags:
  - 傅里叶分析/cards
  - formula
  - finite-fourier
  - convolution
  - multiplier
---

> [!abstract]
> 平移不变算子对角化：卷积在频域变成逐点乘法。

# 可调用口径
- $Z_N$ 上循环卷积：$(f*g)\widehat{\ }=\widehat f\cdot\widehat g$。
- 一般有限 Abel 群同理（把循环卷积替换为群卷积）。
- 用途：把计数/相关/平滑问题变成频域点乘，再做估计或算法实现。
- 误区：线性卷积与循环卷积不是同一个对象；必须与底层群结构匹配。

# 真源（勿在本卡重复维护）
![[7.1 Z_N上的Fourier分析#^thm-7-1-convolution]]
![[7.1 Z_N上的Fourier分析#^pf-7-1-convolution]]
![[7.2 有限Abel群上的Fourier分析#^thm-7-2-convolution]]
![[7.2 有限Abel群上的Fourier分析#^pf-7-2-convolution]]
