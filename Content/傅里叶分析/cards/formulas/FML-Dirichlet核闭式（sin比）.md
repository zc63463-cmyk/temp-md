---
title: "FML-Dirichlet核闭式（sin比）"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - formula
  - Dirichlet核
  - 点态收敛
  - 振荡
---

> [!abstract]
> Dirichlet 核的闭式把“部分和”转成振荡积分的主振荡项；它同时揭示了奇异性（分母）与振荡性（分子）的叠加来源。
>
# 可调用口径
- **闭式**：$D_N(t)=\frac{\sin((N+\tfrac12)t)}{\sin(t/2)}$（$t\not\equiv 0\ \mathrm{mod}\ 2\pi$）。
- **近零行为**：分母 $\sin(t/2)\sim t/2$ 使得核在 $t=0$ 附近呈现尖峰与奇异结构。
- **振荡来源**：分子 $\sin((N+\tfrac12)t)$ 频率随 $N$ 增大而增加，导致强振荡。
- **常用用途**：将 $S_N f=f*D_N$ 的误差项化为振荡积分，从而使用 Dirichlet 判别/分部积分。
- **对照**：Fejér/Poisson 核满足“好核”性质，因此收敛更稳；Dirichlet 核不满足好核口径。
- **注意**：闭式主要用于分析点态问题，而不是 $L^2$ 投影问题。

# 真源（勿在本卡重复维护）
![[3.2 逐点收敛#^fml-3-2-dirichlet-closed-form]]

# 关联
- [[THM-Dirichlet点态收敛定理（BV_分段光滑）]]
- 对照：[[THM-Fejér定理（Cesàro求和一致收敛）]]（换核得到更稳的收敛）
