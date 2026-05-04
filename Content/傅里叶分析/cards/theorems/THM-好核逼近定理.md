---
title: "THM-好核逼近定理"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第02章"
tags:
  - 傅里叶分析/cards
  - theorem
  - 好核
  - 逼近恒等
  - convolution
---

> [!abstract]
> 好核三条件的作用可以拆解为：归一化让常数不变、$L^1$ 控制防止放大误差、质量集中把“局部正则性”（连续/Lebesgue 点）转成“局部平均恢复点值”。这就是第02章把 Fejér/Poisson 两类求和法统一推出收敛的机制核心。
>
>
# 1. 结论（可调用口径）
设 $\{K_\alpha\}$ 是圆周 $\mathbb T$ 上的好核（见 [[OBJ-好核（近似恒等）]] 的三条件）。

1)（连续一致口径）若 $f\in C(\mathbb T)$，则
$$ \|f*K_\alpha-f\|_\infty\to 0. $$

2)（$L^1$ 点态口径，按本书后续用法）若 $f\in L^1(\mathbb T)$，则在 $f$ 的 Lebesgue 点 $x$ 有 $(f*K_\alpha)(x)\to f(x)$（因此 a.e. 收敛）。

# 2. 条件作用
- 归一化：把误差写成 $\int (f(x-y)-f(x))K_\alpha(y)\,dy$，否则无法把 $f(x)$“塞进同一个积分”。  
- $L^1$ 有界：保证误差估计能用 $\int |K_\alpha|$ 控制，不会被核放大。  
- 质量集中：把积分分成近区/远区；远区贡献趋零，近区贡献由连续性（或 Lebesgue 点的局部平均振荡趋零）控制。

# 3. 证明骨架（只留主干）
- Step 1：用归一化把差写成
  $$ (f*K_\alpha)(x)-f(x)=\frac{1}{2\pi}\int (f(x-y)-f(x))K_\alpha(y)\,dy. $$
- Step 2：固定 $\varepsilon$，选 $\delta$ 控制近区（连续：$|y|<\delta$ ⇒ $|f(x-y)-f(x)|<\varepsilon$）。  
- Step 3：把积分分成 $|y|<\delta$ 与 $|y|\ge\delta$；近区用 $L^1$ 控制 + $\varepsilon$，远区用质量集中控制。  
- 最关键一跳：**先用函数的局部性质拿到“近区小”，再用核的集中性拿到“远区小”**，两步小量合并成一致小量。

> [!faq]- 完备证明（真源：连续一致口径）
> 见：[[2.4 好核#^pf-2-4-good-kernel-approx]]
>
# 4. 最容易“看懂但不会用”的点
1) 不会选顺序：必须先用 $f$ 的性质选 $\delta$，再用核的性质选足够大的 $\alpha$。  
2) 把“质量集中”误当点态：需要的是积分尾部 $\int_{|y|>\delta}|K_\alpha|$ 变小。  
3) 忽略归一化常数 $1/(2\pi)$：会导致“误差表达式”错位。  
4) 在 $L^1$ 口径下，连续性要换成 Lebesgue 点（局部平均振荡趋零），否则证明断裂。

# 5. 关联
- 来源小节：[[2.4 好核]]  
- 上游：[[FML-部分和=卷积（Dirichlet核）]]（把收敛问题核化）  
- 下游：[[THM-Fejér定理（Cesàro求和一致收敛）]]、[[THM-Fourier系数唯一性（Poisson核_Abel平均）]]
