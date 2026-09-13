#!/usr/bin/env python3
"""xxd-skill（小小东）· 查作者随笔记发布的附件（docx / pdf）

背景：@小小东 的部分笔记正文只有一句引子，完整提示词放在**笔记附件**里
（小红书「文件」组件，正文里常写「提示词附件中 / 见附件吧」）。全库 139 条里
有 21 条带附件，其中 20 条的正文已提取成文本并写进 `data/styles.json` 的 `prompt`。

用法：
  python find_attachment.py --list          # 列出全部附件
  python find_attachment.py --no 34         # 按系列号查
  python find_attachment.py --keyword 金箔    # 关键词查
  python find_attachment.py --no 34 --text   # 顺便打印该附件的完整提示词正文
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "styles.json"
ATT_ROOT = Path(r"C:\Users\snowf\WorkBuddy\2026-09-13-09-42-47\xiaoxiaodong\media\xiaoxiaodong\attachments")


def load():
    if not DATA.exists():
        sys.exit(f"缺少数据文件：{DATA}")
    return json.loads(DATA.read_text(encoding="utf-8"))


def rows_with_att(rows):
    return [r for r in rows if r.get("attachment")]


def show(r, with_text=False):
    a = r["attachment"]
    no = f"P{r['no']}" if r.get("no") else "无编号"
    print(f"{no:>6s}  {r.get('school') or r.get('title')}")
    print(f"        附件：{a.get('doc_title')}  [{a.get('doc_type')} · {a.get('page_count')} 页 · "
          f"{a.get('view_num') or '-'} 浏览 / {a.get('download_num') or '-'} 下载]")
    print(f"        doc_id：{a.get('doc_id')}   发布：{a.get('publish_time')}")
    print(f"        本地文件：{ATT_ROOT / (a.get('local') or '')}")
    print(f"        提取文本：{a.get('text_status')}   {a.get('text_len') or 0} 字"
          + ("" if a.get("text_status") == "ok" else f"   ← {a.get('text_note') or ''}"))
    print(f"        原帖：{r.get('url')}")
    if with_text and a.get("text_status") == "ok":
        print("        ── 提示词全文 ──")
        print("        " + (r.get("prompt") or "").replace("\n", "\n        "))
    print()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--no", type=int)
    ap.add_argument("--keyword")
    ap.add_argument("--text", action="store_true", help="打印完整提示词")
    args = ap.parse_args()

    rows = load()
    rows.sort(key=lambda r: -(r.get("no") or 0))
    hit = rows_with_att(rows)
    if args.no:
        hit = [r for r in hit if r.get("no") == args.no]
    if args.keyword:
        hit = [r for r in hit if args.keyword in ((r.get("school") or "") + (r.get("prompt") or ""))]
    if not (args.list or args.no or args.keyword):
        args.list = True

    print(f"带附件的笔记共 {len(rows_with_att(rows))} 条，当前命中 {len(hit)} 条\n")
    for r in hit:
        show(r, with_text=args.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
