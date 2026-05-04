---
title: "FML-字符正交关系（有限群）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.2"
tags:
  - 傅里叶分析/cards
  - formula
  - finite-fourier
  - orthogonality
  - character
---

> [!abstract]
> 非平凡 character 的求和为 0，是“反演/Plancherel/计数 trick”的发动机。

# 可调用口径
- 典型形态：$\sum_{x\in G}\chi(x)\overline{\psi(x)}=|G|\mathbf 1_{\chi=\psi}$。
- 用途 1：消交叉项（把双重和压成单点/单频率）。
- 用途 2：证明反演与 Parseval。
- 用途 3：在组合/计数中把指示函数展开为 Fourier 系数。
- 常见误区：把它误当作“近似正交”；在有限群上是精确等式。

# 真源（勿在本卡重复维护）
![[7.2 有限Abel群上的Fourier分析#^thm-7-2-orthogonality-1]]
![[7.2 有限Abel群上的Fourier分析#^pf-7-2-dual-basics]]

