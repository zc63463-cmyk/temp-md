---
title: "MOC｜核与求和法（坏核→好核）"
type: moc
tags:
  - 傅里叶分析
  - MOC
  - 核方法
  - 求和法
date: 2026-04-25
cssclasses:
  - wide-page
---

> [!abstract] 定位
> 本 MOC 汇总“用核理解 Fourier 收敛”的主链：从 Dirichlet 部分和（坏核）出发，通过 Cesaro/Abel 等“换核求和法”升级为好核逼近。
^overview

## 1) 一句话主线
把级数写成卷积：$S_N f=f*D_N$（坏核）→ 换成 $F_N/P_r$（好核）→ 用好核逼近定理推收敛。

## 2) 概念入口（concepts）
- 坏核与部分和：[[Content/傅里叶分析/concepts/Dirichlet核]]、[[Content/傅里叶分析/concepts/Fourier部分和]]
- 换核求和法：[[Content/傅里叶分析/concepts/Cesaro平均]]、[[Content/傅里叶分析/concepts/Abel平均]]
- 对应核：[[Content/傅里叶分析/concepts/Fejer核]]、[[Content/傅里叶分析/concepts/Poisson核]]
- 好核抽象口径：[[Content/傅里叶分析/concepts/好核（逼近恒等）]]
- 总结式心法：[[Content/傅里叶分析/concepts/坏核修正为好核]]

## 3) 真源入口（notes）
- 卷积与核化语言：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.3 卷积]]
- 好核与逼近定理：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.4 好核]]
- 换核求和法（Cesaro/Abel）：[[Content/傅里叶分析/notes/第02章 Fourier级数的基本性质/2.5 Cesaro和Abel求和]]
- Dirichlet 核的“坏”来自哪里（点态收敛链）：[[Content/傅里叶分析/notes/第03章 Fourier级数的收敛性/3.2 逐点收敛]]

## 4) 卡片速查（cards）
### formulas
- [[Content/傅里叶分析/cards/formulas/FML-部分和=卷积（Dirichlet核）]]
- [[Content/傅里叶分析/cards/formulas/FML-Dirichlet核闭式（sin比）]]
- [[Content/傅里叶分析/cards/formulas/FML-卷积使 Fourier 系数相乘]]

### theorems
- [[Content/傅里叶分析/cards/theorems/THM-Fejér定理（Cesàro求和一致收敛）]]
- [[Content/傅里叶分析/cards/theorems/THM-Fourier系数唯一性（Poisson核_Abel平均）]]
- [[Content/傅里叶分析/cards/theorems/THM-好核逼近定理]]

## 5) 推荐阅读顺序（最短闭环）
1. 2.3 卷积（先接受“部分和=卷积”的翻译）  
2. 2.4 好核（学会“分裂积分区域估计”的证明模板）  
3. 2.5 Cesaro 和 Abel（把“换核求和法”固定成主工具）  
4. 3.2 逐点收敛（理解为什么 $D_N$ 不是好核，点态为何困难）

