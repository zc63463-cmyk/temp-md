---
title: "THM-无理旋转等分布（nα）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - 等分布
  - 无理数
  - 几何级数
---

> [!abstract]
> 典型应用：当 $\alpha$ 无理时，$\{n\alpha\}$ 在 $[0,1)$ 等分布；证明完全归约为几何级数求和与“分母不为 0”。
>
>
# 可调用口径
- **结论**：若 $\alpha\notin\mathbb Q$，则 $x_n=\{n\alpha\}$ 在 $[0,1)$ 等分布。
- **证明接口**：用 Weyl 判别准则，只需对每个 $k\ne 0$ 证 $S_N(k)\to 0$。
- **显式计算**：$\sum_{n=1}^N e^{2\pi i k n\alpha}=r\frac{1-r^N}{1-r}$，其中 $r=e^{2\pi i k\alpha}$。
- **无理性落点**：无理性确保 $r\ne 1$（分母不为 0），从而平均值 $\lesssim 1/N$。
- **对照**：若 $\alpha\in\mathbb Q$，则轨道周期，显然不可能等分布。

# 真源（勿在本卡重复维护）
![[4.2 Weyl等分布定理#^thm-4-2-irrational-rotation]]
![[4.2 Weyl等分布定理#^pf-4-2-irrational-rotation]]

# 关联
- [[THM-Weyl判别准则（等分布⇔指数和）]]

