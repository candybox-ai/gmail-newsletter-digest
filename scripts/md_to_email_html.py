#!/usr/bin/env python3
"""Convert newsletter markdown to email-safe HTML (inline styles for Gmail).

Locked email typography (Inter-like stack, purple links):
  title ~32px bold, section ~20px bold, body ~16px, compact list indent, purple links.

Usage:
  python scripts/md_to_email_html.py draft.md > draft.html
  python scripts/md_to_email_html.py draft.md --out draft.html
"""
from __future__ import annotations
import argparse, html, re, sys
from pathlib import Path

# Inter-like stack + CJK fallbacks. No nested quotes inside style="...".
FONT = (
    "Inter,Helvetica Neue,Helvetica,Arial,PingFang SC,"
    "Hiragino Sans GB,Microsoft YaHei,Noto Sans SC,sans-serif"
)
BODY_COLOR = "#333333"
HEAD_COLOR = "#111111"
LINK = "#7c3aed"  # purple accent like reference mentions/links

BASE = f"font-family:{FONT};font-size:16px;line-height:1.6;color:{BODY_COLOR};"
H1 = (
    f"font-family:{FONT};font-size:32px;line-height:1.25;font-weight:800;"
    f"color:{HEAD_COLOR};margin:0 0 20px 0;letter-spacing:-0.02em;"
)
H2 = (
    f"font-family:{FONT};font-size:20px;line-height:1.35;font-weight:700;"
    f"color:{HEAD_COLOR};margin:28px 0 12px 0;"
)
H3 = (
    f"font-family:{FONT};font-size:18px;line-height:1.35;font-weight:700;"
    f"color:{HEAD_COLOR};margin:20px 0 10px 0;"
)
P = f"{BASE}margin:0 0 14px 0;"
# Compact indent: bullet close to margin, hanging text edge
UL = (
    "margin:6px 0 16px 0;padding-left:1.1em;"
    "list-style-type:disc;list-style-position:outside;"
)
LI = f"{BASE}margin:0 0 12px 0;padding:0;"
A = f"color:{LINK};text-decoration:underline;"
CODE = (
    "font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;"
    "font-size:0.92em;background:#f4f4f5;padding:1px 4px;border-radius:3px;"
)


def inline_md(s: str) -> str:
    # Protect links while formatting text so emphasis markers never touch hrefs.
    links: list[str] = []
    def link_repl(m: re.Match[str]) -> str:
        label, url = m.group(1), m.group(2)
        links.append(f'<a href="{html.escape(url, quote=True)}" style="{A}">{html.escape(label)}</a>')
        return f"\x00{len(links) - 1}\x00"
    raw = s
    pattern = re.compile(r"\[([^\]]+)\]\((https?://(?:[^()\s]|\([^()]*\))+)\)")
    s = pattern.sub(link_repl, raw)
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", rf'<code style="{CODE}">\1</code>', s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: links[int(m.group(1))], s)
    return s


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    in_ul = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def open_ul():
        nonlocal in_ul
        if not in_ul:
            out.append(f'<ul style="{UL}">')
            in_ul = True

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_ul()
            continue
        if line.startswith("# "):
            close_ul()
            out.append(f'<h1 style="{H1}">{inline_md(line[2:].strip())}</h1>')
        elif line.startswith("## "):
            close_ul()
            out.append(f'<h2 style="{H2}">{inline_md(line[3:].strip())}</h2>')
        elif line.startswith("### "):
            close_ul()
            out.append(f'<h3 style="{H3}">{inline_md(line[4:].strip())}</h3>')
        elif re.match(r"^\d+\.\s+", line):
            open_ul()
            item = re.sub(r"^\d+\.\s+", "", line)
            out.append(f'<li style="{LI}">{inline_md(item)}</li>')
        elif line.startswith("- ") or line.startswith("* "):
            open_ul()
            out.append(f'<li style="{LI}">{inline_md(line[2:].strip())}</li>')
        else:
            close_ul()
            out.append(f'<p style="{P}">{inline_md(line)}</p>')
    close_ul()

    body = "\n".join(out)
    return (
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "</head>"
        f'<body style="{BASE}max-width:640px;margin:0 auto;padding:24px 16px;">\n'
        f"{body}\n</body></html>\n"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--out")
    args = ap.parse_args()
    html_doc = md_to_html(Path(args.path).read_text(encoding="utf-8"))
    if args.out:
        Path(args.out).write_text(html_doc, encoding="utf-8")
    else:
        sys.stdout.write(html_doc)


if __name__ == "__main__":
    main()
