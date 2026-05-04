---
title: "OBJ-Dirichlet L函数（定义_Euler乘积）"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2–8.3"
tags:
  - 傅里叶分析/cards
  - object
  - number-theory
  - dirichlet-L
---

> [!abstract]
> Dirichlet $L$-函数 $L(s,\chi)$ 是把 Dirichlet 特征 $\chi(n)$ 的算术信息编码进复变量 $s$ 的解析对象；它同时有 Dirichlet 级数定义与 Euler 乘积表示。Dirichlet 定理最终依赖于：主特征包含 $\zeta(s)$ 的极点，而非主特征在 $s=1$ 处连续且非零。

# 可调用口径
- **级数定义**（$\mathrm{Re}(s)>1$）：$L(s,\chi)=\sum_{n\ge 1}\chi(n)n^{-s}$。
- **Euler 乘积**（$\mathrm{Re}(s)>1$）：$L(s,\chi)=\prod_p(1-\chi(p)p^{-s})^{-1}$，从而把素数信息直接编码进解析对象。
- **对数主项**：$\log L(s,\chi)=\sum_p \chi(p)p^{-s}+O(1)$（$s\to 1^+$），把“加权素数和”与“对数行为”绑定。

# 真源（勿在本卡重复维护）
![[8.2 Dirichlet定理#^def-8-2-L-function]]
![[8.2 Dirichlet定理#^thm-8-2-euler-product-L]]
![[8.3 Dirichlet定理的证明#^lem-8-3-logL-main]]

