import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
BOOT = ROOT / 'tools/bootstrap.py'


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='devkit-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.target = self.base / 'project with spaces'

    def run_boot(self, *extra):
        return subprocess.run([sys.executable, str(BOOT), '--target', str(self.target),
                               '--name', 'test-project', *extra], capture_output=True, text=True)

    def snapshot(self):
        return {str(p.relative_to(self.target)): p.read_bytes()
                for p in self.target.rglob('*') if p.is_file()}

    def test_dry_run_creates_nothing(self):
        result = self.run_boot('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.target.exists())

    def test_new_project_is_complete_and_offline(self):
        result = self.run_boot('--profile', 'python')
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((self.target / '.devkit/import.json').read_text())
        self.assertEqual(manifest['pending_manual_merges'], [])
        for rel, expected in manifest['files'].items():
            self.assertEqual(hashlib.sha256((self.target / rel).read_bytes()).hexdigest(), expected, rel)
        self.assertTrue((self.target / '.agents/skills/grilling/SKILL.md').is_file())
        self.assertTrue((self.target / '.agents/skills/domain-modeling/ADR-FORMAT.md').is_file())
        self.assertTrue((self.target / '.agents/skills/dev-workflow/SKILL.md').is_file())
        self.assertTrue((self.target / '.agents/skills/update-devkit/SKILL.md').is_file())
        self.assertTrue((self.target / '.agents/skills/update-devkit/references/research.md').is_file())
        self.assertFalse((self.target / '.git').exists())
        config = json.loads((self.target / '.devkit/project.json').read_text())
        self.assertEqual(config['profile'], 'python')
        self.assertIsNone(config['commands']['test'])

    def test_nonempty_requires_explicit_existing(self):
        self.target.mkdir()
        (self.target / 'user.txt').write_text('keep')
        before = self.snapshot()
        result = self.run_boot()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_existing_instructions_are_preserved_and_proposals_recorded(self):
        (self.target / 'docs/agents').mkdir(parents=True)
        for name in ['AGENTS.md', 'CONTEXT.md', '.gitignore', 'docs/agents/domain.md']:
            (self.target / name).write_text('Original user content')
        (self.target / 'source.py').write_text('print(42)')
        result = self.run_boot('--existing')
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((self.target / '.devkit/import.json').read_text())
        self.assertIn('AGENTS.md', manifest['pending_manual_merges'])
        for name in manifest['pending_manual_merges']:
            self.assertEqual((self.target / name).read_text(), 'Original user content')
            self.assertTrue((self.target / '.devkit/proposed' / name).exists())
        self.assertEqual((self.target / 'source.py').read_text(), 'print(42)')

    def test_collision_aborts_before_any_write(self):
        (self.target / '.agents/skills/tdd').mkdir(parents=True)
        (self.target / '.agents/skills/tdd/SKILL.md').write_text('My custom skill')
        before = self.snapshot()
        result = self.run_boot('--existing')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_second_identical_import_is_idempotent(self):
        self.assertEqual(self.run_boot().returncode, 0)
        before = self.snapshot()
        result = self.run_boot('--existing')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_project_config_edit_is_not_overwritten(self):
        self.assertEqual(self.run_boot().returncode, 0)
        config = self.target / '.devkit/project.json'
        data = json.loads(config.read_text())
        data['commands']['test'] = 'pytest'
        config.write_text(json.dumps(data))
        before = self.snapshot()
        self.assertEqual(self.run_boot('--existing').returncode, 2)
        self.assertEqual(self.snapshot(), before)

    @unittest.skipUnless(hasattr(Path, 'symlink_to'), 'Symlink unavailable')
    def test_symlinked_destination_subdirectory_is_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        self.target.mkdir()
        (self.target / '.agents').symlink_to(outside, target_is_directory=True)
        result = self.run_boot('--existing')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(list(outside.iterdir()), [])

    def test_file_in_parent_path_is_rejected(self):
        self.target.mkdir()
        (self.target / '.agents').write_text('not a directory')
        before = self.snapshot()
        self.assertEqual(self.run_boot('--existing').returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_drift_detection_after_import(self):
        self.assertEqual(self.run_boot().returncode, 0)
        command = [sys.executable, str(ROOT / 'tools/verify.py'), '--project', str(self.target)]
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 0)
        (self.target / '.agents/skills/tdd/SKILL.md').write_text('modified')
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('.agents/skills/tdd/SKILL.md', result.stdout)

    @unittest.skipUnless(shutil.which('git') and shutil.which('bash'), 'Git and Bash required')
    def test_sdd_can_extract_task_from_imported_plan_template(self):
        self.assertEqual(self.run_boot().returncode, 0)
        subprocess.run(['git', 'init', '-q'], cwd=self.target, check=True, capture_output=True)
        plan = self.target / 'docs/development/templates/plan.md'
        helper = self.target / '.agents/skills/subagent-driven-development/scripts/task-brief'
        result = subprocess.run(['bash', str(helper), str(plan), '1'], cwd=self.target,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        briefs = list((self.target / '.superpowers').rglob('task-1-brief.md'))
        self.assertEqual(len(briefs), 1)
        self.assertIn('### Task 1:', briefs[0].read_text())
        ignored = subprocess.run(['git', 'check-ignore', str(briefs[0])], cwd=self.target,
                                 capture_output=True, text=True)
        self.assertEqual(ignored.returncode, 0)

    def test_tampered_vendor_is_rejected(self):
        copy = self.base / 'kit-copy'
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('__pycache__', '.git'))
        (copy / 'skills/tdd/SKILL.md').write_text('tampered')
        result = subprocess.run([sys.executable, str(copy / 'tools/bootstrap.py'),
                                 '--target', str(self.target), '--name', 'test'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(self.target.exists())


if __name__ == '__main__':
    unittest.main()
