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

| Track | Model | Paper / source | Setting | Suite | Spatial | Object | Goal | Long | Average | Role | Record ID |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 🔵 VLA | OpenVLA | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `lingbot_va_2026_openvla_baseline` |
| 🔵 VLA | OpenVLA | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `fastwam_2026_openvla_baseline` |
| 🔵 VLA | OpenVLA | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `openvla_oft_2025_openvla_baseline` |
| 🔵 VLA | OpenVLA | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | pd_ac; third-person image + language | all | 91.3 | 92.7 | 90.5 | 86.5 | 90.2 | 🧪 ablation | `openvla_oft_2025_pd_ac` |
| 🔵 VLA | OpenVLA | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | pd_ac_cont_diffusion; third-person image + language | all | 96.9 | 98.1 | 95.5 | 91.1 | 95.4 | 🧪 ablation | `openvla_oft_2025_pd_ac_cont_diffusion` |
| 🔵 VLA | OpenVLA | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | pd_ac_cont_l1; third-person image + language | all | 96.2 | 98.3 | 96.2 | 90.7 | 95.3 | 🧪 ablation | `openvla_oft_2025_pd_ac_cont_l1` |
| 🔵 VLA | OpenVLA | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `oawam_2026_openvla_baseline` |
| 🔵 VLA | OpenVLA | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO per-suite fine-tuning | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | ⭐ main | `openvla_2024_openvla` |
| 🔵 VLA | OpenVLA | [SpatialVLA (2025)](https://arxiv.org/pdf/2501.15830v1) · Table III | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `spatialvla_2025_openvla_baseline` |
| 🔵 VLA | OpenVLA | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | baseline | `streaming_wam_2026_openvla_baseline` |
| 🔵 VLA | OpenVLA-OFT | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | baseline | `lingbot_va_2026_openvla_oft_baseline` |
| 🔵 VLA | OpenVLA-OFT | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | OFT + wrist camera + proprioception | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | ⭐ main | `openvla_oft_2025_openvla_oft_main` |
| 🔵 VLA | OpenVLA-OFT | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | baseline | `lawam_2026_openvla_oft_baseline` |
| 🔵 VLA | OpenVLA-OFT | [Motus (2025)](https://arxiv.org/pdf/2512.13030v1) · Table 9 | LIBERO-Long only | long | — | — | — | 94.5 | — | baseline | `motus_2025_openvla_oft_baseline` |
| 🔵 VLA | SpatialVLA | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | baseline | `lingbot_va_2026_spatialvla_baseline` |
| 🔵 VLA | SpatialVLA | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO comparison as reported in this source | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | baseline | `oawam_2026_spatialvla_baseline` |
| 🔵 VLA | SpatialVLA | [SpatialVLA (2025)](https://arxiv.org/pdf/2501.15830v1) · Table III | LoRA + spatial embedding adaptation | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | ⭐ main | `spatialvla_2025_spatialvla_main` |
| 🟣 Foundation | GR00T-N1 | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 | baseline | `lingbot_va_2026_gr00t_n1_baseline` |
| 🟣 Foundation | GR00T-N1 | [Motus (2025)](https://arxiv.org/pdf/2512.13030v1) · Table 9 | LIBERO-Long only | long | — | — | — | 90.6 | — | baseline | `motus_2025_gr00t_n1_baseline` |
| 🟣 Foundation | GR00T-N1.6 | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 97.7 | 98.5 | 97.5 | 94.4 | 97.0 | baseline | `lawam_2026_gr00t_n1_6_baseline` |
| 🟣 Foundation | π0 | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | baseline | `lingbot_va_2026_pi0_baseline` |
| 🟣 Foundation | π0 | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | baseline | `fastwam_2026_pi0_baseline` |
| 🟣 Foundation | π0 | [OpenVLA-OFT (2025)](https://arxiv.org/pdf/2502.19645v1) · Table I | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 | baseline | `openvla_oft_2025_pi0_baseline` |
| 🟣 Foundation | π0 | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.0 | 96.8 | 94.4 | 88.4 | 94.4 | baseline | `lawam_2026_pi0_baseline` |
| 🟣 Foundation | π0 | [Motus (2025)](https://arxiv.org/pdf/2512.13030v1) · Table 9 | LIBERO-Long only | long | — | — | — | 85.2 | — | baseline | `motus_2025_pi0_baseline` |
| 🟣 Foundation | π0 | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 | baseline | `oawam_2026_pi0_baseline` |
| 🟣 Foundation | π0 | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | baseline | `streaming_wam_2026_pi0_baseline` |
| 🟣 Foundation | π0.5 | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | LIBERO comparison as reported in this source | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | baseline | `fastwam_2026_pi0_5_baseline` |
| 🟣 Foundation | π0.5 | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | baseline | `lawam_2026_pi0_5_baseline` |
| 🟣 Foundation | π0.5 | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | baseline | `oawam_2026_pi0_5_baseline` |
| 🟣 Foundation | π0.5 | [OpenPI (official)](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/README.md) · LIBERO Benchmark results | pi05_libero; 30k fine-tuned checkpoint | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.85 | ⭐ main | `openpi_release_pi05_30k` |
| 🟣 Foundation | π0.5 | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | baseline | `streaming_wam_2026_pi0_5_baseline` |
| 🟢 WAM | Fast-WAM | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | No embodied pretraining; 20k steps | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | ⭐ main | `fastwam_2026_fast_wam_main` |
| 🟢 WAM | Fast-WAM | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | baseline | `lawam_2026_fast_wam_baseline` |
| 🟢 WAM | Fast-WAM | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | baseline | `streaming_wam_2026_fast_wam_baseline` |
| 🟢 WAM | Fast-WAM w/o video co-training | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | No embodied pretraining; 20k steps | all | 89.2 | 99.2 | 95.4 | 90.0 | 93.5 | 🧪 ablation | `fastwam_2026_fast_wam_w_o_video_co_training_ablation` |
| 🟢 WAM | Fast-WAM-IDM | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | No embodied pretraining; 20k steps | all | 98.8 | 97.8 | 97.8 | 97.6 | 98.0 | 🧪 ablation | `fastwam_2026_fast_wam_idm_ablation` |
| 🟢 WAM | Fast-WAM-Joint | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | No embodied pretraining; 20k steps | all | 99.6 | 99.4 | 98.2 | 96.8 | 98.5 | 🧪 ablation | `fastwam_2026_fast_wam_joint_ablation` |
| 🟢 WAM | Fast-WAM-Joint | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 99.2 | 99.2 | 98.4 | 97.6 | 98.6 | baseline | `streaming_wam_2026_fast_wam_joint_baseline` |
| 🟢 WAM | Fast-WAM-Joint-CD | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 99.6 | 100.0 | 98.6 | 97.2 | 98.85 | baseline | `streaming_wam_2026_fast_wam_joint_cd_baseline` |
| 🟢 WAM | Fast-WAM-Optional-IDM | [Fast-WAM release (official)](https://github.com/yuantianyuan01/FastWAM/blob/7faa71108368fbb3b6885649f112af607427a2d4/README.md) · Optional IDM / Inference mode results | Optional-IDM checkpoint; First-frame (Fast-WAM) inference | all | 98.2 | 99.2 | 97.8 | 95.8 | 97.75 | ⭐ main | `fastwam_optional_idm_release_first_frame` |
| 🟢 WAM | Fast-WAM-Optional-IDM | [Fast-WAM release (official)](https://github.com/yuantianyuan01/FastWAM/blob/7faa71108368fbb3b6885649f112af607427a2d4/README.md) · Optional IDM / Inference mode results | Optional-IDM checkpoint; IDM inference; action scheduler shift 1.0 | all | 99.0 | 99.6 | 98.6 | 97.0 | 98.55 | ⭐ main | `fastwam_optional_idm_release_idm` |
| 🟢 WAM | Fast-WAM-RTC | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 92.8 | 93.2 | 91.4 | 79.2 | 89.15 | baseline | `streaming_wam_2026_fast_wam_rtc_baseline` |
| 🟢 WAM | LaWAM | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO fine-tuning | all | 99.4 | 99.6 | 98.4 | 97.0 | 98.6 | ⭐ main | `lawam_2026_lawam_main` |
| 🟢 WAM | LingBot-VA | [LingBot-VA (2026)](https://arxiv.org/pdf/2601.21998v1) · Table 2 | LIBERO fine-tuning | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | ⭐ main | `lingbot_va_2026_lingbot_va_main` |
| 🟢 WAM | LingBot-VA | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | LIBERO comparison as reported in this source | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | baseline | `fastwam_2026_lingbot_va_baseline` |
| 🟢 WAM | LingBot-VA | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | baseline | `lawam_2026_lingbot_va_baseline` |
| 🟢 WAM | Motus | [Fast-WAM (2026)](https://arxiv.org/pdf/2603.16666v1) · Table 2 | LIBERO comparison as reported in this source | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | baseline | `fastwam_2026_motus_baseline` |
| 🟢 WAM | Motus | [LaWAM (2026)](https://arxiv.org/pdf/2606.15768v1) · Table 1 | LIBERO comparison as reported in this source | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | baseline | `lawam_2026_motus_baseline` |
| 🟢 WAM | Motus | [Motus (2025)](https://arxiv.org/pdf/2512.13030v1) · Table 9 | LIBERO-Long only | long | — | — | — | 97.6 | — | ⭐ main | `motus_2025_motus_main` |
| 🟢 WAM | Motus | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | baseline | `streaming_wam_2026_motus_baseline` |
| 🟢 WAM | OA-WAM | [OA-WAM (2026)](https://arxiv.org/pdf/2605.06481v1) · Table 1 | LIBERO fine-tuning | all | 98.9 | 99.0 | 97.4 | 95.9 | 97.8 | ⭐ main | `oawam_2026_oa_wam_main` |
| 🟢 WAM | Streaming-WAM | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO fine-tuning | all | 98.8 | 100.0 | 97.8 | 96.8 | 98.35 | ⭐ main | `streaming_wam_2026_streaming_wam_main` |
| 🟢 WAM | Streaming-WAM w/o Action Conditioning | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 97.2 | 99.2 | 95.4 | 90.2 | 95.5 | 🧪 ablation | `streaming_wam_2026_streaming_wam_w_o_action_conditioning_ablation` |
| 🟢 WAM | Streaming-WAM w/o Slot Encoder | [Streaming-WAM (official)](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) · LIBERO success results | LIBERO comparison as reported in this source | all | 98.4 | 98.0 | 96.4 | 92.6 | 96.35 | 🧪 ablation | `streaming_wam_2026_streaming_wam_w_o_slot_encoder_ablation` |
| ⚪ Reference | Diffusion Policy | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO training from scratch | all | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 | baseline | `openvla_2024_diffusion_policy_baseline` |
| ⚪ Reference | Octo | [OpenVLA (2024)](https://arxiv.org/pdf/2406.09246v3) · Table 12 | LIBERO per-suite fine-tuning | all | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 | baseline | `openvla_2024_octo_baseline` |

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
