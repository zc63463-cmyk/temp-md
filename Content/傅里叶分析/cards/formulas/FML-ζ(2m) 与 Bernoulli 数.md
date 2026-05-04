---
title: "FML-ζ(2m) 与 Bernoulli 数"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.4"
tags:
  - 傅里叶分析/cards
  - formula
  - zeta
  - Bernoulli数
  - 特殊函数
---

> [!abstract]
> $\zeta(2m)$ 的闭式与 Bernoulli 数是经典结果：既可由 $\cot$ 的部分分式/留数法得到，也可由本章“生成函数 + 幂级数比较”路径得到。
>
>
# 可调用口径
- **结论**（$m\ge 1$）：$\zeta(2m)=(-1)^{m+1}\frac{(2\pi)^{2m}}{2(2m)!}B_{2m}$。
- **本章路线**：从 $\frac{z}{e^z-1}$ 的 Bernoulli 数生成函数出发，得到 $z\cot z$ 的幂级数，再比较系数推出 $\zeta(2m)$。
- **意义**：把“特殊值公式”转为“生成函数/幂级数比较”的系统化模板。
- **注意**：Bernoulli 数约定（尤其 $B_1$）会影响中间展开的符号；对照外部资料前先对齐约定。
- **外部对照**：NIST DLMF §25.6 给出标准公式与约定说明。

# 真源（勿在本卡重复维护）
![[3.4 问题#^pf-3-4-04c]]

# 关联
- 对照来源：https://dlmf.nist.gov/25.6

