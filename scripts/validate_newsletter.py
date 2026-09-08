#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
from link_safety import is_sensitive

EN = {
    "brief": "Today's Brief",
    "deep": "Deep Dives",
    "updates": "Important Updates",
    "more": "More to Read",
    "insight": "Insight",
    "sources": "Sources",
    "tools": "Engineering & Tools",
    "tool_picks": "Tool picks",
    "more_a": "Don't miss",
    "more_b": "Worth a look",
}
ZH = {
    "brief": "今日速览",
    "deep": "重点解读",
    "updates": "重要简讯",
    "more": "更多阅读",
    "insight": "洞察",
    "sources": "来源",
    "tools": "工程与工具",
    "tool_picks": "工具精选",
    "more_a": "非读不可",
    "more_b": "推荐读",
}
FORBIDDEN = [
    r"^Subject\b",
    r"来源列表",
    r"编辑备注",
    r"覆盖窗口",
    r"本报截至今",
    r"下面只列前面",
    r"小工具扫描",
    r"^Sources list\b",
    r"^Editor'?s? notes?\b",
    r"coverage window",
]
OPAQUE = [
    "约束迁移",
    "品类宣言",
    "过夜工程侧",
    "文内数字",
    "透明了一层又糊了一层",
]


def detect_pack(text: str) -> dict[str, str] | None:
    en_hit = sum(1 for k in ("brief", "deep", "more") if f"## {EN[k]}" in text)
    zh_hit = sum(1 for k in ("brief", "deep", "more") if f"## {ZH[k]}" in text)
    if en_hit >= zh_hit and en_hit > 0:
        return EN
    if zh_hit > 0:
        return ZH
    return None


def section_body(text: str, heading: str) -> str | None:
    m = re.search(rf"^## {re.escape(heading)}[ \t]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else None


def h3_headings(block: str) -> list[str]:
    return re.findall(r"^### (.+?)\s*$", block, re.M)


def urls(block: str) -> set[str]:
    return set(re.findall(r"https?://[^\s\)\]\>]+", block or ""))


def has_source(text: str, pack: dict[str, str]) -> bool:
    if re.search(r"https?://[^\s)]+", text):
        return True
    marker = "Restricted source" if pack is EN else "受限来源"
    unknown = "date unknown" if pack is EN else "日期未知"
    return bool(re.search(
        rf"[^\n·]+\S[ \t]*·[ \t]*(?:\d{{4}}-\d{{2}}-\d{{2}}|{unknown})"
        rf"[ \t]*·[ \t]*\[{marker}\]", text
    ))


def check(text: str) -> list[str]:
    text = text.replace("\r\n", "\n")
    errs: list[str] = []
    title = re.search(r"^# (\d{4}-\d{2}-\d{2}) · (Morning|Evening) Newsletter\s*$", text, re.M)
    if not title:
        errs.append("title must be `# YYYY-MM-DD · Morning|Evening Newsletter`")
    else:
        from datetime import date
        try:
            date.fromisoformat(title.group(1))
        except ValueError:
            errs.append("title date must be a real calendar date")
    pack = detect_pack(text)
    if pack is None:
        errs.append(
            "missing required sections (need English Today's Brief/Deep Dives/More to Read "
            "or Chinese 今日速览/重点解读/更多阅读)"
        )
        return errs
    headings = re.findall(r"^## (.+?)\s*$", text, re.M)
    required = ("brief", "deep", "updates", "more")
    for key in required:
        if headings.count(pack[key]) != 1:
            errs.append(f"need exactly one ## {pack[key]}")
    if all(pack[key] in headings for key in required):
        order = ("brief", "deep", "updates", "tools", "more") if pack["tools"] in headings else required
        positions = [headings.index(pack[key]) for key in order]
        if positions != sorted(positions):
            errs.append("sections must be ordered Brief, Deep Dives, Important Updates, Tools, More to Read")
    other = ZH if pack is EN else EN
    for key in ("brief", "deep", "updates", "tools", "more"):
        if f"## {other[key]}" in text:
            errs.append(
                f"mixed language headings: found both ## {pack[key]} pack and ## {other[key]}"
            )
            break
    for pat in FORBIDDEN:
        if re.search(pat, text, re.M | re.I):
            errs.append(f"forbidden meta/opaque pattern: {pat}")
    for w in OPAQUE:
        if w in text:
            errs.append(f"opaque jargon: {w}")

    brief = section_body(text, pack["brief"])
    if not brief or not re.search(r"(?m)^\s*[-*]\s+\S", brief):
        errs.append(f"{pack['brief']} must contain at least one bullet")

    for url in re.findall(r"https://mail\.google\.com/mail/u/\d+/#[^\s)]+", text):
        if "#inbox/" not in url:
            errs.append(f"gmail link must use #inbox/: {url[:80]}")
        if "rfc822msgid" in url:
            errs.append(f"avoid rfc822msgid gmail links: {url[:80]}")
    for url in re.findall(r"https?://[^\s)\]>]+", text):
        if is_sensitive(url):
            errs.append(f"sensitive URL must not be cited: {url[:100]}")

    deep_block = section_body(text, pack["deep"]) or ""
    parts = [
        p
        for p in re.split(r"(?=^### )", deep_block, flags=re.M)
        if p.strip().startswith("###")
    ]
    if len(parts) > 3:
        errs.append(f"{pack['deep']} has {len(parts)} items; usually ≤3")
    for i, p in enumerate(parts, 1):
        # Labeled field required — bare "Insightful" / "洞察力" must not count.
        if pack["insight"] == "Insight":
            ok_i = bool(re.search(r"(?m)^\*\*Insight:\*\*\s*\S", p))
        else:
            ok_i = bool(re.search(r"(?m)^\*\*洞察[：:]\*\*\s*\S", p))
        if not ok_i:
            errs.append(f"{pack['deep']} #{i} missing **{pack['insight']}:** label")
        if pack["sources"] == "Sources":
            ok_s = bool(re.search(r"(?m)^\*\*Sources:\*\*\s*\S", p))
        else:
            ok_s = bool(re.search(r"(?m)^\*\*来源[：:]\*\*\s*\S", p))
        if not ok_s:
            errs.append(f"{pack['deep']} #{i} missing **{pack['sources']}:** label")
        else:
            source = re.search(r"(?m)^\*\*(?:Sources:|来源[：:])\*\*[ \t]*(.*)$", p)
            if not source or not has_source(source.group(1), pack):
                errs.append(f"{pack['deep']} #{i} needs a URL or named/dated restricted source")

    updates = section_body(text, pack["updates"]) or ""
    for i, item in enumerate(re.split(r"(?m)^[-*] ", updates)[1:], 1):
        if not has_source(item, pack):
            errs.append(f"{pack['updates']} #{i} needs a URL or named/dated restricted source")
    if updates.strip() and not re.search(r"(?m)^[-*] \S", updates):
        errs.append(f"{pack['updates']} must use bullets")

    # More to Read: required subsection names for the language pack
    more_block = section_body(text, pack["more"]) or ""
    h3s = h3_headings(more_block)
    allowed_more = {pack["more_a"], pack["more_b"]}
    if more_block.strip():
        if re.search(r"(?m)^\s*[-*]\s+", more_block) and not h3s:
            errs.append(f"{pack['more']} bullets require a canonical subsection")
        else:
            for h in h3s:
                # strip optional bold/trailing
                name = re.sub(r"\*+", "", h).strip()
                if name not in allowed_more:
                    errs.append(
                        f"{pack['more']} subsection must be "
                        f"`### {pack['more_a']}` or `### {pack['more_b']}`; found `### {h}`"
                    )

    # Tools subsection name if Engineering section present
    if f"## {pack['tools']}" in text:
        tools_block = section_body(text, pack["tools"]) or ""
        th = h3_headings(tools_block)
        if th and pack["tool_picks"] not in th:
            errs.append(
                f"{pack['tools']} should use `### {pack['tool_picks']}`; found {th}"
            )
        # wrong-language tool picks
        if other["tool_picks"] in th:
            errs.append(f"mixed tools subsection: {other['tool_picks']}")

    # Different facts can share a URL. Semantic deduplication is an agent review.

    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    args = ap.parse_args()
    errs = check(Path(args.path).read_text(encoding="utf-8"))
    if errs:
        print("FAIL")
        for e in errs:
            print("-", e)
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
