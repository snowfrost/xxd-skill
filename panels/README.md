# panels/ · 223 期开源 panel 文字库

> 上游：[github.com/nevertoday](https://github.com/nevertoday) 的 `xxd-panel-001` ~ `xxd-panel-223`
> 全量索引（含风格名、字数、示例图链接、与小红书 P 号的对照）见 [`../references/panels-index.md`](../references/panels-index.md)

## 每期目录里有什么

| 文件 | 是什么 | 怎么用 |
| --- | --- | --- |
| **`prompt.zh-CN.md`** | **风格本体**（上游 `references/original-prompt/zh-CN.md`） | **逐字复制**，这是作者钦定的唯一审美权威 |
| `prompt.en.md` | 风格本体·英文版 | 国际平台用 |
| `SKILL.md` | 该期的 Skill 入口（上游原样） | 想按上游流程跑图时读 |
| `README.zh-CN.md` / `README.en.md` | 该期的完整说明文档 | 了解风格细节、示例与参数 |
| `SOURCE.md` | 溯源 + 文件映射 + **示例图在线链接** | 想看图时点这里 |
| `samples.json` | 示例清单 | — |
| `sample-workflow.md` | 示例工作流 | — |
| `openai.yaml` | 上游的 agent 配置 | — |
| `original-prompt.README.md` | 上游 original-prompt 目录说明 | — |
| `examples.README.md` | 上游示例图目录说明 | — |

## 没带什么、为什么

- **示例图 PNG/JPG 没带**——每期约 18 MB，223 期合计 8.6 GB，是上游仓库体积的绝对主体。
  本库只在 `SOURCE.md` 里留了每一张的在线链接，点开就能看。
- **日/韩/阿拉伯语版本没带**——按约定只保留中文和英文。
- **`.github/`、`.gitattributes`、`.gitignore` 没带**——仓库基建，与风格无关。

## 223 期共用的东西（只存一份）

在 [`_shared/`](_shared/)：

| 文件 | 说明 |
| --- | --- |
| `soldier-runtime.md` | 全 family 共用的运行期契约（参数、批量、预检、验收），上游每仓一份、内容完全一致 |
| `runtime-preferences.md` | 运行期偏好 |
| `sample-plan.md` | 示例规划 |
| `prompt-authoring-guide.zh-CN.md` / `.en.md` | **「如何撰写 panel 提示词」指南**。上游文件名叫 `references/xxd-panel-NNN-prompt.*.md`，名字带编号，但 223 期内容逐字相同——它不是每期提示词，是写法指南。真正的风格本体在每期的 `prompt.zh-CN.md` |
| `scripts/*.py` | 上游的 4 个运行期脚本（出图、拼版、偏好管理） |

## 怎么找风格

1. 先翻 [`../references/panels-index.md`](../references/panels-index.md) 的表格，按风格名/字数粗筛；
2. 点编号直达该期 `prompt.zh-CN.md`；
3. 想看效果点「图」列，跳上游 `assets/examples/` 图集。
