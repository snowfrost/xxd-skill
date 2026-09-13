# 小小东的「笔记附件」：作者放完整提示词的地方

小红书从 2025 年底开始支持**笔记文件附件**（笔记编辑页 →「添加组件」→「文件」，官方叫「文件」组件，网页端渲染为 `web_related_file` 组件）。@小小东 把 139 条笔记里的 **21 条**用上了这个功能——因为这些笔记的正文是引子，完整提示词太长，塞不进正文。

正文里他自己写得很直白：

> 「小红书一千字设置，发不上来，见附件吧~skills也在制作中。」
> 「需要提示词的朋友附件自取！」
> 「提示词在附件，很稳，去尝试吧，记得来交作业！」

## 为什么要专门做这一层

**同一套风格，正文版和附件版差了一倍。**

| | 条数 | 平均字数 |
| --- | --- | --- |
| 附件版（本次落库） | 20 | 约 1129 字 |
| 正文版 | 119 | 约 719 字 |

而这 21 条的**正文只有 92–379 字**，纯粹是「这组提示词干什么用」的介绍。真正的指令、材质词、禁忌词全在附件里。

所以 `data/styles.json` 里的 `prompt` 字段按优先级取值：

- `prompt_source: "attachment"` —— 用附件里的完整原文（20 条）
- `prompt_source: "caption"` —— 用笔记正文（119 条）

`attachment` 字段记着每条的 `doc_id`、文件名、页数、浏览量、下载量、发布日和本地文件路径。

## 附件清单速查

```bash
python scripts/find_attachment.py --list          # 全部 21 条
python scripts/find_attachment.py --no 34         # 按系列号
python scripts/find_attachment.py --no 34 --text  # 连完整提示词一起打印
python scripts/search_style.py --attachments      # 从风格库角度看这 20 条
```

附件原件（19 个 `.docx` + 2 个 `.pdf`）落在工作区：

```
<工作区>/media/xiaoxiaodong/attachments/          # 原件，文件名前缀是系列号
<工作区>/media/xiaoxiaodong/attachments_text/     # 提取出的提示词纯文本
```

## 21 条附件一览

| 系列 | 风格 | 附件文件 | 类型 | 页 | 下载 | 提示词 |
| --- | --- | --- | --- | --- | --- | --- |
| P053 | 手绘 · 即兴 | 小小东提示词-手绘.docx | DOCX | 2 | 19 | 1084 字 |
| P050 | 矢量插画 · 旅行 | 小小东提示词-矢量插画.docx | DOCX | 2 | 20 | 1345 字 |
| P049 | 版画 · 治愈系 | 小小东提示词-版画.docx | DOCX | 3 | 27 | 1232 字 |
| P048 | 蓝图 · 拆解 | 小小东提示词-蓝图.docx | DOCX | 2 | 17 | 1042 字 |
| P047 | 立体 · 厚涂 · 3D | 小小东提示词-立体.docx | DOCX | 2 | 403 | 1147 字 |
| P046 | 厚涂 · 浮现 | 小小东提示词-厚涂.docx | DOCX | 2 | 27 | 1031 字 |
| P045 | 积木 · 重构 | 小小东提示词-积木重构.docx | DOCX | 2 | 21 | 1132 字 |
| P044 | 金箔 · 转绘 | 小小东提示词-金箔转绘.docx | DOCX | 2 | 8 | 993 字 |
| P043 | 泡沫 · 重构 | 小小东提示词-泡沫重构.docx | DOCX | 2 | 6 | 1049 字 |
| P042 | 拆解 · 分层（水彩结构解构） | 小小东提示词-水彩结构解构.docx | DOCX | 3 | 24 | 1565 字 |
| P041 | 达芬奇手稿 | 小小东提示词-达芬奇手稿.docx | DOCX | 2 | 29 | 1272 字 |
| P035 | 乐高 · 转绘 | 小小东-乐高-35_提示词.docx | DOCX | 2 | 26 | 1065 字 |
| P034 | 断墨 · 印章 · 油墨 | 小小东-34_提示词.docx | DOCX | 3 | 322 | 805 字 |
| P033 | 喷墨 · 干刷 · 海报 | 小小东-33.docx | DOCX | 2 | 62 | 1078 字 |
| P032 | LOGO · 视觉 · 几何 | logo_提示词.docx | DOCX | 2 | 43 | 879 字 |
| P031 | 拓印粗粝 · 做旧 · 印刷 | 拓印_提示词.docx | DOCX | 2 | 218 | 1021 字 |
| P030 | GPT2 · 植物 · 重构 | 小小东提示词.docx | DOCX | 2 | 41 | 975 字 |
| — | 线条 · 色块 · 治愈（36 期） | 小小东提示词-36期极简线条.docx | DOCX | 2 | 9 | 1131 字 |
| — | isometric · 达芬奇 | 高级设计海报提示词.pdf | PDF | 1 | 33 | 1272 字 |
| — | 中式美学 · 窗景 · 朦胧 | 提示词.docx | DOCX | 2 | 27 | 1039 字 |
| — | 拆解 · 分层（制作说明） | 高级设计海报制作说明.pdf | PDF | 1 | 38 | **未能提取** |

最后一条：作者上传的 PDF 本身就把正文右侧裁掉了（页面是 A4 位图，文字行超出页面宽度），
原件与渲染图都已存档，但正文不可完整复原，故未纳入提示词库。同风格的完整版见上一行的
「isometric · 达芬奇」。

## 附件是怎么取到的（可复用配方）

需要**已登录的浏览器会话**（登录态在本地持久化目录里），页面上自带的签名函数 `window._webmsxyw` 可以直接算 XHS 接口要的 `X-s` / `X-t` 头。

**第一步 · 列出笔记下挂的附件**

```
POST https://edith.xiaohongshu.com/api/sns/web/v2/widgets
签名：_webmsxyw("/api/sns/web/v2/widgets", body)   ← POST 传 body
body：{"note_id": "<note_id>", "scene": "web", "mode": 1, "source": "web_feed",
       "exp_flags": {"web_support_related_search": true}}

→ data.widgets.widget_list[] 里找 biz_type == "web_related_file"
  model.title     文件名（如「小小东-34_提示词.docx」）
  model.biz_extra 是 JSON 字符串：{"doc_id": ..., "page_num": 3,
                                  "view_num": 1090, "download_num": 322}
```

**第二步 · 换真实下载地址**

```
GET https://edith.xiaohongshu.com/web_api/sns/v1/file/preview
    ?doc_id=<doc_id>&note_id=<note_id>&need_note_interact_info=true
签名：_webmsxyw(完整 path+query, null)              ← GET 必须把 query 一起签进去
      只签 path 会返回 406

→ data.download_url      带作者水印的原件（docx/pdf）
  data.preview_pdf_url   转档后的 PDF
  data.type / size / page_count / title / publish_time
  data.doc_interact_info {view_stats, download_stats, share_stats}
```

两点容易踩：**GET 的签名要把 query 拼进去**；**不带签名的裸请求返回 500 `create invoker failed`**——所以别想着绕开浏览器直接抓。

**第三步 · 拿到文件之后**

- `.docx` 是标准 zip，用 `python-docx` 或直接解 `word/document.xml` 取段落；
- 作者习惯把「引子 + Prompt by xiaoxiaodong: + 正式提示词」写在同一份文档里，
  甚至把同一段贴两遍（文本框一次、正文一次）；
  **可靠做法是以「请将我上传的每一张照片」为锚点截取**，再去掉相邻重复段。

## 顺手记一笔：作者开源的排版图鉴

同一批笔记里，@小小东 提到他在 GitHub 开源了排版构图图鉴（原「100 种排版」已扩到 350 种）：

- 仓库：`github.com/nevertoday/350-layout-compositions`（旧地址 `100-layout-compositions` 仍可访问）
- 内容：350 张高清排版构图 PNG，按 **8 个一级分类 / 33 个二级主题**组织（构图逻辑、视觉原则、出版广告、字体网格、网页 UI、影视、中国传统构图、演示文稿）
- 机器可读目录：`v2/catalog.csv`、`v2/catalog.json`
- 许可：交流、学习、个人参考可直接下载使用；二次发布/改编/商用需自行确认素材权利

跟本库的关系：本库解决「**怎么把照片重构成某种风格**」，那个仓库解决「**画面怎么排**」。
写提示词时想指定版式，可以先从它的分类里挑一个构图名塞进构图那一段。

## 边界

- 附件版权归原作者 @小小东，本层仅供个人学习检索；转载、商用、二次分发请回原帖并获授权。
- 不抓取、不搬运作者的付费内容（知识星球 / 会员提示词库 / 付费 Skills）；本层只覆盖**公开笔记上可直接下载的公开附件**。
- 附件里的作者水印是平台自动加的，不做去除。
