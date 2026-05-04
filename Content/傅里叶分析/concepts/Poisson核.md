---
title: "Poisson核"
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
> Poisson 核 $P_r$（$0<r<1$）是 Abel 平均/Poisson 积分的卷积核，是“好核”的典型代表：非负、质量为 1、并随 $r\uparrow 1$ 质量集中。
^overview

## 真源回链（先止血）
- Abel 平均方法入口：[[Content/傅里叶分析/cards/methods/MTH-Abel平均]]
- 相关定理（Fourier 系数唯一性口径）：[[Content/傅里叶分析/cards/theorems/THM-Fourier系数唯一性（Poisson核_Abel平均）]]
- 第02章求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]

## 1. 定义
Poisson 核是一族由参数 $0<r<1$ 指定的 $2\pi$-周期函数。常用的两种等价表示：

- Fourier 展开（频域最自然）：
$$ P_r(\theta)=\sum_{n\in\mathbb Z} r^{|n|}e^{in\theta}. $$

- 闭式（便于看出非负与集中性）：
$$ P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}. $$

## 2. 关键性质（速查）
| 性质 | 结论 | 备注 |
|---|---|---|
| 非负性 | $P_r(\theta)\ge 0$ | 由闭式分母正且分子 $1-r^2>0$ |
| 归一化（质量为 1） | $$ \frac{1}{2\pi}\int_{-\pi}^{\pi}P_r(\theta)\,d\theta=1 $$ | 等价于 $\widehat{P_r}(0)=1$ |
| Fourier 系数 | $\widehat{P_r}(n)=r^{|n|}$ | 直接来自 Fourier 展开 |
| 半群性质 | $P_r*P_s=P_{rs}$ | “先平滑再平滑”等价于一次平滑 |
| 好核（近似恒等） | 当 $r\uparrow 1$，质量向 $\theta=0$ 集中 | 连接到 [[好核（逼近恒等）]] |

## 3. 与卷积/乘子等价
对可积函数 $f$，Abel 平均（见 [[Abel平均]]）满足：
$$ A_r f = f*P_r. $$
因此 Poisson 核对应的频域乘子是 $m_r(n)=r^{|n|}$：它用“软衰减”替代了部分和的“硬截断”。

## 4. 收敛口径（应该取什么极限）
- 连续函数口径：若 $f\in C(\mathbb T)$，则 $A_r f\to f$（$r\uparrow 1$）一致收敛。  
- $L^1$ 口径：若 $f\in L^1(\mathbb T)$，则在 $f$ 的 Lebesgue 点处有 $A_r f(x)\to f(x)$。  
- 跳点口径：若 $f(x+),f(x-)$ 存在，则（偶核/对称化机制）
$$ \lim_{r\uparrow 1}A_r f(x)=\frac{f(x+)+f(x-)}{2}. $$

## 5. 与 Dirichlet 核对照（为何 Abel 更稳）
| 维度 | Poisson 核 $P_r$（Abel） | Dirichlet 核 $D_N$（部分和） |
|---|---|---|
| 空间域 | 非负、像局部平均 | 强振荡、变号 |
| $L^1$ | 归一化后恒为 1 | $\|D_N\|_{L^1}$ 随 $N$ 增长 |
| 频域权重 | 软衰减 $r^{|n|}$ | 硬截断 $1_{|n|\le N}$ |

## 6. 常见误区
- ❌ 直接把 $r=1$ 代回 $A_r f$ 的级数；✅ 必须先固定 $0<r<1$（绝对收敛/可控），再取 $r\uparrow 1$。  
- ❌ 把权重写成 $r^n$；✅ 双边 Fourier 必须是 $r^{|n|}$（负频率同样衰减）。  

## 7. 参见
- 求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]
- 对照：[[Dirichlet核]]、[[Fejer核]]
