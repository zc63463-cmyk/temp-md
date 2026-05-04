---
title: "FML-Dirichlet特征正交关系（mod q）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2"
tags:
  - 傅里叶分析/cards
  - formula
  - number-theory
  - orthogonality
  - dirichlet-character
---

> [!abstract]
> Dirichlet characters 在有限群 $Z^*(q)$ 上形成正交基：这是把同余类条件写成 Fourier 展开（delta）的根本原因。

# 可调用口径
- 对任意 Dirichlet characters $\chi,\psi$（mod $q$），
  $$\sum_{a\in Z^*(q)} \chi(a)\overline{\psi(a)}=\varphi(q)\cdot \mathbf 1_{\chi=\psi}.$$
- 典型用途：把指示函数展开成对 $\chi$ 的平均，并把乘法同余条件转成有限求和（再接 Euler 乘积）。

# 真源（勿在本卡重复维护）
![[8.2 Dirichlet定理#^thm-8-2-orthogonality]]
