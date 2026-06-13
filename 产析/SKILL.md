---
name: 产析
description: 产析skill，industry-cycle-analysis 的中文可调用别名。用于研究一个行业、赛道或产业链的供需矛盾、产能周期、价格变化、资本开支、企业盈利、产业链传导和资本市场预期映射。适合分析半导体、光通信、AI算力、新能源、化工、钢铁、焦煤、铁矿石、机器人、数据中心、电力、液冷等周期性或成长性行业。不要用于短线荐股、技术分析、K线预测或直接给投资建议。
argument-hint: [industry-or-sector]
version: 1.2.0
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

## 时间同步规则（必须首先执行）

**每次调用此技能时，你必须：**

1. 在分析开始时查询当前系统时间
2. 存储时间戳以供整个报告使用
3. 在所有日期引用和数据时效性检查中使用此时间戳

```bash
# 查询当前时间（在技能调用开始时运行）
date "+%Y-%m-%d %H:%M:%S %Z"
```

**根据当前时间确定数据搜集范围：**

| 当前月份 | 必须搜集的最新数据 | 数据状态 |
|---------|-------------------|---------|
| 1-3月 | 上年Q4、上年全年 | 实际数据（年报已发布） |
| 4-6月 | 当年Q1、上年全年 | 实际数据（Q1季报已发布） |
| 7-9月 | 当年Q2、当年Q1 | 实际数据 |
| 10-12月 | 当年Q3、当年Q2 | 实际数据 |

**示例：**
- 如果当前是2026年6月 → 必须搜集2026年Q1数据（4-5月已发布）
- 如果当前是2026年6月 → 必须搜集2025年全年数据（1-3月已发布）
- **禁止**使用超过6个月的"预测"数据而不搜集最新实际数据

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

1. **检查来源日期**：如果当前是2026年6月，2025年的数据必须标注为"2025年实际"，而不是"2025年预计"
2. **检查术语**：寻找"预计"、"预测"、"forecast"、"estimate"等关键词，这些表示预测
3. **检查数据期间**：如果当前日期是2026年6月，2025年的数据应该是实际数据，2026年Q1的数据也应该是实际数据

### 数据标注要求：

```markdown
# 正确标注（使用实际数据）：
- 2025年全球半导体市场实际规模约7,160亿美元（Source: Gartner 2026-02）
- 台积电2026年Q1营收255亿美元（Source: 台积电季报 2026-04）

# 错误标注（禁止使用）：
- 2025年全球半导体市场预计约6,970亿美元（Source: WSTS 2025）← 过时预测
- 2026年Q1数据待发布 ← 现在应该已发布
```

### 数据时效性检查表（每次分析必须填写）：

```markdown
## 数据时效性表

| 数据点 | 状态 | 来源 | 发布日期 | 是否最新 |
|--------|------|------|---------|---------|
| [行业]2025年市场规模 | 实际/预测 | [来源] | [日期] | ✓/✗ |
| [公司]2025年全年营收 | 实际/预测 | [来源] | [日期] | ✓/✗ |
| [公司]2026年Q1营收 | 实际/预测 | [来源] | [日期] | ✓/✗ |
```

**如果发现数据不是最新的，必须立即搜索补充！**

## Workflow

### Step 1: 定义行业边界和产业链

- 识别上游、中游、下游、终端需求和替代品
- 绘制自上而下和自下而上的产业链
- 如果产业链或分析框架不清晰，加载 `references/framework.md`

### Step 2: 搜集最新数据（强制执行）

**在定义完产业链后，必须立即搜集以下数据：**

1. **行业整体数据**
   - 最近2年的市场规模、增长率
   - 月度/季度数据（如可用）

2. **关键公司数据**
   - 最新财报（年报/季报）
   - 营收、利润率、出货量

3. **供需信号**
   - 最新价格走势
   - 产能利用率
   - 订单/库存情况

**数据搜集工具：**
```bash
# 搜索行业整体数据
WebSearch: "[行业名] 市场规模 2025 2026"

# 搜索公司财报
WebSearch: "[公司名] 2026年Q1 财报 营收"

# 搜索供需数据
WebSearch: "[产品名] 价格 产能 供需 2026"
```

### Step 3: 找到需求驱动因素

- 识别需求来自实际终端使用、政策、替换、库存回补、资本支出还是投机预期
- 区分当前需求和预期未来需求

### Step 4: 找到供应约束

- 识别产能、良率、设备交期、原材料、人才、专利、监管、电力、土地、物流或客户认证约束
- 对于半导体和光通信，重点关注良率、节点/工艺、封装、光芯片、模块、晶圆产能、代工产能和数据中心资本支出

### Step 5: 定位供需矛盾

- 使用 `references/supply-demand-questions.md`
- 询问短缺或过剩发生在何处、持续多久、谁可以扩产、能扩产多少、新产能何时进入市场

### Step 6: 审查过去两年的行业数据

- 尽可能优先使用月度或季度数据
- 使用 `references/source-priority.md` 对数据源质量进行排序
- 如果数据缺失，说明缺失。不要编造精确数字

### Step 7: 合并冲突证据

- 优先使用原始披露而非媒体摘要
- 保留冲突数据，注明来源、日期、地区和数据定义
- 如果两个来源冲突且都不是权威来源，将结论标记为未解决

### Step 8: 判断周期阶段

- 使用 `references/cycle-stages.md`
- 区分导入期、增长期、短缺期、扩张期、盈利兑现期、供过于求期和出清期

### Step 9: 映射到资本市场预期

- 使用 `references/capital-market-mapping.md`
- 始终将产业现实与市场定价分开
- 明确询问股市是在交易预期开始、预期扩散、盈利兑现、估值消化还是预期反转

### Step 10: 生成报告

- 使用 `references/report-template.md`
- 将结论分为事实、推断和假设
- 包含用于未来月度更新的跟踪表

### Step 11: 验证

- 使用 `references/quality-checklist.md`
- 如果创建PDF，使用 `scripts/md_to_pdf.py`

### Step 12: 清理临时文件（必须执行）

**在报告完成后，必须删除所有为获取数据而下载的临时文件：**

```bash
# 删除下载的数据文件（如xlsx、csv、pdf等）
rm -f [工作目录]/*.xlsx
rm -f [工作目录]/*.csv
rm -f [工作目录]/*.pdf
rm -f [工作目录]/*.json
```

**为什么重要：**
- 避免临时文件堆积占用磁盘空间
- 防止敏感数据泄露
- 保持工作目录整洁
- 避免版本混乱（旧数据文件可能干扰后续分析）

## Output Requirements

Every serious analysis should include:

- **分析时间戳和数据时效声明**（必须放在报告开头）
- industry-chain map
- key supply-demand conflict
- past two years of relevant data or a note explaining data gaps
- capacity expansion timeline
- price/order/inventory evidence
- beneficiary and non-beneficiary distinction
- cycle-stage judgment
- capital-market expectation stage
- evidence matrix with source quality and unresolved gaps
- follow-up indicators to track monthly
- **数据时效性表**（必须包含）

Keep these warnings visible:

```text
supply-demand gap != stock price rise
correct industry direction != correct timing
earnings realization != continued stock rise
complete public data != market has not priced it
AI answer != fact
过时数据 != 当前事实
```

## Optional PDF Export

After writing the final Markdown report, run:

```bash
python scripts/md_to_pdf.py report.md report.pdf
```

If local PDF dependencies are missing, leave the Markdown report as the primary deliverable and explain what dependency is missing.
