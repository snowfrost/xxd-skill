<div align="center">

# XXD Panel 118｜Graphite Whitespace Sketch Chronicle

Keep the relationships worth remembering, then recompose with pencil and whitespace.

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 16:9 Left–Right Samples

Four independent sources on complete 16:9 canvases: reality left, this Panel's design right, exact 50:50. English copy is generated from each photograph.

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 118 Sample 5"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 118 Sample 6"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 118 Sample 7"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 118 Sample 8"></td>
  </tr>
</table>

## 3:4 Top–Bottom Samples

Four further independent sources, different from the 16:9 set, regenerated as complete 3:4 top–bottom canvases. The original photograph remains above; the lower design follows this Panel's original brief.

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 118 additional top-bottom sample 1"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 118 additional top-bottom sample 2"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 118 additional top-bottom sample 3"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 118 additional top-bottom sample 4"></td>
  </tr>
</table>


## Best-fit situations and problems solved

When a subject is tiny, a background is cluttered, or an ordinary photograph needs the expression of an independent publication, **Panel 118** preserves the real photograph and re-directs the design region as a graphite thematic assemblage. It first decides what matters, then rebuilds scale, position, and whitespace.

### Best for

- Preserving photographic identity and texture while gaining an independently directed editorial poster.
- Keeping recognisable thematic relationships without tracing every object or copying the source layout.
- Black-and-white graphite, natural hatching, and generous whitespace rather than complex academic realism.
- Top-bottom, left-right, design-only, wallpaper, or directory-batch delivery.

### What it solves

- Actively improves tiny subjects, cluttered backgrounds, and ordinary compositions.
- Establishes a thematic assemblage through subtraction, rearrangement, cropping, and scale changes.
- Makes whitespace an active element using positive/negative shapes, density, and asymmetrical balance.
- Generates each original independently in one pass; paired modes remain exactly two 50:50 regions.

## Usage tips

- **Start with one clear photo:** choose a source whose subject, action, and relationships are easy to recognize before choosing the delivery format.
- **Join the parameters in one sentence:** say “top-bottom / left-right / design-only + 16:9 / 3:4 / phone wallpaper”; you can also name desktop, tablet, or smartwatch sizes.
- **State what must stay:** identify the people, objects, actions, relationships, and copy to preserve, while leaving room for the style to design the layout.
- **Choose a text mode:** let the model write from the image, lock exact wording with `--text exact --copy`, or remove text completely with `--text none`.
- **Clarify reality and design regions:** for top-bottom or left-right, say which region keeps the photograph and which region is redesigned; for design-only and wallpapers, say that the whole canvas is redesigned.
- **Test one image before batching:** confirm mode, ratio, text, and language on one source, then reuse the settings for a folder; change one variable per iteration.

## Getting started

```bash
git clone https://github.com/nevertoday/xxd-panel-118.git
npx skills add https://github.com/nevertoday/xxd-panel-118 --skill xxd-panel-118
```

Restart the agent session after installation, then invoke `$xxd-panel-118`. Add `--global --agent codex --yes` when a user-level Codex installation is wanted.

Common examples:

```text
/xxd-panel-118 photo.jpg --mode top-bottom --size 3:4 --text prompt --locale en-US
/xxd-panel-118 photo.jpg --mode left-right --size 16:9 --text prompt --locale en-US
/xxd-panel-118 photo.jpg --mode design-only --size 9:16 --text none
/xxd-panel-118 ./photos --mode design-only --size auto,3:4 --text prompt --locale ja-JP
```

See [SKILL.md](SKILL.md) for the full runtime contract and the [English](references/xxd-panel-118-prompt.en.md) or [Chinese](references/xxd-panel-118-prompt.zh-CN.md) runtime adapter.

## Original prompt · five languages

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

The Chinese original is preserved verbatim and is the sole runtime creative and aesthetic authority. The other four languages are complete reading translations and never rewrite generation instructions.

**Signature:** graphite pencil · natural hatching · little cross-hatching · light grey tones · thematic assemblage · active subtraction · abundant whitespace · optional 1–2 source-derived recognition colours

## Quick fit check

| What you need to know | What Panel 118 gives you |
|---|---|
| An ordinary source composition? | Independently re-directs the design instead of relying on the original layout. |
| Will it remain recognisable? | Keeps the most meaningful theme, structural movement, and relationships. |
| Traditional realistic drawing? | Loose, slightly naive forms with an illustrative quick-sketch sensibility. |
| Multiple delivery sizes? | Four modes, common/custom ratios, exact pixels, and directory batches. |

## Four output modes

- `top-bottom`: exactly two full-width regions, reality above and design below, 50% each.
- `left-right`: exactly two full-height regions, reality left and design right, 50% each; it never rotates into a top-bottom layout.
- `design-only`: the full canvas contains only Panel 118's designed translation; the photograph remains a non-visible reference.
- `wallpaper-pack`: creates complete artworks for phone, iPad, desktop, and watch, either `linked` as a coherent family or `independent` as four separate works.

Modes and sizes may be combined. Supported sizes include `1:1`, `3:4`, `4:3`, `4:5`, `5:4`, `2:3`, `3:2`, `9:16`, `16:9`, `21:9`, `5:7`, `7:5`, and exact pixels. Text can be prompt-generated, user-exact, or absent. A directory is inventoried recursively and every source is isolated while sharing one set of delivery settings; final PNG files remain flat in one fresh task directory.

<!-- xxd-readme-ads:start -->
## About XXD

XXD is Xiaoxiaodong's abbreviated brand name. This project is created and maintained by [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).

## Xiaoxiaodong multi-platform membership · CNY 699/year

> **Advertising disclosure:** The QR code, membership, and paid-service links below are XXD promotional information. Scanning or purchasing is entirely optional and does not affect access to this open-source project.

One annual membership unlocks three benefits together: **Knowledge Planet + the XXD Member Prompt Library + membership for all General Skills**. They are included in one membership; no separate purchase is required.

<!-- xxd-panel-command-system:start -->

### How the Skills work together

| Level | Included | What it does |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/xiaoxiaodong-ai/xxd-panel-all) | Detects available numbered Skills, recommends them by image, theme, or use, and organizes multi-style and batch tasks. |
| **Soldier** | `xxd-panel-NNN` | Each numbered Skill follows its own original brief and aesthetic to complete the specific task assigned by the General. |

<!-- xxd-panel-command-system:end -->

### What you receive

1. **One-to-one WeChat AI learning and project support**
   Add Xiaoxiaodong on WeChat via the QR code below to discuss AI learning, tools, and real projects one to one, with practical guidance and answers. Representative questions may be organized into member resources.
2. **A growing member prompt library**
   The [XXD Member Prompt Library](https://vip.xiaoxiaodong.ai/) currently contains about 32,000 prompts and will keep expanding, with a goal of exceeding 100,000.
3. **All General Skills and usage support**
   One membership covers every General Skill, with usage guidance and Q&A when you need help.
4. **Priority for high-need requests**
   Frequently requested, high-need prompts and Skills are reviewed and developed first where appropriate.

### How to join

- [Activate membership on the member website](https://vip.xiaoxiaodong.ai/).
- Or scan the QR code below to add Xiaoxiaodong on WeChat for one-to-one activation support.

<p align="center"><a href="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png"><img src="https://xiaoxiaodong.pages.dev/assets/wechat-qr.png" alt="Contact Xiaoxiaodong" width="280"></a></p>
<!-- xxd-readme-ads:end -->

## License

This project—including the Skill, prompts, scripts, documentation, and accompanying sample images—is licensed under the **PolyForm Noncommercial License 1.0.0**. See [LICENSE](LICENSE) for the full legal text and <https://polyformproject.org/licenses/noncommercial/1.0.0> for the official page.

In plain language:

- Individuals may use it for study, research, experimentation, testing, hobby projects, and private entertainment. Charities, educational institutions, public research, safety or health organisations, environmental organisations, and government institutions may also use it.
- For **noncommercial purposes**, you may use, copy, modify, create derivative works, and share it. When sharing, you must also provide this license (or the link above) and every `Required Notice:` statement supplied by the author.
- It may not be used in commercial products or services, paid delivery, sale of access or licences, or any use expected to lead to commercial application. Obtain separate written permission from the copyright holder before commercial use.
- The agreement grants only the copyright licence and limited patent licence expressly stated. It grants no trademarks, brand names, or other unstated rights, and you may not sublicense your licence to others.
- After written notice of a violation, you must return to compliance and take practical remedial steps within 32 days, or the licences terminate immediately. A written patent-infringement claim also terminates the patent licence.
- The material is provided “as is”, without warranty to the extent permitted by law. Users bear the risks and potential losses arising from its use.
