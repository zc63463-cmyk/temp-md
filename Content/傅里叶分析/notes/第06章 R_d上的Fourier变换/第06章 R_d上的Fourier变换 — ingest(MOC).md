---
title: "第06章 R_d上的Fourier变换 — ingest(MOC)"
type: chapter-ingest
book: "Stein Fourier Analysis"
chapter: "第06章 R_d上的Fourier变换"
tags:
  - 傅里叶分析
  - 傅里叶-强度
  - ChapterIngest
  - MOC
cssclasses:
  - wide-page
date: 2026-04-24
---

> [!abstract]
> 本章把 $R$ 上的 Fourier 变换升级为 $R^d$：基础定理（反演/Plancherel）在多变量保持；在此基础上，用“频域乘子 + 对称性 + 核方法”处理波动方程、径向对称（Bessel 核）与 Radon 变换（切片定理）。

^overview

## 0. 导航
- 章节汇总：[[第06章 R_d上的Fourier变换 — 章节汇总]]
- 节笔记：[[6.1 预备知识]]｜[[6.2 Fourier变换的初等理论]]｜[[6.3 R_d_x_R上的波动方程]]｜[[6.4 径向对称与Bessel函数]]｜[[6.5 Radon变换及其应用]]｜[[6.6 练习]]｜[[6.7 问题]]
- 上游回链（去重）：[[5.1 Fourier变换的基本理论]]｜[[5.2 偏微分方程中的一些应用]]｜[[5.3 Poisson求和公式]]｜[[5.4 Heisenberg不确定性原理]]

> [!note] 去重策略声明（全库）
> - 第05章维护一维版本的“细节推导”；第06章只维护多维新增点（对称性、球坐标、Bessel、Radon、波动方程的维数现象）。  
> - 证明/公式的唯一可维护真源固定在节笔记中的 `^thm-6-*` / `^pf-6-*` block-id。  
> - 如后续需要 cards：cards 仅转引真源 block-id，不复制证明正文。
<!-- callout-break -->
> [!faq]- 完备证明入口（去重版）
> - 6.1 球坐标积分：[[6.1 预备知识#^pf-6-1-spherical-coordinates]]
> - 6.2 Fourier 反演：[[6.2 Fourier变换的初等理论#^pf-6-2-inversion]]
> - 6.2 Plancherel：[[6.2 Fourier变换的初等理论#^pf-6-2-plancherel]]
> - 6.3 波动方程 Fourier 解：[[6.3 R_d_x_R上的波动方程#^pf-6-3-wave-fourier-solution]]
> - 6.4 径向 Fourier 核表示：[[6.4 径向对称与Bessel函数#^pf-6-4-radial-ft-kernel]]
> - 6.5 Fourier slice theorem：[[6.5 Radon变换及其应用#^pf-6-5-fourier-slice]]

# 1. 外部参考（用于“补充理解与易混淆点”；附访问日期）
- Fourier transform on $R^d$（Plancherel/Parseval，Gressman）：https://www2.math.upenn.edu/~gressman/analysis/14-plancherel.html （访问：2026-04-24）
- Fourier inversion（Stanford notes）：http://virtualmath1.stanford.edu/~andras/172-4.pdf （访问：2026-04-24）
- Wave equation via Fourier transform（Berkeley write-up）：https://math.berkeley.edu/~yudx/fourier_analysis_project_write_up.pdf （访问：2026-04-24）
- Central slice theorem（Croke chap6）：https://www2.math.upenn.edu/~ccroke/chap6.pdf （访问：2026-04-24）
