---
title: "Abel平均"
type: concept
tags:
  - 傅里叶分析
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> Abel 平均把 Fourier 部分和替换为“指数衰减的频域加权和”（等价于与 Poisson 核卷积），从而把收敛问题转化为好核逼近。
^overview

## 真源回链（先止血）
- 方法卡片：[[Content/傅里叶分析/cards/methods/MTH-Abel平均]]
- Poisson 核口径：[[Content/傅里叶分析/concepts/Poisson核]]
- 第02章求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]

## 1. 定义（频域软化）
对 $2\pi$-周期函数 $f$，其 Abel 平均定义为
$$ A_r f(x)=\sum_{n\in\mathbb Z} r^{|n|}\widehat f(n)e^{inx},\qquad 0<r<1. $$

直觉：把部分和的“硬截断”换成频域上的“软衰减权重” $r^{|n|}$（$r$ 越接近 1，保留的高频越多）。

## 2. 与卷积/乘子等价
- 乘子视角：$A_r$ 在频域的乘子是 $m_r(n)=r^{|n|}$，即 $\widehat{A_r f}(n)=r^{|n|}\widehat f(n)$。  
- 卷积视角：令 Poisson 核满足 $\widehat{P_r}(n)=r^{|n|}$，则
$$ A_r f = f*P_r. $$
（一句话推导：卷积使 Fourier 系数相乘，因此 $f*P_r$ 的系数就是 $r^{|n|}\widehat f(n)$。）

## 3. 收敛口径（取极限 $r\uparrow 1$）
把 $A_r f$ 视作与 Poisson 核卷积后，收敛性直接来自“好核逼近”：
- 若 $f\in C(\mathbb T)$，则 $A_r f\to f$（$r\uparrow 1$）一致收敛；  
- 若 $f\in L^1(\mathbb T)$，则在 Lebesgue 点处 $A_r f(x)\to f(x)$；  
- 若 $f(x\pm)$ 存在，则
$$ \lim_{r\uparrow 1}A_r f(x)=\frac{f(x+)+f(x-)}{2}. $$

## 4. 与 Dirichlet 部分和对照
| 维度 | Abel 平均 $A_r$ | 部分和 $S_N$ |
|---|---|---|
| 参数 | $r\uparrow 1$ | $N\to\infty$ |
| 频域权重 | 软衰减 $r^{|n|}$ | 硬截断 $1_{|n|\le N}$ |
| 空间域核 | Poisson 核（好核，非负） | Dirichlet 核（坏核，振荡） |

## 5. 常见误区
- ❌ 把 Abel 平均当作“把 $r$ 直接取成 1 的形式操作”；✅ 必须先在 $0<r<1$ 下工作（绝对收敛/卷积可控），再令 $r\uparrow 1$。  
- ❌ 混淆 Abel 平均（Fourier 级数的算子）与 Abel 求和（一般级数的求和法）；✅ 可把 Abel 平均视为 Abel 求和法在 Fourier 级数上的实例（参见：[[Abel求和]]）。  

## 6. 参见
- Poisson 核：[[Poisson核]]
- 对照：[[Dirichlet核]]、[[Cesaro平均]]
