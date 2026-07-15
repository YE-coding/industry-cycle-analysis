# Report Template

Use this template for full research. Keep gaps explicit; delete unused optional rows rather than filling them with generic prose.

````markdown
# [行业]行业供需周期分析

分析日期：[YYYY-MM-DD HH:mm:ss timezone]
地理范围：[范围]
数据时效：[latest full-period actuals; partial actuals; forecasts]
行业边界：[included and excluded scope]
研究模式：完整深研

## 0. 结论与证据就绪度

一句话判断：[cycle hypothesis + core conflict + biggest evidence gap]

- 结论状态：[可发布 / 暂定 / 阶段待验证]
- 置信度：[高 / 中 / 低]
- 最大缺口：[gap]

| Evidence Lane | Status | Opened Reliable Sources | Required | Gap / Limitation |
|---|---|---:|---:|---|
| Industry chain | Ready / Gap |  | 2 |  |
| Demand | Ready / Gap |  | 3 |  |
| Supply and effective capacity | Ready / Gap |  | 3 |  |
| Price/order/inventory/margin | Ready / Gap |  | 3 or explicit gap |  |
| Capital-market expectations | Ready / Gap |  | 2 or explicit gap |  |

Facts:

- [claim ID + sourced fact]

Inferences:

- [inference derived from claim IDs]

Assumptions:

- [assumption and falsifier]

## 1. 数据时效与证据覆盖

| Metric | Period | Status | Release Date | Access Date | Freshness | Source | Locator | Limitation |
|---|---|---|---|---|---|---|---|---|
|  |  | Actual / Partial actual / Guidance / Forecast |  |  | current / superseded / unchecked |  | page/table/section |  |

Release-status notes:

- [what has been released]
- [what has not yet been released]
- [which newer source superseded an older one]

## 2. 产业链与关系

### 2.1 Physical / Production Flow

```text
[show parallel inputs explicitly]
```

| From | Relation | To | Evidence IDs | Notes |
|---|---|---|---|---|
|  | material input / equipment input / production / purchase / service |  |  |  |

### 2.2 Order and Budget Flow

```text
[end use] -> [budget owner] -> [system/product orders] -> [component/process orders] -> [capacity and equipment orders]
```

### 2.3 Chain Node Explanation

| Node | What It Is / Does | Suppliers | Buyers | Representative Companies | Monetization | Bottleneck Role | Evidence IDs |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

### 2.4 Power and Profit Map

| Question | Answer | Evidence IDs | Gap |
|---|---|---|---|
| Who pays? |  |  |  |
| Who captures gross profit? |  |  |  |
| Who bears capex and inventory risk? |  |  |  |
| Who has pricing power? |  |  |  |
| Who is important but cannot monetize well? |  |  |  |

## 3. 需求

Facts:

- [claim ID + metric, period, geography and source]

Demand segmentation:

| End Use | Buyer / Budget Owner | Trigger | Current or Expected | Observable Indicator | Evidence IDs |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Inferences and assumptions:

- [inference]
- [assumption + falsifier]

## 4. 供给

| Node / Project | Announced Capacity | Installed | Qualified / Yield-Ramped | Customer-Backed | Release Window | Evidence IDs | Gap |
|---|---:|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |

Facts:

- [capacity, yield, qualification, lead-time or capex fact]

Inferences and assumptions:

- [inference]
- [assumption + falsifier]

## 5. 供需矛盾与高频信号

Core conflict:

- What is short or excessive?
- At which node and under which definition?
- How long can it persist?
- Who can solve it, and when does qualified capacity arrive?

| Signal | Latest Value / Direction | Period | Evidence IDs | Interpretation | Gap |
|---|---|---|---|---|---|
| Price |  |  |  |  |  |
| Orders |  |  |  |  |  |
| Inventory |  |  |  |  |  |
| Utilization / Yield |  |  |  |  |  |
| Margin / Cash Flow |  |  |  |  |  |

If a comparable public series does not exist, write an evidence gap, why it is unavailable, and the exact source to monitor next.

## 6. 周期与利润/订单传导

```text
[demand/budget]
-> [orders]
-> [revenue recognition]
-> [bottleneck margin]
-> [capex]
-> [qualified capacity]
-> [price/margin reversal or continued shortage]
```

| Stage / Date | Signal | Profit Pool Shift | Key Lag | Evidence IDs | Next Verification |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Current stage:

- Phase: [stage or stage pending verification]
- Entry date / anchor: [date]
- Expected transition: [conditional trigger, not a generic time range]
- Confidence: [high / medium / low]
- What would prove this wrong: [measurable condition]

## 7. 资本市场预期

Keep market-pricing evidence separate from industry evidence.

| Industry Reality | Market Narrative / Pricing Evidence | Source | Interpretation | Gap |
|---|---|---|---|---|
|  |  |  |  |  |

If no market evidence was collected, write `Evidence gap: capital-market expectation mapping not researched` and keep the industrial conclusion provisional for this section.

## 8. 情景与反证

| Scenario | Trigger Conditions | Evidence to Watch | Probability / Confidence | Consequence for Cycle Judgment |
|---|---|---|---|---|
| Base |  |  |  |  |
| Upside |  |  |  |  |
| Downside |  |  |  |  |

Conflicting evidence:

| Topic | Supporting Evidence IDs | Disconfirming Evidence IDs | Definition Difference | Handling |
|---|---|---|---|---|
|  |  |  |  | resolved / unresolved |

## 9. 观察哨与跟踪

| Indicator | Baseline | Source | Frequency | Positive Trigger | Disconfirming Trigger | Meaning |
|---|---|---|---|---|---|---|
|  |  | [specific source or URL] | monthly / quarterly / event | [numeric or event threshold] | [numeric or event threshold] |  |

Tracking database:

| Date | Indicator | Node | Value | YoY/QoQ | Direction | Source | Impact on Judgment | Note |
|---|---|---|---:|---:|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## 10. 证据台账

| Claim ID | Claim | Type | Source | Publisher | Published | Accessed | Period | Geography / Unit | Locator | Opened | Freshness | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 |  | Fact / Guidance / Forecast / Inference |  |  |  |  |  |  | page/table/section | yes / no | current / superseded / unchecked |  |

## 11. 研究执行记录

Populate this only from the actual run.

| Subtask | Search Rounds | Route Actually Used | Evidence IDs | Status | Gap / Fallback |
|---|---:|---|---|---|---|
|  |  |  |  | complete / gap |  |

## 12. Final Notes

- Supply-demand gap does not equal stock-price rise.
- Correct direction does not equal correct timing.
- Earnings realization does not equal continued stock rise.
- AI answers and search snippets are not facts.
- Stale data is not a current fact.
````
