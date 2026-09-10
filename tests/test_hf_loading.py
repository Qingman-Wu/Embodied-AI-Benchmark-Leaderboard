"""Optional integration test: pip install datasets, then run unittest discovery."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

@unittest.skipUnless(importlib.util.find_spec('datasets'), 'optional datasets dependency is not installed')
class HuggingFaceLoadingTests(unittest.TestCase):
    def test_default_and_wam_load_without_changing_dates_nulls_or_precision(self):
        from datasets import load_dataset
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable,str(ROOT/'scripts/export_hf_dataset.py'),'--output-dir',d],check=True,capture_output=True)
            for name,kwargs in [('libero',{}),('wam',{'name':'wam'})]:
                actual=load_dataset(d,**kwargs)['train'].to_list()
                expected=[json.loads(line) for line in (ROOT/'data'/f'{name}_results.jsonl').read_text().splitlines()]
                self.assertEqual(actual,expected)
