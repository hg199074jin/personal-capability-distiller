---
name: personal-capability-distiller
description: 把课程、文章、书籍、审计项目、AI 教程、副业资料、内容素材、认知材料、复盘或高质量对话转成可复用能力、能力卡、SOP、Prompt 或 Skill 时使用。触发词：能力蒸馏、不要只总结、更新能力树。常见反例：纯 Excel 公式排错、单次问答、临时数据清洗等不构成"把材料蒸馏成可复用能力"的场景。
---

# 个人能力蒸馏总控

只接 Markdown 或纯文本。原始 PDF / Word / PPT / Excel 和图片先由 MinerU 转换。本 Skill 是唯一日常入口，自身包含三个子流程契约：

- `references/subflows/skill-builder.md`：候选 Skill 生成器；
- `references/subflows/scenario-validator.md`：候选 Skill 模拟验证器；
- `references/subflows/obsidian-librarian.md`：Obsidian 能力库管家。

必读契约（按顺序加载）：

1. `references/workflow.md`：完整阶段顺序。
2. `references/workflow-states.md`：阶段状态与确认点。
3. `references/human-material-ladder.md`：四层人用材料。
4. `references/depth-levels.md`：A/B/C 深度规则。
5. `references/output-contracts.md`：标准输出契约。
6. `references/provenance-and-ip.md`：来源、重构、人格与知识产权边界。

### 阶段产出（每阶段产物落地契约）

下表按 `workflow.md` 阶段排序；运行后**每一格都必须填齐**或在产物内说明跳过理由。

| 阶段 | 输入 | 关键动作 | 产出 | 下一阶段触发 |
|---|---|---|---|---|
| 资料清点 | 用户原始材料 + 来源链接 | 检索既有能力节点（`00_能力地图`）避免重复 | 节点检索报告 + 主/辅/A-B-C 草案 | 用户确认主领域、档位 |
| 保真还原 | 上阶段产物 | 按 `human-material-ladder.md` 第 1 层还原 | 03_能力卡片（草案）| 用户点头 |
| 对应关系 | 保真版 | 逐段标"事实 / 来源观点 / AI 重构 / 个人应用 / 待核实" | 同上卡片标记完整 | 用户点头 |
| 逻辑版 | 对应关系版 | 合并重复、重排结构、提取主线 | 02_蒸馏记录（逻辑版）| 用户点头 |
| 使用版 | 逻辑版 | 针对具体使用者和真实任务改写 | 02_蒸馏记录（使用版）| 用户点头 |
| 定稿版 | 使用版 | 来源核对 + 适用性检查 + 用户批准 | 状态置 `human_material_approved` | 用户明示"定稿" |
| 候选 Skill | 定稿版 | 读 `skill-builder.md` 并按其 9 部分生成 | 04_Skill候选 | Skill 自检通过 |
| 模拟测试 | 候选 Skill | 读 `scenario-validator.md`，跑矩阵中 7 类用例 | 06_测试记录，全部用例通过 | 全部通过且无禁用信号 |
| 安装确认 | 通过的候选 | 用户确认 + 候选进 `05_Skill已验证` | `skill_simulation_passed` | 用户明示安装 |
| 真实应用 | 已装 Skill | 在真实任务使用 | 07_应用反馈 | 真实任务完成 |
| 反馈修订 | 真实应用反馈 | 修订 Skill 并升版本 | 05_Skill已验证 vN+1 | 新一轮模拟 |
| 内容复盘 | 修订结果 | 沉淀到能力库、标注关系 | 00_能力地图更新 | — |
| 能力树更新 | 内容复盘产物 | 链接到根/枝干/叶子节点 | 关系网最终态 | — |

### 用户调用 → Agent 行为（典型轨迹）

| 用户说 | Agent 立刻做 | 不该做 |
|---|---|---|
| 「帮我蒸馏 XXX 课」 | 检索既有节点 → 提"主领域 + 档位 + 是否 A 档"反问 | 不一气出 14 阶段全部产物 |
| 「C 档就够」 | 只产 4 项（价值/资产/连接/今日动作）+ 状态停在 `intake` | 不生成候选 Skill、不进 `human_material_approved` |
| 「PDF 在这个文件夹」 | 检查是否已转 Markdown；未转则提示 MinerU 并停主流程 | 不硬读 PDF |
| 「帮我把它做成 Skill」 | 检查是否先经过 `human_material_approved` | 跳过定稿直接生成候选 |
| 「安装吧」 | 检查是否 `skill_simulation_passed` + 用户明示 | 不自动安装到平台 Skills 目录 |
| 「跟张三发的笔记合并」 | 走"建关系（重复/补充/增强/冲突）"，两来源都保留 | 不覆盖、不静默合并 |
| 「对外发布」 | 自动重跑 🚫 #1/2 + `provenance-and-ip.md` 后才动笔 | 不冒充人物署名 |

## 运行规则（9 条）

1. 检索既有能力节点 → 定主领域、辅助领域、A/B/C 深度。
2. A 档按确认点推进，不得一气呵成（对应"阶段产出"表全部 13 行）。
3. 先完成人用材料（逻辑版→使用版→定稿版），再生成候选 Skill。
4. 读匹配的 `references/domains/*.md`。
5. 生成候选 Skill：读 `references/subflows/skill-builder.md` 并按其规则。
6. 模拟测试：读 `references/subflows/scenario-validator.md` 并按其规则。
7. 归档：读 `references/subflows/obsidian-librarian.md` + 调 `scripts/archive_to_obsidian.py`。
8. 模拟测试与真实应用必须分开记录（不进同一份 06_测试记录）。
9. 网站 / 表单 / 工具入口保持可选，非 V1 必经。

## 🚫 反例与黑名单

命中即停手。相似动作先回本表复核。

1. **冒充来源人物**（老师 / 作者 / 专家本人）→ 改"方法介绍 / 待验证观点"，原话标来源，AI 重构显式标记。
2. **大段复制付费资料 / 生成可替代原课程的成品** → 只摘关键事实与公开框架；>200 字连续引用须用户授权；提醒原课程才是商业交付。
3. **跳过保真阶段直接给"使用版" / 把 C 档伪装成 A 档** → 按 `workflow.md` 顺序；C 档只输出"价值 / 资产 / 连接 / 今日动作"，状态停在 `intake` 或 `archived`。
4. **来源观点 / AI 重构 / 个人应用混在一起** → 强制分字段：`事实 / 来源观点 / AI 重构 / 个人应用 / 待核实`。
5. **未真实应用就标"已验证" / 覆盖既有笔记 / 模拟通过直接安装** → 须 `application_feedback` + 一次真实任务；撞名不覆盖、建关系（重复/补充/增强/冲突）；安装须 `skill_simulation_passed` + 用户明示。
6. **越过阶段确认点直跳 / 把网站·表单·工具入口当必经步骤** → `workflow-states.md` 9 状态未确认不得跳；三项可选，走 `90_模板与配置`。

## 失败模式与恢复（症状 / 一线修复 / 仍失败兜底）

- **未指定档位** → 默认 C + 显式声明，可一键升档；明示"C 档就够"不追问。
- **资料非 Markdown** → 提示 MinerU 并停主流程；给调用模板，用户完成后重启。
- **候选模拟失败** → 保留入 `06_测试记录`，按建议只重测受影响用例；连续两次同用例失败降级能力卡。
- **归档撞同名不同内容（`FileExistsError`）** → 不覆盖，建关系；两来源都保留交用户合并。

## 🔴 检查点

- 🔴 **阶段确认**：每阶段对照"阶段产出"表自检 → 显式问"通过 → 下一阶段 / 修订 → 留本阶段"，未点头不跳。
- 🛑 **对外发布前**：自动重跑 🚫 #1 / #2 + `provenance-and-ip.md`，命中即停。
- 🛑 **用户明示才执行**：安装候选 Skill 前等 `skill_simulation_passed`；覆盖既有笔记前给"差异摘要"+ 用户确认键。
- 🛑 **跨主领域切换时**：用户改投 `audit → content`，重跑受影响阶段（资料清点 → 对应关系），保留旧领域链接为"上游"。
