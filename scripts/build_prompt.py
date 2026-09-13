#!/usr/bin/env python3
"""xxd-skill（小小东）· 生成可直接复制的出图提示词

用法：
  python build_prompt.py --no 165
  python build_prompt.py --school 中央撕纸揭景风
  python build_prompt.py --keyword 纸雕 --pick 1
  python build_prompt.py --no 165 --text "SHANGHAI" --subject "傍晚的外滩天际线"

输出：一段完整、可整段复制的提示词（原文逐字保留），外加使用说明。
数据取自 styles.json 的 `prompt` —— 有附件时是作者附件 docx/pdf 里的完整原文，
没有附件时是笔记正文。
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "styles.json"

USAGE = """\
**怎么用**
1. 把原照片放进画布上半部分（或直接把照片 + 提示词一起给模型），画布比例 3:4（1080×1440）。
2. 整段复制下面提示词，不要拆散、不要精简——留白比例、材质词、禁忌词都是效果的一部分。
3. 成图应为「上：原照片 / 下：风格化重构」的对照版式；若不是对照构图，可把开头一句改成「整张画面按以下语言重构」。
4. 提示词里说「从上方照片中提取 2–4 种颜色」时，如果模型看不到原图，请把这 2–4 种颜色写进去替换。"""


def load():
    if not DATA.exists():
        sys.exit(f"缺少数据文件：{DATA}")
    return json.loads(DATA.read_text(encoding="utf-8"))


TAG_NOISE = re.compile(r"\s*#\S+\[话题\]#|\s*@\S+")


def strip_noise(text: str) -> str:
    """去掉原帖末尾的话题标签与 @提及——那是发布用的，投喂模型只会干扰。"""
    t = TAG_NOISE.sub("", text or "")
    return re.sub(r"[ \t]+\n", "\n", t).strip()


def haystack(r) -> str:
    return ((r.get("prompt") or "") + "\n" + (r.get("desc") or "") + "\n" +
            (r.get("school") or "") + (r.get("title") or "") + "、" + "、".join(r.get("tags") or []))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no", type=int, dest="no")
    ap.add_argument("--school")
    ap.add_argument("--keyword")
    ap.add_argument("--pick", type=int, default=1, help="关键词命中多条时取第几条（默认 1）")
    ap.add_argument("--subject", default="", help="替换主体提示（可选，会追加在末尾）")
    ap.add_argument("--text", default="", help="指定画面文字（可选）")
    ap.add_argument("--ratio", default="3:4（1080×1440）")
    ap.add_argument("--raw", action="store_true", help="只输出提示词原文，不带说明")
    args = ap.parse_args()

    rows = load()
    rows.sort(key=lambda r: -(r.get("no") or 0))
    hit = rows
    if args.no:
        hit = [r for r in rows if r.get("no") == args.no]
    elif args.school:
        hit = [r for r in rows if args.school in (r.get("school") or "")]
    elif args.keyword:
        hit = [r for r in rows if args.keyword in haystack(r)]
    else:
        sys.exit("请给 --no / --school / --keyword 之一")

    if not hit:
        sys.exit("没有匹配的风格，试试 --list")
    r = hit[min(args.pick, len(hit)) - 1]

    body = strip_noise(r.get("prompt") or r.get("desc") or "")
    extra = []
    if args.text:
        extra.append(f"本次画面文字请使用：{args.text}。除此之外不额外添加任何文字。")
    if args.subject:
        extra.append(f"本次主体要点：{args.subject}。仍须遵守上面的删减、重组、留白与配色规则。")
    if extra:
        body = body + "\n\n" + "\n".join(extra)

    if args.raw:
        print(body)
        return 0

    m = re.search(r"重构为\s*\*\*(.+?)\*\*", body) or re.search(r"重构为\s*\*{0,2}([^。\n*]{4,64})", body)
    core = (m.group(1).strip().rstrip("*／/ ") if m else "")
    src = "附件原文" if r.get("prompt_source") == "attachment" else "笔记正文"
    no = f"P{r['no']}" if r.get("no") else "无编号"
    print(f"# {r.get('school') or r.get('title')}（{no}）")
    print(f"- 提示词来源：{src}（{len(body)} 字）")
    if r.get("attachment"):
        a = r["attachment"]
        print(f"- 作者附件：{a.get('doc_title')}（{a.get('doc_type')}，{a.get('page_count')} 页）")
    print(f"- 核心语言：{core or '—'}")
    print(f"- 原帖对照图：{r.get('url')}")
    print(f"- 画布：{args.ratio}")
    print()
    print(USAGE)
    print()
    print("---")
    print()
    print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
