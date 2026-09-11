#!/usr/bin/env python3
"""Generate one unified, provenance-preserving Markdown table; never impute or rank."""
import argparse
import json
from pathlib import Path
import sys
from validate_json import ROOT, CATEGORIES, SCORES, validate_database

BEGIN, END = '<!-- leaderboard:start -->', '<!-- leaderboard:end -->'
TRACKS = dict(zip(CATEGORIES, ('Track 1 · VLA', 'Track 2 · Foundation',
                              'Track 3 · WAM', 'Reference')))
CATEGORY_MARK = {
    'Open-source VLA': '🔵 VLA',
    'Foundation Robot Model': '🟣 Foundation',
    'World Action Model': '🟢 WAM',
    'Reference Policy': '⚪ Reference',
}
SOURCE_LABELS = {
    'openvla_2024': 'OpenVLA (2024)', 'openvla_oft_2025': 'OpenVLA-OFT (2025)',
    'spatialvla_2025': 'SpatialVLA (2025)', 'fastwam_2026': 'Fast-WAM (2026)',
    'oawam_2026': 'OA-WAM (2026)', 'lawam_2026': 'LaWAM (2026)',
    'motus_2025': 'Motus (2025)', 'lingbot_va_2026': 'LingBot-VA (2026)',
    'streaming_wam_2026': 'Streaming-WAM (official)',
    'openpi_release_2026': 'OpenPI (official)',
    'fastwam_optional_idm_release_2026': 'Fast-WAM release (official)',
}


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')


def score(value):
    return '—' if value is None else str(value)


def render_results(rows):
    lines = ['# LIBERO Leaderboard', '',
             '统一实验表：每行是一个“来源论文/官方报告 × 模型 × 设置”。同名模型的不同来源结果保留为不同 row；不做跨协议总排名。',
             '', '图例：🔵 VLA　🟣 Foundation Robot Model　🟢 World Action Model　⚪ Reference Policy；`—` 表示 null。',
             '', '| Track | Model | Paper / source | Setting | Suite | Spatial | Object | Goal | Long | Average | Role | 备注 | Record ID |',
             '| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |']
    ordered = sorted(rows, key=lambda r: (CATEGORIES.index(r['category']) if r['category'] in CATEGORIES else 99,
                                          r['model'].lower(), r['paper'].lower(), r['setting'].lower(), r['id']))
    for r in ordered:
        source = '—' if not r['source_url'] else f'[{SOURCE_LABELS.get(r["paper_id"], cell(r["paper"]))}]({r["source_url"]}) · {cell(r["source_table"])}'
        cols = [CATEGORY_MARK.get(r['category'], '⚪ '+cell(r['category'])), cell(r['model']), source,
                cell(r['setting']), r['suite']]
        cols += [score(r[k]) for k in SCORES]
        role_mark = {'main': '⭐ main', 'baseline': 'baseline', 'ablation': '🧪 ablation', 'reproduction': '🔁 reproduction'}
        cols += [role_mark.get(r['result_role'], r['result_role']), cell(r.get('notes', '')), '`'+r['id']+'`']
        lines.append('| '+' | '.join(cols)+' |')
    return '\n'.join(lines)+'\n'


def render_wam(rows, checkpoints):
    lines = ['# WAM Comparison', '', '这是 LIBERO 实验的 WAM 子集。Baseline 名称来自该结果所在来源；发布状态来自独立审计，null 不代表未发布。', '',
             '| Record ID | Model | Source / role | Average (%) | LIBERO checkpoint | Baselines |',
             '| --- | --- | --- | ---: | --- | --- |']
    for r in rows:
        lines.append('| '+' | '.join(['`'+r['id']+'`', cell(r['model']),
            f'[{cell(r["paper"])} · {r["result_role"]}]({r["source_url"]})', score(r['average']),
            str(checkpoints[r['model']]['libero_checkpoint'] or '—'), cell(', '.join(r['baseline_list'])) or '—'])+' |')
    return '\n'.join(lines)+'\n'


def generate(root, check=False):
    data, errors = validate_database(root/'data', check_projection=False)
    if errors:
        raise ValueError('\n'.join(errors))
    rows = data['libero_results.jsonl']
    wam = [r for r in rows if r['category'] == 'World Action Model']
    md = render_results(rows)
    readme = (root/'README.md').read_text(encoding='utf-8')
    if readme.count(BEGIN) != 1 or readme.count(END) != 1 or readme.index(BEGIN) >= readme.index(END):
        raise ValueError('README requires one ordered leaderboard marker pair')
    # Keep the same single table visible in README under the marker.
    embedded = '\n'.join(md.splitlines()[2:])
    readme = readme.split(BEGIN)[0]+BEGIN+'\n\n'+embedded+'\n\n'+END+readme.split(END)[1]
    outputs = {root/'tables/libero_leaderboard.md': md,
               root/'tables/wam_comparison.md': render_wam(wam, {c['model']:c for c in data['checkpoints.json']}),
               root/'data/wam_results.jsonl': ''.join(json.dumps(r, ensure_ascii=False, allow_nan=False)+'\n' for r in wam),
               root/'README.md': readme}
    stale = []
    for path, content in outputs.items():
        if not path.exists() or path.read_text(encoding='utf-8') != content:
            stale.append(str(path.relative_to(root)))
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
    if check and stale:
        raise ValueError('Stale generated files: '+', '.join(stale))
    return len(rows), len(wam)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        total, wam = generate(args.root.resolve(), args.check)
    except (OSError, ValueError) as e:
        print(e, file=sys.stderr)
        return 1
    print(f'{"Checked" if args.check else "Generated"} {total} LIBERO / {wam} WAM records.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
