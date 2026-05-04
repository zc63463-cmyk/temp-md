---
title: "THM-Heisenberg不确定性原理（Fourier形式）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第05章 5.4"
tags:
  - 傅里叶分析/cards
  - theorem
  - Fourier变换
  - 不确定性原理
  - 极值
  - 高斯
---

> [!abstract]
> “时域集中”与“频域集中”不能同时发生；等号刻画把极值函数锁定为高斯（及其平移/调制）。

# 可调用口径
- **结论**：对 $f\in\mathcal S(\mathbb R)$，存在中心 $x_0,\xi_0$ 使 $$ \left(\int (x-x_0)^2|f(x)|^2dx\right)\left(\int (\xi-\xi_0)^2|\widehat f(\xi)|^2d\xi\right)\ge \frac{1}{16\pi^2}\left(\int |f(x)|^2dx\right)^2. $$
- **等号刻画**：当且仅当 $f$ 是某个高斯经平移与调制得到的函数。
- **用途**：把“支撑/集中性”转化为可计算的 $L^2$ 二次矩约束；也是很多不等式与极值问题的母式。
- **常见误区**：混淆中心化（选择 $x_0,\xi_0$）与未中心化版本；常数会随约定与中心化方式变化。
- **证明骨架**：对 $xf$ 与 $f'$ 做 Cauchy–Schwarz + 分部积分，等号对应一阶 ODE，从而得到高斯。
- **复用方式**：涉及“等号情形”时，直接回链真源证明块，避免二次维护。

# 真源（勿在本卡重复维护）
![[5.4 Heisenberg不确定性原理#^thm-5-4-heisenberg]]
![[5.4 Heisenberg不确定性原理#^pf-5-4-heisenberg]]

# 关联
- 上游：[[THM-Plancherel定理（R上）]]
- 参见：[[THM-Poisson求和公式]]（高斯是两者共同的“结构性极值/自对偶”对象）
