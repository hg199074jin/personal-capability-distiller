# 个人能力蒸馏总控（personal-capability-distiller）

<div align="center">

![Darwin Optimized](https://img.shields.io/badge/Darwin-Optimized_2.0-FF6B35?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTkgMS40MSAxLjQxTDEwIDE3eiIvPjwvc3ZnPg==)
![9 Dim Score](https://img.shields.io/badge/9%E7%BB%B4_Score-85%2F100-4CAF50?style=flat-square&labelColor=2E7D32)
![Skills Standard](https://img.shields.io/badge/Agent_Skills-Standard-2196F3?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMjQgMjQiIGZpbGw9IndoaXRlIj48cGF0aCBkPSJNMTIgMkM2LjQ4IDIgMiA2LjQ4IDIgMTJzNC40OCAxMCAxMCAxMCAxMC00LjQ4IDEwLTEwUzE3LjUyIDIgMTIgMnptLTEgMTdIOVY3aDJ2MTJ6bTAtMTVoMlY0aC0ydjE0eiIvPjwvc3ZnPg==)
![Runtime Agnostic](https://img.shields.io/badge/Runtime-Agnostic-9C27B0?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-FBC02D?style=flat-square)
![Backup Safe](https://img.shields.io/badge/Rollback-File_Backup_Only-00897B?style=flat-square)
![Tested](https://img.shields.io/badge/Tested-3_Prompts-43A047?style=flat-square)
![Claude Code Verified](https://img.shields.io/badge/Claude_Code-Verified-1E88E5?style=flat-square)
![Score Improved](https://img.shields.io/badge/Score-%2B85%25-8E24AA?style=flat-square)

</div>

> **一句话**：把你看过的课程、文章、书籍、项目复盘……这些"原料"，蒸馏成能反复用的能力卡 / SOP / Prompt / Skill。

---

## 🏷️ 徽章说明（怎么看这些色块）

| 徽章 | 含义 |
|---|---|
| Darwin Optimized 2.0 | 本 skill 经过 Darwin Skill 2.0 自动评估 + 优化 |
| 9 维 Score 85/100 | 用 SkillLens-style rubric 评的 9 维度加权总分 |
| Agent Skills Standard | 兼容 Agent Skills Standard 规范（Claude Code / Codex / Cursor / OpenClaw 等） |
| Runtime Agnostic | 不会被 "Claude Code only" 之类的措辞拒绝 |
| License MIT | 沿用 MIT 许可（按原作者约定） |
| Rollback File Backup | 不进 git 仓库，回滚靠 `.backup/` 时间戳目录（最不侵入） |
| Tested 3 Prompts | 已用 `test-prompts.json` 跑过 3 个典型场景 |
| Claude Code Verified | Claude Code 实测加载通过 |
| Score +85% | 相对基线 46 分的提升幅度 |

---

## 它是做什么的？

你经常会遇到这些场景：

| 场景 | 你想要什么 | 这个 skill 能帮你做什么 |
|---|---|---|
| 听完一门审计 / 财务 / AI / 副业 课 | 把老师讲的"独家方法"变成自己能用的 SOP | 按 4 层人用材料（保真→逻辑→使用→定稿）逐步产出 |
| 读完一本专业书 | 一张能贴在桌边的"能力卡"，下次遇到类似问题能查 | 输出 1 张能力卡，含触发条件 / 步骤 / 验收 |
| 做完一个项目 / 一次复盘 | 把零散心得沉淀成方法论，下次能复用 | 走完 13 阶段 → 在 Obsidian 能力库里建一条记录 |
| 看了几篇高质量对话 / 评论 | 把"金句"整理成可复用 prompt 或判断标准 | 蒸馏出 prompt 卡 + 触发词 + 反例 |

**它不是**：写个 Excel 公式、临时数据清洗、单次问答、单纯排版 — 这些请用别的 skill。

---

## 三步快速上手

### 第 1 步：把这个 skill 装到 Claude Code（或同等 skills 兼容工具）

把它拷到任意一个 skills 目录即可。Claude Code 默认在 `~/.claude/skills/`：

```bash
# Windows PowerShell / Git Bash 都行
cp -r "这个项目路径" ~/.claude/skills/personal-capability-distiller
```

装完不需要配置环境变量、不需要装 Python 包（除了运行归档脚本时用 `pyyaml`）。

### 第 2 步：准备一份 Markdown / 纯文本原料

PDF / Word / PPT / Excel / 图片先用 MinerU 转成 Markdown 或纯文本（这是 skill 启动时会问你确认的）。

### 第 3 步：用一段自然语言 prompt 叫醒它

打开任意一个 Claude Code 会话，输入：

```
帮我蒸馏 <原料名>，输出可复用的能力卡和 SOP。
```

例如：

```
帮我蒸馏《审计准则第 1231 号——了解被审计单位及其环境并评估重大错报风险》的核心要点，输出审计风险评估 SOP 和能力卡。
```

skill 会自动按规则走 4 层人用材料 → 13 阶段 → 候选 Skill → 模拟测试 → 归档。

---

## 怎么叫醒它（完整触发词清单）

skill 不靠命令触发，靠**触发词 + 场景描述**自然触发。

### ✅ 会触发（正面示例）

- "帮我蒸馏 / 提炼 / 蒸馏出 / 把 X 蒸馏成 Y"
- "能力蒸馏 / 不要只总结"
- "更新能力树 / 沉淀到能力库 / 能力卡"
- "把课程 / 文章 / 书 / 笔记 → SOP / 能力卡 / Prompt / Skill"
- "复盘这段对话 → 可复用方法"
- "AI 教程 / 审计项目 / 副业资料 → 体系化"

### ❌ 不会触发（反面示例）

- "写一段 Excel 公式把中文姓名按拼音排序" — 这是公式排错
- "这个报销凭证怎么做账" — 这是单次问答
- "把 A 列的脏数据清一下" — 这是数据清洗

> 以上反面示例命中时，skill 会礼貌告诉你"不属于能力蒸馏范围"，并建议用别的工具 — 不会硬套模板（见 SKILL.md 🚫 #3）。

---

## 档位：A / B / C 三档可选

| 档位 | 适用场景 | 速度 | 深度 |
|:---:|---|---|---|
| **A** | 完整方法论 / 大型 SOP / 候选 Skill 生成 | 慢 | 13 阶段全走 |
| **B** | 复用既有能力 / 小修小补 | 中 | 合并 4 层为 2 层 |
| **C** | 临时捕获 / 快速过一下 | 快 | 只产 4 项：价值 / 资产 / 连接 / 今日动作 |

**默认**：C 档起步（"先用 30 秒看一眼"），用户可一键升 A 档。

**怎么选**：

- 你想产出**一个新的 skill** → 选 A
- 你想**完善既有 skill** → 选 B
- 你只是想**记一下** → 选 C

---

## 13 个阶段（A 档完整流程）

| # | 阶段 | 输入 | 产出 | 谁来确认 |
|---|---|---|---|---|
| 1 | 资料清点 | 原始材料 + 链接 | 主/辅/A-B-C 草案 | 🔴 你 |
| 2 | 保真还原 | 上一步 | 03_能力卡片（草案） | 🔴 你 |
| 3 | 对应关系 | 保真版 | 强制分 5 字段 | 🔴 你 |
| 4 | 逻辑版 | 对应关系 | 02_蒸馏记录（逻辑版） | 🔴 你 |
| 5 | 使用版 | 逻辑版 | 02_蒸馏记录（使用版） | 🔴 你 |
| 6 | 定稿版 | 使用版 | 状态 = `human_material_approved` | 🛑 你要明示"定稿" |
| 7 | 候选 Skill | 定稿版 | 04_Skill候选 | Skill 自检 |
| 8 | 模拟测试 | 候选 Skill | 06_测试记录 | 全部 7 类用例通过 |
| 9 | 安装确认 | 通过的候选 | 05_Skill已验证 | 🛑 你要明示安装 |
| 10 | 真实应用 | 已装 Skill | 07_应用反馈 | 真实任务完成 |
| 11 | 反馈修订 | 应用反馈 | 05_Skill已验证 v(N+1) | — |
| 12 | 内容复盘 | 修订结果 | 00_能力地图更新 | — |
| 13 | 能力树更新 | 复盘产物 | 关系网最终态 | — |

> ⚠️ **不要跳确认点**：每一阶段都要 🔴 你点头才能继续。如果你说"一气呵成"，skill 会 🚫 把它列为反例 #6 并重置当前状态。

---

## 项目结构

```
personal-capability-distiller/
├── SKILL.md                                 ← 主控（唯一入口）
├── README.md                                ← 本文档
├── test-prompts.json                        ← 测试 prompt 集（3 个典型场景）
├── .darwin-output/                          ← 进化成果（本次 Darwin Skill 2.0 产出）
│   ├── result-card.html
│   └── result-card.png                      ← 2x 高清成果卡片（46→85）
├── .backup/20260706-1855/                   ← 进化前的完整备份
└── references/                              ← 契约文件（按顺序加载）
    ├── workflow.md                          ← 13 阶段
    ├── workflow-states.md                   ← 9 个允许状态
    ├── human-material-ladder.md             ← 4 层人用材料
    ├── depth-levels.md                      ← A/B/C 档位规则
    ├── output-contracts.md                  ← 标准输出契约
    ├── provenance-and-ip.md                 ← 来源 / 重构 / 人格边界
    ├── domains/                             ← 各领域特殊处理
    │   ├── audit.md                         ← 审计领域
    │   ├── ai.md                            ← AI 教程领域
    │   ├── cognition.md                     ← 认知材料领域
    │   ├── content.md                       ← 内容创作领域
    │   ├── side-business.md                 ← 副业领域
    │   └── general.md                       ← 通用
    └── subflows/                            ← 三段子流程契约
        ├── skill-builder.md                 ← 候选 Skill 生成器
        ├── scenario-validator.md            ← 模拟验证器
        └── obsidian-librarian.md            ← Obsidian 归档管家
└── scripts/
    └── archive_to_obsidian.py               ← 归档脚本（不会覆盖既有笔记）
```

**重要**：用户**只需要装这一个目录**。`references/`、`scripts/`、`test-prompts.json` 都在它里面，安装时会一起拷过去。

---

## 归档脚本用法（可选）

如果你想把产物落 Obsidian 库，跑 `scripts/archive_to_obsidian.py`。

### 前置依赖

```bash
python -m pip install pyyaml
```

### 三种调用方式

```bash
# 1. 只检查 vault 是否齐全（不写文件）
python scripts/archive_to_obsidian.py \
  --vault-root "E:\Obsidian\Skill_Library" \
  --check-vault

# 2. 预览要写什么（不写文件）
python scripts/archive_to_obsidian.py \
  --vault-root "E:\Obsidian\Skill_Library" \
  --request /path/to/request.yaml \
  --dry-run

# 3. 真归档（写文件）
python scripts/archive_to_obsidian.py \
  --vault-root "E:\Obsidian\Skill_Library" \
  --request /path/to/request.yaml
```

### 安全保证

脚本**绝不**：
- 覆盖已有但内容不同的笔记（遇此情况抛 `FileExistsError`）
- 删除任何文件
- 静默合并两个相似内容

会写时新建目录 + 新建文件（`open(..., "x")` 独占模式）。

### vault 必需的 8 个目录

```
00_能力地图  01_来源资料  02_蒸馏记录  03_能力卡片
04_Skill候选  05_Skill已验证  06_测试记录  07_应用反馈
90_模板与配置（可选）
```

`--check-vault` 会列出缺失项。

---

## 🚫 反例黑名单（千万不要做的事）

| # | ❌ 不要做 | ✅ 应该做 |
|---|---|---|
| 1 | 冒充老师 / 作者 / 专家本人"我"的口吻 | 改"方法介绍 / 待验证观点"，原话标来源 |
| 2 | 大段复制付费资料 / 生成可替代原课程的成品 | 只摘关键事实 + 公开框架；>200 字连续引用须授权 |
| 3 | 跳过保真阶段直接给"使用版"，或把 C 档伪装成 A 档 | 按 workflow.md 顺序走；C 档只产 4 项 |
| 4 | 来源观点 / AI 重构 / 个人应用混在一起 | 强制分 5 字段 |
| 5 | 未真实应用就标"已验证"，或覆盖笔记，或模拟通过直接装 | 必须有 `application_feedback` + 真实任务 |
| 6 | 越过阶段确认点直跳，把网站·表单·工具入口当必经 | 13 阶段未确认不得跳；三项可选 |

---

## 故障与恢复（症状 / 一线修复 / 仍失败兜底）

| 出错 | 一线修复 | 还失败怎么办 |
|---|---|---|
| 用户未指定档位 | 默认 C 档 + 显式声明，可一键升档 | 明示"C 档就够"则不再追问 |
| 原料是 PDF / Word / PPT / Excel / 图片 | 提示"先 MinerU 转换"并停主流程 | 给 MinerU 调用模板，你转换完重启 |
| 候选 Skill 模拟测试失败 | 保留候选入 `06_测试记录`，按建议只重测受影响用例 | 连续两次同用例失败 → 降级能力卡 |
| 归档撞同名不同内容（`FileExistsError`） | 不覆盖，建重复/补充/增强/冲突关系 | 两份都保留给你人工合并 |
| 你中途改了来源资料 | 停止当前阶段，回到受影响阶段重跑 | 取消则把状态冻结到 `archived` |
| Obsidian vault 根目录缺失 | 先 `--check-vault` 列缺失项，给你补齐 | 仍失败则产物暂存 `drafts/` 等恢复后重归档 |

---

## 🔴 检查点（4 个 STOP 节点）

- 🔴 **阶段确认**：每阶段显式问"通过 → 下一阶段 / 修订 → 留本阶段"，未点头不跳。
- 🛑 **对外发布前**：自动重跑反例 #1 / #2 + `provenance-and-ip.md`，命中即停。
- 🛑 **安装候选 Skill 前**：必须等 `skill_simulation_passed` + 你明示。
- 🛑 **覆盖既有笔记前**：给"差异摘要"+ 你确认键。

---

## 自己测一下：3 个典型 prompt

skill 目录里有个 `test-prompts.json`，包含 3 个典型场景，你直接拿去喂 Claude Code 试试看：

| # | 测试 prompt | 期望行为 |
|---|---|---|
| 1 | "帮我蒸馏《审计准则第 1231 号》的核心要点，输出可复用 SOP" | A 档全走，主领域=audit，IP 边界守住 |
| 2 | "我刚听完某讲师的小红书爆款公式课（已授权），把他的转写蒸馏成 SOP" | 拒绝冒充讲师；原话标来源；AI 重构显式 |
| 3 | "帮我写一段 Excel 公式把中文姓名按拼音排序" | **不触发** — 礼貌说明边界，不硬套模板 |

> 这正是「反面示例」的价值 — 测试 #3 验证 skill 不会越界。

---

## FAQ

### Q：这个 skill 装完 Claude Code 要重启吗？

**A**：不需要。下次会话自动加载。SKILL.md 的 frontmatter 会被 Claude Code 在启动时索引。

### Q：我有 PDF 怎么办？

**A**：先用 MinerU 转 Markdown（脚本提示会给调用模板）。Skill 不直接读 PDF。

### Q：归档后找不到了 / 出错了怎么办？

**A**：脚本**不会**覆盖现有笔记（见 `archive_to_obsidian.py` 的 `FileExistsError`）。出错时产物留在 `drafts/` 或抛出具体错误信息。

### Q：这个 skill 自己是怎么"进化"的？

**A**：用 Darwin Skill 2.0（一个独立的 meta-skill）按 9 维度 rubric 自动评估 + 优化。本次进化 46 → 85 分详见 `.darwin-output/result-card.html` / `.png`。完整日志在全局 `~/.claude/skills/darwin-skill/results.tsv`。

### Q：我能改 SKILL.md 吗？

**A**：能。但要注意 4 条：

1. 别删除「必读契约」列表里的 6 个文件
2. 别删除「🚫 反例与黑名单」章节（这是质量保证）
3. 别删「🔴 检查点」中的 STOP 标记（用户安全网）
4. 别把体积压到 baseline 的 50% 以下（信息密度会崩）

### Q：怎么更新这个 skill？

**A**：直接覆盖 `~/.claude/skills/personal-capability-distiller/` 目录即可。如果项目在 git 仓库，pull 重启会话。

### Q：我只想要归档脚本，不要 skill 主文件，行不行？

**A**：可以单跑 `scripts/archive_to_obsidian.py`，但产物**不**带 9 个允许状态、不带领域元数据。建议装整个 skill 目录。

### Q：哪些 skills 兼容工具能用？

**A**：理论上所有支持 `SKILL.md` 文件结构 + frontmatter description 触发词的 skills 兼容工具都行（Claude Code / Claude.ai / OpenClaw 等）。本项目已在 Claude Code 验证。

---

## 致谢

- **Darwin Skill 2.0**：本次进化所用的评估 / 优化 / 评分 meta-skill，融合 SkillLens（arXiv 2605.23899）+ SkillOpt（arXiv 2605.23904）+ Karpathy autoresearch。GitHub: https://github.com/alchaincyf/darwin-skill
- **SkillLens**：微软研究院，9 维 rubric 的实证基础。
- **SkillOpt**：微软研究院，validation-gated 编辑框架。
- **Microsoft Research**：SkillOpt 在 2026-06-03 把 Darwin Skill 列入官方集成名单。

---

## 许可

按原项目 README 约定。
