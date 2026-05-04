---
title: "第05章 R上的Fourier变换 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第05章 R上的Fourier变换"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
cssclasses:
  - wide-page
date: 2026-04-23
---

> [!abstract]
> 本章主线（去重版）：在 $\mathbb R$ 上建立 Fourier 变换的“可逆 + 等距”框架（反演/Plancherel），并把 PDE、离散求和、极值不等式统一为频域乘子与核估计问题；每节用 proof 真源块承载可维护证明，用 cards 只做可调用入口。

^overview

## 0. 导航
- 章节汇总：[[第05章 R上的Fourier变换 — 章节汇总]]
- 节笔记：[[5.1 Fourier变换的基本理论]]｜[[5.2 偏微分方程中的一些应用]]｜[[5.3 Poisson求和公式]]｜[[5.4 Heisenberg不确定性原理]]｜[[5.5 练习]]｜[[5.6 问题]]
- 上游回链（去重）：[[2.3 卷积]]｜[[2.4 好核]]｜[[3.1 Fourier级数的均方收敛]]

> [!note] 去重策略声明（全库）
> - 第05章作为 $\mathbb R$ 上 Fourier 变换的一维真源；第06章再维护 $\mathbb R^d$ 高维版本（避免重复维护）。
> - 证明/公式的唯一可维护真源固定在节笔记中的 `^thm-5-*` / `^pf-5-*` block-id。
> - cards 仅转引真源 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 5.1 Fourier 反演：[[5.1 Fourier变换的基本理论#^pf-5-1-inversion]]
> - 5.1 Plancherel：[[5.1 Fourier变换的基本理论#^pf-5-1-plancherel]]
> - 5.2 热方程乘子解：[[5.2 偏微分方程中的一些应用#^pf-5-2-heat-solution]]
> - 5.3 Poisson 求和：[[5.3 Poisson求和公式#^pf-5-3-poisson-summation]]
> - 5.4 Heisenberg 不确定性：[[5.4 Heisenberg不确定性原理#^pf-5-4-heisenberg]]

## 1. 本章 cards（去重入口）
- [[THM-Fourier反演公式（R上）]]
- [[THM-Plancherel定理（R上）]]
- [[THM-热方程的Fourier乘子解（R上）]]
- [[THM-Poisson求和公式]]
- [[THM-Heisenberg不确定性原理（Fourier形式）]]

# 2. 外部参考（用于“补充理解与易混淆点”callout；附访问日期）
- Fourier 变换基本性质与反演（Stanford）：http://virtualmath1.stanford.edu/~andras/172-4.pdf （访问：2026-04-23）
- Plancherel（UPenn Gressman）：https://www2.math.upenn.edu/~gressman/analysis/14-plancherel.html （访问：2026-04-23）
- Poisson 求和（UPenn Gressman）：https://www2.math.upenn.edu/~gressman/analysis/14-poisson.html （访问：2026-04-23）
- Poisson 求和（MIT 18.785，Schwartz 版本）：https://math.mit.edu/classes/18.785/2025/LectureNotes17.pdf （访问：2026-04-23）
- Fourier 不确定性原理综述（UChicago）：http://math.uchicago.edu/~may/REU2021/REUPapers/Dubey.pdf （访问：2026-04-23）
