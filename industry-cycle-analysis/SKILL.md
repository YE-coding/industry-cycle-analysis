---
name: industry-cycle-analysis
description: 产业供需周期分析 Skill，触发词包括“产析skill”。用于研究一个行业、赛道或产业链的供需矛盾、产能周期、价格变化、资本开支、企业盈利、产业链传导和资本市场预期映射，并采用 DeepSearch 式子问题拆解、证据矩阵、冲突信息合并和检索成本控制。适合分析半导体、光通信、AI算力、新能源、化工、钢铁、焦煤、铁矿石、机器人、数据中心、电力、液冷等周期性或成长性行业。不要用于短线荐股、技术分析、K线预测或直接给投资建议。
argument-hint: [industry-or-sector]
version: 1.1.0
user-invocable: true
allowed-tools: Read, WebSearch, WebFetch, Bash
---

# Industry Cycle Analysis

## Purpose

Use this skill to analyze industries from the real economy first, then map findings to capital-market expectations only after the industrial logic is clear.

Core principle:

```text
Do not use K-lines to understand the world.
Understand the real world first, then come back to interpret K-lines.
```

The central model:

```text
real world
-> industry chain
-> supply-demand conflict
-> capacity expansion
-> price/order/inventory change
-> company earnings
-> market expectation
-> stock-price projection
```

## Boundary

Use this skill for industry systems, not single objects.

- For one company, product, technology, concept, or person, prefer `hv-analysis`.
- For industry supply-demand cycles, capacity bottlenecks, market expectation mapping, or "where is this sector in the cycle", use this skill.
- Do not produce direct investment advice, stock recommendations, target prices, or short-term trading calls.
- Treat public data, AI answers, media summaries, and broker commentary as clues, not facts.
- For deep research tasks, use DeepSearch-style decomposition with strict search budgets and stopping conditions. Load `references/deepsearch-research-protocol.md`.

## Time Synchronization Rule

**Every time this skill is invoked, you MUST:**

1. Query current system time at the start of analysis
2. Store the timestamp for use throughout the report
3. Use this timestamp in all date references and data currency checks

```bash
# Query current time (run at skill invocation start)
date "+%Y-%m-%d %H:%M:%S %Z"
```

**Why this matters:**
- Industry data is time-sensitive (quarterly reports, monthly shipments, capacity updates)
- Stale data leads to incorrect cycle-stage judgment
- Reports must clearly state the analysis date for future reference

**Storage format:**
```
Analysis Timestamp: [YYYY-MM-DD HH:MM:SS]
Data Currency: [Latest data period covered]
```

## Hard Research Controls

Use these controls whenever web search, agentic browsing, logs, journals, or long tool outputs are involved:

1. Cap each subtask at 3 search rounds by default. If evidence remains incomplete after the cap, summarize current evidence and mark the gap instead of searching indefinitely.
2. Never read complete `journal`, `jsonl`, `log`, or agent trace files. Read only the latest 80-120 lines, or filter by `result`, `error`, `timeout`, `source`, `claim`, or `evidence`.
3. Compress every round of tool observations into a short local summary before using it in reasoning. Do not repeatedly paste raw web pages, logs, or long tool outputs back into context.

## Workflow

1. Define the industry boundary and chain.
   - Identify upstream, midstream, downstream, end demand, and substitutes.
   - Draw a top-down and bottom-up chain if the industry is complex.
   - Load `references/framework.md` if the chain or analysis frame is unclear.

2. Plan the DeepSearch-style research split.
   - Load `references/deepsearch-research-protocol.md`.
   - Split the industry into 6-10 research subtasks: chain map, demand, supply, capacity, price/order/inventory, company beneficiaries, policy/technology variables, market expectation.
   - Set evidence minimums and search budgets before browsing.

3. Find the demand driver.
   - Identify whether demand comes from real end use, policy, replacement, inventory restocking, capital expenditure, or speculative expectation.
   - Separate current demand from expected future demand.

4. Find the supply constraint.
   - Identify capacity, yield, equipment lead time, raw materials, talent, patents, regulation, power, land, logistics, or customer qualification constraints.
   - For semiconductors and optical communications, focus especially on yield, node/process, packaging, optical chips, modules, wafer capacity, foundry slots, and data-center capex.

5. Locate the supply-demand conflict.
   - Use `references/supply-demand-questions.md`.
   - Ask where the shortage or surplus occurs, how long it lasts, who can expand, how much they can expand, and when new capacity enters the market.

6. Review the last two years of industry data.
   - Prioritize monthly or quarterly data where possible.
   - Use `references/source-priority.md` to rank source quality.
   - If data is missing, say it is missing. Do not invent precise numbers.

7. Merge conflicting evidence.
   - Prefer primary disclosures over media summaries.
   - Keep conflicting numbers visible with source, date, geography, and data definition.
   - If two sources conflict and neither is authoritative, mark the conclusion as unresolved.

8. Judge the cycle stage.
   - Use `references/cycle-stages.md`.
   - Distinguish introduction, growth, shortage, expansion, earnings realization, oversupply, and clearing.

9. Map to capital-market expectations.
   - Use `references/capital-market-mapping.md`.
   - Always separate industrial reality from market pricing.
   - Explicitly ask whether the stock market is trading expectation start, expectation diffusion, earnings realization, valuation digestion, or expectation reversal.

10. Produce the report.
   - Use `references/report-template.md`.
   - Keep conclusions split into facts, inferences, and assumptions.
   - Include a tracking table for future monthly updates.

11. Validate before final delivery.
   - Use `references/quality-checklist.md`.
   - If creating a PDF, use `scripts/md_to_pdf.py`.

## Output Requirements

Every serious analysis should include:

- industry-chain map
- key supply-demand conflict
- past two years of relevant data or a note explaining data gaps
- capacity expansion timeline
- price/order/inventory evidence
- beneficiary and non-beneficiary distinction
- cycle-stage judgment
- capital-market expectation stage
- evidence matrix with source quality and unresolved gaps
- search budget note for deep research tasks
- follow-up indicators to track monthly

Keep these warnings visible:

```text
supply-demand gap != stock price rise
correct industry direction != correct timing
earnings realization != continued stock rise
complete public data != market has not priced it
AI answer != fact
```

## Optional PDF Export

After writing the final Markdown report, run:

```bash
python scripts/md_to_pdf.py report.md report.pdf
```

If local PDF dependencies are missing, leave the Markdown report as the primary deliverable and explain what dependency is missing.

For long logs or agent traces, use:

```bash
python scripts/safe_log_extract.py path/to/log.jsonl --tail 120 --filter result error timeout evidence source
```
