---
name: xxd-skill
description: "小小东（@xiaoxiaodong01）GPT-Image-2 美学提示词整合库。整合 37 个开源 xxd-panel 风格 + 6 个 X 帖子独有风格（矢量旅行海报/包装MOCKUP/词义视觉化/局部破框/手撕纸荧光/东方编辑美学知识卡片）。核心方法论：上下分割双联法（3:4 竖版、上下 1:1、上保真摄影+下风格化重构）+ 上层建筑五件套 + 批量出图咒语。当用户需要：①把照片转成高级设计海报/插画/包装提案；②写 GPT-Image-2 风格转换提示词；③批量生成 10 张风格统一的视觉作品；④词/概念视觉化海报；⑤知识卡片/课件排版。触发词：xxd、小小东、GPT2 提示词、美学提示词、上下分割、双联海报、纸雕、版画、旅行海报、包装灵感、大字海报。"
---

# XXD Skill · 小小东 GPT-Image-2 美学提示词整合库

> 整合来源：@xiaoxiaodong01（小小东）X 帖子 + 开源 xxd-panel 体系（github.com/nevertoday）
> 知识库存档：ima「提示词工程」（标题 `xiaoxiaodong01-GPT2 x XX x XX x 美学提示词 x VOL.xxx`）

## 结构

```
xxd-skill/
├── SKILL.md                    ← 本文件：方法论 + 风格路由
├── styles/                     ← 37 个开源 panel 风格（完整 SKILL.md）
│   └── xxd-panel-001/ ... xxd-panel-046/
├── styles-extra/               ← 6 个 X 帖子独有风格（panel 未覆盖）
│   ├── xxd-vector-travel-poster/      矢量旅行海报（VOL.050）
│   ├── xxd-packaging-mockup/          包装 MOCKUP 系统（VOL.001）
│   ├── xxd-word-visualization/        词义视觉化大字海报
│   ├── xxd-broken-frame-portrait/     局部破框人像编辑海报
│   ├── xxd-torn-paper-fluorescent/    手撕纸荧光活动海报
│   └── xxd-eastern-editorial-cards/   东方编辑美学知识卡片
└── references/
    └── xxd-methodology.md      ← 方法论总纲（五件套/批量咒语/双语转换）
```

## 使用流程

1. **接需求**：用户提供照片/主题/目标风格
2. **路由**（按需求关键词选风格）：
   - 剪纸/纸艺/微缩 → `styles/xxd-panel-014` `xxd-panel-018` `xxd-panel-028`
   - 版画/木刻/丝网 → `styles/xxd-panel-005` `xxd-panel-009` `xxd-panel-016` `xxd-panel-025`
   - 水彩 → `styles-extra/xxd-word-visualization` 无；水彩用 `styles/xxd-panel-013`
   - 旅行/矢量 → `styles-extra/xxd-vector-travel-poster`
   - 包装/品牌 → `styles-extra/xxd-packaging-mockup`
   - 词/概念/大字 → `styles-extra/xxd-word-visualization`
   - 人像/杂志编辑 → `styles-extra/xxd-broken-frame-portrait`
   - 活动海报/荧光/贴纸 → `styles-extra/xxd-torn-paper-fluorescent`
   - 知识卡片/课件/PPT → `styles-extra/xxd-eastern-editorial-cards`
   - 其他 → 按 `references/xxd-methodology.md` 的六种风格插槽组装
3. **组装提示词**：使用对应 SKILL.md 中的完整提示词（可直接复制），按需追加批量咒语
4. **交付**：整段可复制提示词，标注风格标签与使用建议

## 核心方法论速览（详见 references/xxd-methodology.md）

### 上下分割双联法（母模板）

```
请将我上传的每一张照片分别制作成一张独立的高级设计海报，不多图拼接，每张照片单独输出。
整体采用3:4竖版构图，上下两个区域高度严格1:1，各占画面50%。
上半部分：保留原始照片 + 轻微高级摄影调色（艺术杂志/独立出版物/展览摄影质感）
下半部分：提取主体、轮廓、姿态与叙事关系，重构为【风格插槽】
```

### 风格插槽（六选一）

| 插槽 | 关键词 | 出处 |
|---|---|---|
| 剪纸/纸雕 diorama | miniature 3D paper-craft | VOL.051/052 |
| 木刻版画 | 限色版画、刀刻不规则 | VOL.049 |
| 矢量旅行海报 | flat-vector travel poster | VOL.050 |
| 包装系统 | 5-8 种载体品牌物料 | VOL.001 |
| 水彩编辑插画 | 包豪斯+稚拙+时尚速写 | Topview 版 |
| 厚涂微景观 | impasto miniature | panel-046 |

### 上层建筑五件套（每篇必备）

1. **构图**：单一视觉锚点 + 大面积留白 + 明确前后层次，可居中/偏置/轻微裁切
2. **配色**：浅粉蓝/雾蓝/天空蓝空气感主氛围 + 象牙白/奶油白/浅米色平衡 + 少量 dusty rose/muted blush 点缀；柔和通透略微去饱和
3. **材质**：真实手工触感（纸纤维/折边/切口/颗粒/毛边）；柔和自然漫射光 + macro 质感
4. **文字**：从照片提炼 1-3 词简短标题，克制优雅排版，像艺术家签名；不固定年份
5. **禁忌**：塑料3D、玩具感、儿童手工、过度可爱、电商展示感、模板感、灰脏陈旧

### 批量出图咒语

```
连续生成10张图片,每张都是不同的角色逻辑,还有金句逻辑,还有配色和排版逻辑,类似于ppt,生成10张确保彼此的排版差异
```

## 与上游关系

- `styles/` 下的 37 个 panel 为上游 nevertoday/xxd-panel-* 的 SKILL.md 完整副本（开源 Codex Skill），完整可运行版（含 scripts/assets/references）见上游仓库
- `styles-extra/` 为 X 帖子蒸馏的独有风格（panel 体系未覆盖），为本库独有内容
- 去重结论：X 帖子的剪纸（VOL.051/052）、版画（VOL.049）、水彩与 panel 体系重叠，以 panel 工程化版本为准；其余 6 风格为独有

## 维护记录

- 2026-08-23：创建。整合 37 panel + 6 独有风格 + 方法论总纲；上传 github.com/snowfrost/xxd-skill
