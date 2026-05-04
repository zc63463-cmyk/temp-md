---
title: "THM-固定端波动方程的模态分解（正弦级数）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis §1.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - 波动方程
  - 正弦级数
---

> [!abstract]
> 固定端边界把允许的空间形状离散化为正弦模态；线性与正交性把 PDE 解变成“模态叠加 + 投影求系数”。
>
# 1. 结论（可调用口径）
在 $0<x<L$ 上，若
$$ u_{tt}=c^2u_{xx},\qquad u(0,t)=u(L,t)=0, $$
且初值 $u(x,0)=f(x)$、$u_t(x,0)=g(x)$，则形式解写为
$$ u(x,t)=\sum_{n\ge 1}\Big(a_n\cos\frac{n\pi c t}{L}+b_n\sin\frac{n\pi c t}{L}\Big)\sin\frac{n\pi x}{L}. $$
系数由正交投影给出：
$$ a_n=\frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx, $$
以及
$$ b_n=\frac{2}{n\pi c}\int_0^L g(x)\sin\frac{n\pi x}{L}\,dx. $$

# 2. 条件作用
- 固定端边界：强迫空间特征函数为正弦，频率离散化为 $n\pi/L$。  
- 线性：允许模态叠加。  
- 两条初值：对应二阶时间方程的两自由度（$\cos/\sin$ 系数）。

# 3. 证明骨架（只留主干）
1) 分离变量 $u=XT$，得到分离常数 $-\lambda$。  
2) 空间方程 + 边界：
$$ X''+\lambda X=0,\qquad X(0)=X(L)=0 $$
给出
$$ \lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad X_n(x)=\sin\frac{n\pi x}{L}. $$
3) 时间方程
$$ T_n''+c^2\lambda_n T_n=0 $$
给出 $\cos(n\pi c t/L)$ 与 $\sin(n\pi c t/L)$。  
4) 用线性叠加得到级数形式；用正交性投影 $f,g$ 得到系数。

> [!faq]- 完备证明：固定端波动方程的模态分解（转引）
> 本卡不重复书写完整推导细节；唯一真源放在小节笔记的完备证明 callout 中：  
> - 参见：[[1.1 弦振动#^pf-1-1-wave-modes]]  
> 这保证“证明只维护一份”，避免卡片与小节页产生分叉。
>
# 4. 最容易“看懂但不会用”的点
- 你需要能独立完成“把初值投影到正弦基上”的系数计算（这一步是接口）。  
- 形式解与真正解之间的差异来自收敛与逐项微分合法性（后续章节用核/能量补）。

> [!warning] 易混淆点：这一定理的“线性模型”边界在哪里？
> 这里的模态分解依赖于 **线性、常系数** 的波动方程 $$ u_{tt}=c^2u_{xx} $$。  
> 从物理上说，它来自“小振幅线性化 + 张力近似常数”等假设；一旦进入非线性或变系数模型，正弦模态不再是自然的本征基。  
> 参考：Shawn D. Ryan, Lecture 10.7（弦振动推导中的近似假设）  
> [lecture10.7.pdf](https://academic.csuohio.edu/shawn-ryan/wp-content/uploads/sites/66/2022/06/lecture10.7.pdf)
>
# 5. 关联
- 来源小节：[[1.1 弦振动]]
- 上游方法：[[MTH-分离变量法（PDE）]]
- 下游接口：[[MTH-正交投影求系数]]
