---
title: "MTH-Euler乘积对数化与发散比较（Dirichlet证明主线）"
type: card
card_type: method
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第08章 8.1–8.3"
tags:
  - 傅里叶分析/cards
  - method
  - number-theory
  - euler-product
  - log-trick
---

> [!abstract]
> 把“素数无穷/同余类素数无穷”转化为“对数发散比较”的标准模板：先用 Euler 乘积把素数写进解析对象，再取对数把乘积变求和，提取主项（通常是 $\sum_p p^{-s}$ 或 $\sum_p \chi(p)p^{-s}$），最后用 $s\to 1^+$ 的发散/有界对比推出结论。

# 可调用口径
- Step A：Euler 乘积（把整数级数写成素数乘积）。
- Step B：取对数并用 $\log(1-z)=-z+O(z^2)$ 提取主项；误差由 $\sum_p p^{-2s}$ 控制进 $O(1)$。
- Step C：识别发散来源（通常是主特征对应的 $\log\zeta(s)$），并证明其余项有界（例如 $L(1,\chi)\ne 0$）。
- Step D：把发散/有界对比翻译回素数集合无穷。

# 真源（勿在本卡重复维护）
![[8.1 一些基本的数论知识#^thm-8-1-sum-1-over-p-diverges]]
![[8.3 Dirichlet定理的证明#^lem-8-3-logL-main]]
![[8.3 Dirichlet定理的证明#^pf-8-3-dirichlet]]

