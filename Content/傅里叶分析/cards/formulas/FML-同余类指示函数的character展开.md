---
title: "FML-同余类指示函数的character展开"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2"
tags:
  - 傅里叶分析/cards
  - formula
  - number-theory
  - dirichlet-character
  - indicator
---

> [!abstract]
> 同余类筛选 $\mathbf 1_{n\equiv a\ (q)}$ 可以用 Dirichlet characters 的正交性写成有限 Fourier 展开；这是 Dirichlet 定理证明里把“同余类素数”变成“加权素数和”的关键一步。

# 可调用口径
- 若 $\gcd(a,q)=1$，则对任意整数 $n$，
  $$\mathbf 1_{n\equiv a\ (q)}\mathbf 1_{\gcd(n,q)=1}=\frac{1}{\varphi(q)}\sum_{\chi\ (\mathrm{mod}\ q)} \overline{\chi(a)}\,\chi(n).$$
- 典型用途：把 $\sum_{p\equiv a}p^{-s}$ 写成对 $\sum_p \chi(p)p^{-s}$ 的线性组合，从而与 $\log L(s,\chi)$ 主项连接。

# 真源（勿在本卡重复维护）
![[8.2 Dirichlet定理#^lem-8-2-indicator-expansion]]

