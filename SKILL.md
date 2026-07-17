---
name: industry-cycle-analysis
description: 产业供需周期分析 Skill，触发词包括“产析skill”。用于研究一个行业、赛道或产业链的需求来源、有效供给、产能周期、价格/订单/库存/利润、资本开支、产业链传导和资本市场预期阶段。适合半导体、AI算力、光通信、新能源、化工、钢铁、资源品、机器人、数据中心、电力、液冷等周期性或成长性行业；不要用于短线荐股、技术分析、K线预测、目标价或直接投资建议。
---

# Industry Cycle Analysis

## Core rule

Start from the real economy. Map market expectations only after the industrial chain, evidence coverage, and supply-demand conflict are clear.

```text
real demand -> buyer/budget -> orders -> effective supply -> price/inventory/margin
-> capex -> qualified capacity -> cycle turn -> market expectation stage
```

Never convert a filled template into a confident conclusion. A missing metric is an evidence gap, not permission to write generic prose.

## Write for two audiences at once

Every full report must work for both readers:

1. **First-time reader**: after one pass of the main body they can retell the industry chain, who pays whom, representative companies, the current cycle stage, capital flows, and where money may go next. Requirements:
   - Main body (sections 0-10) comes first; all audit material (evidence ledger, data currency, readiness, execution record) goes to appendices.
   - Section 0 opens with a plain-language "这个行业是做什么的" before any cycle judgment.
   - Every jargon term or abbreviation used in the body appears in the `## 10. 术语表` section with a plain-language explanation.
   - Representative companies get real introductions (listing venue/ticker, position in the segment, why representative) — never bare name lists.
   - All table headers and section labels are Chinese.
2. **Experienced reader**: the report must contain judgment they cannot get from a Wikipedia-level summary. Requirements:
   - Each of sections 1.2 (per node), 2, 3, and 5 carries a `进阶视角` block: calibration traps, the sharpest current controversy, prior-cycle comparison, or where nominal capacity dies before becoming effective supply. These blocks must state a position backed by evidence IDs, or explicitly record that no controversy was found and where you looked.
   - Section 8 must contrast the mainstream market narrative with this report's judgment and say whose evidence is harder. "无分歧" is acceptable only with the search trail recorded.
   - Prior-cycle comparison in section 5 names concrete years and lag lengths, or states honestly that no comparable prior cycle exists.

Anti-boilerplate rules (hard):

- No explanatory sentence may repeat 3+ times within one report. If you notice yourself reusing a sentence pattern across nodes or rows, the content is not yet researched — go back to evidence.
- Node explanations must describe the concrete action and output of that node ("把设计图变成硅片上的电路"), never circular definitions ("X负责把上游投入转成Y可采购的产品").
- Chain nodes are stages or actors, never products (焦炭 is a product; 焦化厂 is the node).
- Parallel inputs (equipment, materials, energy, software, finance) must appear as parallel branches in the mermaid chart, not be omitted or serialized.
- Every data period must be an explicit year-month or quarter; "最新已披露期" is banned.
- Watchpoint `指标` cells contain indicator names, never values.

## Choose the research mode

- Use a **quick scan** for boundary clarification, a preliminary cycle hypothesis, or a short update. Keep the evidence table compact, but still label facts, inferences, assumptions, freshness, and gaps.
- Use **full research** when the user asks for a report, deep research, cross-chain comparison, or capital-market mapping. Load `references/report-template.md`, `references/quality-checklist.md`, `references/evidence-ledger.md`, and `references/capital-market-mapping.md` (the last is mandatory because sections 6-7 of the template require its attempt checklist).
- For agentic or multi-round deep research, also load `references/deepsearch-research-protocol.md`.
- Load `references/framework.md`, `references/supply-demand-questions.md`, or `references/cycle-stages.md` only when that part of the analysis needs them.

## Synchronize time and release status first

1. Query the system time before collecting data.
2. Store the timestamp and timezone in the report.
3. Build a release-status list for the important sources and metrics.
4. Treat “latest” as the latest officially released value available at the analysis timestamp. Never infer that a quarterly report exists merely because the calendar entered the next quarter.
5. Distinguish full-quarter actuals, partial monthly actuals, guidance, plans, forecasts, and stale values.

Windows PowerShell:

```powershell
Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"
```

POSIX:

```bash
date "+%Y-%m-%d %H:%M:%S %z"
```

If Q2 monthly data exist but Q2 financial results have not been released, write “Q2 partial monthly actuals + Q1 financial actuals”; do not write “Q2 actuals covered”.

## Route and verify evidence

Before web research, load `references/search-routing.md`. Rank sources with `references/source-priority.md`.

Use this ladder:

```text
discovery -> open original -> verify metric and definition -> freshness check
-> contradiction search -> evidence ledger -> conclusion
```

Treat search snippets, generated summaries, reposts, and social posts as leads. Promote a claim to evidence only after opening an original or authoritative reproduction and recording its metadata and locator.

## Maintain an evidence ledger

Record every important claim using `references/evidence-ledger.md`.

- Set `opened=yes` only when the source was actually opened in the current research run or a preserved auditable run.
- Set `freshness=current` only after checking whether a newer release supersedes the source.
- Record publisher, publication date, access date, period, geography, unit/definition, locator, actual/forecast status, and limitations.
- Derive search rounds, tool routes, source counts, and completion status from the run. Never hard-code `Latest`, `Opened`, or `Complete` in a report generator.
- Keep industry evidence separate from market-pricing or narrative evidence.

## Apply the evidence-readiness gate

Assess these lanes before naming a cycle stage:

| Lane | Full-research minimum |
|---|---:|
| Industry chain and relationships | 2 opened reliable sources |
| Demand | 3 opened reliable sources |
| Supply and effective capacity | 3 opened reliable sources |
| Price/order/inventory/margin | 3 opened sources, or an explicit gap |
| Capital-market expectations | 2 opened sources, or a gap documented via the mandatory attempts below |

Rules:

- If demand, supply/effective capacity, or price/order/inventory/margin has a material gap, mark the cycle conclusion **provisional** and cap confidence at medium.
- If both demand and effective supply are unresolved, write `阶段待验证` rather than forcing a stage label.
- An explicit evidence gap is honest completion of a search subtask, but it is not positive evidence for the industry conclusion.
- Do not reuse one source as if it independently satisfied several unrelated lanes.

## Capital-market lane: mandatory attempts before declaring a gap

Declaring the capital-market lane a gap without trying is not allowed. Before writing any gap:

1. Load `references/capital-market-mapping.md` and actually attempt the free-source checklist there (index valuation percentile, sector ETF flows/shares, northbound/margin balances where applicable, leader price-vs-earnings divergence). Record every attempt and its outcome in the section-6 attempts table — including failures.
2. Whether or not quantitative data was obtained, section 6 must contain the qualitative paragraph: what the market has probably already priced, what it probably has not, and on what indirect evidence — clearly labeled as inference, never as measured fact.
3. Section 7 (未来资金可能流向) is mandatory: for each of the three scenarios in section 8's logic, state which chain node the profit pool would shift toward, which benefits first/later, derived from order lead times, qualification barriers, and capacity elasticity — never from price charts. Keep the no-buy/sell-advice disclaimer visible.
4. Only after steps 1-2 are recorded may the lane be marked gap, and the conclusion stays provisional.

## Model relationships explicitly

1. Define the industry boundary, adjacent industries, substitutes, and geography.
2. Represent important nodes and explicit edges: `from`, `relation`, `to`, and evidence IDs.
3. Do not infer suppliers and buyers from array adjacency. Equipment, materials, infrastructure, and finance often enter a production process in parallel.
4. Separate:
   - production/physical flow;
   - order and budget flow;
   - profit and cost-bearing flow.
5. For each important node, explain what it is, what it does, suppliers, buyers, representative companies, monetization, bottleneck role, and evidence.

For AI-related semiconductors, distinguish at least:

```text
AI use -> model/cloud budget -> data center/server -> GPU or ASIC + HBM
-> advanced packaging and test -> foundry
materials/equipment -> packaging/foundry capacity (parallel inputs)
```

## Execute the analysis

1. Define the boundary and explicit relationship graph.
2. Build the release-status list and research plan with a maximum of three search rounds per subtask by default.
3. Collect the latest available actuals for demand, supply/effective capacity, price/orders/inventory/margins, expansion timing, and representative companies.
4. Separate announced capacity from installed, qualified, yield-ramped, and customer-backed capacity.
5. Find the buyer and demand trigger; separate actual use from policy, restocking, capex, or expectation.
6. Locate the bottleneck or surplus and explain the transmission lag from demand to orders, revenue, margin, capex, qualified capacity, and reversal.
7. Preserve conflicting evidence and unresolved definitions instead of averaging them away.
8. Judge the cycle stage only after applying the evidence-readiness gate.
9. Map industrial reality to the market expectation stage without giving a buy/sell call.
10. Produce 3-5 falsifiable watchpoints with an actual source, baseline, frequency, direction, and numeric or event threshold.
11. When public data permits, preserve at least one real comparable time series: the same indicator, definition, unit, geography, and reporting entity across two or more dates. Never combine revenue, margin, inventory, forecasts, or different companies into a synthetic line. If no such series is available, write the precise evidence gap and the source to monitor next.

## Write and validate the report

For full research:

1. Use `references/report-template.md` and preserve the exact header labels `分析日期`, `地理范围`, `数据时效`, and `行业边界`. Follow its section order: reader-facing body (0-10) first, audit appendices (A/B/C) last.
2. Separate facts, inferences, assumptions, and gaps.
3. Include the mermaid chain map with parallel inputs, per-node explanations with representative-company tables, the money-flow table, capital-flow attempts table plus qualitative pricing paragraph, future-capital-flow scenarios, mainstream-vs-report contrast, watchpoints, the glossary, and either a comparable time-series table or an explicit time-series evidence gap.
4. Do not use placeholders such as `官方/协会/公司`, `待按产品核验`, `市场可能交易`, `见数据时效表`, or a generic “连续两期改善”. Also banned as filler: `钱和订单从…的需求向前传`, `负责把上游投入转成…可采购、可验证的产品或服务`, `核心产品需求`, `新增场景`, `直接观测`/`交叉验证` as an entire interpretation cell, `最新已披露期` as a period, and reusing one identical Limitation sentence across every ledger row.
5. Run:

```bash
python scripts/validate_report.py path/to/report.md --mode full --strict
```

6. Use `references/quality-checklist.md` for the final substantive pass. A structurally valid Skill does not prove that a generated report is valid.

## One industry, one research run

Never batch-generate reports for multiple industries by re-instantiating one filled report with different nouns. Each industry requires its own search rounds, its own evidence ledger, and its own chain map. Shared boilerplate across reports for different industries is a defect: if two reports contain the same explanatory sentence outside the fixed template scaffolding and 尾注, at least one of them was not researched.

## Optional export and cleanup

- If a PDF is requested, resolve the Skill directory first and run its `scripts/md_to_pdf.py`; do not assume the current working directory is the Skill directory.
- Create a task-specific temporary directory for downloads. Clean it only if temporary files were actually created, record those paths, and verify the resolved cleanup target stays inside that directory.
- Never wildcard-delete workspace or user data.

Keep these warnings visible in full reports:

```text
supply-demand gap != stock-price rise
correct direction != correct timing
earnings realization != continued stock rise
AI answer != fact
stale data != current fact
```
