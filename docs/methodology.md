# 数据采集与维护方法

## 独立实验与数据流

`data/libero_results.jsonl` 是唯一实验事实源。记录粒度为“报告来源/版本 × 模型 × 设置 × suite”。
同名模型出现在另一篇论文中，即使数字完全相同，也必须新增 ID。论文内部重复展示同一实验的表格行可保留一个 ID，并说明重复位置；独立设置、消融和复现不能合并。
修正同一来源的录入错误时可更新原 ID，Git 历史与本文件迁移说明保留变化；新论文版本结果必须新增记录。

`data/wam_results.jsonl` 是生成器从事实源选择 `category == "World Action Model"` 后原样生成的子集。
不要手工编辑该文件。校验器要求它与事实源完全一致，避免双份数据漂移。

## 字段契约

| 字段 | 约定 |
| --- | --- |
| `id` | 稳定、全局唯一的小写标识符；不使用模型名作为唯一键 |
| `paper_id` / `paper` / `year` | 关联 `papers.json` 的来源 ID、名称、发表年；网页发表年未知为 null |
| `model` / `category` | 引用 `model_catalog.json`；别名在目录记录，不改变论文结果身份 |
| `suite` | `all`、`spatial`、`object`、`goal`、`long`；all 表示涵盖四 suite 的表，不保证所有数值完整 |
| `spatial/object/goal/long/average` | 0–100 的来源报告成功率或 null；禁止 bool、NaN、Infinity、字符串分数 |
| `average` | 只存来源均值；缺失不能用分项补算，更不能用 Long 代替全套平均 |
| `result_role` | `main`：来源主结果；`baseline`：来源比较项；`ablation`：消融/受控变体；`reproduction`：明确声明的复现 |
| `setting` | 训练方式、输入、推理模式等身份信息；不把 baseline 标记为本项目复现 |
| `baseline_list` | 主结果所在表/协议列出的比较方法原名；名称清单不代表已完整录入其所有成绩；可包含仅在同表其他 benchmark 上有成绩的方法，须备注 |
| `source_type` | paper_pdf、official_project_page、official_github_readme、official_hf_model_card |
| `source_url/source_table/source_version/source_page` | 来源、具体表/栏目、版本、PDF 页序号（从 1 开始）；网页页码 null |
| `verification_status` / `verified_at` | verified 或 pending；数值记录必须 verified 且有 YYYY-MM-DD 核验日期；只表示转录核验，不表示实验复现 |
| `episodes` / `episodes_scope` | 明确给出的试验总数及统计口径；口径不清楚时 null；不是训练 demonstrations 数 |
| `num_seeds/trials_per_task/trials_per_suite_per_seed` | 分别存已确认的 seed 与 trial 口径，不把主方法协议自动复制给引用 baseline |
| `uncertainty/uncertainty_type` | 原文误差值和类型；无法确认是 SE/SD 时用 reported_plus_minus，不推断 |
| `checkpoint_status` | 模型级 LIBERO 权重审计状态快照，必须与 checkpoints.json 一致；具体 suite 范围见 libero_suites |
| `protocol_source` / `notes` / `reported_average_note` | 协议定位、差异和缺失原因；不能用 notes 代替数值来源 |

`papers.json` 是“报告来源目录”，可以包含官方网页/README，网页记录不伪装成论文。
原始 PDF 使用带 arXiv 版本的 URL 和 SHA-256；官方 README 尽可能固定 commit SHA。网页 SHA-256 对应当次抓取的完整 HTML 字节，仅用于核对，不代表已存档其全部内容。
不随仓库再分发论文 PDF，也不将摘要描述当作表格数字来源。

## Checkpoint 证据

`checkpoints.json` 与模型目录一一对应，code、pretrained_checkpoint、libero_checkpoint、huggingface、evaluation_code 独立审核。
允许 `released`、`announced`、`not_released`、`not_applicable`、null；每个非 null 状态需要 field-specific URL 和 locator 证据。
未找到不是未发布，统一用 null。`evaluation_code` 在本版特指可执行 LIBERO rollout 的官方代码，其他 benchmark 的评估代码不够。
`pretrained_checkpoint` 指该模型本身的预训练权重，不能用 Wan、Qwen、OpenVLA 等外部骨干替代。
官方链接与权重文件索引可证明发布；并不证明下载完整、可运行、硬件需求适宜或与每行论文结果匹配。
`libero_suites` 仅列已核验发布范围；`reproduce_level` 在亲自复现之前为 null。

## 审核与贡献

1. 优先打开原论文 PDF 的版本化 URL，核对表头、行名、脚注和评估协议。
2. 建立/补齐来源与模型目录；代码与 checkpoint 分别提供证据。
3. 按新来源/设置追加独立实验 ID。未知信息使用 null，不使用空字符串、0 或猜测数字填缺。
4. 运行 `python3 scripts/generate_leaderboard.py`，随后 validate、unittest 和 `--check`。
5. PR 中列出来源、表号、协议差异和未核实项，由维护者做研究审核后合入。

脚本校验结构与一致性，无法自动判断论文真实性或实验质量。数据维护与研究审核分开：自动渲染审核后的数据，不自动吸收二手榜单数字。

## 2026-09-10 初始迁移

保留 `openvla_2024_diffusion_policy_baseline`、`openvla_2024_octo_baseline`、`openvla_2024_openvla` 三个原始 ID 与分数。
为原 `episodes: 2000` 补充“每 seed 四个 suite”的口径，另外记录 3 seeds、每 suite 每 seed 500 trials。
Diffusion Policy 的设置修正为 from scratch，原无发布证据的 checkpoint 标记恢复为 null。
移除 `wam_results_schema` 伪实验占位行；以本文件说明 schema。
目录 `pi0/pi0.5` 规范化为 `π0/π0.5`，保留 aliases。既有 ACT、BC-Z、3D Diffuser Actor 占位目录继续保留，未知状态使用 null。

## HF 导出类型契约

导出依赖 `requirements-hf.txt`；原始 JSON/JSONL 字节保持一致，并提供 typed Parquet 作为默认 config 的数据文件。日期保持字符串，成绩为 float64、计数为 int64，缺失值仍为 null。此设计规避 datasets JSON reader 自动把日期识别成 timestamp 的行为；完整 HF 集成测试比较所有行的全部字段。
