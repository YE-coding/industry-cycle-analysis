# Industry Cycle Analysis

产业供需周期分析 Skill。它从真实需求、预算与订单出发，核验有效供给、价格、库存、利润和资本开支，再判断产业周期及市场预期阶段。

> 先理解真实世界，再解释市场预期。证据不足时必须保留缺口，不能用模板化措辞代替事实。

## 适用范围

适合半导体、AI 算力、光通信、新能源、化工、钢铁、资源品、机器人、数据中心、电力、液冷等周期性或成长性行业。

不适用于：

- 短线荐股、K 线预测或目标价；
- 缺少产业链和供需证据的单点结论；
- 把规划、指引或预测当成已经实现的产能与收入。

## 核心能力

- 产业边界、环节、关系边和代表性公司映射；
- 需求来源、付款方、预算、订单和需求持续性核验；
- 名义产能与有效供给、认证、良率和交付瓶颈区分；
- 价格、订单、库存、利润与资本开支传导；
- 周期阶段、反证条件和市场预期映射；
- 证据台账、数据时效检查和严格报告校验；
- 逐节点六字段质量契约与跨报告语料审计；
- 真实时间序列可比性检查，避免把不同口径数据拼成趋势。
- 阶段判断、结论状态、置信度与证据截至时间分离，避免把“扩张”与“暂定”误画成矛盾。
- 行业、子链和代表公司三级市场代理，披露覆盖边界而不是要求单一 ETF 代表全产业链。
- 4–6 个行业事件锚点的时间线，以及未来资金情景六字段完整性检查。

## 使用方式

安装后可以直接提出：

```text
用 industry-cycle-analysis 分析半导体产业周期
用产析 skill 分析光通信的需求、有效供给和利润传导
```

中文触发词已经写入同一个 `SKILL.md`。仓库不再维护内容重复的 `产析/` 副本，以免两个版本发生漂移。

## 安装

将本仓库克隆到对应客户端的 Skills 目录：

```bash
# Claude Code
git clone https://github.com/YE-coding/industry-cycle-analysis.git ~/.claude/skills/industry-cycle-analysis

# Codex
git clone https://github.com/YE-coding/industry-cycle-analysis.git ~/.codex/skills/industry-cycle-analysis
```

如果目标目录已经存在，请在该目录中执行 `git pull`，不要再次嵌套克隆。

## 报告校验

生成报告后可以运行：

```bash
python scripts/validate_report.py path/to/report.md --mode full --strict
```

快速扫描报告可将 `--mode full` 改为 `--mode quick`。严格校验失败表示报告仍有结构、证据、时效或可比性缺口，不应把它当作完整结论发布。

批量报告在逐篇校验后，还必须运行语料级审计：

```bash
python scripts/validate_corpus.py path/to/reports --pattern "??_*.md" \
  --benchmark path/to/reports/01_半导体行业供需周期分析.md --strict
```

语料审计会检查跨报告重复句、节点平均信息量、公司覆盖、证据发布者与 URL 多样性，并量化相对基准报告的结构差距。完整报告至少有 4 个关键节点；每个节点必须独立填写“它是干什么的、向谁采购、卖给谁、怎么赚钱、为什么会卡住、进阶视角”，并列出至少 2 个可核验主体。

## 文件结构

```text
industry-cycle-analysis/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── capital-market-mapping.md
│   ├── cycle-stages.md
│   ├── deepsearch-research-protocol.md
│   ├── evidence-ledger.md
│   ├── framework.md
│   ├── quality-checklist.md
│   ├── report-template.md
│   ├── search-routing.md
│   ├── source-priority.md
│   └── supply-demand-questions.md
└── scripts/
    ├── md_to_pdf.py
    ├── safe_log_extract.py
    ├── validate_corpus.py
    └── validate_report.py
```

## 版本与历史

- `main` 是唯一维护分支和默认分支；
- `v1.3.0` 标签保留旧双目录版本；
- `v1.4.0` 起使用根目录单一 Skill 包；
- `v1.5.0` 起启用逐节点质量契约和语料级审计；
- `v1.6.0` 起启用系统性证据覆盖评分、分层市场代理和阶段状态分离；
- 版本变化见 [CHANGELOG.md](CHANGELOG.md)。
