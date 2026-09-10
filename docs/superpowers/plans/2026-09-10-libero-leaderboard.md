# LIBERO Leaderboard Implementation Plan

**Goal:** 实施用户提供的 v1.0 交接规范，建立可追溯、多来源独立记录的 LIBERO 数据库。
**Architecture:** JSONL 是实验事实源；模型、论文、checkpoint 为独立 JSON 元数据。Python 标准库校验、生成三条 track 表格、导出 Hugging Face 数据包，GitHub Actions 校验生成物。
**Tech Stack:** Python 3.10+ 标准库、unittest、GitHub Actions；HF 导出使用可选 pyarrow，加载验证使用可选 datasets。
**Spec:** 用户在本任务提供的 LIBERO VLA / World Action Model Leaderboard Implementation Specification v1.0。

## Global Constraints

不创造实验数字；未核实值为 null；不同论文/版本/设置保留不同 ID；README 使用中文说明和英文模型名；不生成全局排名。公开发布 HF Dataset 属于后续阶段。

## Execution

- [x] 1. 检查仓库，保留现有三个实验 ID；移除伪实验 schema 占位行并记录迁移。
- [x] 2. 先写 CLI 回归测试：拒绝重复 ID、非有限数、布尔分数、缺少来源；保留 null、跨论文同模型；确定性生成、HF 导出无记录损失。运行 `python3 -m unittest discover -s tests -v` 确认缺少实现时失败。
- [x] 3. 实施 `scripts/validate_json.py`：校验 JSON/JSONL、类型、枚举、引用、数字证据、WAM 投影一致性。实施 `scripts/generate_leaderboard.py`：按 track 和来源分组，生成两个 tables 文件及 README 标记区域，支持 `--check`。
- [x] 4. 核对目标模型原始 PDF/官方页，逐条录入 source_url、source_table、source_version、result_role、协议、核验日期。checkpoint 每个 release 状态单独列证据，缺少证据为 null。
- [x] 5. 实施 `scripts/export_hf_dataset.py --output-dir PATH`，输出标准 JSON 数据、默认 libero config 和独立 wam config 的 dataset card；验证本地 `load_dataset(PATH)`。
- [x] 6. 更新 README、methodology、evaluation_protocol、data_sources、website README、数据贡献指南与 CI。自动维护只做确定性校验/渲染，新研究结果经来源审核再录入。
- [x] 7. 运行 unittest、数据校验、生成器 `--check`、导出集成验证及 `git diff --check`，审查数据和变更，修正发现的问题。
- [x] 8. 提交并推送实现分支，创建可审核 PR，报告链接和未核实项目。

## Verification evidence

2026-09-10：57 条 LIBERO、23 条 WAM，14 项 unittest 通过（包含可选 HF 集成测试）；本地 Hugging Face datasets 默认/ wam config 成功加载并验证 null 与精度。已渲染核对 8 份原论文表格页，核验 11 个报告来源。独立审查子代理因模型容量未完成，已执行本地代码与数据复核；研究审核通过 draft PR 交由维护者继续。

HF 集成测试发现 datasets JSON reader 会将 YYYY-MM-DD 转为 timestamp，声明 string feature 后也会增加时间后缀。导出改为保留原始 JSONL 并附加 typed Parquet 作为默认加载文件，逐条全字段往返相等；这是为保持 schema 的实现调整。

交付：[Draft PR #1](https://github.com/Qingman-Wu/Embodied-AI-Benchmark-Leaderboard/pull/1)。初次 push 的 GitHub CI 已在 Python 3.10 / 3.12 上通过；主分支未合并。
