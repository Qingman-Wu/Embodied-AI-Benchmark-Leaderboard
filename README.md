# Embodied-AI-Benchmark-Leaderboard

A continuously maintained benchmark database for embodied AI models, with a focus on Vision-Language-Action (VLA) models and robot policies.

## Current Focus

### LIBERO Leaderboard

This repository currently starts with a systematic collection of LIBERO benchmark results reported in embodied AI papers.

The goal is not only to rank models, but to preserve:

- original paper-reported results
- evaluation settings
- compared baselines
- checkpoint availability
- reproducibility information

## Data Organization

```
.
├── data/
│   ├── libero_results.jsonl        # Experiment-level benchmark records
│   ├── papers.json                 # Paper metadata
│   └── checkpoints.json            # Release status audit
│
├── docs/
│   └── methodology.md              # Data collection rules
│
└── README.md
```

## LIBERO Evaluation Suites

We track the standard LIBERO suites:

- LIBERO-Spatial
- LIBERO-Object
- LIBERO-Goal
- LIBERO-Long

## Data Principles

1. Every reported number should be traceable to a paper, appendix, official project page, or released evaluation result.
2. Results from different papers are stored separately even for the same model.
3. Different training settings are not merged.
4. Missing information is marked as unknown instead of estimated.

## Planned Coverage

- Classical policies
  - ACT
  - Diffusion Policy
  - BC-Z

- Generalist robot policies
  - Octo

- Vision-Language-Action models
  - OpenVLA
  - OpenVLA-OFT
  - π0 / π0.5
  - GR00T
  - RoboMamba
  - CogACT
  - SpatialVLA
  - VLA-JEPA
  - WorldVLA

## Status

🚧 LIBERO database construction in progress.
