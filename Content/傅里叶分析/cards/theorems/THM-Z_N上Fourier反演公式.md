---
title: "THM-Z_N上Fourier反演公式"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第07章 7.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - finite-fourier
  - Z_N
  - inversion
---

> [!abstract]
> 在 $Z_N$ 上把“频谱坐标”无损还原为原函数：离散 Fourier 分析的闭环接口。

# 可调用口径
- 适用对象：任意函数 $f:Z_N\to\mathbb C$（有限维，无需正则性）。
- 关键前提：必须与所选 Fourier 变换归一化常数一致（前向/逆向的 $1/N$ 放置）。
- 常见用途：把卷积/滤波在频域做完后反演回时域。
- 误区提醒：若把 $1/N$ 放错，反演会多出整体系数，后续 Plancherel 与卷积定理常数同步错。
- 复用方式：本卡不重复维护证明正文，只转引节笔记真源块。

# 真源（勿在本卡重复维护）
![[7.1 Z_N上的Fourier分析#^thm-7-1-inversion]]
![[7.1 Z_N上的Fourier分析#^pf-7-1-inversion]]

