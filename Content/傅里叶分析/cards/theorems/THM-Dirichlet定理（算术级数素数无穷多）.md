---
title: "THM-Dirichlet定理（算术级数素数无穷多）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2–8.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - number-theory
  - dirichlet
---

> [!abstract]
> 对任意互素同余类 $a\pmod q$，算术级数 $a,a+q,a+2q,\dots$ 中含无穷多个素数。证明的核心是：用 characters 的正交性筛选同余类，再用 $L$-函数 Euler 乘积对数化，把问题变成 $\log\zeta(s)$ 的发散比较。

# 可调用口径
- 条件：$q\ge 1$，$\gcd(a,q)=1$。
- 结论：存在无穷多个素数 $p$ 满足 $p\equiv a\pmod q$。
- 证明结构（可复用）：
  1) 指示函数展开（正交性）；
  2) $\log L(s,\chi)$ 主项提取；
  3) 主特征贡献发散（$\log\zeta(s)$）+ 非主特征有界（$L(1,\chi)\ne 0$）；
  4) 推出 $\sum_{p\equiv a}p^{-s}$ 发散。

# 真源（勿在本卡重复维护）
![[8.3 Dirichlet定理的证明#^thm-8-3-dirichlet]]
![[8.3 Dirichlet定理的证明#^pf-8-3-dirichlet]]

