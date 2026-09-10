# 官方来源与核验记录

本阶段核验日期：2026-09-10。8 份版本化论文 PDF 均已下载、提取表格并渲染对应页进行视觉核对；官方网页/README 单独标注来源类型。
原始来源的完整 SHA-256 见 `papers.json`；具体 baseline 成绩归属于出现它的报告，不能冒充模型原论文结果。

| Source ID | 来源 | 表/栏目 | PDF 页序号 | 版本 |
| --- | --- | --- | --- | --- |
| `openvla_2024` | [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/pdf/2406.09246v3) | Table 12 | 37 | `2406.09246v3` |
| `openvla_oft_2025` | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/pdf/2502.19645v1) | Table I | 6 | `2502.19645v1` |
| `spatialvla_2025` | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/pdf/2501.15830v1) | Table III | 8 | `2501.15830v1` |
| `fastwam_2026` | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/pdf/2603.16666v1) | Table 2 | 8 | `2603.16666v1` |
| `oawam_2026` | [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation](https://arxiv.org/pdf/2605.06481v1) | Table 1 | 7 | `2605.06481v1` |
| `lawam_2026` | [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/pdf/2606.15768v1) | Table 1 | 6 | `2606.15768v1` |
| `motus_2025` | [Motus: A Unified Latent Action World Model](https://arxiv.org/pdf/2512.13030v1) | Table 9 | 15 | `2512.13030v1` |
| `lingbot_va_2026` | [Causal World Modeling for Robot Control](https://arxiv.org/pdf/2601.21998v1) | Table 2 | 14 | `2601.21998v1` |
| `streaming_wam_2026` | [Streaming Your World-Action Model for Real-Time Robot Manipulation.](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) | LIBERO success results | — | `accessed 2026-09-10` |
| `openpi_release_2026` | [OpenPI official LIBERO benchmark results](https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/examples/libero/README.md) | LIBERO Benchmark results | — | `215abfb217dbac7d5f1273282331b9b1866c0479` |
| `fastwam_optional_idm_release_2026` | [Fast-WAM official Optional-IDM release results](https://github.com/yuantianyuan01/FastWAM/blob/7faa71108368fbb3b6885649f112af607427a2d4/README.md) | Optional IDM / Inference mode results | — | `7faa71108368fbb3b6885649f112af607427a2d4` |

## 已知差异与待审核项

- π0：OpenVLA-OFT/OA-WAM 报告 94.2，Fast-WAM/LingBot-VA/Streaming-WAM 报告 94.1；LaWAM 中的 π0 分项本身也不同。均按来源分别保存。
- π0.5：OpenPI 官方 README 原始均值 96.85；论文 baseline 常为 96.9，不互相覆盖。
- Motus：v1 原论文 Table 9 只有 Long；四 suite 97.7 的引用记录归属于 Fast-WAM、LaWAM 或 Streaming-WAM。
- Fast-WAM-Joint：原论文 98.5，Streaming-WAM 官网 98.60；后者不是前者的勘误。
- Fast-WAM Optional-IDM：官方后续 release 两种 inference mode 为独立记录，不覆盖 v1 Fast-WAM-IDM。
- Streaming-WAM：官方项目页和模型卡可见，technical report 仍标 Coming Soon。
- GR00T-N1.6：本版采用 LaWAM 的 Table 1 baseline。[官方 release-tag LIBERO README](https://github.com/NVIDIA/Isaac-GR00T/blob/n1.6-release/examples/LIBERO/README.md) 的计数和括号百分比存在不一致（如 Spatial 的 195/200 与 97.65%）；此官方表暂不新增为数值记录，等待研究审核。N1.7 不是 N1/N1.6 的同名更新记录。
- Fast-WAM-H3 / VLA-JEPA：本阶段只保留未来收录入口，不虚构实验行。
- 不把 OA-WAM 的第三方 reproduction repo 当作官方开源项目；未确认的代码/权重保持 null。

## 发布审计摘要

`released` 表示核验到官方链接/权重文件索引，未执行下载与仿真复现。每字段证据 URL、文件定位、suite 范围见 [checkpoints.json](../data/checkpoints.json)。

| Model | Code | Pretrained | LIBERO checkpoint | HF | LIBERO evaluation code | Confirmed suites |
| --- | --- | --- | --- | --- | --- | --- |
| OpenVLA | released | released | released | released | released | spatial, object, goal, long |
| OpenVLA-OFT | released | — | released | released | released | spatial |
| SpatialVLA | released | released | — | released | — | — |
| π0 | released | released | — | — | released | — |
| π0.5 | released | released | released | — | released | spatial, object, goal, long |
| GR00T-N1 | released | released | — | released | — | — |
| GR00T-N1.6 | released | released | — | released | released | — |
| Fast-WAM | released | — | released | released | released | spatial, object, goal, long |
| Streaming-WAM | released | — | released | released | released | spatial, object, goal, long |
| OA-WAM | — | — | — | — | — | — |
| LaWAM | released | released | released | released | released | spatial, object, goal, long |
| LingBot-VA | released | released | released | released | released | long |
| Motus | released | released | — | released | — | — |
| Fast-WAM-Joint-CD | released | — | released | released | released | spatial, object, goal, long |
| Fast-WAM-Optional-IDM | released | — | released | released | released | spatial, object, goal, long |

未列出的模型/变体仍保留目录与 null 审计记录；父模型发布状态不会自动赋给子变体。发布状态会随时间变化，核验日期不是永久保证。
