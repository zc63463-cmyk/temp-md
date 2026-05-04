---
title: "THM-圆盘Dirichlet问题的分离变量表示（Fourier边界展开）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis §1.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - 调和函数
  - Dirichlet问题
  - 极坐标
---

> [!abstract]
> 圆盘几何强迫使用极坐标；角变量周期性强迫频率整数化；圆心有界性筛掉发散径向解；边界数据用 Fourier 系数决定内部调和解。
>
# 1. 结论（可调用口径）
在单位圆盘 $r<1$ 内满足 $\Delta u=0$ 且在 $r=0$ 有界的调和函数可写成
$$ u(r,\theta)=\frac{a_0}{2}+\sum_{n\ge 1} r^n\big(a_n\cos(n\theta)+b_n\sin(n\theta)\big). $$
若边界条件为 $u(1,\theta)=F(\theta)$，则 $a_n,b_n$ 是 $F$ 的 Fourier 系数：
$$ a_n=\frac{1}{\pi}\int_0^{2\pi}F(\theta)\cos(n\theta)\,d\theta, $$
以及
$$ b_n=\frac{1}{\pi}\int_0^{2\pi}F(\theta)\sin(n\theta)\,d\theta. $$

# 2. 条件作用
- 角变量周期性：把角频率限制为整数 $n$。  
- 圆心有界：舍弃 $r^{-n}$ 这类在 $r\to 0$ 发散的径向解。  
- Dirichlet 边界数据：完全决定 Fourier 系数，从而决定内部解。

# 3. 证明骨架（只留主干）
1) 使用二维极坐标下 Laplacian：
$$ \Delta u=u_{rr}+\frac{1}{r}u_r+\frac{1}{r^2}u_{\theta\theta}. $$
2) 分离变量 $u(r,\theta)=R(r)\Theta(\theta)$，得到
$$ \Theta''+n^2\Theta=0 $$
（周期性迫使 $n\in\mathbb Z_{\ge 0}$），以及相应的径向方程。  
3) 径向方程给出 $r^n$ 与 $r^{-n}$；由圆心有界性保留 $r^n$。  
4) 边界匹配 $u(1,\theta)=F(\theta)$，用正交投影计算 $a_n,b_n$。

> [!faq]- 完备证明：圆盘 Dirichlet 的分离变量表示（转引）
> 本卡只保留可调用口径与证明骨架；完整推导细节以小节笔记的完备证明为准：  
> - 参见：[[1.2 热传导方程#^pf-1-2-disk-dirichlet]]  
> 这样可以避免同一证明在卡片与小节页重复维护。
>
# 4. 最容易“看懂但不会用”的点
- 你需要能清晰说明：为什么“周期性”让 $n$ 必须是整数（这是离散化的关键门）。  
- 你需要能说明：为什么“有界性”会丢掉 $r^{-n}$（这是解空间筛选的关键门）。

> [!note] 补充理解：Poisson 核是这一定理的“算子版”
> 本定理给的是“系数版”表示：边界 Fourier 系数决定内部解。  
> 其算子版是 $$ u(r,\theta)=(P_r * F)(\theta) $$，Poisson 核在频域对应乘子 $r^{|n|}$，这同时解释了 Abel 求和的平滑性与 $r\uparrow 1$ 的回收机制。  
> 参考：Y.-T. Siu, Poisson kernel notes  
> [18_poisson_kernel.pdf](https://people.math.harvard.edu/~siu/math113/18_poisson_kernel.pdf)
>
# 5. 关联
- 来源小节：[[1.2 热传导方程]]
- 上游方法：[[MTH-分离变量法（PDE）]]、[[MTH-正交投影求系数]]
- 下游承接：Poisson 核/Abel 求和见 [[2.5 Cesaro和Abel求和]]
