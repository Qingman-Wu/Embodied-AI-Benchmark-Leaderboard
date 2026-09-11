# LIBERO 评估协议

本数据库不是统一复现排行榜。只有输入、训练数据、评估环境、trial/seed 口径等一致的记录，才适合直接比较。
每篇论文中的 baseline 必须保留来源身份；论文“比较了某模型”不等于作者重新训练/评估了该模型。

| 来源主方法 | 已确认协议 | 注意事项 |
| --- | --- | --- |
| OpenVLA v3 Table 12 | 每 suite 500 trials，3 seeds；分别训练四 suites；仅第三人称图像 | 全四 suite 每 seed 2000 trials；按原文 SE 保存误差 |
| OpenVLA-OFT v1 Table I | 本文 OpenVLA 变体每 suite 500 trials；完整 OFT 使用 wrist image 与 proprioception | 单图消融与完整 OFT 分开；引用 baseline 不套用主方法 trials |
| SpatialVLA v1 Table III | 3 seeds，每 suite 500 trials；LoRA 与 spatial embedding adaptation | SE 按表转录 |
| Fast-WAM v1 Table 2 | 40 tasks 合计 2000 trials，20k training steps；无 embodied pretraining | seed 数未明确为 null；Joint/IDM/no-video 独立记录 |
| OA-WAM v1 Table 1 / Appendix H | 每 suite 100 episodes，3 seeds | 与 500 trials/suite 的其他方法不同；baseline 为引用结果 |
| LaWAM v1 Table 1 / Appendix D.1 | 40 tasks 合计 2000 trials，每任务 50 trials | baseline 引用与复现混用但表未逐行明确，不统一标为 reproduction |
| LingBot-VA v1 Table 2 / §4.3.2 | 每 suite 每 seed 500 trials，3 seeds | baseline 引自 X-VLA；仅确认 Long checkpoint 发布 |
| Motus v1 Table 9 | 只报告 LIBERO-Long | 不从后续引用回填其他 suite；source_page=15 为 PDF 页序号，印刷页码为附录 3 |
| Streaming-WAM 官网 LIBERO 表 | 每 suite 10 tasks，每 task 50 trials | 官网尚未提供论文；FastWAM-Joint 等结果区别于 Fast-WAM v1 原表 |
| OpenPI 官方 README | π0.5 @ 30k checkpoint | 均值 96.85；其他论文的 96.9 独立保存 |
| Fast-WAM Optional-IDM README | 40 tasks，每 task 50 episodes；action scheduler shift 1.0 | 同 checkpoint 的 IDM/First-frame 两种推理分别记录，区别于论文 IDM 变体 |

不要从相同小数精度推断 trials，不要由均值反推各 suite，不要把 demonstrations 的数量当作 evaluation episodes。
`average` 原值存在四舍五入或统计口径差异时保留并备注；不自动修正。
仅 Long 记录的 `average` 为 null，防止误显示为四套任务总平均。

后续统一复现必须创建 `result_role: reproduction` 新记录，附代码 commit、checkpoint revision、数据版本、环境版本、图像输入、action chunk、seed、每任务 trials 和原始日志链接。
训练/评估配置及硬件尚未核实时可保留 null，不能声称不同来源的数值具有相同复现条件。
