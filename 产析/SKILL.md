---
name: 产析
description: 产析skill，industry-cycle-analysis 的中文可调用别名。用于研究一个行业、赛道或产业链的供需矛盾、产能周期、价格变化、资本开支、企业盈利、产业链传导和资本市场预期映射。适合分析半导体、光通信、AI算力、新能源、化工、钢铁、焦煤、铁矿石、机器人、数据中心、电力、液冷等周期性或成长性行业。不要用于短线荐股、技术分析、K线预测或直接给投资建议。
argument-hint: [industry-or-sector]
version: 1.0.0
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

## Workflow

1. Define the industry boundary and chain.
   - Identify upstream, midstream, downstream, end demand, and substitutes.
   - Draw a top-down and bottom-up chain if the industry is complex.
   - Load `references/framework.md` if the chain or analysis frame is unclear.

2. Find the demand driver.
   - Identify whether demand comes from real end use, policy, replacement, inventory restocking, capital expenditure, or speculative expectation.
   - Separate current demand from expected future demand.

3. Find the supply constraint.
   - Identify capacity, yield, equipment lead time, raw materials, talent, patents, regulation, power, land, logistics, or customer qualification constraints.
   - For semiconductors and optical communications, focus especially on yield, node/process, packaging, optical chips, modules, wafer capacity, foundry slots, and data-center capex.

4. Locate the supply-demand conflict.
   - Use `references/supply-demand-questions.md`.
   - Ask where the shortage or surplus occurs, how long it lasts, who can expand, how much they can expand, and when new capacity enters the market.

5. Review the last two years of industry data.
   - Prioritize monthly or quarterly data where possible.
   - Use `references/source-priority.md` to rank source quality.
   - If data is missing, say it is missing. Do not invent precise numbers.

6. Judge the cycle stage.
   - Use `references/cycle-stages.md`.
   - Distinguish introduction, growth, shortage, expansion, earnings realization, oversupply, and clearing.

7. Map to capital-market expectations.
   - Use `references/capital-market-mapping.md`.
   - Always separate industrial reality from market pricing.
   - Explicitly ask whether the stock market is trading expectation start, expectation diffusion, earnings realization, valuation digestion, or expectation reversal.

8. Produce the report.
   - Use `references/report-template.md`.
   - Keep conclusions split into facts, inferences, and assumptions.
   - Include a tracking table for future monthly updates.

9. Validate before final delivery.
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
