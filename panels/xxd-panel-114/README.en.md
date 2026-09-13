<div align="center">

# XXD Panel 114｜Retro Pastel Scrapbook Doodles

Understand the photograph, then rebuild it as a paper-breathing pastel hand-drawn collage

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

## 16:9 Left–Right Samples

Four independent sources on complete 16:9 canvases: reality left, this Panel's design right, exact 50:50. English copy is generated from each photograph.

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 114 Sample 5"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 114 Sample 6"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 114 Sample 7"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 114 Sample 8"></td>
  </tr>
</table>

## 3:4 Top–Bottom Samples

Four further independent sources, different from the 16:9 set, regenerated as complete 3:4 top–bottom canvases. The original photograph remains above; the lower design follows this Panel's original brief.

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 114 additional top-bottom sample 1"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 114 additional top-bottom sample 2"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 114 additional top-bottom sample 3"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 114 additional top-bottom sample 4"></td>
  </tr>
</table>

## Samples

**16:9 left–right samples**

| sample-05 | sample-06 |
|---|---|
| ![XXD Panel 114 16:9 left-right sample 05](assets/examples/sample-05.png) | ![XXD Panel 114 16:9 left-right sample 06](assets/examples/sample-06.png) |
| ![XXD Panel 114 16:9 left-right sample 07](assets/examples/sample-07.png) | ![XXD Panel 114 16:9 left-right sample 08](assets/examples/sample-08.png) |

**3:4 top–bottom samples**

| sample-09 | sample-10 |
|---|---|
| ![XXD Panel 114 3:4 top-bottom sample 09](assets/examples/sample-09.png) | ![XXD Panel 114 3:4 top-bottom sample 10](assets/examples/sample-10.png) |
| ![XXD Panel 114 3:4 top-bottom sample 11](assets/examples/sample-11.png) | ![XXD Panel 114 3:4 top-bottom sample 12](assets/examples/sample-12.png) |

Sample sources come from different original reference images, are isolated by reference directory, and were generated independently by this Panel in a single complete-canvas pass. Samples 05–08 place the original photograph on the left and the design on the right; samples 09–12 place the original above and the design below. Both layouts use a strict 50:50 split. Every sample uses intelligent English copy derived from its current photograph; its dimensions, format, and basic metadata have been verified, and AI metadata has been removed.

## Where this Panel fits — and what it solves

For posters, covers, social content, wallpapers, or independent publications, Panel 114 first understands the photograph’s most memorable core theme, relationships between subjects, structural flow, emotional atmosphere, and visual metaphor. It then translates that reading into a pastel hand-drawn doodle illustration with retro paper texture. It avoids the stiffness of object-by-object redraws, the suffocation of a filled frame, an overly digital finish, and muddy retro colour.

## Usage tips

- **Start with one clear photo:** choose a source whose subject, action, and relationships are easy to recognize before choosing the delivery format.
- **Join the parameters in one sentence:** say “top-bottom / left-right / design-only + 16:9 / 3:4 / phone wallpaper”; you can also name desktop, tablet, or smartwatch sizes.
- **State what must stay:** identify the people, objects, actions, relationships, and copy to preserve, while leaving room for the style to design the layout.
- **Choose a text mode:** let the model write from the image, lock exact wording with `--text exact --copy`, or remove text completely with `--text none`.
- **Clarify reality and design regions:** for top-bottom or left-right, say which region keeps the photograph and which region is redesigned; for design-only and wallpapers, say that the whole canvas is redesigned.
- **Test one image before batching:** confirm mode, ratio, text, and language on one source, then reuse the settings for a folder; change one variable per iteration.

## Get started

```bash
git clone https://github.com/nevertoday/xxd-panel-114.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-114" ~/.codex/skills/xxd-panel-114
```

You can also install it directly with `npx skills`:

```bash
npx skills add https://github.com/nevertoday/xxd-panel-114 --skill xxd-panel-114
```

The command fetches the repository and installs the same-named Skill. Add `--global --agent codex --yes` for a user-level Codex install. Restart the Agent session, then invoke `$xxd-panel-114`.

## Original prompt · five languages

[简体中文](references/original-prompt/zh-CN.md) · [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

The Chinese file preserves the supplied original prompt word for word and is the sole creative and aesthetic authority at runtime. The other four files are complete, faithful reading translations and never rewrite the image-generation prompt.

**Keywords:** hand-drawn doodles · material collage · pastel crayon · kraft/recycled/handmade paper texture · small seal-like motif · intentional negative space · retro typewriter microtype

## Quick check: is Panel 114 right for you?

| You need | Panel 114 provides |
|---|---|
| Keep the photograph recognisable without copying every object | Understand theme, relations, flow, mood, and metaphor, then retain only essential structure and memory points. |
| A scrapbook feeling rather than a children’s illustration | Irregular hand lines, dry pastel grain, real paper texture, and restrained editorial layout. |
| Room to breathe | A small seal-like motif and generous intentional negative space create pause, space, and asymmetrical balance. |

## Recognisable output signature

- The original photograph and design belong to one complete canvas; `top-bottom` and `left-right` comparisons are strict 50:50 with no third band.
- The design rests on authentic kraft-, recycled-, or handmade-paper texture with subtle grain and a reduced digital feel.
- Lines stay deliberately irregular and colour fields have dry edges, like light marks from crayon, chalk, or coloured pencil; the subject and a few supporting elements are recombined like stickers, paper pieces, or symbols around the narrative.
- The subject remains a small seal-like motif; negative space is active composition, working with positive/negative shapes, density, gathering, dispersion, and asymmetry.
- Text is a minimal editorial intervention in small, restrained, slightly mechanical, subtly misregistered retro typewriter lettering—not stacked commercial headlines.

## Capabilities and boundaries

Supports four modes, common ratios or exact pixels, prompt/exact/none text, directory batches, and linked or independent four-device wallpapers. Directories are scanned recursively, counted before generation, and resolved once for shared settings; every source is generated independently and all PNGs go directly into one fresh task directory. Generate one complete canvas by default. Never send an intermediate, sample, or another Panel result through a second transformation pass; `compose_panel.py` is only for final lossless sizing, splitting, or audits.

## Text and language

Specify the target language or locale whenever text is requested. `prompt` follows the brief’s small retro typewriter logic, `exact` preserves the user’s wording verbatim, and `none` forbids letters, numbers, logos, and pseudo-text. The Skill does not prewrite titles or infer language from a person, place, or filename.

## Four output modes

- `top-bottom`: original photograph above, Panel 114 design below, exactly 50% each.
- `left-right`: original photograph left, design right, exactly 50% each; never rotate into a top-bottom layout.
- `design-only`: the full canvas shows only this Panel’s translation; the photograph is reference only.
- `wallpaper-pack`: generate a complete canvas for each device; linked packs establish an anchor from the original, then recompose each device independently.

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
