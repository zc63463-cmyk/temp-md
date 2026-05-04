---
title: "FML-卷积使 Fourier 系数相乘"
type: card
card_type: formula
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第02章"
tags:
  - 傅里叶分析/cards
  - formula
  - 卷积
  - Fourier系数
---

> [!abstract]
> 这是第02章的“结构桥梁公式”：它把空间域的卷积算子翻译成频域上的逐点乘法，使“选核/滤波”变成“选乘子”的问题。
>
>
# 1. 公式
若 $f,g\in L^1(\mathbb T)$（$2\pi$-周期口径），则对任意 $n\in\mathbb Z$：
$$ \widehat{f*g}(n)=\widehat f(n)\,\widehat g(n). $$

# 2. 角色
- 结论型恒等式（结构定理），不是定义。  
- 它把“卷积=平均/平滑”的直觉变成可计算的频域规则。

# 3. 它连接了哪两步
1) 空间：$f\mapsto f*g$ 是积分算子（加权平均）。  
2) 频域：$\widehat{\cdot}$ 把该算子对角化，变成“每个频率单独乘上 $\widehat g(n)$”。

# 4. 为什么值得单独保存
- 直接驱动两条主线：
  - 2.3：用它识别 $S_N f=f*D_N$（因为 $\widehat{D_N}$ 是硬窗口）；
  - 2.5：用它把 Cesàro/Abel 求和写成卷积，并快速读出乘子（Fejér 的线性权重、Poisson 的 $r^{|n|}$）。

# 5. 推导骨架
- 把 $\widehat{f*g}(n)$ 写成二重积分；
- 用 Fubini 交换积分；
- 变量替换 $u=x-y$，并用周期性把区间平移回 $[-\pi,\pi]$；
- 得到两个积分的乘积，分别是 $\widehat f(n)$ 与 $\widehat g(n)$。

> [!faq]- 完备证明（真源）
> 见：[[2.3 卷积#^pf-2-3-conv-mult]]
>
# 6. 最容易误用的点
1) 忘记归一化常数（$1/(2\pi)$）会导致整个公式差一个系数。  
2) 对 $L^1$ 以外的函数类（分布/测度）需要额外解释“卷积/系数”的定义。  
3) 交换积分（Fubini）需要可积性门槛；不要把“形式推导”当作无条件事实。

# 7. 关联
- 上游对象：[[2.3 卷积]]  
- 下游：[[FML-部分和=卷积（Dirichlet核）]]、[[THM-Fejér定理（Cesàro求和一致收敛）]]、[[THM-Fourier系数唯一性（Poisson核_Abel平均）]]
