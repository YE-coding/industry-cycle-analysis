---
name: industry-cycle-analysis
description: 产业供需周期分析 Skill，触发词包括"产析skill"。用于研究一个行业、赛道或产业链的供需矛盾、产能周期、价格变化、资本开支、企业盈利、产业链传导和资本市场预期映射，并采用 DeepSearch 式子问题拆解、证据矩阵、冲突信息合并和检索成本控制。适合分析半导体、光通信、AI算力、新能源、化工、钢铁、焦煤、铁矿石、机器人、数据中心、电力、液冷等周期性或成长性行业。不要用于短线荐股、技术分析、K线预测或直接给投资建议。
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
-> profit/order transmission chain
-> supply-demand conflict
-> capacity expansion
-> price/order/inventory change
-> company earnings
-> market expectation
-> stock-price projection
```

Dynamic-cycle rule:

```text
Do not stop at "demand is strong" or "supply is tight".
Explain how the contradiction transmits across the chain, when capacity responds,
which indicators would falsify the judgment, and how to update the database later.
```

## Boundary

Use this skill for industry systems, not single objects.

- For one company, product, technology, concept, or person, prefer `hv-analysis`.
- For industry supply-demand cycles, capacity bottlenecks, market expectation mapping, or "where is this sector in the cycle", use this skill.
- Do not produce direct investment advice, stock recommendations, target prices, or short-term trading calls.
- Treat public data, AI answers, media summaries, and broker commentary as clues, not facts.
- For deep research tasks, use DeepSearch-style decomposition with strict search budgets and stopping conditions. Load `references/deepsearch-research-protocol.md`.

## Hard Research Controls

Use these controls whenever web search, agentic browsing, logs, journals, or long tool outputs are involved:

1. Cap each subtask at 3 search rounds by default. If evidence remains incomplete after the cap, summarize current evidence and mark the gap instead of searching indefinitely.
2. Never read complete `journal`, `jsonl`, `log`, or agent trace files. Read only the latest 80-120 lines, or filter by `result`, `error`, `timeout`, `source`, `claim`, or `evidence`.
3. Compress every round of tool observations into a short local summary before using it in reasoning. Do not repeatedly paste raw web pages, logs, or long tool outputs back into context.

## Workflow

1. Define the industry boundary and chain.
   - Identify upstream, midstream, downstream, end demand, and substitutes.
   - Draw a top-down and bottom-up chain if the industry is complex.
   - Draw a profit/order transmission chain, not only a textbook production chain.
   - For AI-related semiconductors, distinguish: AI applications -> model companies -> cloud capex -> data centers -> servers -> GPU/ASIC -> HBM -> advanced packaging -> foundry -> equipment.
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
   - Explain the transmission path from end demand to orders, prices, capex, capacity release, margins, and possible reversal.
   - Separate immediate bottlenecks from delayed second-order beneficiaries.

6. Review the last two years of industry data.
   - Prioritize monthly or quarterly data where possible.
   - Use `references/source-priority.md` to rank source quality.
   - If data is missing, say it is missing. Do not invent precise numbers.
   - When possible, convert the report into a tracking database with date, indicator, value, direction, source, and implication.

7. Merge conflicting evidence.
   - Prefer primary disclosures over media summaries.
   - Keep conflicting numbers visible with source, date, geography, and data definition.
   - If two sources conflict and neither is authoritative, mark the conclusion as unresolved.

8. Judge the cycle stage.
   - Use `references/cycle-stages.md`.
   - Distinguish introduction, growth, shortage, expansion, earnings realization, oversupply, and clearing.
   - Build a timeline from demand discovery to shortage, price rise, capex, capacity release, oversupply risk, and clearing.
   - State the time lag that matters most: order lead time, capex cycle, qualification cycle, yield ramp, or inventory digestion.

9. Trace the profit/order transmission chain.
   - Map how demand changes propagate upstream: end demand → orders → revenue → margin → capex → upstream orders.
   - Identify where profit pools shift during cycle turns (who captures margin at each stage).
   - Distinguish order信号 from revenue realization timing.
   - Use `references/framework.md` "Depth Axis: Power and Money" section.

10. Map to capital-market expectations.
   - Use `references/capital-market-mapping.md`.
   - Always separate industrial reality from market pricing.
   - Explicitly ask whether the stock market is trading expectation start, expectation diffusion, earnings realization, valuation digestion, or expectation reversal.

11. Build observation posts (watchpoints).
   - Define 3-5 specific, measurable indicators to track monthly.
   - For each watchpoint: indicator name, data source, frequency, trigger threshold, and what signal change means.
   - Keep observation posts few and falsifiable; prefer 5 core indicators over a long unfocused list.
   - Examples: monthly utilization rate, order-to-revenue ratio, inventory days, margin trend, capex announcement timing.

12. Construct the cycle timeline.
   - Map the industry's historical cycle turns (past 2-3 cycles if data allows).
   - Estimate current position on the timeline with date anchors.
   - Identify which phase the industry is entering next and the expected transition window.

13. Produce the report.
   - Use `references/report-template.md`.
   - Keep conclusions split into facts, inferences, and assumptions.
   - Include a tracking table for future monthly updates.
   - Include 3 dynamic sections: profit transmission map, cycle timeline, and observation posts.
   - Keep observation posts few and falsifiable; prefer 5 core indicators over a long unfocused list.

14. Validate before final delivery.
   - Use `references/quality-checklist.md`.
   - Verify the report is not static: must include forward-looking tracking and conditional triggers.
   - If creating a PDF, use `scripts/md_to_pdf.py`.

## Output Requirements

Every serious analysis should include:

- industry-chain map
- profit/order transmission map
- key supply-demand conflict
- dynamic transmission explanation from demand to price/order/capex/capacity/profit
- past two years of relevant data or a note explaining data gaps
- capacity expansion timeline
- cycle timeline with likely transition points
- price/order/inventory evidence
- beneficiary and non-beneficiary distinction
- cycle-stage judgment
- falsifiable observation posts, not generic risk reminders
- tracking database template for monthly or quarterly updates
- capital-market expectation stage
- evidence matrix with source quality and unresolved gaps
- search budget note for deep research tasks

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
