from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_corpus import audit  # noqa: E402
from validate_report import validate  # noqa: E402


def valid_report(timestamp: datetime | None = None) -> str:
    timestamp = timestamp or datetime.now(timezone(timedelta(hours=8)))
    nodes = []
    for index, name in enumerate(("矿物提纯", "核心部件", "整机集成", "终端运营"), start=1):
        nodes.append(
            f"""#### 1.2.{index} {name}

**它是干什么的**：节点{index}把特定物料和工艺转成可验收产品，决定下游能否按计划投产并持续运行。

**向谁采购**：节点{index}向专业材料商、关键设备制造商和能源服务机构采购不同投入品。

**卖给谁**：节点{index}向下一制造环节、系统集成商以及具备明确预算的终端运营者销售。

**代表企业**：

| 企业/机构 | 上市地/代码或属性 | 角色 | 代表性依据 | 证据 |
|---|---|---|---|---|
| 节点{index}甲公司 | 上交所 / 60000{index} | 主要供应商 | 已披露产品收入和客户结构 | E{index} |
| 节点{index}乙机构 | 未上市/机构 | 行业运营者 | 发布持续运营及招标数据 | E{index + 4} |

**怎么赚钱、议价能力**：节点{index}依靠合格产能利用率、良率和服务附加值取得毛利；只有认证稀缺时才有提价能力。

**为什么会卡住**：节点{index}受认证周期、熟练人员和专用设备交付约束，名义产能不能直接等同有效供给。

**进阶视角**：节点{index}的领先指标不是规划产能，而是认证通过后连续交付与单位利润同步改善；若只有订单没有良率，利润不会兑现（E{index}、E{index + 4}）。
"""
        )

    ledger_rows = []
    publishers = ("国家统计局", "行业协会", "甲公司年报", "交易所", "能源署", "海关", "乙机构", "研究院")
    for index, publisher in enumerate(publishers, start=1):
        ledger_rows.append(
            f"| E{index} | {publisher} | 指标或披露 {index} | https://example.com/source-{index} | 第{index}页 | 2026-07-18 | yes | 当前 | 口径仅覆盖样本{index} |"
        )

    return f"""# 示例行业供需周期分析

分析日期：{timestamp.isoformat(timespec="seconds")}
地理范围：全球，并对中国市场单列说明
数据时效：截至分析日期已经正式发布的原始资料
行业边界：从上游原料到终端运营，不包含纯金融交易

## 0. 一页看懂

### 这个行业是做什么的
该行业把稀缺物料转成终端可以持续使用的工业系统，收入由真实交付和运行服务共同形成。

### 三个最重要的数字
1. 2025 年有效供给为 120 单位（E1）。
2. 2025 年真实需求为 116 单位（E2）。
3. 2026 年已公告但未认证产能为 30 单位（E3）。

结论状态：可发布

## 1. 产业链地图

```mermaid
flowchart LR
  A[矿物提纯] --> B[核心部件] --> C[整机集成] --> D[终端运营]
```

### 1.1 钱和订单怎么走
终端运营者依据实际使用量付款，整机集成商再用验收回款覆盖部件和原料采购。

{''.join(nodes)}

### 1.3 权力与利润传导

| 环节 | 谁最终付款 | 利润来源 | 当前约束 |
|---|---|---|---|
| 矿物提纯 | 部件厂 | 提纯费与收率 | 环保许可 |
| 核心部件 | 集成商 | 良率与认证溢价 | 专用设备 |
| 整机集成 | 运营商 | 系统毛利 | 验收周期 |
| 终端运营 | 使用客户 | 运行服务费 | 上电进度 |

## 2. 需求

需求由存量替换、终端新增利用量和安全冗余共同推动，不能把意向订单直接计入已经发生的采购（E2）。

**进阶视角**：当使用量增速高于预算增速时，运营者会先消化闲置资源；预算、招标和验收连续出现才能确认需求进入兑现阶段（E2、E5）。

## 3. 供给

供给必须区分公告、开工、安装、认证与稳定良率，只有最后两项才能形成短期有效产能（E1、E3）。

**进阶视角**：新增厂房只改变远期供给上限，认证和良率爬坡决定当期交付；设备到位而人员不足仍会造成供给延迟（E1、E3）。

## 4. 供需矛盾与高频信号

| 信号 | 当前读数 | 解释 | 证据 |
|---|---|---|---|
| 终端使用量 | 同比增加 12% | 使用量快于存量释放，需求真实改善 | E2 |
| 订单覆盖 | 1.4 倍 | 可见度增加但仍需观察取消率 | E3 |
| 交付周期 | 18 周 | 认证资源紧张形成排队 | E4 |
| 单位利润 | 同比增加 8% | 供需改善开始进入利润表 | E5 |
| 在制库存 | 环比下降 4% | 交付快于投料，尚未形成积压 | E6 |

## 5. 周期位置与传导

| 时段 | 需求 | 有效供给 | 价格利润 | 阶段 |
|---|---|---|---|---|
| 2024H2 | 温和增加 | 相对充足 | 价格承压 | 去库存 |
| 2025H1 | 利用量加速 | 认证偏慢 | 利润企稳 | 修复 |
| 2025H2 | 订单兑现 | 部分受限 | 利润扩张 | 上行确认 |

**进阶视角**：与上轮只靠补库存不同，本轮需要终端使用量和认证交付共同成立；利润先于大规模扩产改善才是有效收紧（E5、E6）。

什么会证明这个判断错了：终端使用量连续下降，同时新增认证产能提前释放并造成库存回升。

## 6. 资金动向

| 尝试的来源类型 | 结果 | 已定价 | 未定价 | 证据 |
|---|---|---|---|---|
| 交易所公告 | 已打开 | 订单增长 | 取消风险 | E4 |
| 公司年报 | 已打开 | 当前利润 | 新线良率 | E3 |
| 行业统计 | 已打开 | 使用量增长 | 区域错配 | E2 |

产业现实是利润先在认证稀缺的部件端改善，估值反应是否充分需要与可比公司的订单兑现交叉验证。

## 7. 未来资金可能流向

- 基准：认证按计划完成，利润由核心部件向集成环节扩散。
- 上行：终端使用超预期且设备交付延后，稀缺环节获得更高议价权。
- 下行：新增产能集中认证，价格和库存同时转弱。

以上情景不构成任何买卖建议。

## 8. 分歧与反证

主流叙事强调规划产能足够；本报告认为短期有效供给取决于认证、人员和良率，二者应由交付周期验证。

## 9. 观察哨与跟踪

| 指标 | 基线 | 来源 | 频率 | 正向触发 | 反证触发 |
|---|---|---|---|---|---|
| 终端使用量 | 2025 年 116 单位 | 行业协会 | 月度 | 三个月同比加速 | 三个月同比转负 |
| 认证产能 | 2025 年 120 单位 | 公司公告 | 季度 | 增速低于需求 | 集中提前释放 |
| 交付周期 | 2025 年末 18 周 | 交易所问询 | 季度 | 延长且利润改善 | 缩短且库存上升 |
| 单位利润 | 2025 年 8 元 | 公司年报 | 季度 | 连续两个季度上升 | 连续两个季度下降 |
| 在制库存 | 2025 年 32 单位 | 统计机构 | 月度 | 下降且交付增加 | 上升且订单减少 |

### 9.1 可比时间序列

| 指标 | 时点 | 数值 | 单位 | 证据 |
|---|---|---:|---|---|
| 终端使用量 | 2024 | 104 | 单位 | E2 |
| 终端使用量 | 2025 | 116 | 单位 | E2 |

## 10. 术语表

| 术语 | 解释 |
|---|---|
| 有效产能 | 已认证并能以稳定良率交付的产能 |
| 在制库存 | 已投料但尚未完成验收的产品 |
| 订单覆盖 | 在手订单相对当前收入的倍数 |

## 附录A 证据台账

| 证据ID | 发布方 | 材料 | URL | 定位 | 访问日期 | 已打开 | 时效 | 局限 |
|---|---|---|---|---|---|---|---|---|
{chr(10).join(ledger_rows)}

## 附录B 数据时效与证据覆盖

所有数字均使用分析时点已经发布的资料；计划值与实际值分别标注，缺口不以预测值填补。

## 附录C 证据就绪度与研究执行记录

| 证据泳道 | 状态 | 已打开 | 最低要求 | 证据 |
|---|---|---:|---:|---|
| 产业链 | Ready | 3 | 2 | E1、E3、E4 |
| 需求 | Ready | 2 | 2 | E2、E5 |
| 供给与有效产能 | Ready | 2 | 2 | E1、E3 |
| 价格/订单/库存/利润 | Ready | 3 | 2 | E4、E5、E6 |
| 资本市场预期 | Ready | 2 | 2 | E7、E8 |
"""


class ValidateReportTests(unittest.TestCase):
    def assert_has_error(self, report: str, needle: str) -> None:
        errors, _ = validate(report, "full", True)
        self.assertTrue(any(needle in item for item in errors), errors)

    def test_complete_report_passes(self) -> None:
        errors, warnings = validate(valid_report(), "full", True)
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_combined_upstream_downstream_is_rejected(self) -> None:
        report = valid_report().replace(
            "**向谁采购**：节点1向专业材料商、关键设备制造商和能源服务机构采购不同投入品。\n\n**卖给谁**：节点1向下一制造环节、系统集成商以及具备明确预算的终端运营者销售。",
            "**上游买什么 / 下游卖给谁**：向材料商采购，并向系统集成商销售。",
        )
        self.assert_has_error(report, "combined upstream/downstream")

    def test_missing_field_is_rejected(self) -> None:
        report = valid_report().replace(
            "**为什么会卡住**：节点2受认证周期、熟练人员和专用设备交付约束，名义产能不能直接等同有效供给。\n\n",
            "",
        )
        self.assert_has_error(report, "node '核心部件' missing structured field: bottleneck")

    def test_duplicate_fields_are_rejected(self) -> None:
        shared = "节点3向专业材料商、关键设备制造商和能源服务机构采购不同投入品。"
        report = valid_report().replace(
            "节点3向下一制造环节、系统集成商以及具备明确预算的终端运营者销售。",
            shared,
        )
        self.assert_has_error(report, "repeats the same content")

    def test_future_timestamp_is_rejected(self) -> None:
        report = valid_report(datetime.now(timezone.utc) + timedelta(days=1))
        self.assert_has_error(report, "timestamp is in the future")

    def test_company_coverage_is_rejected(self) -> None:
        report = valid_report().replace(
            "| 节点4乙机构 | 未上市/机构 | 行业运营者 | 发布持续运营及招标数据 | E8 |\n",
            "",
        )
        self.assert_has_error(report, "fewer than 2 representative companies")

    def test_cross_report_prose_reuse_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "01_first.md"
            second = root / "02_second.md"
            first.write_text(valid_report(), encoding="utf-8")
            second.write_text(valid_report(), encoding="utf-8")
            errors, _, _ = audit([first, second], first, True)
        self.assertTrue(any("cross-report repeated prose" in item for item in errors), errors)


if __name__ == "__main__":
    unittest.main()
