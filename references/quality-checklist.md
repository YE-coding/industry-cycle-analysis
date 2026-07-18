# Quality Checklist

Use this after drafting and before delivery. Run `scripts/validate_report.py` first, then perform this substantive review.

## Hard blockers

Do not deliver a full report when any blocker remains:

- The analysis timestamp is missing, stale because it was hard-coded, or lacks a timezone.
- A source is marked `opened=yes` without an actual opened original and a page/table/section locator.
- A metric is marked `freshness=current` without checking whether a newer release supersedes it.
- A research subtask is marked `complete` from a template or source-array length rather than the actual run.
- Demand, effective supply, or price/order/inventory/margin has a material gap while the stage is presented as definitive or high-confidence.
- Parallel inputs are represented as a false serial chain, or suppliers/buyers are inferred from array adjacency.
- The final report contains placeholders such as `官方/协会/公司`, `待按产品核验`, `市场可能交易`, `视公开口径`, or `见数据时效表`.
- Any explanatory sentence repeats 3+ times in one report, or the same boilerplate appears in reports for different industries (e.g. `钱和订单从…的需求向前传`, `负责把上游投入转成…可采购、可验证的产品或服务`).
- A chain node explanation is a circular definition, or a node is a product instead of a stage/actor, or a node's description was copy-pasted from a different node type (e.g. a foundry described as "回款入口").
- The capital-market lane is declared a gap without a recorded attempts table (section 6), or section 6 lacks the qualitative priced/unpriced paragraph, or section 7 lacks the three-scenario future-capital-flow table.
- Observation posts lack a specific source, baseline, direction, and numeric or event threshold — or an indicator cell contains a value instead of an indicator name, or a baseline is stale beyond one release cycle without a 数据滞后 note.
- Qualification, pilot line, announced capacity, installed capacity, and volume production are conflated.

## Reader experience (both audiences)

First-time reader — after reading only the main body, could they:

- Say in one sentence what the industry sells and who pays for it? (Section 0 plain-language intro exists and avoids jargon.)
- Redraw the chain from the mermaid map, including parallel inputs and the final payer?
- Name 2-3 representative companies per key node, with listing venue and why they represent it?
- State the current cycle stage and the reasoning behind it?
- Say what the market has likely priced in and where money might flow next under each scenario?
- Look up every unfamiliar term in the glossary? (Every jargon term in the body appears there.)

Experienced reader — does the report contain anything they could not get from a generic summary:

- Does each 进阶视角 block take a position with evidence IDs (or record a genuine no-controversy search trail), rather than restating the section above it?
- Does section 5 compare against a named prior cycle with concrete years and lags, or honestly state none is comparable?
- Does section 8 name the mainstream narrative and say where this report disagrees and whose evidence is harder?
- Are calibration traps (shipment vs consumption, announced vs effective capacity, restocking vs end demand) called out where they actually bite in this industry?

Structure:

- Main body (0-10) is fully readable without opening any appendix; all audit tables live in appendices A/B/C.
- Table headers and section labels are Chinese.
- Reading-route note near the top tells each audience where to start.

## Evidence readiness

- Does the report show the five evidence lanes and opened-source counts?
- Does each lane meet the minimum in `source-priority.md` or show a precise evidence gap?
- Are important sources independently useful rather than one source being counted repeatedly for unrelated claims?
- Are actuals, partial actuals, guidance, plans, forecasts, and analysis clearly separated?
- Are source period, geography, unit/definition, publication date, access date, and locator visible?
- Are original links stable and as direct as possible rather than taxonomy/search landing pages?

## Boundary and relationship graph

- Is the included and excluded scope explicit?
- Are adjacent industries and substitutes named?
- Are production flow, order/budget flow, and profit/cost flow separated?
- Does every important edge specify `from`, `relation`, `to`, and evidence IDs?
- Does each important node identify suppliers, buyers, monetization, bottleneck role, representative companies, and evidence IDs?
- Are suppliers and buyers written under separate labels, with different content, rather than combined or inferred from a generic paragraph containing “客户”?
- Does a full report contain at least four important nodes, two representative companies/institutions per node, and a distinct evidence-backed 进阶视角 for every node?
- Across a multi-report corpus, does each report average at least 200 structured node characters and avoid reusing explanatory prose from another industry?

## Supply-demand reasoning

- Is the buyer or budget owner clear?
- Is actual use separated from policy, restocking, capex, and expectation?
- Are announced, installed, qualified, yield-ramped, and customer-backed capacities separated?
- Are yield, qualification, equipment lead time, materials, power, land, logistics, and cancellation/delay signals considered where relevant?
- Does the report explain demand -> orders -> revenue -> margin -> capex -> qualified capacity -> reversal?

## Cycle and market expectations

- Is the stage tied to date anchors and evidence IDs?
- Is the next transition conditional on measurable triggers rather than a generic “future 2-6 quarters”?
- Is there at least one real disconfirming source or a clearly stated contradiction-search gap?
- Are industrial evidence and market-pricing/narrative evidence kept separate?
- Does the report avoid buy/sell calls, target prices, and short-term forecasts?

## Tracking quality

- Are 3-5 watchpoints sufficient and non-duplicative?
- Does each watchpoint include a current baseline, a stable source, cadence, positive trigger, disconfirming trigger, and meaning?
- Does the report include at least one same-definition, same-unit comparable time series when public data allows it, or state a precise evidence gap when it does not?
- Does every plotted series avoid mixing companies, actuals with forecasts, or unlike measures such as revenue, margin, and inventory?
- Is indicator polarity correct, such as lower inventory versus higher yield, rather than using one generic “improvement” rule?
- Can the next update be performed from the tracking table without rereading the whole report?

## Delivery commands

```bash
python scripts/validate_report.py report.md --mode full --strict
```

Treat `quick_validate.py` as Skill-package validation only. It does not validate report truth, freshness, evidence coverage, or industrial relationships.
