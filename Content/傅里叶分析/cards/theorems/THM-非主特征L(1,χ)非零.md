---
title: "THM-非主特征L(1,χ)非零"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - number-theory
  - dirichlet-L
  - nonvanishing
---

> [!abstract]
> Dirichlet 定理证明中的关键闸门：若 $\chi$ 是非主 Dirichlet character，则 $L(1,\chi)\ne 0$。它保证 $\log L(s,\chi)$ 在 $s\to 1^+$ 时保持有界，从而“主特征的发散”不会被其他项抵消掉。

# 可调用口径
- 若 $\chi\ne \chi_0$，则 $L(1,\chi)=\sum_{n\ge 1}\chi(n)/n$ 收敛且非零。
- 证明思路：先用 Dirichlet 判别法证明收敛，再通过“对数化 Euler 乘积 + cyclotomic 单位表示”排除为 0。

# 真源（勿在本卡重复维护）
![[8.3 Dirichlet定理的证明#^thm-8-3-nonvanishing]]
![[8.3 Dirichlet定理的证明#^pf-8-3-nonvanishing]]

