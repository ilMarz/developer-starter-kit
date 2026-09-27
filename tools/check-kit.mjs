#!/usr/bin/env node
// Read-only maintainer checks. Not an importer or a runtime requirement for skills.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
const readJSON = file => JSON.parse(fs.readFileSync(file, 'utf8'));
function safeRelative(rel) {
  if (typeof rel !== 'string' || !rel || rel.includes('\\') || rel.includes('\0') ||
      path.posix.isAbsolute(rel) || rel.split('/').some(p => !p || p === '.' || p === '..')) {
    throw new Error(`Unsafe relative path: ${rel}`);
  }
}
function regular(root, rel) {
  safeRelative(rel);
  let current = fs.realpathSync(root);
  for (const part of rel.split('/')) {
    current = path.join(current, part);
    if (fs.lstatSync(current).isSymbolicLink()) throw new Error(`Symlink rejected: ${rel}`);
  }
  if (!fs.statSync(current).isFile()) throw new Error(`Not a regular file: ${rel}`);
  return current;
}
function files(root, relative) {
  const dir = path.join(root, relative);
  if (fs.lstatSync(dir).isSymbolicLink()) throw new Error(`Symlink rejected: ${relative}`);
  return fs.readdirSync(dir).flatMap(name => {
    const rel = `${relative}/${name}`;
    const stat = fs.lstatSync(path.join(root, rel));
    if (stat.isSymbolicLink()) throw new Error(`Symlink rejected: ${rel}`);
    if (stat.isDirectory()) return files(root, rel);
    if (!stat.isFile()) throw new Error(`Unsupported file: ${rel}`);
    return [rel];
  });
}
function sameSet(actual, expected, label) {
  if (actual.size !== expected.size || [...actual].some(x => !expected.has(x))) {
    throw new Error(`${label}: file inventory differs`);
  }
}
export function verifyVendor(root = ROOT) {
  const lock = readJSON(regular(root, 'skills.lock.json'));
  const contract = readJSON(regular(root, 'import-contract.json'));
  if (lock.schema_version !== 1 || !Array.isArray(lock.sources) ||
      !Array.isArray(contract.first_party_skills)) throw new Error('Invalid source metadata');
  const expected = new Set();
  for (const source of lock.sources) {
    for (const record of source.files) {
      safeRelative(record.path);
      if (!/^(skills|licenses)\//.test(record.path) || expected.has(record.path) ||
          !/^[a-f0-9]{64}$/.test(record.sha256)) throw new Error('Invalid vendor record');
      if (hash(fs.readFileSync(regular(root, record.path))) !== record.sha256) {
        throw new Error(`Vendor hash mismatch: ${record.path}`);
      }
      expected.add(record.path);
    }
  }
  const actual = new Set([...files(root, 'skills'), ...files(root, 'licenses')].filter(rel =>
    !(rel.startsWith('skills/') && contract.first_party_skills.includes(rel.split('/')[1]))));
  sameSet(actual, expected, 'Vendor');
  return { vendorFiles: expected.size, vendorSkills: lock.sources.reduce((n, s) => n + s.skills.length, 0) };
}
export function verifyProject(root) {
  const manifest = readJSON(regular(root, '.devkit/import.json'));
  if (manifest.schema_version !== 1 || !manifest.files || Array.isArray(manifest.files) ||
      typeof manifest.files !== 'object' || !Array.isArray(manifest.pending_manual_merges)) {
    throw new Error('Invalid import manifest');
  }
  // Validate the complete manifest before reading any payload file.
  for (const [rel, digest] of Object.entries(manifest.files)) {
    safeRelative(rel);
    if (!/^[a-f0-9]{64}$/.test(digest)) throw new Error(`Invalid hash: ${rel}`);
  }
  for (const rel of manifest.pending_manual_merges) safeRelative(rel);
  const modified_or_missing = [];
  for (const [rel, digest] of Object.entries(manifest.files)) {
    try {
      if (hash(fs.readFileSync(regular(root, rel))) !== digest) modified_or_missing.push(rel);
    } catch (error) {
      if (['ENOENT', 'ENOTDIR'].includes(error.code) || /^(Symlink rejected|Not a regular file)/.test(error.message)) {
        modified_or_missing.push(rel);
      } else throw error;
    }
  }
  return { modified_or_missing, pending_manual_merges_at_import: manifest.pending_manual_merges };
}
export function checkKit(root = ROOT) {
  const result = verifyVendor(root);
  const contract = readJSON(regular(root, 'import-contract.json'));
  if (contract.schema_version !== 1 || !Array.isArray(contract.mappings) || !Array.isArray(contract.protected_paths)) {
    throw new Error('Invalid import contract');
  }
  for (const mapping of contract.mappings) {
    safeRelative(mapping.source);
    if (mapping.destination !== '.') safeRelative(mapping.destination);
    const source = path.join(root, mapping.source);
    if (fs.lstatSync(source).isDirectory()) files(root, mapping.source);
    else regular(root, mapping.source);
  }
  for (const rel of contract.protected_paths) safeRelative(rel);
  for (const key of ['proposal_directory', 'manifest', 'setup_notes']) safeRelative(contract[key]);
  const config = readJSON(regular(root, 'template/.devkit/project.json'));
  if (config.name !== null || !contract.profiles.includes(config.profile) ||
      !config.commands || Object.values(config.commands).some(v => v !== null)) {
    throw new Error('Project template must await setup');
  }
  let skillCount = 0;
  for (const [name, rel] of [['devkit', 'SKILL.md'], ...fs.readdirSync(path.join(root, 'skills')).map(name => [name, `skills/${name}/SKILL.md`])]) {
      const text = fs.readFileSync(regular(root, rel), 'utf8');
      const frontmatter = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
      if (!frontmatter || !frontmatter[1].includes(`name: ${name}\n`) ||
          !/^description: .+/m.test(frontmatter[1])) throw new Error(`Invalid skill header: ${name}`);
      skillCount++;
  }
  return { ...result, skills: skillCount };
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const args = process.argv.slice(2);
    if (args.length === 0) console.log(JSON.stringify(checkKit(), null, 2));
    else if (args.length === 2 && args[0] === '--project') {
      const result = verifyProject(args[1]);
      console.log(JSON.stringify(result, null, 2));
      process.exitCode = result.modified_or_missing.length ? 1 : 0;
    } else throw new Error('Usage: node tools/check-kit.mjs [--project PATH]');
  } catch (error) {
    console.error(error.message);
    process.exitCode = 2;
  }
}
