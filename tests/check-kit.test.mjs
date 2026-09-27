import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import { checkKit, verifyVendor, verifyProject, ROOT } from '../tools/check-kit.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'devkit-check-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  return root;
}
function vendorFixture(t) {
  const root = fixture(t);
  for (const name of ['skills', 'licenses', 'skills.lock.json', 'import-contract.json']) {
    fs.cpSync(path.join(ROOT, name), path.join(root, name), { recursive: true });
  }
  return root;
}
function project(t) {
  const root = fixture(t);
  fs.mkdirSync(path.join(root, '.devkit'));
  fs.mkdirSync(path.join(root, 'docs'));
  fs.writeFileSync(path.join(root, 'docs/file.txt'), 'original');
  const manifest = { schema_version: 1, kit_version: '0.3.0', pending_manual_merges: ['AGENTS.md'],
    files: { 'docs/file.txt': crypto.createHash('sha256').update('original').digest('hex') } };
  fs.writeFileSync(path.join(root, '.devkit/import.json'), JSON.stringify(manifest));
  return { root, manifest };
}
test('kit metadata and all recorded snapshots pass', () => {
  assert.deepEqual(checkKit(), { vendorFiles: 45, vendorSkills: 15, skills: 18 });
});
test('vendor tampering is detected', t => {
  const root = vendorFixture(t);
  fs.appendFileSync(path.join(root, 'skills/tdd/SKILL.md'), 'changed');
  assert.throws(() => verifyVendor(root), /hash mismatch/);
});
test('unregistered vendor additions are rejected', t => {
  const root = vendorFixture(t);
  fs.writeFileSync(path.join(root, 'skills/tdd/extra.txt'), 'extra');
  assert.throws(() => verifyVendor(root), /inventory differs/);
});
test('missing vendor files are rejected', t => {
  const root = vendorFixture(t);
  fs.unlinkSync(path.join(root, 'skills/tdd/SKILL.md'));
  assert.throws(() => verifyVendor(root), /ENOENT/);
});
test('legacy manifests remain readable and inspection is read-only', t => {
  const { root } = project(t);
  const before = fs.readFileSync(path.join(root, '.devkit/import.json'));
  assert.deepEqual(verifyProject(root), { modified_or_missing: [], pending_manual_merges_at_import: ['AGENTS.md'] });
  assert.deepEqual(fs.readFileSync(path.join(root, '.devkit/import.json')), before);
});
test('modified and missing project files are reported', t => {
  const { root } = project(t);
  fs.writeFileSync(path.join(root, 'docs/file.txt'), 'changed');
  assert.deepEqual(verifyProject(root).modified_or_missing, ['docs/file.txt']);
  fs.unlinkSync(path.join(root, 'docs/file.txt'));
  assert.deepEqual(verifyProject(root).modified_or_missing, ['docs/file.txt']);
});
test('symlinked parent cannot escape project inspection', t => {
  const { root } = project(t);
  const outside = fixture(t);
  fs.writeFileSync(path.join(outside, 'file.txt'), 'original');
  fs.rmSync(path.join(root, 'docs'), { recursive: true });
  fs.symlinkSync(outside, path.join(root, 'docs'), 'dir');
  assert.deepEqual(verifyProject(root).modified_or_missing, ['docs/file.txt']);
});
test('traversal and absolute paths in manifest are rejected', t => {
  const { root, manifest } = project(t);
  const digest = manifest.files['docs/file.txt'];
  for (const rel of ['../outside', '/etc/passwd', 'docs/../../outside', 'docs\\file.txt']) {
    manifest.files = { [rel]: digest };
    fs.writeFileSync(path.join(root, '.devkit/import.json'), JSON.stringify(manifest));
    assert.throws(() => verifyProject(root), /Unsafe relative path/);
  }
});
test('invalid hashes fail as malformed metadata', t => {
  const { root, manifest } = project(t);
  manifest.files['docs/file.txt'] = 'not-a-hash';
  fs.writeFileSync(path.join(root, '.devkit/import.json'), JSON.stringify(manifest));
  assert.throws(() => verifyProject(root), /Invalid hash/);
});
test('whole-folder installation validates without Git metadata', t => {
  const root = fixture(t);
  fs.cpSync(ROOT, root, {
    recursive: true, verbatimSymlinks: true,
    filter: source => !path.relative(ROOT, source).split(path.sep).some(p => ['.git', '__pycache__'].includes(p))
  });
  assert.equal(fs.existsSync(path.join(root, '.git')), false);
  assert.equal(fs.existsSync(path.join(root, 'SKILL.md')), true);
  assert.equal(fs.existsSync(path.join(root, 'references/tool-based-import.md')), true);
  assert.deepEqual(checkKit(root), { vendorFiles: 45, vendorSkills: 15, skills: 18 });
});
