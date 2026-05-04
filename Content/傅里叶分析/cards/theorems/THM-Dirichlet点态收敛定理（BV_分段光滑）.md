---
title: "THM-Dirichlet点态收敛定理（BV_分段光滑）"
aliases:
  - "THM-Dirichlet点态收敛定理（BV/分段光滑）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第03章"
tags:
  - 傅里叶分析/cards
  - theorem
  - 点态收敛
  - Dirichlet核
  - BV
  - 分段光滑
---

> [!abstract]
> 在足够的局部正则性（如 BV/分段 $C^1$）下，Fourier 部分和在点 $x$ 处收敛到左右极限的平均。
>
# 可调用口径
- **结论**：若 $f$ 在点 $x$ 附近具有左右极限且满足 BV/分段光滑等条件，则 $S_N f(x)\to \frac{f(x+)+f(x-)}{2}$。
- **适用条件**：点态结论依赖局部正则性（控制振荡积分），不是纯 $L^2$/纯系数结论。
- **含义**：Dirichlet 核的振荡被“局部规则性”压住；跳点处的自然目标值是左右平均。
- **常用用途**：在分段光滑/BV 模型下给出点态收敛与极限值；用于解释 Gibbs/振荡现象的边界。
- **对照**：连续并不足以保证 $S_N f(x)$ 收敛（存在连续发散反例）；更稳的方案是 Cesàro/Abel（好核）。
- **注意**：证明的关键结构是“对称化 + BV 控制振荡积分”（见下方真源与关联卡）。

# 真源（勿在本卡重复维护）
![[3.2 逐点收敛#^pf-3-2-dirichlet-convergence]]

# 关联
- 章节：[[第03章 Fourier级数的收敛性 — 章节汇总]]｜[[第03章 Fourier级数的收敛性 — ingest(MOC)]]
- 上游：[[FML-部分和=卷积（Dirichlet核）]]｜[[FML-Dirichlet核闭式（sin比）]]
- 方法：[[MTH-对称化（偶核→左右平均）]]｜[[OBJ-有界变差（BV）在Dirichlet收敛中的角色]]
- 对照：[[THM-Fejér定理（Cesàro求和一致收敛）]]｜[[MTH-Abel平均]]
