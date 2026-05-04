---
title: "THM-主特征与s=1极点的角色"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.2–8.3"
tags:
  - 傅里叶分析/cards
  - theorem
  - number-theory
  - dirichlet-L
  - zeta
---

> [!abstract]
> Dirichlet 定理的“发散来源”来自主特征 $\chi_0$：$L(s,\chi_0)$ 含有 $\zeta(s)$，因此在 $s\to 1^+$ 发散（极点）。证明把这一发散从其他项中分离出来，再证明非主特征项有界，完成发散比较。

# 可调用口径
- 主特征分解：
  $$L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}).$$
- 因而 $\log L(s,\chi_0)=\log\zeta(s)+O(1)$，并且 $\log\zeta(s)\to\infty$ 当 $s\to 1^+$。

# 真源（勿在本卡重复维护）
![[8.2 Dirichlet定理#^lem-8-2-principal-zeta]]
![[8.2 Dirichlet定理#^pf-8-2-principal-zeta]]

