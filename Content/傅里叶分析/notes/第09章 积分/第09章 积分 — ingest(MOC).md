---
title: "第09章 积分 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第09章 积分"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
  - 积分
cssclasses:
  - wide-page
date: 2026-04-24
---

> [!abstract]
> 第09章为全书提供“积分合法性”的底层接口：Riemann 可积（含零测集判别）、$R^d$ 上的多重/累次积分与变量替换、以及 $R^d$ 上反常积分（缓降函数的可积性与换序/卷积接口）。本章后续将直接支撑第10章及以后关于 Fourier 变换的换序、极限交换与核估计。

^overview

## 0. 导航
- 章节汇总：[[第09章 积分 — 章节汇总]]
- 节笔记：[[9.1 Riemann可积函数的定义]]｜[[9.2 多重积分]]｜[[9.3 反常积分 R_d上的积分]]

> [!note] 去重策略声明（全库）
> - 本章所有“定义/定理/证明”的唯一维护真源固定在 9.1–9.3 三节笔记中的 `^def-9-*` / `^lem-9-*` / `^thm-9-*` / `^pf-9-*` block-id。
> - cards 仅转引真源 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 9.1 基本性质：[[9.1 Riemann可积函数的定义#^pf-9-1-basic-properties]]
> - 9.1 可积×连续：[[9.1 Riemann可积函数的定义#^pf-9-1-integrable-times-continuous]]
> - 9.1 单调函数可积：[[9.1 Riemann可积函数的定义#^pf-9-1-monotone-integrable]]
> - 9.1 Lebesgue 判别：[[9.1 Riemann可积函数的定义#^pf-9-1-lebesgue-criterion]]
> - 9.2 连续函数可积：[[9.2 多重积分#^pf-9-2-continuous-integrable]]
> - 9.2 累次积分：[[9.2 多重积分#^pf-9-2-fubini-continuous]]
> - 9.2 变量替换：[[9.2 多重积分#^pf-9-2-change-of-variables]]
> - 9.2 球坐标：[[9.2 多重积分#^pf-9-2-polar]]
> - 9.3 缓降积分存在：[[9.3 反常积分 R_d上的积分#^pf-9-3-existence]]
> - 9.3 截断方式无关：[[9.3 反常积分 R_d上的积分#^pf-9-3-cutoff-independence]]
> - 9.3 缓降换序：[[9.3 反常积分 R_d上的积分#^pf-9-3-fubini-slow]]
> - 9.3 卷积型换序：[[9.3 反常积分 R_d上的积分#^pf-9-3-convolution-swap]]

## 1. 本章 cards（去重入口）
- [[OBJ-Riemann可积（上和_下和）]]
- [[OBJ-振荡与零测集判别（Riemann可积）]]
- [[OBJ-缓降函数（R_d反常积分接口）]]
- [[FML-U-L差=局部振荡加权和]]
- [[FML-球坐标积分公式（R_d）]]
- [[THM-Lebesgue判别（Riemann可积⇔不连续点零测）]]
- [[THM-连续函数的累次积分（矩体上Fubini）]]
- [[MTH-ε细分法（压U-L到任意小）]]
- [[MTH-截断+尾部控制实现无界域换序]]

# 2. 外部参考（章级；附访问日期）
- Wikipedia：Riemann integral：https://en.wikipedia.org/wiki/Riemann_integral （访问：2026-04-24）
- Wikipedia：Fubini–Tonelli theorem：https://en.wikipedia.org/wiki/Fubini%E2%80%93Tonelli_theorem （访问：2026-04-24）
- HandWiki：Improper integral：https://handwiki.org/wiki/Improper_integral （访问：2026-04-24）
