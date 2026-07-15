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
- Observation posts lack a specific source, baseline, direction, and numeric or event threshold.
- Qualification, pilot line, announced capacity, installed capacity, and volume production are conflated.

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
- Is indicator polarity correct, such as lower inventory versus higher yield, rather than using one generic “improvement” rule?
- Can the next update be performed from the tracking table without rereading the whole report?

## Delivery commands

```bash
python scripts/validate_report.py report.md --mode full --strict
```

Treat `quick_validate.py` as Skill-package validation only. It does not validate report truth, freshness, evidence coverage, or industrial relationships.
