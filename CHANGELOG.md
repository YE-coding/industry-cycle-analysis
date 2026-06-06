# Changelog

## v1.1.0 (2025-06-05)

### 新增功能

#### 时间同步规则 (Time Synchronization Rule)
- **原因**：行业数据具有时效性（季度报告、月度出货量、产能更新），过时的数据会导致周期阶段判断错误
- **实现**：每次调用技能时，自动查询当前系统时间并存储时间戳
- **影响范围**：
  - `industry-cycle-analysis/SKILL.md` - 英文版技能
  - `产析/SKILL.md` - 中文版技能
- **使用方式**：在报告中明确说明分析日期和数据时效

#### DeepSearch 研究协议
- **原因**：复杂行业分析需要系统化的子问题拆解和证据管理
- **新增文件**：`references/deepsearch-research-protocol.md`
- **功能**：定义搜索预算、证据矩阵、冲突信息合并规则

#### 日志提取工具
- **原因**：长日志和代理跟踪文件难以直接分析
- **新增文件**：`scripts/safe_log_extract.py`
- **功能**：安全提取日志中的关键信息（结果、错误、超时、证据、来源）

### 改进

#### 研究控制增强
- 每个子任务默认限制为3轮搜索
- 限制日志文件读取（仅最新80-120行）
- 压缩工具观察结果，避免上下文膨胀

#### 质量检查清单更新
- 添加时间戳验证步骤
- 增加数据时效性检查

#### 报告模板更新
- 添加分析时间戳字段
- 明确数据时效性说明

### 修复

- 清理重复的 `产析/产析/` 嵌套目录
- 统一中英文技能的版本号

---

## v1.0.0 (2025-06-05)

### 初始发布

#### 核心功能
- 产业供需周期分析框架
- 产业链图谱绘制
- 供需矛盾定位
- 周期阶段判断
- 资本市场预期映射

#### 文件结构
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

#### 调用方式
- `/产析 光通信` - 中文调用
- `/industry-cycle-analysis 光通信` - 英文调用
