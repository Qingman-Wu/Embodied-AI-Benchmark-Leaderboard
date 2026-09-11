# WAM Comparison

这是 LIBERO 实验的 WAM 子集。Baseline 名称来自该结果所在来源；发布状态来自独立审计，null 不代表未发布。

| Record ID | Model | Source / role | Average (%) | LIBERO checkpoint | Baselines |
| --- | --- | --- | ---: | --- | --- |
| `fastwam_2026_fast_wam_main` | Fast-WAM | [Fast-WAM: Do World Action Models Need Test-time Future Imagination? · main](https://arxiv.org/pdf/2603.16666v1) | 97.6 | released | OpenVLA, π0, π0.5, LingBot-VA, Motus |
| `oawam_2026_oa_wam_main` | OA-WAM | [OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation · main](https://arxiv.org/pdf/2605.06481v1) | 97.8 | — | OpenVLA, SpatialVLA, π0, π0.5, InternVLA-M1, CogACT, F1-VLA, MemoryVLA, VLA-JEPA, CoWVLA, ThinkAct, VITA |
| `lawam_2026_lawam_main` | LaWAM | [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies · main](https://arxiv.org/pdf/2606.15768v1) | 98.6 | released | OpenVLA-OFT, π0, π0.5, GR00T-N1.6, LAPA, UniVLA, Mantis, VLA-JEPA, F1, Motus, Cosmos-Policy, LingBot-VA, Fast-WAM |
| `lingbot_va_2026_lingbot_va_main` | LingBot-VA | [Causal World Modeling for Robot Control · main](https://arxiv.org/pdf/2601.21998v1) | 98.5 | released | Octo, Seer, MoDE, SuSIE, SpatialVLA, TraceVLA, CoT-VLA, ThinkAct, SmolVLA, CronusVLA, FLOWER, GR00T-N1, π0, π0 + FAST, OpenVLA, OpenVLA-OFT, DD-VLA, UniVLA, X-VLA |
| `motus_2025_motus_main` | Motus | [Motus: A Unified Latent Action World Model · main](https://arxiv.org/pdf/2512.13030v1) | — | — | π0, GR00T-N1, UniVLA, OpenVLA-OFT, X-VLA |
| `streaming_wam_2026_streaming_wam_main` | Streaming-WAM | [Streaming Your World-Action Model for Real-Time Robot Manipulation. · main](https://sjtu-deng-lab.github.io/Streaming-WAM/#results) | 98.35 | released | OpenVLA, π0, π0.5, Motus, Fast-WAM, Fast-WAM-RTC, Fast-WAM-Joint, Fast-WAM-Joint-CD |
