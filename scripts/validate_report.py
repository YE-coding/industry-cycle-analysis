#!/usr/bin/env python3
"""Validate an industry-cycle Markdown report for structural, evidence-integrity, and readability gates."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


FULL_SECTIONS = [
    "## 0. 一页看懂",
    "## 1. 产业链地图",
    "## 2. 需求",
    "## 3. 供给",
    "## 4. 供需矛盾与高频信号",
    "## 5. 周期位置与传导",
    "## 6. 资金动向",
    "## 7. 未来资金可能流向",
    "## 8. 分歧与反证",
    "## 9. 观察哨与跟踪",
    "## 10. 术语表",
    "## 附录A 证据台账",
    "## 附录B 数据时效与证据覆盖",
    "## 附录C 证据就绪度与研究执行记录",
]

REQUIRED_HEADERS = ["分析日期", "地理范围", "数据时效", "行业边界"]
READINESS_LANES = [
    "产业链",
    "需求",
    "供给与有效产能",
    "价格/订单/库存/利润",
    "资本市场预期",
]

PLACEHOLDERS = {
    "generic source": r"官方/协会/公司|公司披露或行业数据|官方或交易所高频数据优先",
    "unverified metric": r"待按产品核验|视公开口径|见数据时效表",
    "generic market statement": r"市场可能交易",
    "generic watchpoint": r"连续2期改善且与价格/利润同向|连续2期恶化或与库存背离",
    "generic transition window": r"未来2[-至]6(?:个)?季度",
    "boilerplate chain note": r"钱和订单从\s*\S+\s*的需求向前传",
    "circular node definition": r"负责把上游投入转成\S*可采购",
    "generic demand slot": r"核心产品需求|新增场景",
    "undated period": r"最新已披露期",
    "generic budget-entry description": r"把真实使用需求变成预算和采购[，,]是整条链最终能否回款的入口",
}

# Interpretation-style cells that carry zero information when they are the whole cell.
EMPTY_INTERPRETATION_CELLS = {"直接观测", "交叉验证"}

# Sentences at least this long that repeat REPEAT_LIMIT+ times indicate template filling.
REPEAT_MIN_LEN = 18
REPEAT_LIMIT = 3


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    rest = text[start + len(heading) :]
    match = re.search(r"\n##\s+", rest)
    return rest if match is None else rest[: match.start()]


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells if cell):
            continue
        rows.append(cells)
    return rows


def validate(text: str, mode: str, strict: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for header in REQUIRED_HEADERS:
        if not re.search(rf"^{re.escape(header)}[：:]\s*\S+", text, re.MULTILINE):
            errors.append(f"missing required header: {header}")

    timestamp = re.search(r"^分析日期[：:]\s*(.+)$", text, re.MULTILINE)
    if timestamp and not re.search(r"\d{4}-\d{2}-\d{2}.*(?:[+-]\d{2}:?\d{2}|(?:UTC|GMT))", timestamp.group(1)):
        errors.append("analysis timestamp must include a date and timezone")

    if mode == "full":
        for heading in FULL_SECTIONS:
            if heading not in text:
                errors.append(f"missing full-report section: {heading}")

    for label, pattern in PLACEHOLDERS.items():
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"placeholder or generic content remains: {label}")

    # --- Anti-boilerplate: no long sentence may repeat REPEAT_LIMIT+ times ---
    sentences = re.split(r"[。；;\n]", text)
    counts = Counter(s.strip() for s in sentences if len(s.strip()) >= REPEAT_MIN_LEN)
    for sentence, count in counts.items():
        if count >= REPEAT_LIMIT and not sentence.startswith("|") and not sentence.startswith("-"):
            errors.append(
                f"sentence repeated {count}x (template filling suspected): {sentence[:40]}..."
            )

    # --- Section 0: plain-language intro and key numbers ---
    overview = section(text, "## 0. 一页看懂")
    if mode == "full":
        if "这个行业是做什么的" not in overview:
            errors.append("section 0 missing plain-language intro '这个行业是做什么的'")
        if "三个最重要的数字" not in overview:
            errors.append("section 0 missing '三个最重要的数字'")
        if not re.search(r"结论状态[：:]", overview):
            errors.append("section 0 missing 结论状态")

    # --- Section 1: mermaid chart, node explanations, representative companies ---
    chain = section(text, "## 1. 产业链地图")
    if mode == "full":
        if "```mermaid" not in chain:
            errors.append("industry chain map must be a mermaid diagram")
        if not re.search(r"###\s*1\.2", chain):
            errors.append("missing per-node explanations (### 1.2.x)")
        if "代表企业" not in chain:
            errors.append("missing representative-company tables in chain nodes")
        if not re.search(r"上市地|代码|未上市", chain):
            errors.append("representative companies lack listing venue/ticker information")
        if "谁最终付款" not in chain:
            errors.append("missing money-flow table (谁最终付款…)")

    # --- Section 4: interpretation cells must carry content ---
    signals = section(text, "## 4. 供需矛盾与高频信号")
    if mode == "full" and signals:
        for row in table_rows(signals):
            for cell in row:
                if cell in EMPTY_INTERPRETATION_CELLS:
                    errors.append(
                        f"signal interpretation cell is contentless boilerplate: '{cell}'"
                    )

    # --- Section 5: prior-cycle comparison and falsification ---
    cycle = section(text, "## 5. 周期位置与传导")
    if mode == "full":
        if "进阶视角" not in cycle:
            errors.append("section 5 missing 进阶视角 prior-cycle comparison")
        if not re.search(r"什么会证明这个判断错了|What would prove this wrong", cycle):
            errors.append("section 5 missing falsification condition")

    # --- Advanced-reader blocks across the body ---
    if mode == "full":
        advanced_count = len(re.findall(r"进阶视角", text))
        if advanced_count < 3:
            errors.append(
                f"only {advanced_count} 进阶视角 blocks; need them in chain nodes, demand, supply and cycle sections"
            )

    # --- Section 6: capital-flow attempts table + qualitative paragraph ---
    capital = section(text, "## 6. 资金动向")
    if mode == "full":
        for required in ["尝试的来源类型", "已定价", "未定价"]:
            if required not in capital:
                errors.append(f"section 6 missing mandatory element: {required}")
        attempt_rows = [
            row
            for row in table_rows(capital)
            if row and row[0] not in ("尝试的来源类型", "产业现实")
            and any(cell for cell in row[1:])
        ]
        if "尝试的来源类型" in capital and len(attempt_rows) < 3:
            errors.append("capital-flow attempts table has fewer than 3 recorded attempts")

    # --- Section 7: future capital flow scenarios ---
    future = section(text, "## 7. 未来资金可能流向")
    if mode == "full":
        for scenario in ["基准", "上行", "下行"]:
            if scenario not in future:
                errors.append(f"section 7 missing scenario: {scenario}")
        if not re.search(r"不构成.{0,12}买卖建议", future):
            errors.append("section 7 missing no-advice disclaimer")

    # --- Section 8: mainstream narrative contrast ---
    contrast = section(text, "## 8. 分歧与反证")
    if mode == "full" and "主流叙事" not in contrast:
        errors.append("section 8 missing mainstream-narrative vs report contrast")

    # --- Section 9: watchpoints ---
    watch = section(text, "## 9. 观察哨与跟踪")
    for header in ["基线", "来源", "频率", "正向触发", "反证触发"]:
        if mode == "full" and header not in watch:
            errors.append(f"watchpoint table missing field: {header}")

    # Watchpoint indicator cells must be names, not values.
    watch_rows = table_rows(watch.split("### 9.1", 1)[0])
    for row in watch_rows[1:]:
        if row and re.search(r"\d[\d,.]*\s*(元|美元|欧元|亿|万|吨|百万|GWh|MW|TWh|%)", row[0]):
            errors.append(f"watchpoint indicator cell contains a value, not an indicator name: '{row[0][:30]}'")

    series_heading = re.search(r"^###\s*9\.1\s+可比时间序列\s*$", watch, re.MULTILINE)
    series_gap = re.search(
        r"可比时间序列缺口|Evidence gap:\s*comparable time series unavailable|可比时间序列(?:不可用|缺口)",
        watch,
        re.IGNORECASE,
    )
    if mode == "full" and not series_heading and not series_gap:
        errors.append("missing comparable time-series table or explicit time-series evidence gap")
    if series_heading:
        series_block = watch[series_heading.end() :].split("跟踪数据库", 1)[0].split("Tracking database:", 1)[0]
        lines = [line for line in series_block.splitlines() if line.strip().startswith("|")]
        if len(lines) >= 3:
            headers = [cell.strip() for cell in lines[0].strip().strip("|").split("|")]
            idx = {h: i for i, h in enumerate(headers)}
            ind_key = "指标" if "指标" in idx else "Indicator"
            unit_key = "单位" if "单位" in idx else "Unit"
            val_key = "数值" if "数值" in idx else "Value"
            missing = [k for k in (ind_key, unit_key, val_key) if k not in idx]
            if missing:
                errors.append(f"comparable time-series table missing columns: {', '.join(missing)}")
            groups: dict[tuple[str, str], int] = {}
            for line in lines[2:]:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) < len(headers):
                    continue
                indicator = cells[idx[ind_key]] if ind_key in idx else ""
                unit = cells[idx[unit_key]] if unit_key in idx else ""
                value = cells[idx[val_key]] if val_key in idx else ""
                if indicator and unit and re.fullmatch(r"[-+]?\d[\d,]*(?:\.\d+)?", value):
                    groups[(indicator, unit)] = groups.get((indicator, unit), 0) + 1
            if not any(count >= 2 for count in groups.values()):
                errors.append("comparable time-series table needs at least two numeric points for one indicator and unit")
        elif mode == "full" and not series_gap:
            errors.append("comparable time-series table has fewer than two data rows")

    # --- Section 10: glossary ---
    glossary = section(text, "## 10. 术语表")
    if mode == "full":
        glossary_terms = [row[0] for row in table_rows(glossary)[1:] if row and row[0]]
        if len(glossary_terms) < 3:
            errors.append("glossary has fewer than 3 terms; jargon must be explained for first-time readers")

    # --- Appendix A: evidence ledger ---
    ledger = section(text, "## 附录A 证据台账")
    if not ledger:
        ledger = section(text, "## 10. 证据台账")  # legacy fallback
    ledger_headers = ["证据ID", "发布方", "访问日期", "已打开", "时效", "局限"]
    legacy_headers = ["Claim ID", "Publisher", "Accessed", "Opened", "Freshness", "Limitation"]
    if mode == "full":
        if not any(h in ledger for h in ledger_headers) and not any(h in ledger for h in legacy_headers):
            errors.append("evidence ledger missing (appendix A)")
        else:
            active = ledger_headers if any(h in ledger for h in ledger_headers) else legacy_headers
            for header in active:
                if header not in ledger:
                    errors.append(f"evidence ledger missing field: {header}")

    opened_rows = [line for line in ledger.splitlines() if re.search(r"\|\s*(?:yes|是)\s*\|", line, re.IGNORECASE)]
    for row in opened_rows:
        if re.search(r"\|\s*(?:—|-|未记录|n/a)\s*\|\s*(?:yes|是)\s*\|", row, re.IGNORECASE):
            errors.append("opened evidence row is missing a usable locator")
        if not re.search(r"https?://", row):
            errors.append("opened evidence row is missing an original-source URL")

    # Ledger limitation cells must not all be one identical sentence.
    ledger_data_rows = table_rows(ledger)
    if len(ledger_data_rows) > 3:
        limitations = [row[-1] for row in ledger_data_rows[1:] if row and len(row[-1]) > 8]
        if limitations and len(set(limitations)) == 1:
            errors.append("every ledger Limitation cell is the same sentence; write per-source limitations")

    ledger_ids = re.findall(r"^\|\s*(E\d+)\s*\|", ledger, re.MULTILINE)
    duplicate_ids = sorted({claim_id for claim_id in ledger_ids if ledger_ids.count(claim_id) > 1})
    if duplicate_ids:
        errors.append(f"duplicate evidence IDs in ledger: {', '.join(duplicate_ids)}")
    referenced_ids = set(re.findall(r"\bE\d+\b", text))
    missing_ids = sorted(referenced_ids - set(ledger_ids))
    if missing_ids:
        errors.append(f"evidence IDs referenced but absent from ledger: {', '.join(missing_ids)}")
    if mode == "full" and strict and len(ledger_ids) < 6:
        errors.append(f"full strict report has only {len(ledger_ids)} evidence-ledger rows; expected at least 6")

    # --- Appendix C: readiness + execution ---
    readiness = section(text, "## 附录C 证据就绪度与研究执行记录")
    if not readiness:
        readiness = section(text, "## 0. 结论与证据就绪度")  # legacy fallback
    for lane in READINESS_LANES:
        if mode == "full" and lane not in readiness:
            errors.append(f"missing evidence-readiness lane: {lane}")

    for row in readiness.splitlines():
        match = re.match(
            r"^\|\s*(.+?)\s*\|\s*(Ready|Gap|就绪|缺口)\s*\|\s*(\d+)\s*\|\s*(\d+)",
            row,
            re.IGNORECASE,
        )
        if not match:
            continue
        lane, status, opened, required = match.groups()
        if status.lower() in ("ready", "就绪") and int(opened) < int(required):
            errors.append(
                f"readiness lane '{lane.strip()}' is Ready but has {opened} opened sources; requires {required}"
            )

    has_gap = bool(re.search(r"\|\s*(?:Gap|缺口)\s*\|", readiness, re.IGNORECASE))
    conclusion_zone = overview if overview else readiness
    if has_gap and re.search(r"结论状态[：:]\s*可发布", conclusion_zone):
        errors.append("report has evidence gaps but conclusion status is publishable")
    if has_gap and not re.search(r"结论状态[：:]\s*(?:暂定|阶段待验证)", conclusion_zone):
        errors.append("report has evidence gaps but conclusion is not marked provisional")

    for row in readiness.splitlines():
        if re.search(r"\|\s*(?:complete|完成)\s*\|", row, re.IGNORECASE) and not re.search(r"\bE\d+\b", row):
            errors.append("research row marked complete without evidence IDs")

    urls = set(re.findall(r"https?://[^)\s|>]+", text))
    if mode == "full" and strict and len(urls) < 6:
        errors.append(f"full strict report has only {len(urls)} distinct source URLs; expected at least 6")
    elif mode == "full" and len(urls) < 6:
        warnings.append(f"only {len(urls)} distinct source URLs")

    if re.search(r"Original Opened\?", text):
        errors.append("legacy self-attestation column 'Original Opened?' remains; use the evidence ledger")
    if re.search(r"\|\s*Latest\?\s*\|", text):
        errors.append("legacy 'Latest?' checkbox remains; use metric-level freshness and access dates")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--mode", choices=("quick", "full"), default="full")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    text = args.report.read_text(encoding="utf-8")
    errors, warnings = validate(text, args.mode, args.strict)

    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        print(f"Report validation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"Report validation passed: {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
