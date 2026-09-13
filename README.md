# 🦁 xxd-skill · 小小东 AI 出图提示词与风格全库

> 把普通照片变成高级设计海报 / 编辑插画 / 包装提案 / 概念海报的**提示词与风格库**
>
> 作者 [@小小东](https://github.com/nevertoday)（小红书号 `biyiyiyibi`，X [@xiaoxiaodong01](https://x.com/xiaoxiaodong01)）

本仓库把作者散在三个地方的内容合并到一处：

| 层 | 来源 | 规模 |
| --- | --- | --- |
| **A · 小红书提示词库** | 小红书 139 条图文笔记 | 139 条提示词，其中 **21 条带附件完整版** |
| **B · 方法论与帖子独有风格** | X 帖子蒸馏 | 方法论总纲 + 6 个 panel 未覆盖的风格 |
| **C · 开源 panel 风格工程** | GitHub [nevertoday/xxd-panel-*](https://github.com/nevertoday) | **223 期**，每期一份原版风格 brief |

---

## 一、两个核心方法

### 上下分割双联法（版式母模板）

```
请将我上传的每一张照片分别制作成一张独立的高级设计海报，不多图拼接，每张照片单独输出。
整体采用3:4竖版构图，上下两个区域高度严格1:1，各占画面50%。
上半部分：保留原始照片 + 仅轻微高级摄影调色（艺术杂志／独立出版物／展览摄影质感）
下半部分：提取主体、轮廓、姿态与叙事关系，重构为【风格插槽】
```

### 五段式骨架（下半部分怎么写）

```
① 主体提取 → ② 构图留白 → ③ 风格材质 → ④ 配色 → ⑤ 文字
```

配套一句**授权句**：`真正赋予模型重新导演画面的权力`——139 条里 51 条含此意，43 条逐字写着「重新导演」。
**不能省**，省了模型会老实复刻原图，效果退化成滤镜。

详见 [`references/xxd-methodology.md`](references/xxd-methodology.md) 与
[`references/prompt-anatomy.md`](references/prompt-anatomy.md)。

---

## 二、编号体系（已实测确认三者关系）

**小红书的 `P###` 就是 GitHub 的 `xxd-panel-###`，一一对应。**
抽查 P047：小红书正文与 `panels/xxd-panel-047/prompt.zh-CN.md` 除一个标题行外逐字一致。

| 形式 | 含义 | 数量 |
| --- | --- | --- |
| `P###` | 小红书笔记标题里的系列号 | 70 条（编号 30–177） |
| `№###` | 作者正文里自报的解锁序号（`unlock_no`） | 39 条 |
| `xxd-panel-###` | GitHub 开源仓库名，1–223 连续 | 223 期 |

- 小红书发过的 70 个 P 号，GitHub 上**都有**；另外 **153 期**是小红书没发的。
- 全量对照见 [`references/panels-index.md`](references/panels-index.md)。
- ⚠️ `№` 与 `P` 区间重叠，`№` 只作溯源，不能用于 `--no` 检索。

---

## 三、目录结构

```
xxd-skill/
├── SKILL.md                        三层总控 + 风格路由
├── data/styles.json                139 条结构化数据
├── references/
│   ├── xxd-methodology.md          方法论总纲
│   ├── prompt-anatomy.md           五段式骨架逐句解剖
│   ├── styles-index.md             139 条风格索引表
│   ├── panels-index.md             223 期 panel 全索引 + 与 P 号对照
│   ├── attachments.md              笔记附件层（21 条清单 + 抓取配方）
│   └── usage-guide.md              落地细节与常见失败修法
├── scripts/
│   ├── build_prompt.py             生成可直接复制的提示词
│   ├── search_style.py             检索风格库
│   └── find_attachment.py          查作者附件
├── panels/                         223 期开源 panel 的文字部分
│   ├── _shared/                    共用运行期文件 + panel 提示词撰写指南
│   └── xxd-panel-001/ … 223/
├── styles/                         2026-08 早期整合版（37 期，已被 panels/ 取代）
└── styles-extra/                   6 个 panel 未覆盖的帖子独有风格
```

---

## 四、快速开始

```bash
# 取某一条风格的完整提示词（自动优先用附件完整版）
python scripts/build_prompt.py --no 47

# 关键词检索
python scripts/search_style.py 纸雕
python scripts/search_style.py --tag 像素栅格
python scripts/search_style.py --top 20          # 收藏数最高的 20 个
python scripts/search_style.py --attachments     # 只看附件完整版那 20 条

# 查笔记附件
python scripts/find_attachment.py --list
```

或者直接翻 [`panels/`](panels/)：223 期每期一份 `prompt.zh-CN.md`，逐字可复制。

---

## 五、panels/ 层说明

`panels/` 是从作者 223 个公开开源仓库同步下来的**文字部分**：

- **保留**：`prompt.zh-CN.md` / `prompt.en.md`（风格本体）、`SKILL.md`、中英 README、
  `samples.json`、`openai.yaml`、示例清单
- **省略**：`assets/examples/sample-*.png`（每仓约 18 MB，是本仓库体积的绝对主体，
  223 期合计 8.6 GB，故不随附）、`README.{ja,ko,ar}.md`（按要求只保留中英）、仓库基建文件
- **共用**：223 期完全一致的文件只存一份，放在 `panels/_shared/`（`soldier-runtime.md`、
  运行期脚本、「如何撰写 panel 提示词」指南等）

每期目录里另有一份 `SOURCE.md`，记着上游仓库地址与文件映射，方便回源。

> 上游仓库含完整的可运行 Codex Skill（含示例图与运行期脚本），需要跑图请直接去
> [github.com/nevertoday](https://github.com/nevertoday)。

---

## 六、边界与致谢

- 提示词、图片与附件版权归原作者 **@小小东**。本库仅供**个人学习与检索**；
  转载、商用、二次分发请回原帖并获授权。
- 不公开分发原作者图片与附件本体；不涉及作者的付费内容（vip.xiaoxiaodong.ai 提示词库 / 知识星球 / 会员 Skills）。
- 默认**不生成图片**，只交付提示词。
- 数据为公开页面的一次性快照，不含已删除、私密或受限内容。

## License

MIT
