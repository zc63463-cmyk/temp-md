---
title: "MTH-正交投影求系数"
type: card
card_type: method
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第01章"
tags:
  - 傅里叶分析/cards
  - method
  - 正交性
  - Fourier系数
---

> [!abstract]
> 当解被表示为一组正交模态的线性组合时，系数由“把数据投影到每个模态上”得到；这就是 Fourier 系数/展开系数的统一来源。
>
# 1. 方法目标
- 将“匹配初值/边界数据”的问题改写为：在正交基上的**坐标计算**。

# 2. 标准模板
设 $\{\phi_n\}$ 在某内积空间中两两正交，并且（形式上）
$$ f=\sum_{n}a_n\phi_n. $$
两边取内积并用正交性得到
$$ \langle f,\phi_m\rangle=a_m\langle \phi_m,\phi_m\rangle, $$
从而
$$ a_m=\frac{\langle f,\phi_m\rangle}{\langle \phi_m,\phi_m\rangle}. $$

# 3. 适用场景
- Fourier 级数/正交展开（区间的正弦/余弦基，圆周的指数基）
- 特征函数展开（Sturm–Liouville、Laplacian 的本征函数）

# 4. 第01章的两处落点
- 1.1 固定端波动方程：用 $\sin(n\pi x/L)$ 投影 $f$ 与 $g$ 得到 $a_n,b_n$。  
- 1.2 圆盘 Dirichlet：用 $\cos(n\theta),\sin(n\theta)$ 投影边界数据 $F(\theta)$ 得到 $a_n,b_n$，再由径向部分生成内部解。

# 5. 高风险点
- “正交”必须对应正确的内积（权重/区间/测度变了会导致系数公式变）。  
- 投影求得的是“坐标”；要证明级数真的表示原函数，还需要收敛理论（后续用核/能量/唯一性补齐）。

# 6. 关联
- 上游方法：[[MTH-分离变量法（PDE）]]
- 来源小节：[[1.1 弦振动]]、[[1.2 热传导方程]]

## 真源（勿在本卡重复维护）
见：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.1 Fourier级数的均方收敛#^pf-3-1-l2-convergence]]

> [!faq]- 完备证明：系数公式 $a_m=\langle f,\phi_m\rangle/\langle \phi_m,\phi_m\rangle$
> **证明**：假设（在可交换求和与内积的门禁下）
> $$ f=\sum_{n}a_n\phi_n, $$
> 且 $\{\phi_n\}$ 两两正交。对固定 $m$，两边与 $\phi_m$ 取内积：
> $$ \langle f,\phi_m\rangle=\left\langle \sum_{n}a_n\phi_n,\phi_m\right\rangle. $$
> 利用内积对第一变量的线性与正交性，右边化为
> $$ \sum_{n}a_n\langle \phi_n,\phi_m\rangle=a_m\langle \phi_m,\phi_m\rangle. $$
> 若 $\phi_m\ne 0$，则 $\langle \phi_m,\phi_m\rangle>0$，从而
> $$ a_m=\frac{\langle f,\phi_m\rangle}{\langle \phi_m,\phi_m\rangle}. $$
> 证毕。
