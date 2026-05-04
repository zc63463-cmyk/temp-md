---
title: "MOC｜收敛层级（L2 / 点态 / 求和法）"
type: moc
tags:
  - 傅里叶分析
  - MOC
  - 收敛
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 定位
> 本 MOC 把 Fourier 级数常见的收敛意义放在同一张“层级地图”上：先有 $L^2$ 的结构性结论，再到点态收敛的额外门槛，最后用求和法（换核）得到更稳健的极限。
^overview

## 1) 三层收敛视角（快速对照）
1. $L^2$：Hilbert 空间正交投影 → Bessel/Parseval → 均方收敛。  
2. 点态：需要额外正则性（BV/分段光滑）或更精细定理；部分和可能振荡。  
3. 求和法：用好核（Fejer/Poisson）把收敛问题转成“核族逼近”。

## 2) 真源入口（notes）
- $L^2$ 主线：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.1 Fourier级数的均方收敛]]
- 点态主线：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.2 逐点收敛]]
- 求和法主线：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]

## 3) 概念入口（concepts）
- $L^2$ 舞台：[[Content/傅里叶分析/concepts/L2圆周空间]]、[[Content/傅里叶分析/concepts/指数正交系]]、[[Content/傅里叶分析/concepts/Hilbert空间正交展开]]
- 点态门槛：[[Content/傅里叶分析/concepts/有界变差函数（BV）]]、[[Content/傅里叶分析/concepts/左右极限]]、[[Content/傅里叶分析/concepts/对称化技巧]]
- 求和法与核：[[Content/傅里叶分析/concepts/Fejer核]]、[[Content/傅里叶分析/concepts/Poisson核]]、[[Content/傅里叶分析/concepts/好核（逼近恒等）]]

## 4) 卡片速查（cards）
### theorems
- [[Content/傅里叶分析/cards/theorems/THM-Bessel不等式（L2）]]
- [[Content/傅里叶分析/cards/theorems/THM-Parseval恒等式（圆周Plancherel）]]
- [[Content/傅里叶分析/cards/theorems/THM-Fourier部分和的L2均方收敛（S_N f→f）]]
- [[Content/傅里叶分析/cards/theorems/THM-Dirichlet点态收敛定理（BV_分段光滑）]]
- [[Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）]]

### formulas
- [[Content/傅里叶分析/cards/formulas/FML-L2内积（圆周归一化）]]
- [[Content/傅里叶分析/cards/formulas/FML-Fourier系数与部分和（定义）]]

## 5) 常见误区（提醒）
- $L^2$ 收敛不等于点态收敛；点态需要额外结构或换核求和法。  
- “部分和更精细”不等于“更平滑”：$S_N$ 对应 Dirichlet 核，可能更振荡。

