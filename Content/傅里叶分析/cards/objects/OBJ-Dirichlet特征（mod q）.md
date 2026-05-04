---
title: "OBJ-Dirichlet特征（mod q）"
type: card
card_type: object
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2"
tags:
  - 傅里叶分析/cards
  - object
  - number-theory
  - dirichlet-character
---

> [!abstract]
> Dirichlet 特征 $\chi$（mod $q$）是把“模 $q$ 的乘法群 character”延拓到全体整数的对象：在 $\gcd(n,q)=1$ 时给出单位根权重，在 $\gcd(n,q)>1$ 时置 0。它把同余类条件与素数分布问题翻译成有限 Fourier（正交展开）+ Euler 乘积的语言。

# 可调用口径
- **定义三件套**：周期（mod $q$）+ 完全乘法 + 扩零（不互素置 0）。
- **把同余类线性化**：$\mathbf 1_{n\equiv a\ (q)}$（在互素处）可写成 $\chi(n)$ 的有限线性组合（正交性给出 delta）。
- **把素数加权**：在 Euler 乘积里，$\chi(p)$ 会直接作为素数 $p$ 的权重进入 $\log L(s,\chi)$ 的主项。

# 真源（勿在本卡重复维护）
![[8.2 Dirichlet定理#^def-8-2-dirichlet-character]]

