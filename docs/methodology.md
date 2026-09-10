# LIBERO Leaderboard Methodology

## Objective

Build a reproducible database of embodied AI benchmark results.

## Record Policy

Each experiment is stored independently.

A model appearing in multiple papers will have multiple records if the evaluation settings differ.

## Required Information

- Paper
- Model
- Year
- Benchmark suite
- Training setting
- Success rates
- Number of episodes
- Source table or appendix
- Checkpoint availability

## Comparison Rules

Results should not be directly merged when they differ in:

- training data
- fine-tuning protocol
- evaluation protocol
- number of episodes
- environment version

## Verification

Unknown values remain unknown until verified from primary sources.
