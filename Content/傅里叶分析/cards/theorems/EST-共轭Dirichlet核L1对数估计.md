---
title: "EST-共轭Dirichlet核L1对数估计"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章 3.4"
tags:
  - 傅里叶分析/cards
  - estimate
  - theorem
  - Dirichlet核
  - 共轭核
  - L1
  - log
---

> [!abstract]
> 共轭 Dirichlet 核的 $L^1$ 范数至多对数增长：这是“反例/不可能性证明”中最常用的增长上界之一。
>
>
# 可调用口径
- **结论**：存在常数 $C$ 使得 $\frac{1}{2\pi}\int_{-\pi}^{\pi}|\widetilde D_N(x)|\,dx\le C\log N$。
- **证明骨架**：用闭式把 $|\widetilde D_N(x)|$ 粗估为 $\lesssim 1/|x|$，再把积分与 $\int_1^N dt/t$ 比较得到 $\log N$。
- **含义**：即使振荡很强，奇异性会让“平均大小”无法有界，只能做到对数级控制。
- **常用用途**：与某些下界（如 $N^{1-a}$ 级增长）对撞，推出“该级数不可能来自 Riemann 可积函数的 Fourier 展开”。
- **对照**：Fejér/Poisson 好核的 $L^1$ 是一致有界的（这是求和法更稳的原因之一）。

# 真源（勿在本卡重复维护）
![[3.4 问题#^pf-3-4-01b]]

# 关联
- [[FML-共轭Dirichlet核闭式]]
- [[3.4 问题]]

