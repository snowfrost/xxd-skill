<div align="center">

# XXD Panel 228｜Artist-Made Paper Object

**Remakes a photo as a handmade indie paper object: naive cut paper and a few spot colours.**

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 228"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 228"></td>
  </tr>
</table>

<p align="center"><sub>Top: the original photo. Bottom: the same photo in this style.</sub></p>

## What it is

A Skill for AI agents such as Claude Code and Codex. Give it a photo and it paints a finished PNG following the original Panel 228 prompt.

- **What it looks like:** Your subject is remade as a small handmade paper piece: naive drawing, cut-paper colour blocks, rough simple geometry and a few lines, facing you front-on. It can float on its own or be gently held or pinched by a hand that is there only to show its size. You can see matte paper, risograph or screen-print grain, slight misregistration and unevenly cut edges. There are only two or three bold spot colours taken from the photo, such as vermilion, cobalt, grass green, bright yellow or coral, on cream-white paper, in bright soft light with just a faint contact shadow. Text looks drawn, printed or pasted straight onto the paper: small, naive, unevenly spaced, sometimes tilted or curved.
- **Keywords:** Handmade paper piece · Naive drawing · Cut-paper colour blocks · Risograph · Two or three spot colours · Optional hand
- **What you can make:** A top–bottom comparison (photo above, design below), a left–right comparison, the design alone, or a wallpaper set for phone, tablet, desktop and watch. Pick several at once, at any ratio or exact pixel size.
- **What it is not:** Not a filter and not a template: every image is redrawn from your photo, and each photo is its own job.

## Get started in three steps

**1. Install.** Works with Claude Code, Codex and other agents that support Skills:

```bash
npx skills add https://github.com/nevertoday/xxd-panel-228 --skill xxd-panel-228
```

Then restart your agent session. You can also `git clone` this repository and link the folder to `~/.claude/skills/xxd-panel-228` or `~/.codex/skills/xxd-panel-228`.

**2. Make sure your agent can generate images.** This Skill has no image model of its own; it uses your agent's image generation, preferably GPT Image 2.

- Codex works as is when its built-in image generation is on.
- Claude Code and other agents without built-in image generation need an OpenAI-compatible image API. It takes about five minutes: see [Setting up image generation](#setting-up-image-generation).

Not sure? Just try it. If images can't be generated, the Skill stops and tells you before doing any work.

**3. Send a photo and say one sentence:**

> Use xxd-panel-228 to turn this photo into a 3:4 top–bottom poster with an English title.

If your request is complete, it starts right away; anything you left out (layout, ratio, text) it asks about, usually in one or two questions. Results are PNGs in a new folder under `~/Desktop/xxd/xxd-panel-228/`.

## Which photos work best

**Works well**

- Simple subjects with character: a bird, a piece of fruit, a mug, a dog
- Everyday photos with one fun detail: a cat on a windowsill, a postbox on a corner, a potted cactus
- Photos you want as indie merchandise, a zine cover, a postcard or a small exhibition image

**Not a good fit**

- Photos that need realistic reproduction: ID photos, product shots, detailed architecture
- Busy wide scenes with many people that must be shown in full
- Requests for smooth vector art, plastic 3D or commercial packaging

## Samples

Each image below is a finished result this Skill made from one photo. The top–bottom and left–right sets use different photos.

### Top–bottom: photo above, design below

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-09.png" alt="XXD Panel 228"></td>
    <td width="50%"><img src="./assets/examples/sample-10.png" alt="XXD Panel 228"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-11.png" alt="XXD Panel 228"></td>
    <td width="50%"><img src="./assets/examples/sample-12.png" alt="XXD Panel 228"></td>
  </tr>
</table>

### Left–right: photo left, design right

<table>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-05.png" alt="XXD Panel 228"></td>
    <td width="50%"><img src="./assets/examples/sample-06.png" alt="XXD Panel 228"></td>
  </tr>
  <tr>
    <td width="50%"><img src="./assets/examples/sample-07.png" alt="XXD Panel 228"></td>
    <td width="50%"><img src="./assets/examples/sample-08.png" alt="XXD Panel 228"></td>
  </tr>
</table>

## Just say it

No parameters to memorise. Say what you want:

| You want | Say |
|---|---|
| Top–bottom comparison | Make a 3:4 top–bottom comparison |
| Left–right comparison | Make a 16:9 left–right comparison, photo on the left |
| Design only | Just the design, no photo, 9:16 portrait |
| A wallpaper set | Make matching wallpapers for phone, tablet, desktop and watch |
| Several ratios | Make this one at 1:1, 3:4 and 16:9 |
| Your own text | Use the title “Let the wind pass through” exactly as written |
| No text | No text at all |
| Text language | Write the text in Japanese |
| A whole folder | Turn every photo in this folder into a top–bottom comparison |
| Same as last time | Use my settings from last time |

Prefer the command line? The flags map one to one:

```text
/xxd-panel-228 photo.jpg --mode top-bottom --size 3:4 --text prompt --locale en-US
/xxd-panel-228 photo.jpg --mode design-only --size 9:16 --text none
/xxd-panel-228 ./photos --mode left-right --size 16:9 --text prompt --locale ja-JP
```

All flags are listed under [Parameters](#parameters).

## FAQ

**Does the original photo have to appear?** No. Ask for “design only” or a wallpaper set and the whole canvas is design.

**Who writes the text?** By default the image model writes it from your photo; you only choose the language. Give your own words and they are used exactly; or ask for no text. Anything that looks factual (places, dates, numbers) comes only from you or from what is visible in the photo, never invented.

**What if I don't like the result?** Say “one more”. It redraws from the original photo instead of editing the last result, so every attempt is different.

**Do photos in a batch mix together?** No. Each photo is generated on its own and never borrows another photo's colours, text or layout. Settings are asked once for the whole batch.

**Where do my photos go?** Only to the image model your agent uses. The Skill uploads nothing elsewhere and never prints endpoints or keys.

**How does this relate to other Panels?** XXD Panels are a family of styles, one per number, fully independent; install only the ones you like. To have AI recommend a style for a photo, or compare several at once, use the catalog [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all).

## Original prompt

This style is defined entirely by Xiaoxiaodong's [original prompt](references/original-prompt/zh-CN.md) (in Chinese). The Skill only appends the layout, size and text settings you choose; it never summarises, translates or rewrites the prompt.

Reading translations (for reading only; never sent to the image model): [English](references/original-prompt/en.md) · [日本語](references/original-prompt/ja.md) · [한국어](references/original-prompt/ko.md) · [العربية](references/original-prompt/ar.md)

## Setting up image generation

You need an OpenAI-compatible API that serves `gpt-image-2` (or a compatible model) and its API key. This creates a separate config and leaves your Codex settings alone:

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # or your compatible endpoint
env_key = "XXD_IMAGE_API_KEY"
EOF

# add to ~/.zshrc or ~/.bashrc so your agent can read them
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=your-key' >> ~/.zshrc
```

Reopen your terminal and agent, then check once from this Skill's folder:

```bash
python3 scripts/configured_imagegen.py probe
```

`"ok":true` means it works. The check only reports readiness; it never prints the endpoint or key. If your Codex already generates images through a compatible API, skip this step.

## Parameters

| Flag | Values |
|---|---|
| `--mode` | `top-bottom` · `left-right` · `design-only` · `wallpaper-pack` (phone, tablet, desktop, watch); combine freely |
| `--size` | `auto` recommended · `source` match the photo · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · exact pixels such as `2160x3840`; combine freely |
| `--text` | `prompt` written from the photo · `exact` your words (with `--copy "…"`) · `none` no text |
| `--locale` | text language, e.g. `zh-CN` `en-US` `ja-JP` `ko-KR` `ar` |
| `--wallpaper` | `linked` a matching set · `independent` four separate designs |
| `--wallpaper-size` | device pixels, e.g. `phone=1440x3200,desktop=3840x2160` |
| `--out` | another output root (default `~/Desktop/xxd/xxd-panel-228/`) |
| `--prefs` | `last` reuse · `edit` start from last time · `new` choose again · `off` don't remember this time · `clear` forget |

- With every value given, nothing is asked; otherwise only the missing values are. Pass a folder instead of `photo.jpg` to batch.
- Combinations are generated one by one: 2 modes × 3 sizes = 6 images, each composed for its own canvas rather than cropped.
- Comparisons are exactly 50:50. Usually the model paints only the design half and a script places the untouched photo beside it, so the split is centred and the photo is unchanged.
- Files are named like `source-001-street-top-bottom-3x4-1152x1536.png`, all in one flat task folder.
- Only layout, size, text mode and language are remembered, never photos, copy or keys.

## About XXD

XXD is Xiaoxiaodong's abbreviated brand name. This project is created and maintained by [@xiaoxiaodong01](https://x.com/xiaoxiaodong01).



## License

**Free for noncommercial use; commercial use needs separate permission.** This project (Skill, original prompts, scripts and documentation) is licensed under [PolyForm Noncommercial 1.0.0](LICENSE). The source is public, but it is not open source as the OSI defines it.

- **Free:** personal study and hobby work; making images from your own photos to keep or share on your personal accounts (not ads, sponsored posts or product promotion); noncommercial changes and redistribution with the LICENSE included.
- **Commercial use by individuals needs permission:** paid client work, ads and product promotion, small-batch merchandise, paid courses or communities. Usually granted, as the author confirms in writing.
- **Organisations must sign an agreement:** any commercial use by a company, studio, MCN or brand, internal use included, and any integration into an app, website, SaaS or API.
- **Not licensed:** reselling, renaming or repackaging the Skills, prompts or samples.
- The Xiaoxiaodong membership does not include a commercial licence. The original photos in the samples belong to their photographers and are shown for demonstration only.

To apply, add Xiaoxiaodong on WeChat and write "commercial licence". Full terms and the QR code: [Commercial licensing](COMMERCIAL.md).
