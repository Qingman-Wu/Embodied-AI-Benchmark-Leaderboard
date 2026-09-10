# LIBERO Leaderboard

数值为来源报告的成功率（%）；— 表示 null。按模型类别及来源分组，不做跨协议总排名。
同名模型在不同来源/设置中分别保留；完整协议、baseline_list 和核验信息见 data/libero_results.jsonl。

## Track 1 · LIBERO VLA

### Fast-WAM: Do World Action Models Need Test-time Future Imagination?

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `fastwam_2026_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |

### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lawam_2026_openvla_oft_baseline` | OpenVLA-OFT / LIBERO comparison as reported in this source | baseline | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |

### Causal World Modeling for Robot Control

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lingbot_va_2026_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |
| `lingbot_va_2026_openvla_oft_baseline` | OpenVLA-OFT / LIBERO comparison as reported in this source | baseline | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |
| `lingbot_va_2026_spatialvla_baseline` | SpatialVLA / LIBERO comparison as reported in this source | baseline | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |

### Motus: A Unified Latent Action World Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `motus_2025_openvla_oft_baseline` | OpenVLA-OFT / LIBERO-Long only | baseline | long | — | — | — | 94.5 | — | [Table 9](https://arxiv.org/pdf/2512.13030v1) |

### OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `oawam_2026_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table 1](https://arxiv.org/pdf/2605.06481v1) |
| `oawam_2026_spatialvla_baseline` | SpatialVLA / LIBERO comparison as reported in this source | baseline | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | [Table 1](https://arxiv.org/pdf/2605.06481v1) |

### OpenVLA: An Open-Source Vision-Language-Action Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `openvla_2024_openvla` | OpenVLA / LIBERO per-suite fine-tuning | main | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table 12](https://arxiv.org/pdf/2406.09246v3) |

### Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `openvla_oft_2025_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table I](https://arxiv.org/pdf/2502.19645v1) |
| `openvla_oft_2025_openvla_oft_main` | OpenVLA-OFT / OFT + wrist camera + proprioception | main | all | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 | [Table I](https://arxiv.org/pdf/2502.19645v1) |
| `openvla_oft_2025_pd_ac` | OpenVLA / pd_ac; third-person image + language | ablation | all | 91.3 | 92.7 | 90.5 | 86.5 | 90.2 | [Table I](https://arxiv.org/pdf/2502.19645v1) |
| `openvla_oft_2025_pd_ac_cont_diffusion` | OpenVLA / pd_ac_cont_diffusion; third-person image + language | ablation | all | 96.9 | 98.1 | 95.5 | 91.1 | 95.4 | [Table I](https://arxiv.org/pdf/2502.19645v1) |
| `openvla_oft_2025_pd_ac_cont_l1` | OpenVLA / pd_ac_cont_l1; third-person image + language | ablation | all | 96.2 | 98.3 | 96.2 | 90.7 | 95.3 | [Table I](https://arxiv.org/pdf/2502.19645v1) |

### SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `spatialvla_2025_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [Table III](https://arxiv.org/pdf/2501.15830v1) |
| `spatialvla_2025_spatialvla_main` | SpatialVLA / LoRA + spatial embedding adaptation | main | all | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 | [Table III](https://arxiv.org/pdf/2501.15830v1) |

### Streaming Your World-Action Model for Real-Time Robot Manipulation.

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `streaming_wam_2026_openvla_baseline` | OpenVLA / LIBERO comparison as reported in this source | baseline | all | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |

## Track 2 · Foundation Robot Model

### Fast-WAM: Do World Action Models Need Test-time Future Imagination?

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `fastwam_2026_pi0_5_baseline` | π0.5 / LIBERO comparison as reported in this source | baseline | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |

### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lawam_2026_gr00t_n1_6_baseline` | GR00T-N1.6 / LIBERO comparison as reported in this source | baseline | all | 97.7 | 98.5 | 97.5 | 94.4 | 97.0 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |
| `lawam_2026_pi0_5_baseline` | π0.5 / LIBERO comparison as reported in this source | baseline | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |
| `lawam_2026_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 98.0 | 96.8 | 94.4 | 88.4 | 94.4 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |

### Causal World Modeling for Robot Control

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lingbot_va_2026_gr00t_n1_baseline` | GR00T-N1 / LIBERO comparison as reported in this source | baseline | all | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |
| `lingbot_va_2026_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |

### Motus: A Unified Latent Action World Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `motus_2025_gr00t_n1_baseline` | GR00T-N1 / LIBERO-Long only | baseline | long | — | — | — | 90.6 | — | [Table 9](https://arxiv.org/pdf/2512.13030v1) |
| `motus_2025_pi0_baseline` | π0 / LIBERO-Long only | baseline | long | — | — | — | 85.2 | — | [Table 9](https://arxiv.org/pdf/2512.13030v1) |

### OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `oawam_2026_pi0_5_baseline` | π0.5 / LIBERO comparison as reported in this source | baseline | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | [Table 1](https://arxiv.org/pdf/2605.06481v1) |
| `oawam_2026_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 | [Table 1](https://arxiv.org/pdf/2605.06481v1) |

### OpenPI official LIBERO benchmark results

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `openpi_release_pi05_30k` | π0.5 / pi05_libero; 30k fine-tuned checkpoint | main | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.85 | [LIBERO Benchmark results](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/README.md) |

### Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `openvla_oft_2025_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 | [Table I](https://arxiv.org/pdf/2502.19645v1) |

### Streaming Your World-Action Model for Real-Time Robot Manipulation.

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `streaming_wam_2026_pi0_5_baseline` | π0.5 / LIBERO comparison as reported in this source | baseline | all | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_pi0_baseline` | π0 / LIBERO comparison as reported in this source | baseline | all | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |

## Track 3 · World Action Model

### Fast-WAM: Do World Action Models Need Test-time Future Imagination?

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `fastwam_2026_fast_wam_idm_ablation` | Fast-WAM-IDM / No embodied pretraining; 20k steps | ablation | all | 98.8 | 97.8 | 97.8 | 97.6 | 98.0 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_fast_wam_joint_ablation` | Fast-WAM-Joint / No embodied pretraining; 20k steps | ablation | all | 99.6 | 99.4 | 98.2 | 96.8 | 98.5 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_fast_wam_main` | Fast-WAM / No embodied pretraining; 20k steps | main | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_fast_wam_w_o_video_co_training_ablation` | Fast-WAM w/o video co-training / No embodied pretraining; 20k steps | ablation | all | 89.2 | 99.2 | 95.4 | 90.0 | 93.5 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_lingbot_va_baseline` | LingBot-VA / LIBERO comparison as reported in this source | baseline | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |
| `fastwam_2026_motus_baseline` | Motus / LIBERO comparison as reported in this source | baseline | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | [Table 2](https://arxiv.org/pdf/2603.16666v1) |

### Fast-WAM official Optional-IDM release results

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `fastwam_optional_idm_release_first_frame` | Fast-WAM-Optional-IDM / Optional-IDM checkpoint; First-frame (Fast-WAM) inference | main | all | 98.2 | 99.2 | 97.8 | 95.8 | 97.75 | [Optional IDM / Inference mode results](https://github.com/yuantianyuan01/FastWAM/blob/7faa71108368fbb3b6885649f112af607427a2d4/README.md) |
| `fastwam_optional_idm_release_idm` | Fast-WAM-Optional-IDM / Optional-IDM checkpoint; IDM inference; action scheduler shift 1.0 | main | all | 99.0 | 99.6 | 98.6 | 97.0 | 98.55 | [Optional IDM / Inference mode results](https://github.com/yuantianyuan01/FastWAM/blob/7faa71108368fbb3b6885649f112af607427a2d4/README.md) |

### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lawam_2026_fast_wam_baseline` | Fast-WAM / LIBERO comparison as reported in this source | baseline | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |
| `lawam_2026_lawam_main` | LaWAM / LIBERO fine-tuning | main | all | 99.4 | 99.6 | 98.4 | 97.0 | 98.6 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |
| `lawam_2026_lingbot_va_baseline` | LingBot-VA / LIBERO comparison as reported in this source | baseline | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |
| `lawam_2026_motus_baseline` | Motus / LIBERO comparison as reported in this source | baseline | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | [Table 1](https://arxiv.org/pdf/2606.15768v1) |

### Causal World Modeling for Robot Control

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `lingbot_va_2026_lingbot_va_main` | LingBot-VA / LIBERO fine-tuning | main | all | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 | [Table 2](https://arxiv.org/pdf/2601.21998v1) |

### Motus: A Unified Latent Action World Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `motus_2025_motus_main` | Motus / LIBERO-Long only | main | long | — | — | — | 97.6 | — | [Table 9](https://arxiv.org/pdf/2512.13030v1) |

### OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `oawam_2026_oa_wam_main` | OA-WAM / LIBERO fine-tuning | main | all | 98.9 | 99.0 | 97.4 | 95.9 | 97.8 | [Table 1](https://arxiv.org/pdf/2605.06481v1) |

### Streaming Your World-Action Model for Real-Time Robot Manipulation.

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `streaming_wam_2026_fast_wam_baseline` | Fast-WAM / LIBERO comparison as reported in this source | baseline | all | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_fast_wam_joint_baseline` | Fast-WAM-Joint / LIBERO comparison as reported in this source | baseline | all | 99.2 | 99.2 | 98.4 | 97.6 | 98.6 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_fast_wam_joint_cd_baseline` | Fast-WAM-Joint-CD / LIBERO comparison as reported in this source | baseline | all | 99.6 | 100.0 | 98.6 | 97.2 | 98.85 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_fast_wam_rtc_baseline` | Fast-WAM-RTC / LIBERO comparison as reported in this source | baseline | all | 92.8 | 93.2 | 91.4 | 79.2 | 89.15 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_motus_baseline` | Motus / LIBERO comparison as reported in this source | baseline | all | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_streaming_wam_main` | Streaming-WAM / LIBERO fine-tuning | main | all | 98.8 | 100.0 | 97.8 | 96.8 | 98.35 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_streaming_wam_w_o_action_conditioning_ablation` | Streaming-WAM w/o Action Conditioning / LIBERO comparison as reported in this source | ablation | all | 97.2 | 99.2 | 95.4 | 90.2 | 95.5 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |
| `streaming_wam_2026_streaming_wam_w_o_slot_encoder_ablation` | Streaming-WAM w/o Slot Encoder / LIBERO comparison as reported in this source | ablation | all | 98.4 | 98.0 | 96.4 | 92.6 | 96.35 | [LIBERO success results](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) |

## Reference · Classical / Generalist Policies

### OpenVLA: An Open-Source Vision-Language-Action Model

| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `openvla_2024_diffusion_policy_baseline` | Diffusion Policy / LIBERO training from scratch | baseline | all | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 | [Table 12](https://arxiv.org/pdf/2406.09246v3) |
| `openvla_2024_octo_baseline` | Octo / LIBERO per-suite fine-tuning | baseline | all | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 | [Table 12](https://arxiv.org/pdf/2406.09246v3) |
