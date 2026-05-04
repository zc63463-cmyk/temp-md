---
title: "Fourier系数"
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
> Fourier 系数是把函数投影到指数正交系上的“坐标”（频域表示），决定了部分和、求和法与收敛性质。
^overview

## 真源回链（先止血）
- 定义与部分和：[[Content/傅里叶分析/cards/formulas/FML-Fourier系数与部分和（定义）]]
- 第02章动机页：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.1 问题的例子和公式]]
- $L^2$ 视角（均方收敛/Parseval）：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.1 Fourier级数的均方收敛]]
- 内积归一化：[[Content/傅里叶分析/cards/formulas/FML-L2内积（圆周归一化）]]

## 1. 定义（本库归一化口径）
在 $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ 上，Fourier 系数定义为
$$ \widehat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)e^{-inx}\,dx. $$
对应的指数正交系为 $\{e^{inx}\}_{n\in\mathbb Z}$。

## 2. 关键性质（速查）
| 性质 | 表述 | 备注 |
|---|---|---|
| 线性 | $\widehat{af+bg}(n)=a\widehat f(n)+b\widehat g(n)$ | 直接由积分线性 |
| 共轭对称 | 若 $f$ 实值，则 $\widehat f(-n)=\overline{\widehat f(n)}$ | 常用于把复系数翻回实函数 |
| 平移 | 若 $g(x)=f(x-x_0)$，则 $\widehat g(n)=e^{-inx_0}\widehat f(n)$ | 频域相位变化 |
| Riemann–Lebesgue（必要条件） | 若 $f\in L^1(\mathbb T)$，则 $\widehat f(n)\to 0$ | 只给必要性，不给充分性 |

## 3. 与 $L^2$ 正交投影的关系
在 $L^2(\mathbb T)$ 内积
$$ \langle f,g\rangle=\frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)\overline{g(x)}\,dx $$
下，有
$$ \widehat f(n)=\langle f,e^{inx}\rangle. $$
因此 Fourier 系数就是把 $f$ 投影到正交基方向上的“坐标”，并直接导出 Bessel/Parseval 与均方收敛主线（见第03章 3.1）。

## 4. 常见误区
- ❌ “$\widehat f(n)\to 0$ ⇒ Fourier 级数收敛”；✅ 这是必要不充分条件，点态收敛需要额外结构或换核求和法。  
- ❌ 忽略不同资料的归一化因子；✅ 本库默认使用 $\frac{1}{2\pi}\int$ 口径，常数因子错位会传染到所有公式。  
