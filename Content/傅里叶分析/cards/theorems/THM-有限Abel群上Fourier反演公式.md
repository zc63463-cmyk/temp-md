---
title: "THM-有限Abel群上Fourier反演公式"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - finite-fourier
  - abelian-group
  - inversion
---

> [!abstract]
> 在有限 Abel 群 $G$ 上，characters 充当正交基；反演公式就是在该基下重建 $f$ 的坐标回写。

# 可调用口径
- 输入：$f:G\to\mathbb C$（有限维）。
- 输出：$f(x)$ 由所有 characters 的 Fourier 系数线性组合给出。
- 关键点：共轭与 $1/|G|$ 的放置必须与定义配套（否则反演常数错）。
- 适用场景：把组合/计数问题放到一般有限 Abel 群（如 $Z_p^n$）上做 Fourier。

# 真源（勿在本卡重复维护）
![[7.2 有限Abel群上的Fourier分析#^thm-7-2-inversion]]
![[7.2 有限Abel群上的Fourier分析#^pf-7-2-inversion]]

