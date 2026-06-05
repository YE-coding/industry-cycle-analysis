# Industry Cycle Analysis Skill

产业供需周期分析 Skill，用于分析行业、赛道或产业链的供需矛盾、产能周期、价格变化、资本开支、企业盈利、产业链传导和资本市场预期映射。

## 核心原则

```
不要用K线去理解世界。
先理解真实世界，再回来解读K线。
```

## 适用范围

适合分析：
- 半导体、光通信、AI算力
- 新能源、化工、钢铁
- 焦煤、铁矿石、机器人
- 数据中心、电力、液冷

等周期性或成长性行业。

**不适用于：**
- 单一公司分析（请用 `hv-analysis`）
- 短线荐股、技术分析、K线预测
- 直接投资建议

## 调用方式

```bash
# 中文调用
/产析 光通信

# 英文调用
/industry-cycle-analysis 光通信
```

## 分析框架

```
真实世界
-> 产业链
-> 供需矛盾
-> 产能扩张
-> 价格/订单/库存变化
-> 企业盈利
-> 市场预期
-> 股价映射
```

## 输出要求

每份完整分析报告应包含：

- [ ] 产业链图谱
- [ ] 核心供需矛盾
- [ ] 近两年相关数据（或说明数据缺口）
- [ ] 产能扩张时间表
- [ ] 价格/订单/库存证据
- [ ] 受益者与非受益者区分
- [ ] 周期阶段判断
- [ ] 资本市场预期阶段
- [ ] 月度跟踪指标

## 重要提醒

```
供需缺口 ≠ 股价上涨
产业方向正确 ≠ 时机正确
盈利兑现 ≠ 持续上涨
公开数据完整 ≠ 市场未定价
AI回答 ≠ 事实
```

## 文件结构

```
industry-cycle-analysis/
├── SKILL.md                    # 技能定义
├── references/
│   ├── framework.md            # 分析框架
│   ├── supply-demand-questions.md  # 供需问题清单
│   ├── cycle-stages.md         # 周期阶段定义
│   ├── capital-market-mapping.md   # 资本市场映射
│   ├── report-template.md      # 报告模板
│   ├── source-priority.md      # 数据来源优先级
│   └── quality-checklist.md    # 质量检查清单
├── scripts/
│   └── md_to_pdf.py           # PDF导出脚本
└── agents/
    └── openai.yaml            # OpenAI配置

产析/                           # 中文别名（内容相同）
└── ...
```

## 安装

1. 克隆此仓库
2. 将 `industry-cycle-analysis` 和 `产析` 文件夹复制到 `~/.claude/skills/` 目录
3. 重启 Claude Code

## 许可证

MIT License
