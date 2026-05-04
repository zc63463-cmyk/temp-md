---
title: "THM-Weyl判别准则（等分布⇔指数和）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.2"
tags:
  - 傅里叶分析/cards
  - theorem
  - 等分布
  - Weyl准则
  - 指数和
---

> [!abstract]
> 等分布可以完全由 Fourier 模式（指数和）刻画：这是把“分布问题”降维为“有限频率逼近 + 显式求和”的接口。
>
>
# 可调用口径
- **结论**：序列 $(x_n)\subset[0,1)$ 等分布，当且仅当对每个非零整数 $k$，指数和平均 $S_N(k)=\frac1N\sum_{n=1}^N e^{2\pi i k x_n}\to 0$。
- **2⇒1 的关键**：先在三角多项式上成立（只用有限多个 $S_N(k)$），再用一致逼近把一般连续函数归约到三角多项式。
- **1⇒2 的关键**：把测试函数取成 $e^{2\pi i k x}$，其空间平均为 0（$k\ne 0$）。
- **意义**：把“分布均匀”翻译为“所有非零 Fourier 模式被平均抹平”。
- **注意**：稠密不等于等分布；只检验有限多个频率也不够（只能控制有限维投影）。

# 真源（勿在本卡重复维护）
![[4.2 Weyl等分布定理#^thm-4-2-weyl-criterion]]
![[4.2 Weyl等分布定理#^pf-4-2-weyl-2to1]]
![[4.2 Weyl等分布定理#^pf-4-2-weyl-1to2]]

# 关联
- [[THM-无理旋转等分布（nα）]]
- 章节入口：[[第04章 Fourier级数的一些应用 — ingest(MOC)]]

