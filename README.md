# 🦁 XXD Skill · 小小东 GPT-Image-2 美学提示词整合库

> 蒸馏自 @xiaoxiaodong01（小小东）的 GPT-Image-2 美学提示词方法论
> 整合 **37 个开源 xxd-panel 风格** + **6 个 X 帖子独有风格** + **方法论总纲**

## 这是什么

把普通照片变成高级设计海报/编辑插画/包装提案/概念海报的**提示词配方库**，核心方法论来自 X 用户 [@xiaoxiaodong01](https://x.com/xiaoxiaodong01)（国际不知名提示词专家 / 2.3 万粉 / 个人站 [vip.xiaoxiaodong.ai](https://vip.xiaoxiaodong.ai)）。

## 去重说明（2026-08-23）

对「X 新收集帖子」与「GitHub xxd-panel 仓库」做了逐项比对：

| X 帖子风格 | 与 panel 体系关系 | 处理 |
|---|---|---|
| 剪纸素雅（VOL.052） | 重叠 → panel-014/018/028 | 以 panel 工程化版本为准 |
| 剪纸盆景（VOL.051） | 重叠 → panel-018/028 | 以 panel 工程化版本为准 |
| 木刻版画（VOL.049） | 重叠 → panel-005/009/016/025 | 以 panel 工程化版本为准 |
| 水彩编辑插画 | 重叠 → panel-001/013 | 以 panel 工程化版本为准 |
| 矢量旅行海报（VOL.050） | **独有** | 收入 styles-extra |
| 包装 MOCKUP（VOL.001） | **独有** | 收入 styles-extra |
| 词义视觉化大字海报 | **独有** | 收入 styles-extra |
| 局部破框人像 | **独有** | 收入 styles-extra |
| 手撕纸荧光活动海报 | **独有** | 收入 styles-extra |
| 东方编辑美学知识卡片 | **独有**（panel 无批量课件版） | 收入 styles-extra |

**结论**：panel 体系已覆盖剪纸/版画/水彩/东方四大类；6 个独有风格（矢量旅行、包装、词义视觉化、破框人像、手撕纸、知识卡片）为本库特有增量。

## 结构

```
xxd-skill/
├── SKILL.md                    总控入口（方法论 + 风格路由）
├── styles/                     37 个开源 panel 风格（完整 SKILL.md）
│   ├── xxd-panel-001/ ...     稚拙复古手绘编辑插画 ... 明亮厚涂微景观
├── styles-extra/               6 个 X 帖子独有风格（本库独有）
│   ├── xxd-vector-travel-poster/      矢量旅行海报
│   ├── xxd-packaging-mockup/          包装 MOCKUP 系统
│   ├── xxd-word-visualization/        词义视觉化大字海报
│   ├── xxd-broken-frame-portrait/     局部破框人像
│   ├── xxd-torn-paper-fluorescent/    手撕纸荧光海报
│   └── xxd-eastern-editorial-cards/   东方编辑美学知识卡片
└── references/
    └── xxd-methodology.md     方法论总纲（五件套/批量咒语/双语转换）
```

## 快速开始

1. 安装：将 `xxd-skill` 放入 `~/.workbuddy/skills/`（或直接用本仓库）
2. 对 AI 说：`用 xxd-skill 把这张照片变成矢量旅行海报` / `用 xxd-skill 生成包装提案` / `把这个词视觉化成海报`
3. 或直接打开对应 SKILL.md，复制完整提示词到 GPT-Image-2 使用

## 核心方法论（30 秒版）

- **上下分割双联法**：3:4 竖版、上下严格 1:1、上半保真摄影 + 下半风格化重构
- **五件套**：构图（锚点+留白）/ 配色（雾蓝+象牙白+少量dusty rose）/ 材质（手工触感）/ 文字（签名式标题）/ 禁忌（塑料3D等）
- **批量咒语**：`连续生成10张图片,每张都是不同的角色逻辑,还有金句逻辑,还有配色和排版逻辑,类似于ppt,生成10张确保彼此的排版差异`

## 致谢与来源

- 方法论与提示词：[@xiaoxiaodong01](https://x.com/xiaoxiaodong01)（小小东）
- 37 个 panel 风格：上游开源仓库 [nevertoday/xxd-panel-*](https://github.com/nevertoday)（Codex Skill，完整可运行版见上游）
- 6 个独有风格：本库从 X 帖子蒸馏
- 原始素材归档：ima「提示词工程」知识库（标题 `xiaoxiaodong01-GPT2 x XX x XX x 美学提示词 x VOL.xxx`）

## License

MIT
