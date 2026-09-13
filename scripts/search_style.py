#!/usr/bin/env python3
"""xxd-skill（小小东）· 风格库检索

用法：
  python search_style.py 纸雕              # 关键词检索（风格名/提示词全文/标签）
  python search_style.py --no 165          # 按系列号定位
  python search_style.py --list            # 列出全部风格（编号 + 风格名 + 核心语言）
  python search_style.py --top 20          # 按收藏数排序取前 N
  python search_style.py --tag 纸艺         # 按归纳类别筛（见 prompt-anatomy.md 的分类）
  python search_style.py --attachments     # 只看「提示词来自附件」的那 20 条
  python search_style.py --no 165 --full   # 打印完整提示词

提示词来源：`prompt_source` 为 `attachment` 时，用的是作者放在笔记附件（docx/pdf）里的
完整版原文；为 `caption` 时，用的是笔记正文。附件版普遍更全（平均 1129 字 vs 719 字）。
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "styles.json"

CATS = {
    "纸艺": ["纸雕", "剪纸", "拼贴", "纸纹", "纸纤维", "纸艺", "撕纸", "手撕", "纸片",
             "cutout", "cut-paper", "paper-cut", "papercut", "collage"],
    "浮雕": ["浮雕", "厚度", "油墨", "emboss", "relief", "压印", "拓片", "墨拓", "层叠"],
    "线描": ["线描", "线稿", "钢笔", "墨线", "草图", "速写", "版画", "蚀刻", "刻线", "线条"],
    "淡彩": ["淡彩", "水彩", "wash", "watercolor", "晕染"],
    "水墨": ["水墨", "淡墨", "山水", "新中式", "国画", "东方极简"],
    "像素栅格": ["像素", "pixel", "栅格", "bitmap", "点阵", "网点", "dithering", "字符", "halftone", "risograph"],
    "极简构成": ["留白", "纯色", "章印", "色场", "负空间", "极小主体", "小尺度"],
    "绘本插画": ["绘本", "童趣", "涂鸦", "手帐", "稚拙", "蜡笔", "油画棒", "彩铅"],
    "透视场景": ["透视", "等距", "isometric", "微缩", "diorama", "室内设计"],
    "实验海报": ["海报", "排版", "typography", "字体", "标题", "monospace", "实验"],
}


def load():
    if not DATA.exists():
        sys.exit(f"缺少数据文件：{DATA}")
    return json.loads(DATA.read_text(encoding="utf-8"))


def full_text(r) -> str:
    """该条最权威的提示词版本。"""
    return (r.get("prompt") or r.get("desc") or "")


def haystack(r) -> str:
    return full_text(r) + "\n" + (r.get("desc") or "") + "\n" + (r.get("school") or "") + \
        (r.get("title") or "") + "、" + "、".join(r.get("tags") or [])


def cats_of(r) -> list:
    d = haystack(r).lower()
    return [c for c, kws in CATS.items() if any(k.lower() in d for k in kws)]


BOLD_CORE = re.compile(r"重构为\s*\*\*(.+?)\*\*")
PLAIN_CORE = re.compile(r"重构为\s*\*{0,2}([^。\n*]{4,64})")
BOLD_ANY = re.compile(r"\*\*(.+?)\*\*")
# 这些词是骨架里的通用成分，不是风格名，命中就跳过
CORE_BAD = ("下半部分", "上半部分", "主体", "轮廓", "结构", "姿态", "叙事关系",
            "留白", "构图", "配色", "文字", "提示词", "照片", "不要", "禁止",
            "如果都留白", "避免", "禁止出现")
# 句子以这些词起头，是五段式骨架的说明句，不是风格语言
SKELETON_HEAD = ("画面", "构图", "整体", "下半部分", "上半部分", "主体", "色彩",
                 "配色", "文字", "材质", "线条", "留白", "这张", "请将", "避免")


def brief(r):
    """摘出「重构为 **X**」的核心风格语言；没有就退到任一加粗短语，再不行回风格名。"""
    for src in (r.get("prompt") or "", r.get("desc") or ""):
        m = BOLD_CORE.search(src)
        if m:
            return m.group(1).strip()
        m = PLAIN_CORE.search(src)
        if m:
            return m.group(1).strip().rstrip("*／/ ")
    for src in (r.get("prompt") or "", r.get("desc") or ""):
        for bm in BOLD_ANY.finditer(src):
            c = bm.group(1).strip()
            if 3 <= len(c) <= 40 and not any(b in c for b in CORE_BAD):
                return c
    first = re.split(r"[。\n]", full_text(r).strip())[0].strip().strip("* \t")
    if 8 <= len(first) <= 80 and not first.startswith(SKELETON_HEAD):
        return first
    return r.get("school") or first[:80]


def label(r) -> str:
    """P### 是标题里的系列号；№### 是作者在正文里自报的解锁序号（区间与 P 号重叠，只作溯源）。"""
    if r.get("no"):
        return f"P{r['no']}"
    if r.get("unlock_no"):
        return f"№{r['unlock_no']}"
    return "—"


def src_tag(r) -> str:
    return "附件" if r.get("prompt_source") == "attachment" else "正文"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("keyword", nargs="*", help="关键词")
    ap.add_argument("--no", type=int, help="系列号")
    ap.add_argument("--tag", help="归纳类别（纸艺/浮雕/线描/淡彩/水墨/像素栅格/极简构成/绘本插画/透视场景/实验海报）")
    ap.add_argument("--top", type=int, help="按收藏数取前 N")
    ap.add_argument("--attachments", action="store_true", help="只看有附件的条目")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--full", action="store_true", help="打印完整提示词")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = load()
    rows.sort(key=lambda r: -(r.get("no") or 0))

    if args.top:
        def num(v):
            try:
                return int(str(v).replace("万", "0000") or 0)
            except Exception:
                return 0
        rows = sorted(rows, key=lambda r: -num((r.get("interact") or {}).get("collected")))[: args.top]
    if args.attachments:
        rows = [r for r in rows if r.get("prompt_source") == "attachment"]
    if args.tag:
        rows = [r for r in rows if args.tag in cats_of(r)]
    if args.no:
        rows = [r for r in rows if r.get("no") == args.no]
    if args.keyword:
        kws = args.keyword
        rows = [r for r in rows if any(k in haystack(r) for k in kws)]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0

    print(f"命中 {len(rows)} 条\n")
    for r in rows:
        print(f"{label(r):>5s}  {r.get('school') or r.get('title')}")
        print(f"    核心：{brief(r)}")
        print(f"    类别：{'、'.join(cats_of(r)) or '—'}   收藏：{(r.get('interact') or {}).get('collected') or '—'}"
              f"   提示词：{src_tag(r)}版 {len(full_text(r))} 字")
        print(f"    出处：{r.get('url')}")
        if args.full:
            print("\n    ── 提示词全文 ──")
            print("    " + full_text(r).replace("\n", "\n    "))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
