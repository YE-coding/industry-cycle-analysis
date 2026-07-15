#!/usr/bin/env python3
"""Validate an industry-cycle Markdown report for structural and evidence-integrity gates."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FULL_SECTIONS = [
    "## 0. 结论与证据就绪度",
    "## 1. 数据时效与证据覆盖",
    "## 2. 产业链与关系",
    "## 3. 需求",
    "## 4. 供给",
    "## 5. 供需矛盾与高频信号",
    "## 6. 周期与利润/订单传导",
    "## 7. 资本市场预期",
    "## 8. 情景与反证",
    "## 9. 观察哨与跟踪",
    "## 10. 证据台账",
    "## 11. 研究执行记录",
]

REQUIRED_HEADERS = ["分析日期", "地理范围", "数据时效", "行业边界"]
READINESS_LANES = [
    "Industry chain",
    "Demand",
    "Supply and effective capacity",
    "Price/order/inventory/margin",
    "Capital-market expectations",
]

PLACEHOLDERS = {
    "generic source": r"官方/协会/公司|公司披露或行业数据|官方或交易所高频数据优先",
    "unverified metric": r"待按产品核验|视公开口径|见数据时效表",
    "generic market statement": r"市场可能交易",
    "generic watchpoint": r"连续2期改善且与价格/利润同向|连续2期恶化或与库存背离",
    "generic transition window": r"未来2[-至]6(?:个)?季度",
}


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    rest = text[start + len(heading) :]
    match = re.search(r"\n##\s+", rest)
    return rest if match is None else rest[: match.start()]


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

    readiness = section(text, "## 0. 结论与证据就绪度")
    for lane in READINESS_LANES:
        if mode == "full" and lane not in readiness:
            errors.append(f"missing evidence-readiness lane: {lane}")

    for row in readiness.splitlines():
        match = re.match(
            r"^\|\s*(.+?)\s*\|\s*(Ready|Gap)\s*\|\s*(\d+)\s*\|\s*(\d+)",
            row,
            re.IGNORECASE,
        )
        if not match:
            continue
        lane, status, opened, required = match.groups()
        if status.lower() == "ready" and int(opened) < int(required):
            errors.append(
                f"readiness lane '{lane.strip()}' is Ready but has {opened} opened sources; requires {required}"
            )

    has_gap = bool(re.search(r"\|\s*(?:Gap|缺口)\s*\|", readiness, re.IGNORECASE))
    if has_gap and re.search(r"结论状态[：:]\s*可发布", readiness):
        errors.append("report has evidence gaps but conclusion status is publishable")
    if has_gap and not re.search(r"结论状态[：:]\s*(?:暂定|阶段待验证)", readiness):
        errors.append("report has evidence gaps but conclusion is not marked provisional")

    chain = section(text, "## 2. 产业链与关系")
    if mode == "full" and not re.search(r"\|\s*From\s*\|\s*Relation\s*\|\s*To\s*\|", chain):
        errors.append("explicit relationship table is missing From/Relation/To")

    ledger = section(text, "## 10. 证据台账")
    ledger_headers = ["Claim ID", "Publisher", "Accessed", "Locator", "Opened", "Freshness", "Limitation"]
    if mode == "full":
        for header in ledger_headers:
            if header not in ledger:
                errors.append(f"evidence ledger missing field: {header}")

    opened_rows = [line for line in ledger.splitlines() if re.search(r"\|\s*yes\s*\|", line, re.IGNORECASE)]
    for row in opened_rows:
        if re.search(r"\|\s*(?:—|-|未记录|n/a)\s*\|\s*yes\s*\|", row, re.IGNORECASE):
            errors.append("opened evidence row is missing a usable locator")
        if not re.search(r"https?://", row):
            errors.append("opened evidence row is missing an original-source URL")

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

    watch = section(text, "## 9. 观察哨与跟踪")
    for header in ["Baseline", "Source", "Frequency", "Positive Trigger", "Disconfirming Trigger"]:
        if mode == "full" and header not in watch:
            errors.append(f"watchpoint table missing field: {header}")

    execution = section(text, "## 11. 研究执行记录")
    for row in execution.splitlines():
        if "| complete |" in row.lower() and not re.search(r"\bE\d+\b", row):
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
