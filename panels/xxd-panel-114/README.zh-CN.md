<div align="center">

# XXD Panel 114｜复古粉彩手账涂鸦

把照片理解后，重构成带纸张呼吸感的粉彩手绘拼贴

<strong>简体中文</strong> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 16:9 左右双联样张

以下四张为独立素材，完整 16:9 画布：左为现实摄影，右为本 Panel 设计转译，严格 50:50。文案由模型按原始提示词从当前照片智能生成。

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 114 样张 5"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 114 样张 6"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 114 样张 7"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 114 样张 8"></td>
  </tr>
</table>

## 3:4 上下双联样张

以下四张使用与 16:9 组完全不同的四张独立素材，重新生成完整 3:4 上下双联画布；上部保留现实摄影，下部遵循本 Panel 原始提示词重构。英文配字只从当前照片的内容、情绪或隐喻中生成。

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 114 新增上下样张 1"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 114 新增上下样张 2"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 114 新增上下样张 3"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 114 新增上下样张 4"></td>
  </tr>
</table>


## 适用场景与解决的问题

当照片需要用于海报、封面、社交内容、壁纸或独立出版物时，Panel 114 先理解照片最值得被记住的核心主题、主体关系、结构走势、情绪气氛与视觉隐喻，再将其转译为复古纸张肌理的粉彩手绘涂鸦插画。它解决了逐物转绘导致的呆板、画面填满导致的窒息、数字感过强以及复古配色灰脏的问题。

## 使用窍门

- **先给一张清楚的照片：** 先选一张主体、动作和关系都容易辨认的图，再决定输出方式与比例。
- **一句话串起参数：** 直接说“上下对照 / 左右对照 / 纯设计 + 16:9 / 3:4 / 手机壁纸”，也可以补充电脑、平板或电子手表尺寸。
- **把必须保留的内容说清楚：** 指定人物、物件、动作、关系和文字；避免同时规定过多布局细节，让风格有空间完成设计。
- **文字有三种选择：** 让模型按图片智能生成、用 `--text exact --copy` 锁定逐字文案，或用 `--text none` 完全不要文字。
- **说明现实区与设计区：** 上下或左右对照时，注明哪一侧保留照片、哪一侧负责设计转译；纯设计和壁纸则说明整张画布都要重新设计。
- **先单张试，再批量做：** 先用一张图确认模式、比例、文字和语言，再把同一套参数用于目录批处理；每轮只改一个变量，结果更容易比较。

## 开始使用

```bash
git clone https://github.com/nevertoday/xxd-panel-114.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-114" ~/.codex/skills/xxd-panel-114
```

也可以直接使用 `npx skills` 安装：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-114 --skill xxd-panel-114
```

命令会从 GitHub 获取仓库并安装同名 Skill；需要用户级 Codex 安装时，可追加 `--global --agent codex --yes`。安装后重新启动 Agent 会话，然后调用 `$xxd-panel-114`。

## 原始提示词 · 五种语言

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

中文文件逐字保存本项目的原始提示词，并且是运行时唯一的创作与审美权威；其他四个版本是完整、忠实的阅读译文，不会反过来改写生图提示词。

**关键词：** 手绘涂鸦 · 材料拼贴 · 粉彩蜡笔 · 牛皮纸／再生纸／手工纸肌理 · 小尺度章印 · 有意识留白 · 复古打字机式微排版

## 快速判断：Panel 114 适合你吗？

| 你关心的问题 | 这套风格的回答 |
|---|---|
| 想保留照片身份，又不想逐物照搬？ | 先理解主题、关系、走势、情绪与隐喻，再以少量结构和记忆点重组。 |
| 想要手账感而不是儿童插画？ | 不规整手绘线、干涩粉彩颗粒、真实纸张肌理与克制排版共同建立独立出版物气质。 |
| 担心画面太满？ | 小尺度章印与大面积有意识留白形成呼吸、空间、停顿和不对称平衡。 |

## 完整能力与边界

支持四种模式、普通比例与准确像素、模型文案／准确文案／无文字、目录批量，以及连贯或独立四端壁纸。输入目录会递归扫描常见位图，先报告数量，再一次解析共享设置；每张源图独立生成，所有 PNG 直接放进同一个新任务目录，不创建来源或模式子目录。默认一次生成完整画布，禁止把生成的中间图、样张或其他 Panel 成品再次送入模型；`compose_panel.py` 只作最终无损尺寸／分区校准或审计，不能创造或重绘设计。

## 文字与语言

需要文字时必须明确指定语言或地区；`prompt` 遵循原始提示词的小量复古打字机式文字逻辑，`exact` 逐字使用用户文案，`none` 禁止字母、数字、Logo 与伪文字。Skill 不预写标题，也不从人物、地点或文件名猜测语言。

## 四种输出模式

- `top-bottom`：现实照片在上，Panel 114 设计在下，严格各占 50%。
- `left-right`：现实照片在左，设计在右，严格各占 50%，不会旋转成上下结构。
- `design-only`：整张画布只呈现本 Panel 的设计转译，照片只作参考。
- `wallpaper-pack`：按设备分别生成完整画布；连贯壁纸先建立原图锚点，再逐设备独立重构。

<!-- xxd-readme-ads:start -->
## 关于 XXD

XXD 是小小东品牌名的缩写，本项目由小小东创建并维护：[@xiaoxiaodong01](https://x.com/xiaoxiaodong01)。

## 小小东多端会员 · 699 元/年

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。

一次年费，同时开通三项会员权益：**知识星球 + 小小东成员提示词库 + 全部 将军总指挥 Skills 会员**。三项权益合并在同一份会员中，无需分别购买。

<!-- xxd-panel-command-system:start -->

### Skills 如何协作

| 层级 | 包含内容 | 用途 |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/xiaoxiaodong-ai/xxd-panel-all) | 识别可用的编号 Skills，按图片、主题和用途推荐，并组织多风格试稿与批量任务。 |
| **Soldier** | `xxd-panel-NNN` | 每个编号执行自己的原始提示词与审美，完成 General 分派的具体任务。 |

<!-- xxd-panel-command-system:end -->

### 会员权益

1. **微信一对一 AI 学习与项目答疑**
   扫描下方二维码，添加小小东微信，围绕 AI 学习、工具使用和实际项目进行一对一沟通，获得答疑与建议；代表性问题将整理为会员内容。
2. **持续更新的成员提示词库**
   [小小东成员提示词库](https://vip.xiaoxiaodong.ai/)当前约有 3.2 万条提示词，会持续整理和扩充，目标超过 10 万条。
3. **全部 将军总指挥 Skills 与使用答疑**
   一份会员覆盖全部 将军总指挥 Skills；使用过程中遇到问题，可以获得相应的使用说明与答疑。
4. **高频刚需优先处理**
   会员提出的高频、刚需提示词与 Skills 需求，会优先评估和开发。

### 如何开通

- 可在[成员网站](https://vip.xiaoxiaodong.ai/)自助开通。
- 也可以扫描下方二维码，添加小小东微信，进行一对一沟通并获得开通协助。

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="联系小小东" width="280"></a></p>
<!-- xxd-readme-ads:end -->

## 许可证

本项目（包括 Skill、提示词、脚本、文档及随附样张）采用 **PolyForm Noncommercial License 1.0.0**。完整法律条文请见 [LICENSE](LICENSE)，官方页面见 <https://polyformproject.org/licenses/noncommercial/1.0.0>。

用人话说：

- 个人可以用于学习、研究、实验、测试、兴趣项目和私人娱乐；慈善机构、教育机构、公共研究/安全/卫生机构、环保组织及政府机构也可以使用。
- 在**非商业目的**下，你可以使用、复制、修改、制作衍生作品并分享；分享时必须同时提供本许可证（或上面的链接）以及作者提供的所有 `Required Notice:` 声明。
- 不允许用于商业产品或服务、收费交付、出售访问权或许可，或任何预期会带来商业应用的用途。需要商业使用时，请先向版权方另行取得书面许可。
- 本协议只授予其中明确写出的著作权许可和有限的专利许可，不授予商标、品牌名称或其他未明确授予的权利，也不能把你的许可再转授给他人。
- 如果收到书面违约通知，须在 32 天内纠正并采取实际补救措施，否则许可会立即终止；就专利侵权提出书面主张也会终止专利许可。
- 内容按“现状”提供，在法律允许的范围内不作任何担保，使用风险和可能的损失由使用者自行承担。
