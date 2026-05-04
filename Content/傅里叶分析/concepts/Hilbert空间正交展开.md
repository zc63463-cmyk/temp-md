---
title: "Hilbert空间正交展开"
type: concept
tags:
  - 傅里叶分析
  - Hilbert空间
  - concept
date: 2026-04-24
cssclasses:
  - wide-page
status: mature
---

> [!abstract] 定位（一句话）
> Hilbert 空间中的正交展开把向量表示为正交系的级数；Fourier 级数是这一抽象理论在 $L^2(\mathbb T)$ 的具体化。
^overview

## 真源回链（先止血）
- [[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.1 Fourier级数的均方收敛]]
- Bessel/Parseval：[[Content/傅里叶分析/cards/theorems/THM-Bessel不等式（L2）]]、[[Content/傅里叶分析/cards/theorems/THM-Parseval恒等式（圆周Plancherel）]]

## 1. ON 系与部分和
设 $H$ 为 Hilbert 空间，$\{e_n\}$ 为正交规范系（ON 系）。对 $f\in H$，定义其部分和
$$ S_N f=\sum_{n=1}^{N}\langle f,e_n\rangle e_n. $$
它是 $f$ 投影到 $V_N=\mathrm{span}\{e_1,\dots,e_N\}$ 的正交投影。

## 2. Bessel 与 Parseval（结构性结论）
| 名称 | 结论 | 意味着什么 |
|---|---|---|
| Bessel 不等式 | $\sum_{n\ge 1}|\langle f,e_n\rangle|^2\le \|f\|^2$ | “坐标平方和”不超过能量 |
| Parseval 恒等式 | 若 ON 系完备，则 $\sum_{n\ge 1}|\langle f,e_n\rangle|^2=\|f\|^2$ | 能量在各坐标方向完全分解 |

## 3. “完备性”在证明链里的位置
完备性（ONB）可理解为：$V_N$ 的并在 $H$ 中稠密。  
它使得投影误差 $\|f-S_N f\|$ 能趋于 0，从而得到“正交展开在范数意义下逼近任意 $f$”。  
在 Fourier 场景中，这正是 $S_N f\to f$ 的均方收敛主线。

## 4. 常见误区
- ❌ 把“正交展开”当作点态级数；✅ 这里的核心是 Hilbert 范数收敛（例如 $L^2$）。  
- ❌ 忽略完备性；✅ 没有完备性时，只能得到 Bessel，不一定能把 $f$ 逼近到任意精度。  
