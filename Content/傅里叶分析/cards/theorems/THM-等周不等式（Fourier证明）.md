---
title: "THM-等周不等式（Fourier证明）"
type: card
card_type: theorem
domain: "傅里叶分析"
source:
  - "Stein Fourier Analysis 第04章 4.1"
tags:
  - 傅里叶分析/cards
  - theorem
  - 等周不等式
  - Parseval
  - CauchySchwarz
---

> [!abstract]
> 通过弧长参数化 + Parseval，把面积/周长翻译到频域系数不等式，从而得到等周不等式及等号刻画。
>
>
# 可调用口径
- **结论**：对平面简单闭曲线，面积 $A$ 与周长 $L$ 满足 $A\le L^2/(4\pi)$，等号当且仅当圆。
- **核心翻译**：面积写成 $\int(xy'-yx')$ 的混合项；周长约束写成导数能量（弧长化后为常数）。
- **不等式链**：混合项 → 系数叉积型项 → 平方和（AM-GM/C-S）→ 用 $|n|\le n^2$ 压到 Parseval 的二次加权能量上。
- **等号刻画**：同时满足“AM-GM 等号”和“只剩 $|n|=1$”的频率约束 → 参数曲线只能是圆（加平移/旋转）。
- **注意**：简单性确保线积分的符号面积与几何面积一致；缩放归一化（先取 $L=2\pi$）是量纲结构而非技巧。

# 真源（勿在本卡重复维护）
![[4.1 等周不等式#^thm-4-1-isoperimetric]]
![[4.1 等周不等式#^pf-4-1-isoperimetric]]

# 关联
- 章节入口：[[第04章 Fourier级数的一些应用 — ingest(MOC)]]
- 上游：[[THM-Parseval恒等式（圆周Plancherel）]]

