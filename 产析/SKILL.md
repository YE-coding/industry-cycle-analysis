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

## 时间同步规则

**每次调用此技能时，你必须：**

1. 在分析开始时查询当前系统时间
2. 存储时间戳以供整个报告使用
3. 在所有日期引用和数据时效性检查中使用此时间戳

```bash
# 查询当前时间（在技能调用开始时运行）
date "+%Y-%m-%d %H:%M:%S %Z"
```

**为什么这很重要：**
- 行业数据具有时效性（季度报告、月度出货量、产能更新）
- 过时的数据会导致周期阶段判断错误
- 报告必须明确说明分析日期以供未来参考

**存储格式：**
```
分析时间戳：[YYYY-MM-DD HH:MM:SS]
数据时效：[覆盖的最新数据期间]
```

## 数据时效性验证规则

**关键：在将任何数据点用于报告之前，你必须验证它是：**

1. **实际/已发布数据** - 来自年报、季报、官方统计
2. **估算/预测数据** - 来自分析师预测、预测、前瞻性声明

### 如何验证：

1. **检查来源日期**：2025年报告的数据应标注为"2025年实际"，而不是"2025年预计"
2. **检查术语**：寻找"预计"、"预测"、"forecast"、"estimate"等关键词，这些表示预测
3. **检查数据期间**：如果当前日期是2026年6月，2025年的数据应该是实际数据，而不是估算

### 数据标注要求：

```markdown
# 正确标注：
- 2025年全球半导体市场实际规模约7,160-7,280亿美元（Source: Gartner/WSTS 2026年发布）
- 台积电2025年全年营收突破3万亿新台币（Source: 台积电年报 2026-02）

# 错误标注（不要使用）：
- 2025年全球半导体市场预计约6,970亿美元（Source: WSTS 2025）← 这是过时的预测
- 台积电2025年营收未确认 ← 现在应该已经确认了
```

### 何时将数据标记为不确定：

- 如果数据期间超过12个月且未更新
- 如果来源是尚未被实际结果验证的预测
- 如果多个来源冲突且都不是权威来源

### 正确的数据时效性检查示例：

```markdown
## 数据时效性表

| 数据点 | 状态 | 来源 | 日期 |
|--------|------|------|------|
| 2025年全球半导体市场规模 | 实际 | Gartner/WSTS | 2026-02 |
| 台积电2025年营收 | 实际 | 台积电年报 | 2026-02 |
| 2026年市场预测 | 估算 | WSTS | 2025-12 |
```

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
