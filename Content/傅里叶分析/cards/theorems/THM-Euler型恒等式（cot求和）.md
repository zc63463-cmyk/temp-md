---
title: "THM-Euler型恒等式（cot求和）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.4"
tags:
  - 傅里叶分析/cards
  - theorem
  - cot
  - Euler恒等式
  - 经典求和
---

> [!abstract]
> 用 Fourier 系数显式计算 + 在特殊点取值，可导出经典求和恒等式：$\sum_{n\ge 1}(n^2-\alpha^2)^{-1}$ 与 $\cot(\pi\alpha)$ 的关系。
>
>
# 可调用口径
- **结论**（$\alpha\notin\mathbb Z$）：$\sum_{n=1}^{\infty}\frac{1}{n^2-\alpha^2}=\frac{1}{2\alpha^2}-\frac{\pi}{2\alpha}\cot(\pi\alpha)$。
- **证明思路**：先求 $\cos(\alpha x)$ 的 Fourier 系数，再在 $x=\pi$ 取值，利用 $e^{in\pi}=(-1)^n$，并把 $\pm n$ 配对化简。
- **意义**：把“解析函数恒等式/部分分式”转为“Fourier 展开 + 取值”的可计算模板。
- **常用用途**：推导 $\cot$ 的部分分式展开、相关积分恒等式与特殊函数公式。
- **注意**：关键步骤是“配对求和 + 排除 $\alpha\in\mathbb Z$（避免除以 0）”。

# 真源（勿在本卡重复维护）
![[3.4 问题#^pf-3-4-03b]]

# 关联
- [[FML-ζ(2m) 与 Bernoulli 数]]
- 外部对照：NIST DLMF（cot 相关条目）https://dlmf.nist.gov/4.7

