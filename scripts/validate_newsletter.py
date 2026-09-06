#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from pathlib import Path

EN = {
    "brief": "Today's Brief",
    "deep": "Deep Dives",
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
    m = re.search(rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else None


def h3_headings(block: str) -> list[str]:
    return re.findall(r"^### (.+?)\s*$", block, re.M)


def urls(block: str) -> set[str]:
    return set(re.findall(r"https?://[^\s\)\]\>]+", block or ""))


def check(text: str) -> list[str]:
    errs: list[str] = []
    if not re.search(
        r"^# \d{4}-\d{2}-\d{2} · (Morning|Evening) Newsletter\s*$", text, re.M
    ):
        errs.append("title must be `# YYYY-MM-DD · Morning|Evening Newsletter`")
    pack = detect_pack(text)
    if pack is None:
        errs.append(
            "missing required sections (need English Today's Brief/Deep Dives/More to Read "
            "or Chinese 今日速览/重点解读/更多阅读)"
        )
        return errs
    for key in ("brief", "deep", "more"):
        if f"## {pack[key]}" not in text:
            errs.append(f"missing ## {pack[key]}")
    other = ZH if pack is EN else EN
    for key in ("brief", "deep", "more"):
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
    if brief and re.search(r"\[.*?\]\(https?://", brief):
        errs.append(f"{pack['brief']} must not contain source links")

    for url in re.findall(r"https://mail\.google\.com/mail/u/\d+/#[^\s)]+", text):
        if "#inbox/" not in url:
            errs.append(f"gmail link must use #inbox/: {url[:80]}")
        if "rfc822msgid" in url:
            errs.append(f"avoid rfc822msgid gmail links: {url[:80]}")

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

    # More to Read: required subsection names for the language pack
    more_block = section_body(text, pack["more"]) or ""
    h3s = h3_headings(more_block)
    allowed_more = {pack["more_a"], pack["more_b"]}
    if more_block.strip():
        if not h3s:
            # empty More with no subsections is OK (both tiers empty)
            pass
        else:
            for h in h3s:
                # strip optional bold/trailing
                name = re.sub(r"\*+", "", h).strip()
                if name not in allowed_more:
                    errs.append(
                        f"{pack['more']} subsection must be "
                        f"`### {pack['more_a']}` or `### {pack['more_b']}`; found `### {h}`"
                    )
            # if any content bullets exist under wrong-only headings already flagged;
            # require both canonical headings when any h3 present? Prefer: if any h3, only allowed names (done). Optional both present when links exist.
            if re.search(r"^\s*[-*]\s+", more_block, re.M):
                for need in (pack["more_a"], pack["more_b"]):
                    if need not in h3s and f"### {need}" not in more_block:
                        # only require the tier that has bullets — softer: require at least one allowed
                        pass

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

    # More must not re-list URLs already cited in Deep Dives
    deep_urls = urls(deep_block)
    more_urls = urls(more_block)
    overlap = sorted(deep_urls & more_urls)
    for u in overlap:
        errs.append(
            f"{pack['more']} must not re-list a URL already in {pack['deep']}: {u[:100]}"
        )

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
