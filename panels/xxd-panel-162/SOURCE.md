# xxd-panel-162 · 来源

- 上游仓库：https://github.com/nevertoday/xxd-panel-162
- 上游自述：（无）
- 本目录只保留**文字部分**并做了扁平化，映射如下：

| 上游路径 | 本目录文件 |
| --- | --- |
| `SKILL.md` | `SKILL.md` |
| `README.md`（中文） | `README.zh-CN.md` |
| `README.en.md` | `README.en.md` |
| `references/original-prompt/zh-CN.md` | **`prompt.zh-CN.md`（风格本体）** |
| `references/original-prompt/en.md` | **`prompt.en.md`（风格本体·英文）** |
| `references/original-prompt/README.md` | `original-prompt.README.md` |
| `references/samples.json` | `samples.json` |
| `references/sample-workflow.md` | `sample-workflow.md` |
| `assets/examples/README.md` | `examples.README.md` |
| `agents/openai.yaml` | `openai.yaml` |

已省略：

- `assets/examples/sample-*.png|jpg` —— 示例图（每仓约 18 MB，是本仓库体积的绝对主体，且不随文字分发）
- `README.{ja,ko,ar}.md`、`references/original-prompt/{ja,ko,ar}.md` —— 按要求只保留中英
- `.github/`、`.gitattributes`、`.gitignore` —— 仓库基建

全库 223 期共用的文件（只存一份）见 `../_shared/`，其中
`_shared/prompt-authoring-guide.{zh-CN,en}.md` 上游名为 `references/xxd-panel-NNN-prompt.*.md`，
名字带编号但 223 个仓库内容完全相同，实为「如何撰写 panel 提示词」的通用指南，不是每期提示词。

## 示例图（未随附，点链接在线看）

共 25 张，位于上游 `assets/examples/`：

- [left_right-01.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/left_right-01.png)
- [left_right-02.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/left_right-02.png)
- [left_right-03.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/left_right-03.png)
- [left_right-04.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/left_right-04.png)
- [top_bottom-01.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/top_bottom-01.png)
- [top_bottom-02.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/top_bottom-02.png)
- [top_bottom-03.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/top_bottom-03.png)
- [top_bottom-04.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/PROMPT/top_bottom-04.png)
- [sample-05-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-05-unique.png)
- [sample-05.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-05.png)
- [sample-06-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-06-unique.png)
- [sample-06.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-06.png)
- [sample-07-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-07-unique.png)
- [sample-07.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-07.png)
- [sample-08-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-08-unique.png)
- [sample-08.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-08.png)
- [sample-09-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-09-unique.png)
- [sample-09.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-09.png)
- [sample-10-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-10-unique.png)
- [sample-10.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-10.png)
- [sample-11-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-11-unique.png)
- [sample-11.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-11.png)
- [sample-12-unique.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-12-unique.png)
- [sample-12.png](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/examples/sample-12.png)
- [input-04.jpg](https://raw.githubusercontent.com/nevertoday/xxd-panel-162/main/assets/inputs/input-04.jpg)

- 上游图集目录：https://github.com/nevertoday/xxd-panel-162/tree/main/assets/examples
