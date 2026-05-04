---
title: "THM-Fejér定理（Cesàro求和一致收敛）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第02章"
tags:
  - 傅里叶分析/cards
  - theorem
  - Cesaro求和
  - Fejér核
  - 好核
---

> [!abstract]
> Fejér 定理成立的核心不在于“又算了一遍部分和”，而在于：Cesàro 平均把 Dirichlet 的硬截断核替换为一个**非负且质量集中的好核**（Fejér 核），从而卷积变成“越来越局部的平均”，自动获得稳定逼近。
>
>
# 1. 结论（可调用口径）
对 $2\pi$-周期连续函数 $f\in C(\mathbb T)$，定义 Cesàro 平均
$$ \sigma_N f=\frac{1}{N+1}\sum_{k=0}^{N} S_k f. $$
则
$$ \|\sigma_N f-f\|_\infty\to 0. $$
（更一般地，$f\in L^1$ 时在 Lebesgue 点处收敛到 $f$。）

# 2. 条件作用
- 连续性：用于调用“好核 ⇒ 一致逼近”的口径；若仅 $L^1$，需要换成 Lebesgue 点口径。  
- “Cesàro 平均”结构：确保对应核 $F_N$ 非负并具备质量集中（这是稳定性的来源）。

# 3. 证明骨架（只留主干）
- Step 1：用卷积语言识别 $\sigma_N f=f*F_N$，其中 $F_N=\frac{1}{N+1}\sum_{k=0}^{N}D_k$。  
- Step 2：用闭式 $F_N(x)=\frac{1}{N+1}\left(\frac{\sin((N+1)x/2)}{\sin(x/2)}\right)^2$ 验证 $F_N\ge 0$，并验证归一化与质量集中。  
- Step 3：调用好核逼近定理得到 $f*F_N\to f$ 一致。  
- 最关键一跳：**从“算子平均”跳到“核的非负 + 集中”**，把收敛问题变成好核判别。

> [!faq]- 完备证明（真源）
> 见：[[2.5 Cesaro和Abel求和#^pf-2-5-fejer]]
>
# 4. 最容易“看懂但不会用”的点
1) 不会把 Cesàro 平均翻译为卷积：必须先用 $S_k f=f*D_k$（来自 2.3）。  
2) “非负”的作用被低估：它让误差估计能直接用积分控制（缺少正性时振荡可能放大误差）。  
3) 质量集中验证被跳过：闭式只是入口，真正要证明的是 $\int_{|x|>\delta}F_N(x)\,dx\to 0$。  
4) 混淆结论口径：一致收敛需要连续性；$L^1$ 只能保证 Lebesgue 点处收敛。

# 5. 关联
- 来源小节：[[2.5 Cesaro和Abel求和]]  
- 上游：[[FML-部分和=卷积（Dirichlet核）]]、[[THM-好核逼近定理]]  
- 并行对照：[[2.5 Cesaro和Abel求和#^pf-2-5-abel|Abel（Poisson）收敛]]  

