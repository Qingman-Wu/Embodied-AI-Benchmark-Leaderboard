#!/usr/bin/env python3
"""Validate experiment provenance and cross-file integrity using the standard library."""
import argparse
from datetime import date
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCORES = ('spatial', 'object', 'goal', 'long', 'average')
CATEGORIES = ('Open-source VLA', 'Foundation Robot Model', 'World Action Model', 'Reference Policy')
SOURCE_TYPES = ('paper_pdf', 'official_project_page', 'official_github_readme', 'official_hf_model_card')
RELEASE_FIELDS = ('code', 'pretrained_checkpoint', 'libero_checkpoint', 'huggingface', 'evaluation_code')
RELEASE_STATES = (None, 'released', 'announced', 'not_released', 'not_applicable')
REQUIRED = set(('id benchmark suite paper_id paper year model model_type category setting episodes '
                'source_table source_url source_type source_version source_page checkpoint_status '
                'result_role verification_status verified_at notes baseline_list').split()) | set(SCORES)


def is_url(value):
    if not isinstance(value, str):
        return False
    p = urlparse(value)
    return p.scheme in ('http', 'https') and bool(p.netloc)


def is_date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_record(r):
    if not isinstance(r, dict):
        return ['record must be an object']
    errors = [f'missing field: {k}' for k in sorted(REQUIRED - r.keys())]
    for k in ('id', 'paper_id', 'paper', 'model', 'model_type', 'setting'):
        if not isinstance(r.get(k), str) or not r[k].strip():
            errors.append(f'{k} must be nonempty text')
    if not re.fullmatch(r'[a-z0-9][a-z0-9_.-]*', str(r.get('id', ''))):
        errors.append('id must be a stable lowercase identifier')
    for k, allowed in [('benchmark', ('LIBERO',)), ('suite', ('all', 'spatial', 'object', 'goal', 'long')),
                       ('category', CATEGORIES), ('result_role', ('main', 'baseline', 'ablation', 'reproduction')),
                       ('verification_status', ('verified', 'pending')), ('checkpoint_status', RELEASE_STATES)]:
        if r.get(k) not in allowed:
            errors.append(f'invalid {k}: {r.get(k)!r}')
    for k in SCORES:
        v = r.get(k)
        if v is not None and (type(v) not in (int, float) or not math.isfinite(v) or not 0 <= v <= 100):
            errors.append(f'{k} must be a finite percentage in [0, 100] or null')
    uncertainty = r.get('uncertainty')
    if uncertainty is not None:
        if not isinstance(uncertainty, dict) or set(uncertainty) != set(SCORES):
            errors.append('uncertainty must contain all five score keys or be null')
        else:
            for k, v in uncertainty.items():
                if v is not None and (type(v) not in (int, float) or not math.isfinite(v)
                                      or not 0 <= v <= 100 or r.get(k) is None):
                    errors.append(f'invalid uncertainty for {k}')
        if r.get('uncertainty_type') not in ('standard_error', 'standard_deviation', 'reported_plus_minus'):
            errors.append('uncertainty requires an explicit uncertainty_type')
    for k in ('episodes', 'source_page', 'year', 'num_seeds', 'trials_per_task', 'trials_per_suite_per_seed'):
        v = r.get(k)
        if v is not None and (type(v) is not int or v <= 0):
            errors.append(f'{k} must be a positive integer or null')
    if r.get('suite') != 'all':
        if any(r.get(k) is not None for k in SCORES if k != r.get('suite')):
            errors.append('single-suite record must leave other scores and all-suite average null')
    numeric = any(r.get(k) is not None for k in SCORES)
    if numeric:
        if r.get('verification_status') != 'verified':
            errors.append('numeric result must be verified')
        if not is_url(r.get('source_url')):
            errors.append('numeric result requires a source URL')
        if r.get('source_type') not in SOURCE_TYPES:
            errors.append('numeric result requires an allowed primary source type')
        if not is_date(r.get('verified_at')):
            errors.append('numeric result requires an ISO verification date')
        for k in ('source_table', 'source_version'):
            if not isinstance(r.get(k), str) or not r[k].strip() or r[k] in ('Table X', 'Table ?', 'TBD'):
                errors.append(f'numeric result requires a concrete {k}')
        if r.get('source_type') == 'paper_pdf' and r.get('source_page') is None:
            errors.append('paper PDF requires a page locator')
    if not isinstance(r.get('notes'), str):
        errors.append('notes must be text')
    baselines = r.get('baseline_list')
    if not isinstance(baselines, list) or any(not isinstance(x, str) or not x.strip() for x in baselines):
        errors.append('baseline_list must be a list of model names')
    return errors


def validate_records(rows):
    errors, seen = [], set()
    for i, r in enumerate(rows, 1):
        errors.extend(f'row {i}: {e}' for e in validate_record(r))
        if isinstance(r, dict) and isinstance(r.get('id'), str):
            if r['id'] in seen:
                errors.append(f'duplicate id: {r["id"]}')
            seen.add(r['id'])
    return errors


def _unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f'duplicate JSON key: {key}')
        obj[key] = value
    return obj


def read_json(path):
    def reject(value):
        raise ValueError(f'nonstandard JSON number: {value}')
    def parse(text):
        return json.loads(text, parse_constant=reject, object_pairs_hook=_unique_object)
    text = path.read_text(encoding='utf-8')
    if path.suffix == '.jsonl':
        return [parse(line) for line in text.splitlines() if line.strip()]
    obj = parse(text)
    if not isinstance(obj, list):
        raise ValueError(f'{path.name}: expected a JSON array')
    return obj


def validate_database(data_dir, check_projection=True):
    data, errors = {}, []
    for name in ('libero_results.jsonl', 'wam_results.jsonl', 'papers.json', 'model_catalog.json', 'checkpoints.json'):
        try:
            data[name] = read_json(data_dir / name)
        except (OSError, ValueError) as e:
            errors.append(f'{name}: {e}')
    if errors:
        return data, errors
    rows = data['libero_results.jsonl']
    errors.extend(validate_records(rows))
    indexes = {}
    for name, key in [('papers.json', 'id'), ('model_catalog.json', 'model'), ('checkpoints.json', 'model')]:
        index = {}
        for obj in data[name]:
            if not isinstance(obj, dict) or not isinstance(obj.get(key), str) or not obj[key]:
                errors.append(f'{name}: object requires {key}')
                continue
            if obj[key] in index:
                errors.append(f'{name}: duplicate {key}: {obj[key]}')
            index[obj[key]] = obj
        indexes[name] = index
    papers, models, checkpoints = (indexes[n] for n in ('papers.json', 'model_catalog.json', 'checkpoints.json'))
    for r in rows:
        if not isinstance(r, dict):
            continue
        p = papers.get(r.get('paper_id'))
        m = models.get(r.get('model'))
        if p is None:
            errors.append(f'{r.get("id")}: unknown paper_id')
        elif r.get('paper') != p.get('paper') or r.get('year') != p.get('year'):
            errors.append(f'{r.get("id")}: paper title/year mismatch')
        if p is not None:
            for field in ('source_url', 'source_type', 'source_version'):
                if r.get(field) != p.get(field):
                    errors.append(f'{r.get("id")}: {field} differs from source registry')
        if m is None or r.get('category') != m.get('category'):
            errors.append(f'{r.get("id")}: unknown model or category mismatch')
        c = checkpoints.get(r.get('model'))
        if c is None or r.get('checkpoint_status') != c.get('libero_checkpoint'):
            errors.append(f'{r.get("id")}: checkpoint status differs from model audit')
    for model, c in checkpoints.items():
        if model not in models:
            errors.append(f'checkpoint references unknown model: {model}')
        evidence = c.get('evidence', [])
        if not isinstance(evidence, list):
            errors.append(f'{model}: evidence must be a list')
            evidence = []
        for field in RELEASE_FIELDS:
            if field not in c or c[field] not in RELEASE_STATES:
                errors.append(f'{model}: invalid or missing {field}')
            if c.get(field) is not None:
                if not any(isinstance(e, dict) and e.get('field') == field and is_url(e.get('url'))
                           and e.get('locator') for e in evidence):
                    errors.append(f'{model}: {field} requires field-specific evidence')
                if not is_date(c.get('verified_at')):
                    errors.append(f'{model}: release audit requires verified_at')
        if c.get('reproduce_level') not in (None, 'easy', 'moderate', 'hard'):
            errors.append(f'{model}: invalid reproduce_level')
    for model, m in models.items():
        if m.get('category') not in CATEGORIES or model not in checkpoints:
            errors.append(f'{model}: invalid category or missing checkpoint audit')
    expected = [r for r in rows if isinstance(r, dict) and r.get('category') == 'World Action Model']
    if check_projection and data['wam_results.jsonl'] != expected:
        errors.append('wam_results.jsonl is stale; run scripts/generate_leaderboard.py')
    return data, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=ROOT/'data')
    args = parser.parse_args()
    data, errors = validate_database(args.data_dir)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Validated {len(data["libero_results.jsonl"])} LIBERO records, {len(data["wam_results.jsonl"])} WAM records.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
