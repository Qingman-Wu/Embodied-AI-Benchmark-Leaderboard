# Embodied-AI-Benchmark-Leaderboard

## 项目简介

公开、可维护的 LIBERO Vision-Language-Action（VLA）/ World Action Model（WAM）实验数据库。
每条记录对应一个来源中的一个模型与设置；同一模型在不同论文、版本、推理模式中的成绩分别保存。
数据已按原始 PDF 或官方页面核验；本项目尚未运行统一复现实验。

**阅读规则：** 数值为成功率（%），`—` 对应 JSON `null`。论文报告、论文中的 baseline、官方发布 checkpoint 的成绩不可混作同一次评估。
`average` 保留来源原值，不自行补算；不同输入、训练数据、评估次数的结果不做全局排序。

## Supported Benchmarks

当前收录 LIBERO-Spatial、LIBERO-Object、LIBERO-Goal、LIBERO-Long（也称 LIBERO-10）。
仅报告 Long 的记录保持 `suite: "long"`，其他 suite 及全套 `average` 为 `null`。
RoboTwin、LIBERO-Plus、SimplerEnv 暂不进入此 LIBERO 表。

## LIBERO Leaderboard

完整数据见 [libero_results.jsonl](data/libero_results.jsonl)，独立表格见 [LIBERO Leaderboard](tables/libero_leaderboard.md)。
WAM 子集与 baseline 名单见 [WAM Comparison](tables/wam_comparison.md)。以下区域由脚本生成。

<!-- leaderboard:start -->

统一实验表：每行是一个“来源论文/官方报告 × 模型 × 设置”。同名模型的不同来源结果保留为不同 row；不做跨协议总排名。

图例：🔵 VLA　🟣 Foundation Robot Model　🟢 World Action Model　⚪ Reference Policy；`—` 表示 null。

| Track | Model | Paper / source | Setting | Suite | Spatial | Object | Goal | Long | Average | Role | 备注 | Record ID |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| 🔵 VLA | OpenVLA | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO per-suite fine-tuning | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | ⭐ main | OpenVLA 原论文报告的结果；LingBot-VA、Fast-WAM、OpenVLA-OFT、SpatialVLA、OA-WAM、Streaming-WAM 论文将该结果作为 OpenVLA baseline 使用。 | `openvla_2024_openvla` |
| 🔵 VLA | OpenVLA-OFT | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | OFT + wrist camera + proprioception | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | ⭐ main | OpenVLA-OFT 原论文报告的主结果；LingBot-VA 和 LaWAM 论文将其作为 baseline，Motus 在 LIBERO-Long 中也报告相同 Long 结果。 | `openvla_oft_2025_openvla_oft_main` |
| 🔵 VLA | SpatialVLA | [SpatialVLA (2025)](https://arxiv.org/pdf/2501.15830v1) · Table III | LoRA + spatial embedding adaptation | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | ⭐ main | SpatialVLA 原论文报告的主结果；LingBot-VA 和 OA-WAM 论文对比 SpatialVLA 时使用相同结果。 | `spatialvla_2025_spatialvla_main` |
| 🟣 Foundation | GR00T-N1 | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 | baseline | LingBot-VA 论文表 2 报告的 GR00T-N1 baseline；Motus 论文仅在 LIBERO-Long 中报告 Long=90.6，与该结果一致。 | `lingbot_va_2026_gr00t_n1_baseline` |
| 🟣 Foundation | GR00T-N1.6 | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 97.7 | 98.5 | 97.5 | 94.4 | 97.0 | baseline | LaWAM 论文表 1 报告的 GR00T-N1.6 baseline；当前未找到 GR00T-N1.6 自己论文的 LIBERO 结果。 | `lawam_2026_gr00t_n1_6_baseline` |
| 🟣 Foundation | π0 | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 | baseline | OpenVLA-OFT 论文表 I 报告的 π0 baseline；其他论文中的 π0 结果存在不同报告值，分别保留可核验的代表记录。 | `openvla_oft_2025_pi0_baseline` |
| 🟣 Foundation | π0 | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.0 | 96.8 | 94.4 | 88.4 | 94.4 | baseline | LaWAM 论文表 1 报告的 π0 baseline，分数与其他来源不同，单独保留。 | `lawam_2026_pi0_baseline` |
| 🟣 Foundation | π0.5 | [OpenPI (official)](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/README.md) · LIBERO Benchmark results | pi05_libero; 30k fine-tuned checkpoint | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.85 | ⭐ main | OpenPI 官方发布的 π0.5 结果；Fast-WAM、LaWAM、OA-WAM、Streaming-WAM 论文对比 π0.5 时报告相同结果（平均值存在四舍五入差异）。 | `openpi_release_pi05_30k` |
| 🟢 WAM | Fast-WAM | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | No embodied pretraining; 20k steps | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | ⭐ main | Fast-WAM 原论文最终主变体结果；LaWAM 和 Streaming-WAM 论文对比 Fast-WAM 时使用相同结果。 | `fastwam_2026_fast_wam_main` |
| 🟢 WAM | LaWAM | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO fine-tuning | all | 99.4 | 99.6 | 98.4 | 97.0 | 98.6 | ⭐ main | LaWAM 原论文主结果。 | `lawam_2026_lawam_main` |
| 🟢 WAM | LingBot-VA | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO fine-tuning | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | ⭐ main | LingBot-VA 原论文报告的主结果；Fast-WAM 和 LaWAM 论文对比 LingBot-VA 时使用相同结果。 | `lingbot_va_2026_lingbot_va_main` |
| 🟢 WAM | Motus | [Motus (2025)](https://arxiv.org/pdf/2512.13030v1) · Table 9 | LIBERO-Long only | long | — | — | — | 97.6 | — | ⭐ main | Motus 原论文主结果；Fast-WAM、LaWAM、Streaming-WAM 论文对比 Motus 时使用相同完整 LIBERO 结果，Motus 自己还报告 LIBERO-Long 的 Long=97.6。 | `motus_2025_motus_main` |
| 🟢 WAM | OA-WAM | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO fine-tuning | all | 98.9 | 99.0 | 97.4 | 95.9 | 97.8 | ⭐ main | OA-WAM 原论文主结果。 | `oawam_2026_oa_wam_main` |
| 🟢 WAM | Streaming-WAM | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO fine-tuning | all | 98.8 | 100.0 | 97.8 | 96.8 | 98.35 | ⭐ main | Streaming-WAM 官方结果；其余论文中的重复 baseline 结果已合并到对应模型原始结果行。 | `streaming_wam_2026_streaming_wam_main` |
| ⚪ Reference | Diffusion Policy | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO training from scratch | all | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 | baseline | 来源中列出的 baseline；不表示本项目复现，也不自动继承该论文主方法的评估次数。 | `openvla_2024_diffusion_policy_baseline` |
| ⚪ Reference | Octo | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO per-suite fine-tuning | all | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 | baseline | 来源中列出的 baseline；不表示本项目复现，也不自动继承该论文主方法的评估次数。 | `openvla_2024_octo_baseline` |

<!-- leaderboard:end -->

## Evaluation Tracks

- **Track 1 · LIBERO VLA：** OpenVLA、OpenVLA-OFT、SpatialVLA。
- **Track 2 · Foundation Robot Model：** π0、π0.5、GR00T；GR00T-N1 与 GR00T-N1.6 分开记录。
- **Track 3 · World Action Model：** Fast-WAM、Streaming-WAM、OA-WAM、LaWAM、Motus、LingBot-VA 及已核验变体。
- **Reference：** 保留仓库原有 Diffusion Policy、Octo 等政策基线记录，不混入三个主 track 排名。

分类是本数据库的组织方式，并不表示相同实验协议。Fast-WAM-H3、VLA-JEPA 保留在模型目录，等待后续审核；未提交实验数字的计划模型不创建伪实验。

## Data Sources

优先级：论文 PDF 表格 → 官方项目页 → 官方 GitHub README → 官方 Hugging Face 模型卡。
不采用 blog、二手榜单或 review 数值。每条数值记录必须提供 `source_url`、`source_table`、`source_version`、`verified_at`；PDF 增加页码。

- [来源目录与已知差异](docs/data_sources.md)
- [采集方法与字段说明](docs/methodology.md)
- [评估协议与可比性](docs/evaluation_protocol.md)
- [模型目录](data/model_catalog.json) · [Checkpoint 审计](data/checkpoints.json)

`released` 只表示官方资产发布证据已确认；不保证该模型的每条历史结果都有完全匹配的权重。
例如 LingBot-VA 当前核实到的 LIBERO 权重范围为 Long。`reproduce_level` 在实际复现之前保持 `null`。

## 更新与自动化

Python 3.10+；校验和生成脚本只使用标准库。HF 导出与完整加载测试另需 `requirements-hf.txt` 中的可选依赖。

```bash
python3 scripts/generate_leaderboard.py
python3 scripts/validate_json.py
python3 scripts/generate_leaderboard.py --check
python3 -m unittest discover -s tests -v
```

新增数据只编辑事实源 `data/libero_results.jsonl` 与相关元数据。生成器同时更新 README、两个 Markdown 表和 `data/wam_results.jsonl`，保留每条记录，不自动重算分数。
GitHub Actions 在 push / PR / 手动触发时校验数据、运行测试并检查生成物，上传 HF 导出包作为 artifact。
新论文的发现、研究审核和录入由维护者确认；本阶段未启用无人审核的自动数值采集或定时监控。

目录：

```text
data/       实验、论文、模型、checkpoint JSON 数据
scripts/    校验、生成 leaderboard、导出 HF Dataset
tables/    自动生成的 LIBERO 与 WAM Markdown 表
docs/      方法、评估协议、来源与实施计划
tests/     数据完整性及导出回归测试
website/   后续网站入口说明
```

## Hugging Face Dataset

计划数据集 ID：`Qingman-Wu/Embodied-AI-Benchmark-Leaderboard`。本阶段提供可加载的导出包，尚未向 Hugging Face 发布。

```bash
python3 -m pip install -r requirements-hf.txt
python3 scripts/export_hf_dataset.py --output-dir dist/hf_dataset
```

```python
from datasets import load_dataset
# 本地导出包
libero = load_dataset("/absolute/path/to/dist/hf_dataset")
wam = load_dataset("/absolute/path/to/dist/hf_dataset", "wam")
# 维护者发布到 Hugging Face 后：
# libero = load_dataset("Qingman-Wu/Embodied-AI-Benchmark-Leaderboard")
```

默认 config 为 `libero`；`wam` 为同一数据的子集，不能把两个 config 拼接后重复计数。
原始 JSON/JSONL 按字节保留，另生成带明确类型的 Parquet 供默认加载，避免日期字符串被 JSON reader 自动转换。元数据 JSON 随包分发；详情见导出包的 dataset card。数据和代码的再分发许可待维护者明确。

## Citation

使用具体成绩时请引用该记录对应的原论文或官方发布页面，并附上 `id` 与 `source_version`。
引用本数据库可使用以下条目，并在论文中记录实际使用的 commit SHA：

```bibtex
@misc{qingmanwu_embodied_ai_benchmark_leaderboard,
  author = {Wu, Qingman},
  title = {Embodied-AI-Benchmark-Leaderboard},
  year = {2026},
  howpublished = {\url{https://github.com/Qingman-Wu/Embodied-AI-Benchmark-Leaderboard}}
}
```
