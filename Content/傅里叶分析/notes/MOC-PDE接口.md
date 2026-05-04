---
title: "MOC｜PDE 接口（波动/热/Poisson）"
type: moc
tags:
  - 傅里叶分析
  - MOC
  - PDE
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 定位
> 本 MOC 汇总 Fourier 方法与 PDE 的接口：分离变量与正交展开给出波动/热方程解；Poisson 核把 Abel 平均与圆盘调和延拓（Dirichlet 问题）连在一起。
^overview

## 1) 真源入口（notes）
- 物理动机（弦振动 / 热传导）：[[Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.1 弦振动]]、[[Content/傅里叶分析/notes/第01章 Fourier分析的起源/1.2 热传导方程]]
- 圆上的热方程：[[Content/傅里叶分析/notes/第04章 Fourier级数的一些应用/4.4 圆上的热方程]]
- Poisson 核与 Abel 平均：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]
- 高维波动方程（Fourier 变换口径）：[[Content/傅里叶分析/notes/第06章 R_d上的Fourier变换/6.3 R_d_x_R上的波动方程]]

## 2) 概念入口（concepts）
- PDE 基础：[[Content/傅里叶分析/concepts/热方程]]、[[Content/傅里叶分析/concepts/波动方程]]、[[Content/傅里叶分析/concepts/Laplacian]]
- 分离变量与边界：[[Content/傅里叶分析/concepts/分离变量法]]、[[Content/傅里叶分析/concepts/固定端边界条件]]、[[Content/傅里叶分析/concepts/Fourier展开（周期边界）]]
- Poisson/Abel 接口：[[Content/傅里叶分析/concepts/Poisson核]]、[[Content/傅里叶分析/concepts/Abel平均]]

## 3) 卡片速查（cards）
### theorems
- [[Content/傅里叶分析/cards/theorems/THM-固定端波动方程的模态分解（正弦级数）]]
- [[Content/傅里叶分析/cards/theorems/THM-圆盘Dirichlet问题的分离变量表示（Fourier边界展开）]]
- [[Content/傅里叶分析/cards/theorems/THM-热方程的Fourier表示解（圆周）]]
- [[Content/傅里叶分析/cards/theorems/THM-热核是好核（t↓0回收初值）]]
- [[Content/傅里叶分析/cards/theorems/THM-热方程的Fourier乘子解（R上）]]

### formulas
- [[Content/傅里叶分析/cards/formulas/FML-热核H_t（定义与关键性质）]]

### methods
- [[Content/傅里叶分析/cards/methods/MTH-分离变量法（PDE）]]

## 4) 推荐最短链路
1. 1.1/1.2（从模型到方程）  
2. 分离变量法（得到正交展开的动机）  
3. Poisson/Abel（调和延拓与边界极限）  
4. 4.4（热方程作为“平滑算子”的直观例子）

