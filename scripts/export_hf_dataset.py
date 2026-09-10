#!/usr/bin/env python3
"""Export a local Hugging Face dataset package; no network upload is performed."""
import argparse
from pathlib import Path
import shutil
import sys
from validate_json import ROOT, SCORES, validate_database


def write_parquet(rows, path):
    """Typed Parquet avoids the JSON loader's implicit date-to-timestamp conversion."""
    import pyarrow as pa
    import pyarrow.parquet as pq
    integers = {'year', 'episodes', 'num_seeds', 'trials_per_task',
                'trials_per_suite_per_seed', 'source_page'}
    fields = []
    for key in dict.fromkeys(key for row in rows for key in row):
        if key == 'baseline_list':
            dtype = pa.list_(pa.string())
        elif key == 'uncertainty':
            dtype = pa.struct([(score, pa.float64()) for score in SCORES])
        else:
            dtype = pa.float64() if key in SCORES else pa.int64() if key in integers else pa.string()
        fields.append(pa.field(key, dtype))
    pq.write_table(pa.Table.from_pylist(rows, schema=pa.schema(fields)), path)

CARD = '''---
language:
- zh
- en
task_categories:
- tabular-regression
pretty_name: Embodied AI Benchmark Leaderboard
configs:
- config_name: libero
  default: true
  data_files:
  - split: train
    path: libero_results.parquet
- config_name: wam
  data_files:
  - split: train
    path: wam_results.parquet
---
# Embodied-AI-Benchmark-Leaderboard

LIBERO VLA / WAM 论文实验记录。每行是独立的来源报告，不是统一复现或全局排名。
`train` 是数据分发 split 名，不表示机器人训练轨迹；数值单位为百分比。
`null` 表示无法确认/未报告。`average` 仅存来源报告均值，不自动计算。

默认加载 LIBERO；WAM config 是同一数据库的子集，二者不可合并计数。

```python
from datasets import load_dataset
results = load_dataset("Qingman-Wu/Embodied-AI-Benchmark-Leaderboard")
wam = load_dataset("Qingman-Wu/Embodied-AI-Benchmark-Leaderboard", "wam")
```

以上远程调用需要维护者先发布本数据包；本地可用 `load_dataset("/absolute/export/path")`。
附带 `papers.json`、`checkpoints.json`、`model_catalog.json` 为 JSON 数组元数据，使用 json.load 读取。
原始 JSONL 按字节保留；默认加载同内容的 typed Parquet，防止 JSON reader 自动改写日期字符串。
source_url/source_table/source_version/source_page 可追溯实验；verified_at 是来源核验日期。
result_role 区分 main、baseline、ablation、reproduction。checkpoint_status 指模型级 LIBERO 权重可用性，
不保证与每条论文成绩一一对应。完整方法与贡献流程见 [GitHub](https://github.com/Qingman-Wu/Embodied-AI-Benchmark-Leaderboard)。

本数据包不包含模型权重或机器人轨迹；引用结果时请引用 source_url 对应原作。
数据与代码再分发许可尚待维护者明确；不继承或替代原论文/模型许可。
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=ROOT/'data')
    parser.add_argument('--output-dir', type=Path, default=ROOT/'dist/hf_dataset')
    args = parser.parse_args()
    data, errors = validate_database(args.data_dir)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    try:
        import pyarrow  # noqa: F401; check the optional export dependency before writing
    except ImportError:
        print('HF export requires pyarrow: pip install -r requirements-hf.txt', file=sys.stderr)
        return 1
    dest = args.output_dir.resolve()
    # Prevent an export from overwriting repository source or documentation.
    if dest == ROOT or dest in ROOT.parents or dest == args.data_dir.resolve():
        print('Choose a separate export directory.', file=sys.stderr)
        return 1
    dest.mkdir(parents=True, exist_ok=True)
    for name in data:
        shutil.copyfile(args.data_dir/name, dest/name)
    for name in ('libero_results', 'wam_results'):
        write_parquet(data[name+'.jsonl'], dest/(name+'.parquet'))
    (dest/'README.md').write_text(CARD, encoding='utf-8')
    print(f'Exported {len(data["libero_results.jsonl"])} records to {dest}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
