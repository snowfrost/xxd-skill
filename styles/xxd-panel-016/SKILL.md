---
name: xxd-panel-016
description: "Create XXD Panel 016 artwork from supplied photos in four independently selectable modes that may be combined: photo above/design below, photo left/design right, transformed Riso design alone, or a four-device wallpaper pack with either independent compositions or anchor-linked visual continuity. Uses source-adaptive sizing by default, exact 50/50 paired layouts, optional custom dimensions, and an explicit preflight choice for copy, locale, or text-free output. Use for grain-field Riso transformations and the exact 016 style; never use it for collages."
---

# XXD Panel 016 · 粗粝动态场版画

Turn every supplied photograph into finished artwork. Each selected mode may show the source photo above, show it on the left, omit it from one transformed canvas, or expand it into four separately composed device wallpapers while still using it as the sole content source.

Operational rules follow the shared XXD Panel workflow contract: four combinable modes; source-adaptive ordinary canvases; exact 50/50 paired geometry; linked or independent four-device wallpapers; copy and locale preflight; fresh generation jobs; privacy-preserving raster generation; and one fresh task directory per source and mode. Style-specific sections may refine aesthetics, copy hierarchy, and acceptance criteria but never override this contract.

## Non-negotiable contract

- One source photo may be processed in one or more selected modes. Each selected ordinary mode (`top-bottom`, `left-right`, `design-only`) produces one output; selected `wallpaper-pack` produces exactly four separate files. Selecting all four modes therefore produces seven final PNGs per source. Keep every mode in its own task directory and never combine modes or wallpaper files into a grid, collage, contact sheet, or overview.
- Resolve a non-empty ordered set of output modes before generation: `top-bottom` (photo above, design below), `left-right` (photo left, design right), `design-only` (only the transformed design is visible), and/or `wallpaper-pack` (phone, iPad, desktop, and watch wallpapers). Accept one choice, multiple choices separated by `+`, Chinese/English commas or whitespace, natural-language names, or `全部` / `all`. Deduplicate repeated choices and execute in menu order 1→4. If none is specified, ask the concise multi-select question in the workflow and wait; never ask again when the selected set is already clear.
- When the selected set contains `wallpaper-pack`, it has a second required choice: `linked` continuity or `independent` compositions. Ask the two-choice follow-up in the workflow whenever that relationship is not already specified. `linked` uses one approved wallpaper as a visual anchor for the other three; `independent` gives every device only the original source photo. Neither relationship permits mechanical resizing, cropping one wallpaper into another, or returning fewer than four files. Do not ask this follow-up when wallpaper mode is not selected.
- In `top-bottom` and `left-right`, the two panels are always exact 50/50. In `design-only`, there is no photographic panel and no seam; the transformed design fills the entire final canvas.
- Pixel dimensions supplied by the user have highest priority, followed by an explicit canvas ratio or destination. Otherwise use source-adaptive sizing: each paired panel keeps the source photo's complete pixel dimensions and aspect ratio, so `top-bottom` becomes source width × twice source height, `left-right` becomes twice source width × source height, and `design-only` uses the source dimensions. Generate the transformed asset at that planned aspect and the closest supported high-quality size before composing; prefer the exact frame size, otherwise resize proportionally without cropping. Never generate at a stock ratio and crop it into place. An exact paired layout requires an even split-axis dimension only when the user overrides the adaptive size.
- Any visible photographic region remains faithful. Allow only restrained editorial color grading and seamless environmental extension needed to fit its frame. Never stretch, distort, redraw, replace, or structurally alter the subject. In `design-only` and every wallpaper output, use the source only as evidence and render none of it in the final artwork.
- The transformed design region is a photo-derived Riso/silkscreen field: one small recognizable anchor, one subject-derived motion logic, and 60%–78% clean void. It is not a trace, realistic painting, clean vector scene, or unrelated abstraction.
- Use a strict 2–3 color system derived from the source: one spirited source color, warm paper, and optional small black.
- Copy has no silent default. Before generation, resolve one explicit choice: source-derived automatic copy, user-supplied exact copy, or text-free output. By default, one source-specific copy package is shared verbatim across all selected modes; accept explicit per-mode copy overrides when the user supplies them. Automatic or direction-led copy contains one main title and 2–4 microtext groups. Custom copy requires an exact main title; user microtext is optional, and supporting microtext may be professionally derived unless the user explicitly requests title-only.
- Resolve copy locale independently from the language used to issue the command. Use this priority for automatic or direction-led copy: explicit target market/audience locale > explicit output language > language of the supplied direction; if none is explicit, ask before generation. Never infer audience language, nationality, or ethnicity from a face, name, clothing, scenery, filename, metadata, or visible signage. Localize by transcreation—native wording, register, rhetoric, punctuation, and line breaking—not literal translation or foreign-looking pseudo-text. Arabic output uses natural Modern Standard Arabic unless the user names a regional variety; preserve connected letterforms, right-to-left reading order, Arabic punctuation, semantic line breaks, and deliberate handling of embedded Latin text or numerals. Do not mirror the artwork indiscriminately: reverse text flow and typographic alignment while keeping source-derived subject direction and composition intentional. Preserve exact finished copy verbatim unless the user explicitly asks to translate/localize it; if exact wording conflicts with an explicitly named target locale and permission is unclear, ask one concise clarification before generation.
- Render no logo, watermark, signature, color swatch, UI chrome, mockup frame, or unrelated explanatory prose.

## Aesthetic motive lock

Mode and device constraints may change placement and aspect ratio, never the 016 aesthetic motive. Every transformed frame must visibly express this chain: **this exact photographed subject → one compressed recognizable anchor → one motion logic derived from its posture, light, or spatial relation → a vast paper void → physical Riso/silkscreen texture → experimental art-book typography as spatial rhythm**.

Reject a result as generic when its source could be replaced by an unrelated photo without materially changing the anchor, motion field, palette, or copy. Do not accept decorative wallpaper, generic rings, sun/wave/mountain icons, stock abstraction, or empty paper texture merely because it uses the right colors. Device safe areas are secondary placement constraints; they must not remove the anchor, motion logic, print texture, main title, or typographic hierarchy.

## Raster generation and privacy

Use Codex's built-in `image_gen` capability by default for every generated or edited visual asset, following the available `imagegen` skill. If a local source image must be used, view it first so it is visible to the built-in edit/generation flow. Issue one built-in call per distinct asset; a four-device wallpaper pack requires four separate calls, not one `n` request. In `linked`, one of those four outputs is the approved visual anchor—it is not an extra fifth master and never becomes a crop source. “Flat,” “graphic,” “printmaking,” or “vector-like edge” describes appearance only; it never authorizes SVG construction. Do not create or return SVG, HTML, CSS, Canvas, diagrams, hand-coded vector markup, or other code-rendered substitutes. Generate bitmap assets, move/copy selected outputs from Codex's generated-images location into the requested output directory, finalize them with `scripts/compose_panel.py`, and deliver PNG files. The script is only for deterministic raster planning, crop/paste, sizing, and audit—not for inventing the artwork.

Judge image-generation readiness by capability, not by a provider name or the presence of one particular environment variable. A missing environment variable is not proof that authentication or bitmap generation is unavailable: the host, an authenticated session, a credential store, a configured SDK, or another compatible route may already provide it. If built-in `image_gen` is not exposed, check only non-secret capability signals for an already configured bitmap route: compatible image model or endpoint, authenticated readiness, and actual PNG/raster output support. Do not hardcode or mention a specific proxy/provider in this policy.

When built-in `image_gen` is unavailable, use the bundled `scripts/configured_imagegen.py`; do not fall back first to a CLI that recognizes only one fixed environment variable. This bridge reuses the active Codex route in-process without changing global configuration:

```bash
# Readiness only: prints sanitized JSON, never route or credential details
python3 scripts/configured_imagegen.py probe

# This skill always has a source reference, so transformed assets use edit
python3 scripts/configured_imagegen.py edit --image source.png \
  --prompt-file /private/job-temp/transform-prompt.txt \
  --out /private/job-temp/design.png --size 1536x1024 --quality high
```

Use `generate` only for an asset that genuinely has no image reference. The bridge normalizes an API generation size when required and writes the requested final PNG dimensions. Keep the prompt file and generated intermediates in a per-job temporary directory outside the finished task directory, then remove the prompt file after the generation step. Do not pass provider settings, credentials, or full prompts as command-line values.

Protect provider identity and credentials throughout discovery and execution. Never display, echo, log, serialize, paste into chat, or include secret values in commands whose output may expose them. Also never report or persist provider names, endpoint URLs, IP addresses, domains, ports, request-header names or values, account identifiers, authentication modes, or credential-store contents. Do not open configuration or credential files for manual inspection or reporting; only the bundled bridge may resolve them internally for the authorized request. Do not run it with shell tracing, verbose HTTP output, environment dumps, `tee`, or process inspection. Its probe/output JSON is the entire allowed diagnostic surface: readiness, sanitized phase/reason, HTTP status, and final artifact path. Do not claim that a key is missing unless a trusted sanitized status explicitly establishes that fact, and never ask the user to paste a key into chat.

An explicit invocation of `/xxd-panel-016` or `$xxd-panel-016`, followed by the source image and requested mode, is the user's explicit confirmation to create the requested PNG deliverable through any already configured, authenticated raster route available to the session. This satisfies the `imagegen` skill's confirmation requirement for switching from an unavailable built-in tool to a compatible configured CLI/API route. Do not ask for a second confirmation merely because the execution route changes. This authorization is limited to the requested image generation: it does not authorize adding or changing credentials, providers, accounts, billing, or global configuration.

Only report image generation as unavailable after built-in capability and `scripts/configured_imagegen.py probe` both fail to establish a usable bitmap route. State the verified limitation narrowly instead of guessing its cause, and refer only to the “configured bitmap route”—never identify the provider. Never silently substitute SVG or programmatic drawing, and never modify credentials, provider settings, accounts, billing, or global environment variables as a workaround.

## Fresh-task and source boundary

Every invocation is a new generation job unless the user explicitly asks to continue, audit, review, edit, or reuse a named earlier result. Repeating the same source, mode, dimensions, or wording means **generate a fresh result**, not return or re-audit a matching old file. Resolve the next unused task-directory name before generation and write the new deliverable there; an existing result can never satisfy the current job.

Build the source set only from images attached to the current invocation, paths explicitly supplied by the user, or earlier user-supplied source images that the current request explicitly identifies with wording such as “same image” or “again.” A conversation attachment remains the intended source even when it has no usable local filesystem path. Do not replace it with an arbitrary workspace file.

Never scan the Desktop, current workspace, default output root, or unrelated folders broadly to find “some image” when a source is missing. Files under `~/Desktop/xxd/xxd-panel-016/`, task directories created by this skill, and files carrying this skill's output suffixes are historical outputs, not source candidates. Do not inspect or reuse them unless the user explicitly names one as an input or asks for comparison/review. If the intended source cannot actually be accessed, ask for that source or its path; do not improvise from an existing poster.

Do not downgrade a new generation request into validation of an old artifact. If no usable raster route is verified, report only that verified execution limitation; never present an earlier file's dimensions, seam audit, or visual review as completion of the new job.

## Workflow

1. Resolve the selected mode set and canvases before generation. If the user did not specify any mode, use the line breaks and numbered-list structure below. Present its contents as normal chat text, not as a code block, and never collapse the choices into one sentence:

   ```text
   请选择一个或多个模式（回复序号；多选可用 +、顿号或逗号）：

   1. 上下双联（完整原图＋同尺寸设计图）
   2. 左右双联（完整原图＋同尺寸设计图）
   3. 纯设计版（沿用原图比例，不显示原照片）
   4. 四端壁纸套装
      手机＋iPad＋电脑＋儿童手表

   前三种不指定尺寸时按原图自适应；也可主动指定尺寸。壁纸套装可按设备分别给分辨率。
   示例：1｜1+3｜1、2、4｜全部
   ```

   Accept names, numbers, natural-language equivalents, `all` / `全部`, ratios, or exact pixels in the same reply. Normalize the answer to a deduplicated set in menu order. Do not ask this question when the request already contains one or more clear modes.
   When the resolved set contains `wallpaper-pack` and the user has not already supplied the relationship, ask only this follow-up and wait:

   ```text
   请选择壁纸关系（回复序号即可）：

   1. 连贯套装（推荐）
      先生成 iPad 定调图；其他三张参考原照片＋定调图分别重构
   2. 四张独立
      每张只参考原照片，构图变化更自由
   ```

   Accept `1`, `linked`, `连贯`, or equivalent as linked; accept `2`, `independent`, `独立`, or equivalent as independent. Do not ask this follow-up when the relationship is already clear. Use iPad as the linked anchor unless the user explicitly names another anchor device.
2. Before any image-generation call, resolve the copy choice and target locale. If either is missing, ask the following single preflight question and wait. Present it as normal chat text, not a code block. The user may answer this together with the mode selection; do not ask again when the request already makes both copy mode and locale clear:

   ```text
   正式做图前，请确认文字设置（回复序号即可）：

   1. 自动文案
      我根据原图内涵创作文案；请同时注明语言或地区
   2. 自定义文案
      请直接输入主标题、可选微型文字，并注明语言或地区
   3. 无文字

   示例：1｜阿拉伯语（现代标准阿拉伯语）
   示例：2｜英式英语｜主标题：STAY CLOSE｜微型文字：...
   ```

   `Automatic` requires an explicit target language or locale; `custom` requires the exact main title and an explicit target language or locale. User microtext is optional: professionally derive 2–4 supporting strings from the exact title and source unless the user supplies them or explicitly requests title-only. `Text-free` needs no locale. Treat wording such as “你来写中文”, “use my Japanese title …”, or “不要字” as already resolved. Never infer the copy language from a photographed person, visible sign, filename, or the language of the command when this preflight is required.
3. Resolve dimensions independently for every selected mode with this priority: exact pixel size > explicit ratio/destination > source-adaptive dimensions. For adaptive `top-bottom`, use source `W×H` as both panel sizes and output `W×2H`; for adaptive `left-right`, use source `W×H` as both panel sizes and output `2W×H`; for adaptive `design-only`, output `W×H`. This preserves the entire photograph and makes the generated design natively fit the adjoining frame. For user-specified paired sizes, height must be even in `top-bottom` and width must be even in `left-right`; do not silently alter an odd split dimension. When multiple modes are selected, custom sizes must be labeled by mode; if one unlabeled size could apply to more than one selected mode, ask which mode or modes it belongs to instead of applying it arbitrarily. Unlabeled ordinary modes remain source-adaptive. `wallpaper-pack` is destination-driven rather than source-adaptive and has no silent size default. Only when wallpaper mode is selected and four device resolutions are not already clear, ask the user to choose either the common device preset—phone 1440×3200, iPad 2048×2732 portrait, desktop 3840×2160, watch 1024×1024—or provide labeled custom resolutions. Wait for this choice before generation; ask which device an unlabeled pack size belongs to rather than applying it arbitrarily.

   For unresolved `wallpaper-pack` sizing, present this as normal chat text and wait:

   ```text
   请选择壁纸尺寸（回复序号即可）：

   1. 常用设备预设
      手机 1440×3200｜iPad 2048×2732｜电脑 3840×2160｜儿童手表 1024×1024
   2. 自定义分辨率
      请分别输入手机、iPad、电脑、儿童手表的尺寸
   ```
4. Open one new job boundary. Reserve one fresh sibling task directory per source and selected mode using the output rules below, even when an identical earlier result exists. Confirm the actual user-supplied source set under the source-discovery rules above. If none is accessible, ask the user to attach it or provide its path; do not invent a source photo or search output folders for a substitute.
5. Inspect each current-job source image separately. For a local file that has not been seen, use the available image-viewing tool before generation. Never inspect an earlier output in place of the current source.
6. Read the full prompt matching the user's working language:
   - Chinese: [references/xxd-panel-016-prompt.zh-CN.md](references/xxd-panel-016-prompt.zh-CN.md)
   - English: [references/xxd-panel-016-prompt.en.md](references/xxd-panel-016-prompt.en.md)
7. Internally lock three to five decisive source facts: the single recognizable subject, essential contour, posture/facing, center of gravity, light or spatial relationship. Read the image on three grounded levels: literal fact, emotional or relational tension, and the latent implication suggested by their combination. Never invent biography, events, ownership, location, or feelings that the visible evidence cannot support. Then derive exactly one motion logic—falling, rising, flowing, radiating, or ripple/echo. Do not print this analysis unless the user asks for it.
8. Resolve and lock one source-specific copy package before generation. Share it verbatim across all selected modes by default, including `wallpaper-pack`, so wording does not drift between formats. If the user explicitly supplies per-mode copy settings, lock and honor those overrides separately. Use this priority: explicit text-free request > exact user wording > user creative direction or editable draft > source-derived 016 copy. Resolve the target locale by the contract above before writing. A Japanese destination uses natural contemporary Japanese, appropriate kanji/kana balance and Japanese punctuation with kinsoku-aware phrase breaks; a Korean destination uses natural contemporary Korean, correct spacing and intact Hangul syllable blocks without decorative pseudo-Hanja; a UK destination uses British spelling, vocabulary, punctuation, date conventions, and culturally natural understatement rather than American wording. Apply the same native-register principle to every other locale. Preserve the semantic turn through transcreation instead of translating a pun or idiom word-for-word. Before writing direction-led or automatic copy, privately state one image-specific semantic core and choose one restrained rhetorical hinge—precise naming, contrast, understatement, double meaning, or reversal. Aim for quiet recognition: the title should make the viewer see the photograph differently and feel inseparable from it, never rely on a forced pun, slogan, generic inspiration, or unsupported story. Apply the swap test: if the same title could fit an unrelated photo without losing force, rewrite it. Exact user wording is semantic authority and stays verbatim; interpret its emphasis and phrase boundaries so hierarchy and line breaks strengthen rather than distort it. For a direction or editable draft, preserve the intended audience, tone, mandatory terms, and implied meaning while refining within the permission given; ask one concise question only when ambiguity would materially change the message, otherwise choose the most conservative faithful reading. For automatic or direction-led copy, record one main title and 2–4 finished microtext strings that form one semantic system rather than random labels. For custom copy, preserve the exact title, use every supplied microtext string, and derive supporting microtext only when the user did not request title-only. The title must be unmistakably larger than the microtext and readable at normal viewing size. Do not reuse one photo's copy for another unless the user explicitly requests shared wording.
9. Run `scripts/compose_panel.py --plan` for every selected mode and its resolved dimensions. For selected `wallpaper-pack`, run four `design-only` plans, one for each resolved device size.
10. For every selected paired mode, use the source photo unchanged in the source-adaptive frame: no crop, outpaint, stretch, or resampling is needed because the frame is exactly the source dimensions. Only when the user explicitly overrides that mode's canvas may a restrained crop or isolated environmental extension be used to fit that chosen frame; prefer extension whenever cropping would diminish the subject. Skip this step entirely in `design-only` and `wallpaper-pack`.
11. Generate each distinct transformed design alone at the planned design-frame aspect and preferably its exact size. When the image route cannot emit those exact pixels, use the closest supported size with the identical aspect and let the compositor resample proportionally without cropping. Use the full reference prompt plus the aesthetic motive lock, source facts, motion, 2–3 colors, locked copy package, and the resolved mode block below. In `design-only`, this frame is the entire final canvas. For an `independent` wallpaper pack, generate all four device compositions separately from the original source. For a `linked` pack, generate the resolved anchor device first—iPad by default—from the original source, then open it and require it to pass the source-identity, aesthetic, copy, and safe-area gates before continuing. Generate each remaining device as a fresh target-size composition using both the original source and that same approved anchor.
   Within the same current invocation, selected ordinary modes may reuse one newly approved transformed intermediate only when design-frame dimensions, aspect ratio, source facts, aesthetic instructions, and locked copy are identical; this is current-job reuse, never historical-output reuse. Otherwise generate each mode separately. Wallpaper assets are always generated separately.
12. Keep every generation or edit call isolated to the current source photo. Selected ordinary modes and `independent` wallpaper calls receive only that source. A `linked` derivative receives exactly two image references: the original photo as content/identity evidence and the approved anchor as visual-family evidence for palette, graphic grammar, typography, motion treatment, and print texture. All three derivatives point directly to the same anchor; never use phone → desktop → watch or any other sequential chain, because accumulated drift would replace the source logic. With the configured bridge, pass the two roles as repeated `--image` arguments. Normally this requires one design generation, or four design generations for `wallpaper-pack`, plus one photographic edit only in a paired mode when environmental extension is necessary.
13. Use the script to compose or finalize every selected mode in menu order. For `wallpaper-pack`, finalize and dimension-audit all four files separately.
14. Open and visually inspect every finalized image at normal view and thumbnail size; never infer aesthetic success from a completed generation call, valid dimensions, or a clean seam. Compare it with the source facts and aesthetic motive lock, then apply the acceptance gate. In a `linked` pack, inspect and approve the anchor before fan-out; never propagate a failed anchor. When a hard invariant is broken—including a generic or source-independent design, generic copy that fails the swap test, distorted or weakened user intent, a missing/weak title hierarchy, second focal subject, multiple motion logics, missing print texture, visible source photo in a source-hidden mode, unsafe wallpaper composition, or linked-family drift—retry only the faulty generated asset once, then finalize, reopen, and recheck. After one failed correction, return the best result and explicitly name the unresolved issue instead of silently presenting it as successful.
15. Return the finished artworks in source order, then menu order 1→4, with absolute saved paths. A wallpaper pack returns phone, iPad, desktop, then watch. Apart from a necessary failure note, do not add design analysis, title candidates, or parameter lists.

## Generation payload and composition commands

Use the same deterministic script for every canvas. `wallpaper-pack` is a skill-level batch of four `design-only` canvases, not a fourth split layout inside the script. The selected wallpaper relationship changes the generation references, not the output count or finalization commands:

For multi-select, run the applicable command block once per selected mode and save each result in its own sibling task directory. `all` / `全部` means the three ordinary results plus four wallpaper files—seven PNGs per source, never a combined overview.

```bash
# top-bottom: source-adaptive, exact horizontal seam
scripts/compose_panel.py --plan --layout top-bottom --source photo.png
scripts/compose_panel.py --source photo.png --design panel.png \
    --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-top-bottom/IMG_4821.png --layout top-bottom

# left-right: source-adaptive, exact vertical seam
scripts/compose_panel.py --plan --layout left-right --source photo.png
scripts/compose_panel.py --source photo.png --design panel.png \
    --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-left-right/IMG_4821-lr.png --layout left-right

# design-only: source-adaptive ratio and dimensions; no visible photo or seam
scripts/compose_panel.py --source photo.png --design panel.png \
    --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-design-only/IMG_4821-design.png \
    --layout design-only

# wallpaper-pack: four separately generated assets, finalized separately
scripts/compose_panel.py --design phone.png --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-wallpaper-pack/IMG_4821-wallpaper-phone.png --layout design-only --size 1440x3200
scripts/compose_panel.py --design ipad.png --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-wallpaper-pack/IMG_4821-wallpaper-ipad.png --layout design-only --size 2048x2732
scripts/compose_panel.py --design desktop.png --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-wallpaper-pack/IMG_4821-wallpaper-desktop.png --layout design-only --size 3840x2160
scripts/compose_panel.py --design watch.png --out ~/Desktop/xxd/xxd-panel-016/IMG_4821-wallpaper-pack/IMG_4821-wallpaper-watch.png --layout design-only --size 1024x1024
```

`--size WIDTHxHEIGHT` has priority over `--canvas` and `--width`. With neither `--size` nor `--canvas`, `--source` activates source-adaptive sizing and no stock ratio is imposed. Legacy `--top` and `--bottom` remain aliases for `--source` and `--design`.

**Photographic panel.** In `top-bottom`, it fills the upper half; in `left-right`, it fills the left half. Under source adaptation, paste it unchanged with no crop or resampling. Only for an explicit canvas override, crop gently or extend only the environment when necessary. `--anchor top|center|bottom|left|right` selects what a residual crop keeps. `design-only` has no photographic panel.

**Transformed design.** Generate it alone for the exact aspect reported by `--plan`, preferably at the exact frame size; otherwise use a closest supported same-aspect size and resample proportionally without cropping, with no photograph and no unused placeholder space. Append this resolved mode block:

```text
OUTPUT MODE: TOP_BOTTOM | LEFT_RIGHT | DESIGN_ONLY | WALLPAPER_PACK
DEVICE PROFILE: NONE | PHONE | IPAD | DESKTOP | WATCH
FINAL SIZE: <exact WIDTHxHEIGHT>
DESIGN FRAME: <exact WIDTHxHEIGHT>
SOURCE VISIBILITY: UPPER PANEL | LEFT PANEL | REFERENCE ONLY — NOT VISIBLE
LAYOUT RULE: Fill the design frame completely. Render no extra photographic panel, seam, frame, or reserved blank area inside the design image.
WALLPAPER RULE: For a device profile, keep system-UI zones low-information, keep essential content inside the safe region, render no fake clock/icons/dock/controls, and recompose for this aspect ratio rather than cropping another device's artwork.
WALLPAPER RELATIONSHIP: NONE | INDEPENDENT | LINKED
ANCHOR DEVICE: NONE | PHONE | IPAD | DESKTOP | WATCH
REFERENCE ROLE: SOURCE ONLY | SOURCE CONTENT + ANCHOR VISUAL DNA
```

For `linked`, the anchor receives `WALLPAPER RELATIONSHIP: LINKED`, its resolved device, and `REFERENCE ROLE: SOURCE ONLY`. Every derivative receives the same relationship and anchor device but `REFERENCE ROLE: SOURCE CONTENT + ANCHOR VISUAL DNA`. The original photo remains authoritative for subject, posture, relationship, and source colors; the anchor governs family resemblance only. Repeat the full aesthetic prompt and locked copy package for every derivative—do not rely on the anchor pixels to preserve correct wording. Recompose geometry and safe areas for the target device rather than copying coordinates from the anchor.

Then append the locked copy package:

```text
COPY MODE: REQUIRED
COPY ORIGIN: USER_EXACT | USER_DIRECTION | SOURCE_DERIVED
COPY LOCALE: <resolved locale, such as ar | ja-JP | ko-KR | en-GB | zh-CN>
COPY INTENT — INSTRUCTION ONLY, NEVER RENDER: <one concise semantic core and intended emotional turn>
MAIN TITLE: <locked exact string>
MICROTEXT 1: <locked exact string>
MICROTEXT 2: <locked exact string>
MICROTEXT 3: <optional locked exact string>
MICROTEXT 4: <optional locked exact string>
COPY RULE: Render only MAIN TITLE and populated MICROTEXT strings, each exactly once. COPY ORIGIN, COPY LOCALE, and COPY INTENT are instructions, never visible text. Do not rewrite, translate, spell-correct, duplicate, or add text. Respect the resolved locale's script shaping, punctuation, spacing, and semantic line-breaking rules.
```

Remove unused optional lines rather than rendering placeholders. When the resolved preflight choice is text-free, replace the entire block with `COPY MODE: NONE — render no text or pseudo-text anywhere.`

**Wallpaper safe regions.** Phone keeps the clock/notch area at the top and controls at the bottom quiet. iPad keeps essential content inside a centered square that survives portrait/landscape crop, with extendable atmosphere outside it. Desktop keeps the top menu area, bottom dock/taskbar, and both icon edges low-information. Watch keeps the main shape and a simplified but visible title hierarchy readable at thumbnail size while reserving the major clock/complication area; safe-area adaptation may enlarge or reposition type, never delete it. On the small watch canvas, the 016 anchor may expand to 24%–40% of frame width; all other 016 one-anchor, one-motion, void, palette, typography, and texture rules remain.

**Finalize.** Paired modes place the two assets into exact equal frames. Under source adaptation, both frames already equal the original source dimensions, so the source is pasted without cropping and the generated asset should use the same aspect and preferably that exact size; a same-aspect supported size may be proportionally resampled. `design-only` uses the source-derived frame without adding a source panel. The script reports any mismatch that would cause a crop so the asset can be regenerated at the planned aspect instead.

Needs Pillow. If the default interpreter lacks it, run `/opt/homebrew/bin/python3 scripts/compose_panel.py ...`.

Audit with the same mode used to build the artwork: `--audit poster.png --layout top-bottom`, `--audit poster.png --layout left-right`, or `--audit artwork.png --layout design-only --size 2048x2048`.

Only when no local scripting is available, fall back to one whole-canvas call. State the exact mode, dimensions, panel order, and seam coordinate. Verify paired-mode offsets with `--audit` and treat an offset above 0.25% as a failure.

## Output location

Save every generated poster under `~/Desktop/xxd/xxd-panel-016/`. Create the shared `~/Desktop/xxd/` wrapper, the skill root, and the task directory if they do not exist.

- Wrap each source-and-mode result in one task directory: `<source-stem>-top-bottom/`, `<source-stem>-left-right/`, `<source-stem>-design-only/`, or `<source-stem>-wallpaper-pack/`. A batch or multi-select creates one sibling task directory per source and selected mode; never mix different sources in one directory.
- Inside an ordinary-mode task directory, name the single final PNG after the source (`IMG_4821.png`), append `-lr` for `left-right`, or append `-design` for `design-only`.
- Inside a wallpaper-pack task directory, keep exactly four finished PNGs named with `-wallpaper-phone`, `-wallpaper-ipad`, `-wallpaper-desktop`, and `-wallpaper-watch`. Do not create four device subdirectories and do not mix another source's files into the pack.
- When the source has no usable name, use the short title slug as `<source-stem>`.
- Never overwrite an existing task directory. On collision append `-2`, `-3`, and so on to the task-directory name; keep filenames inside unchanged.
- Keep temporary generations, plans, audits, and source copies out of the finished task directory. It contains final deliverable PNGs only.
- An explicit user file path overrides this default exactly. When the user supplies only a destination directory, create the same per-source-and-mode task directories inside it unless the user explicitly requests a flat directory.

## Acceptance gate

Before accepting each result, verify all of the following:

- The output mode and dimensions match the resolved explicit selection or source-adaptive formula. `--size` is reproduced pixel-for-pixel. In source-adaptive modes, the source is never cropped and the generated asset either matches the planned frame natively or is proportionally resampled from the same aspect with no crop.
- `top-bottom` has a clean horizontal seam at exactly half height; `left-right` has a clean vertical seam at exactly half width; `design-only` and all wallpaper files contain no seam or visible source photo.
- In paired modes, the photographic panel remains recognizably the original source, appears in the correct upper/left position, and contains no deformation or typography.
- The design anchor is unmistakably the same subject, keeps only its essential contour and posture, occupies roughly 12%–26% of the design-frame width, and does not compete with a second focal subject. The watch wallpaper exception is 24%–40% so it remains readable on a very small display.
- Automatic or direction-led copy expresses a visible fact plus a grounded relational or latent meaning, passes the unrelated-photo swap test, and earns its emotional turn without a forced pun or invented backstory. Its language matches the resolved target locale rather than the command language or presumed identity: Arabic reads as native Arabic with connected shaping and RTL composition, Japanese as native Japanese, Korean as native Korean, and UK English uses British conventions. Exact user copy remains verbatim and its hierarchy, script shaping, punctuation, line breaks, and placement preserve the intended emphasis; editable user direction is transcreated only within the permission given.
- Exactly one source-derived motion logic organizes the field. Lines, broken trajectories, halftone, and grain become denser near the core and dissolve toward the edges.
- Roughly 60%–78% of the transformed design frame remains clean void; the anchor has not been enlarged merely to fill space. In every source-hidden mode, calculate this against the full canvas.
- The transformed construction reads as hand-printed Riso/silkscreen through paper fiber, uneven ink, halftone, and slight misregistration—not gradients, glow, CG volume, or vector polish.
- The palette contains only the source-derived dominant color, warm paper, and optional small black.
- In automatic or direction-led copy mode, the transformed design contains the locked main title and all 2–4 locked microtext strings. In custom-copy mode, it contains the exact title plus every populated or derived microtext string, or the exact title alone when title-only was explicitly requested. All rendered wording is accurate, with no substitution, misspelling, gibberish, extra wording, or invented year; the main title is visually unmistakable and at least three times the microtext scale. In text-free mode, no letters, numbers, captions, or pseudo-text appear anywhere.
- The artwork was reopened and visually inspected. Its anchor, motion, palette, and copy are specific enough that swapping in an unrelated source photo would visibly break the result; generic decorative abstraction is a failure.
- Each wallpaper has its requested exact dimensions, its own aspect-specific composition, usable safe regions, no baked-in system UI, and no evidence of being mechanically cropped from another device output.
- In `independent`, all four wallpapers derive directly from the original source and may explore freer compositions without borrowing a generated wallpaper. In `linked`, the anchor passed its gate before fan-out, the other three all reference the original source plus that same anchor, and the four preserve one recognizable family of palette, print texture, motion grammar, typography, and copy without becoming resized duplicates.
- The final count per source equals one file for each selected ordinary mode plus four files when `wallpaper-pack` is selected. `all` / `全部` therefore means seven finished PNGs across four sibling task directories, with no content borrowed from other inputs.
- Every delivered file was newly generated or composed for this invocation and lives in the fresh task directory reserved for it; no historical output was returned as the current result.

## Override policy

Preserve user-specified subject wording, output count, target locale, language, motion direction, main color, and copy. Copy priority is explicit text-free request > exact supplied wording > supplied creative direction > automatic source-derived 016 copy. Target-locale priority is explicit audience/market > explicit output language > direction language; if none is explicit, ask before generation. Treat exact wording as immutable unless the user asks for rewriting or localization. A shared creative direction may govern a batch, but each photo still receives its own source-aware copy unless the user explicitly requests identical wording.

A user-forced mode set and per-mode exact pixel sizes are always honored. Exact size overrides ratio; ratio overrides source-adaptive sizing. Canvas orientation never changes any selected mode: `top-bottom` always stacks vertically, `left-right` always places source left and design right, and source-hidden modes never reintroduce the photograph. In `wallpaper-pack`, a labeled device size overrides only that device. If a paired frame fights the source orientation, protect the subject with seamless environmental extension rather than stretching it.

Do not relax the one-photo-per-selected-ordinary-mode rule, exact four-output rule in `wallpaper-pack`, exact equal split in paired modes, absence of the photo in source-hidden modes, faithful visible photography, one-anchor/one-motion design logic, or printmaking texture unless the user explicitly asks to leave the 016 style.

## Provenance boundary

The original one-paragraph style brief is archived at [references/016-source.md](references/016-source.md). Use [assets/examples](assets/examples) only as visual input examples; do not reuse their subject matter, colors, or composition unless the user supplies that exact image. The operative visual specification is the local 016 reference prompt.
