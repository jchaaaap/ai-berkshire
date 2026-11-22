---
name: company-valuation
description: "AI Berkshire skill: 公司估值：内在价值与估值复核. Source: skills/company-valuation.md."
---

## Codex adapter note

This skill is generated from `skills/company-valuation.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# 公司估值：内在价值与估值复核

对 $ARGUMENTS 做一次可复算的内在价值估算与估值复核。

**支持输入格式**：`公司名`、`公司名 股票代码`，或附带已有报告路径做复核，例如：`腾讯`、`Mastercard MA`、`复核 reports/腾讯/腾讯-research-20261027.md`

> "价格是你付出的，价值是你得到的。" —— 巴菲特
>
> "宁要模糊的正确，也不要精确的错误。" —— 巴菲特
>
> "反过来想，总是反过来想。" —— 芒格

## 设计理念

估值最常见的错误不在算术，而在三处：把不属于股东的现金算给股东；把同一个风险扣两次（既抬折现率又压现金流）；用一个精确到小数点的数字掩盖一组主观假设。

本Skill的分工：
- **现金流估值（DCF）**回答"按我的假设值多少"；
- **反向估值**回答"今天的价格要求什么"——这一步比正向估值更重要，因为它不依赖分析师的乐观程度；
- **分部估值（SOTP）**只用于确实可拆的业务和资产，不用来凑数；
- **敏感性与情景**说明结论在多大范围内成立。

所有数字必须能复算：每个输入有来源，每一步算术走工具，模型脚本与报告一同保存。

## 执行流程

### 第零步：确认日期与口径

1. 运行 `date` 确认今天日期，报告头写明**研究日**和**行情日**（收盘价日期）。
2. 确定**现金流币种**、**报告币种**、**股价币种**。三者不同时（如港股腾讯：人民币报表、港币股价），列出所用汇率、日期和来源。
3. 确定股本口径：总股本、流通股本、经济股数（扣库存股，加未行权期权/RSU/可转债的稀释）。写明取哪一个、为什么。

### 第一步：收集输入（至少两个来源交叉验证）

使用 Task 工具**并行**获取：

| 类别 | 内容 | 首选来源 |
|---|---|---|
| 行情 | 股价、总股本、市值 | 交易所/公司公告 + 行情网站 |
| 报表 | 近5年收入、经营利润、净利润、经营现金流、资本开支、SBC、租赁支出 | 年报/10-K/20-F、季报 |
| 资产负债 | 现金、短投、有息负债、租赁负债、少数股东权益、投资资产 | 最近一期资产负债表及附注 |
| 股东回报 | 分红、回购、股本变动 | 年报、回购公告 |
| 利率 | 对应币种10年期国债收益率 | 央行/财政部/中债 |

市值必须手算校验，用工具，不要心算：

```bash
python3 tools/financial_rigor.py verify-market-cap --price {股价} --shares {总股本} --reported {报告市值} --currency {币种}
python3 tools/financial_rigor.py cross-validate --field {字段} --values '{"来源A": x, "来源B": y}' --unit {单位}
```

偏差超过2%的数据不得直接使用，先查清口径差异（期间、币种、是否含少数股东、是否 GAAP/Non-GAAP）。

### 第二步：现金流口径——股东到底拿到多少

从**经营利润**出发，不从调整后净利润出发：

```
股东自由现金流 ≈ 经营利润 ×（1 − 现金税率）− 净再投资（资本开支 − 折旧摊销 + 营运资金变化）
               − SBC 经济成本 − 少数股东份额
```

逐项判断并写明理由：
- **SBC**：一律视为真实成本。Non-GAAP 加回的 SBC 要扣回去，或在股数里体现稀释，二选一，不能两边都不算。
- **租赁**：若经营现金流已加回租赁本金，要把租金当作经营成本扣回。
- **预收/递延收入**：一次性的营运资金流入不能外推成永续现金流。
- **投资资产**：上市部分按市值并打折（流动性、税、控制权），未上市部分按最近一轮估值再打折，写明折扣率。被投公司的利润若已通过权益法计入利润，就不能再把投资资产加一遍。
- **"维持性"与"增长性"资本开支**：若无法拆分，诚实写"无法拆分"，按总额扣除。

反面检查：近5年累计股东自由现金流 vs 近5年累计净利润。若前者显著低于后者，必须解释差异去了哪里。

### 第三步：现金流估值（DCF）

**结构**：显式期（通常10年）+ 终值。悲观/基准/乐观三档改变的是**经营路径**（收入、利润率、再投资），不只是换终值倍数。

**折现率 r**：与现金流同币种。参考区间（与 `terminal_value.py` 内置约束一致）：
- 人民币：6%–9%
- 美元/港币：9%–11.5%

推导写明：无风险利率 + 股权风险补偿 × 风险暴露。风险暴露偏离1.0要给理由。**离散风险**（退市、VIE失效、制裁、监管重击、技术替代）只能放进情景或尾部档，不能放进 r。

**终值**：只用永续增长模型，不用同业倍数类比：

```
终值PE = (1 − g/ROIC) / (r − g)
```

- g：人民币不超过2%，美元不超过4%；g 不随 r 变。
- ROIC：稳态增量回报，介于存量 ROIC 和由派息率反推的隐含值之间。
- 每档 r − g 至少5个百分点，否则估值主要在放大假设，不是在估值。

先过准出检查，通过后才出数：

```bash
python3 tools/terminal_value.py audit --currency {币种} --r {r} --roic {ROIC} --g {悲},{基},{乐} --rf {无风险利率} \
  --beta 1.0 --discrete-risks "{风险}:{情景|尾部档|概率|未建模},..."
python3 tools/terminal_value.py pe --roic {ROIC} --g {g} --r {r}
```

**模型脚本**：显式期逐年现金流用 Python 标准库 `decimal.Decimal` 写成 `model.py`，与报告放在同一目录，输入集中在脚本顶部或 `model_inputs.json`。关键中间结果（第1、3、10年现金流，终值，终值现值占比）再用工具独立验算一次：

```bash
python3 tools/financial_rigor.py calc --expr '{第3年收入} * {利润率} * (1 - {税率}) - {净再投资}'
```

报告必须写出**终值现值占企业价值的比例**。超过70%时明确提示：结论主要取决于十年后的假设。

### 第四步：股权桥——从企业价值到每股价值

```
每股价值 = (经营价值 + 现金及短投 + 投资资产(打折后) − 有息负债 − 租赁负债 − 少数股东权益 − 其他债务性义务) / 经济股数
```

逐项列表，每项写来源和期间。注意：
- 境外现金若汇回有税或受限，打折并写明；
- 运营必需的现金（支付平台备付金、保险浮存金等）不能算作可分配现金；
- 有可转债/期权/RSU 时，用经济股数，不用总股本。

### 第五步：分部估值（SOTP，仅在适用时）

适用条件：业务之间资本、客户、成本基本独立，且至少一块有可观察的市场定价。否则跳过并写"不适用"。

每个分部单独估值，然后：
- 扣除总部成本的资本化值（总部成本不会因为拆分消失）；
- 未上市分部按融资估值时，区分**投后估值**和母公司**实际可得权益**，扣除优先清算权和持续亏损需要的追加投入；
- 汇总后与第三步整体 DCF 对比，差异超过20%要解释原因。

### 第六步：反向估值——今天的价格要求什么

固定 r 与终值假设，反解当前市值隐含的：
- 十年收入复合增速，或
- 稳态利润率，或
- 十年末利润。

再算如果十年后估值回到终值PE，今天买入的十年回报：

```bash
python3 tools/terminal_value.py irr --profit {第10年利润} --mcap {今日市值} --pe {退出PE} --years 10 --payout {股息率-稀释率}
```

把隐含要求与公司历史表现、行业天花板放在同一张表里对比，结论用"市场要求 X，历史做到 Y"的格式，不用"便宜/贵"的形容词。

### 第七步：敏感性与压力测试

1. **九格表**：r（±1pp）× g（±1pp）或 r × 关键经营变量，输出每股价值。
2. **结论是否翻转**：

```bash
python3 tools/terminal_value.py flip --name {公司} --r {r} --delta 0.02 --currency {币种} --rf {无风险利率} \
  --roic {ROIC} --g {悲},{基},{乐} --p {悲},{基},{乐} --irr10={悲},{基},{乐} --k {股息率-稀释率}
```

3. **三情景目标价**（与 DCF 互为校验，不替代 DCF）：

```bash
python3 tools/financial_rigor.py three-scenario --price {股价} --eps {EPS} --shares {总股本(亿)} \
  --growth {乐} {中} {悲} --pe {乐} {中} {悲} --years 3 --currency {币种}
```

4. 压力测试逐项单独列出（现金转化率下降、归属比例下降、追加融资、分红政策改变），不自动叠加。

### 第八步：复核已有报告（输入为报告路径时）

逐项检查并给出 ✅/⚠️/❌：

| 检查项 | 常见问题 |
|---|---|
| 市值 = 股价 × 股本 | 用错股本、币种混淆 |
| 现金流起点 | 从调整后净利润出发、SBC 被加回 |
| 现金归属 | 少数股东、受限现金、备付金被算给股东 |
| 风险是否重复扣减 | 既抬 r 又压情景现金流 |
| r 与 g 币种 | 人民币 g 配美元 r |
| r − g 宽度 | 小于5pp |
| 终值占比 | 未披露，或超过70%未提示 |
| 投资资产 | 权益法利润与资产市值重复计算 |
| 算术 | 用 `financial_rigor.py calc` 抽查至少5处 |

复核结论区分三类：**算术错误**（可直接改正）、**口径错误**（需要重算）、**假设分歧**（列出双方理由，不裁决）。

### 第九步：结论与价格观察线

不给"买入/卖出"指令，给价格区间与对应的隐含假设：

| 价格区间 | 对应隐含假设 | 观点 |
|---|---|---|
| 低于 X | 只需悲观情景即可获得 r | 安全边际较高（观点） |
| X – Y | 需要基准情景兑现 | 合理区间（观点） |
| 高于 Y | 需要乐观情景兑现 | 预期已较充分（观点） |

并写出最强反方论点，以及两到三个可观察的跟踪指标（哪个数字出现，就证明估值假设错了）。

## 输出格式

保存到 `reports/{公司名}/{公司名}-valuation-{YYYYMMDD}.md`，模型脚本与输入文件放在同目录（如 `reports/{公司名}/valuation-{YYYYMMDD}/model.py`）。

```markdown
# {公司名}（{代码}）估值：{一句话结论}

> 研究日 YYYY-MM-DD｜行情日 YYYY-MM-DD｜股价 {币种}{价格}｜市值 {币种}{市值}（已验算）｜现金流币种 {币种}

## 一、结论摘要
- 每股内在价值（基准）：{币种}{x}，区间 {悲}–{乐}
- 当前价格隐含：{反向估值一句话}
- 十年回报（基准，按当前价）：{x}%，r = {r}
- 终值现值占比：{x}%

## 二、股东现金流口径
## 三、DCF：经营路径、折现率与终值
## 四、股权桥
## 五、分部估值（如适用）
## 六、反向估值
## 七、敏感性与压力测试
## 八、最强反方论点
## 九、价格观察线与跟踪指标
## 数据来源与可信度
```

## 硬性规则

1. 所有算术走 `tools/financial_rigor.py` 或 `tools/terminal_value.py`，或写进 Decimal 模型脚本；禁止心算出数。
2. 报告含终值或十年 IRR 时，定稿前用最终参数再跑一次 `terminal_value.py audit`，退出码为0才能发布。
3. 每个假设标注"假设"或"估计"，并写出依据；不得把公司指引或卖方预测当作事实。
4. 同一风险只扣一次：要么在情景现金流里，要么在折现率里，写明放在哪里。
5. 货币单位在每张表的表头写明。
6. 遵守 `CLAUDE.md` 的客观性原则：每个核心判断附反面论据；数据不足时写"数据不足"。

> "如果你不能为一项资产估值，那就不要买它。" —— 巴菲特（意译）
