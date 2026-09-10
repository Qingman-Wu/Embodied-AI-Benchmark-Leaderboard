#!/usr/bin/env python3
"""Generate source-grouped Markdown and the WAM projection; never impute or rank."""
import argparse
import json
from pathlib import Path
import sys
from validate_json import ROOT, CATEGORIES, SCORES, validate_database

BEGIN, END = '<!-- leaderboard:start -->', '<!-- leaderboard:end -->'
TRACKS = dict(zip(CATEGORIES, ('Track 1 · LIBERO VLA', 'Track 2 · Foundation Robot Model',
                              'Track 3 · World Action Model', 'Reference · Classical / Generalist Policies')))


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')


def score(value):
    return '—' if value is None else str(value)


def render_results(rows):
    lines = ['# LIBERO Leaderboard', '', '数值为来源报告的成功率（%）；— 表示 null。按模型类别及来源分组，不做跨协议总排名。',
             '同名模型在不同来源/设置中分别保留；完整协议、baseline_list 和核验信息见 data/libero_results.jsonl。', '']
    for category in CATEGORIES:
        selected = [r for r in rows if r['category'] == category]
        if not selected:
            continue
        lines += ['## '+TRACKS[category], '']
        for pid in sorted({r['paper_id'] for r in selected}):
            group = [r for r in selected if r['paper_id'] == pid]
            lines += ['### '+cell(group[0]['paper']), '',
                      '| Record ID | Model / setting | Role | Suite | Spatial | Object | Goal | Long | Average | Source |',
                      '| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |']
            for r in sorted(group, key=lambda x:x['id']):
                source = '—' if not r['source_url'] else f'[{cell(r["source_table"])}]({r["source_url"]})'
                cols = ['`'+r['id']+'`', cell(r['model'])+' / '+cell(r['setting']), r['result_role'], r['suite']]
                cols += [score(r[k]) for k in SCORES] + [source]
                lines.append('| '+' | '.join(cols)+' |')
            lines.append('')
    return '\n'.join(lines).rstrip()+'\n'


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
    # Keep all rows visible in README; shift generated headings under LIBERO Leaderboard.
    embedded = '\n'.join('#'+line if line.startswith('#') else line for line in md.splitlines()[2:])
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
