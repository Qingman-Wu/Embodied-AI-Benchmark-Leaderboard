"""Guard scientific provenance, independent experiments, and reproducible exports."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

def record(**changes):
    r = dict(id='example_main', benchmark='LIBERO', suite='all', paper_id='example',
             paper='Example', year=2026, model='Example', model_type='VLA',
             category='Open-source VLA', setting='LIBERO fine-tuning',
             spatial=80.0, object=90.0, goal=None, long=70.0, average=None,
             episodes=None, source_table='Table 1', source_url='https://arxiv.org/pdf/2601.00001v1',
             source_type='paper_pdf', source_version='v1', source_page=3,
             checkpoint_status=None, result_role='main', verification_status='verified',
             verified_at='2026-09-10', notes='', baseline_list=[])
    r.update(changes)
    return r

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec('validate_json'), 'validator not implemented')
        import validate_json
        self.v = validate_json

    def test_null_scores_remain_valid(self):
        self.assertEqual(self.v.validate_record(record()), [])

    def test_scores_reject_bool_nan_infinity_range_and_strings(self):
        for x in (True, float('nan'), float('inf'), -0.1, 100.1, '80'):
            with self.subTest(x=x):
                self.assertTrue(self.v.validate_record(record(spatial=x)))

    def test_numeric_result_requires_locator_url_and_verification(self):
        for patch in ({'source_url': None}, {'source_table': None},
                      {'source_table': 'Table X'}, {'verified_at': None},
                      {'source_type': 'blog'}, {'verification_status': 'pending'}):
            with self.subTest(patch=patch):
                self.assertTrue(self.v.validate_record(record(**patch)))

    def test_long_only_cannot_claim_all_suite_average(self):
        self.assertTrue(self.v.validate_record(record(suite='long', spatial=None, object=None, average=70)))
        self.assertEqual(self.v.validate_record(record(suite='long', spatial=None, object=None)), [])

    def test_duplicate_ids_fail_but_cross_paper_model_does_not_merge(self):
        self.assertTrue(self.v.validate_records([record(), record()]))
        self.assertEqual(self.v.validate_records([record(), record(id='other_baseline', paper_id='other', paper='Other', result_role='baseline')]), [])

    def test_source_registry_must_match_record_provenance(self):
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)
            for name in ('libero_results.jsonl', 'wam_results.jsonl', 'papers.json', 'model_catalog.json', 'checkpoints.json'):
                (dest/name).write_bytes((ROOT/'data'/name).read_bytes())
            papers = json.loads((dest/'papers.json').read_text())
            papers[0]['source_url'] = 'https://arxiv.org/pdf/9999.00001v1'
            (dest/'papers.json').write_text(json.dumps(papers))
            _, errors = self.v.validate_database(dest)
            self.assertTrue(errors, 'source registry disagreement must fail')

    def test_invalid_uncertainty_is_rejected(self):
        self.assertTrue(self.v.validate_record(record(uncertainty={'spatial': -1}, uncertainty_type='standard_error')))

    def test_duplicate_json_keys_and_stale_wam_are_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            dest = Path(d)
            bad = dest/'bad.json'
            bad.write_text('[{"id":"a","id":"b"}]')
            with self.assertRaises(ValueError):
                self.v.read_json(bad)
            for name in ('libero_results.jsonl', 'wam_results.jsonl', 'papers.json', 'model_catalog.json', 'checkpoints.json'):
                (dest/name).write_bytes((ROOT/'data'/name).read_bytes())
            (dest/'wam_results.jsonl').write_text('')
            _, errors = self.v.validate_database(dest)
            self.assertTrue(any('wam_results' in e for e in errors))

    def test_episode_counts_and_year_are_not_booleans(self):
        self.assertTrue(self.v.validate_record(record(episodes=True)))
        self.assertTrue(self.v.validate_record(record(year=True)))

class PipelineTests(unittest.TestCase):
    def run_script(self, script, *args):
        return subprocess.run([sys.executable, str(ROOT/'scripts'/script), *map(str,args)], capture_output=True, text=True)

    def test_repository_validates(self):
        p = self.run_script('validate_json.py')
        self.assertEqual(p.returncode, 0, p.stdout+p.stderr)

    def test_generated_tables_are_current_and_keep_records(self):
        p = self.run_script('generate_leaderboard.py', '--check')
        self.assertEqual(p.returncode, 0, p.stdout+p.stderr)
        rows = [json.loads(x) for x in (ROOT/'data/libero_results.jsonl').read_text().splitlines()]
        table = (ROOT/'tables/libero_leaderboard.md').read_text()
        for row in rows:
            self.assertIn('`'+row['id']+'`', table)
        self.assertIn('—', table)

    @unittest.skipUnless(importlib.util.find_spec('pyarrow'), 'optional pyarrow export dependency is not installed')
    def test_export_is_lossless_and_has_default_config(self):
        with tempfile.TemporaryDirectory() as d:
            p = self.run_script('export_hf_dataset.py', '--output-dir', d)
            self.assertEqual(p.returncode, 0, p.stdout+p.stderr)
            for name in ('libero_results.jsonl','wam_results.jsonl','papers.json','checkpoints.json','model_catalog.json'):
                self.assertEqual((Path(d)/name).read_bytes(), (ROOT/'data'/name).read_bytes())
            self.assertIn('default: true', (Path(d)/'README.md').read_text())

    def test_renderer_does_not_impute_or_deduplicate(self):
        self.assertIsNotNone(importlib.util.find_spec('generate_leaderboard'), 'generator not implemented')
        import generate_leaderboard
        text = generate_leaderboard.render_results([record(),record(id='other',paper_id='other',paper='Other')])
        self.assertIn('`example_main`', text)
        self.assertIn('`other`', text)
        self.assertIn('—', text)
        self.assertNotIn('80.00', text)

if __name__ == '__main__':
    unittest.main()
