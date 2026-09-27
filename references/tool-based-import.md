# Import with agent file tools

This is the setup procedure for every import. It is agent-executed, not a bundled importer.
It requires file enumeration/read/write/copy, byte comparison, and SHA-256 hashing capabilities
(for example shell tools `cmp` and `shasum -a 256` or `sha256sum`). Use available tools; do not
install a runtime. If a required capability is missing, stop before writes and report it.
Never fabricate hashes.

## 1. Build and verify the complete plan

Read `import-contract.json` in the selected snapshot as the authoritative import contract.
Use the same mapping, including hidden files:

| Source | Destination |
| --- | --- |
| `template/**` | Project root, preserving relative paths |
| `skills/**` | `.agents/skills/**` |
| `licenses/**` | `.devkit/licenses/**` |
| `skills.lock.json` | `.devkit/skills.lock.json` |
| `THIRD_PARTY_NOTICES.md` | `.devkit/THIRD_PARTY_NOTICES.md` |

Do not copy the source `.git/`, `.agents/` discovery symlinks, the root `SKILL.md`, `agents/`, `references/`, tests, tools,
or maintenance documents. Copy source bytes exactly. Generate only the project configuration
and import manifest described below. Do not write an application scaffold during import.

Read the lockfile as data. Verify every vendor/license hash and reject missing, changed,
symlinked, or unexpected vendor files, using `first_party_skills` from that contract.
Do not execute JSON or interpolate untrusted paths into shell code. Validate relative paths:
no absolute paths or parent traversal, and every path must stay within its source/destination root.

Resolve the chosen destination root (system aliases such as macOS `/tmp` are acceptable),
but reject a destination that is itself a symlink. Reject symlinks inside source payload or
destination paths, including dangling symlinks, and file/directory obstructions. The source,
target, and any scratch directory must not overlap. Work in a controlled, nonconcurrent environment.

Before writing any destination files, compare every planned destination:

- Absent: plan an exclusive creation.
- Identical regular file: reuse, without writing.
- Different regular file at a protected path: preserve it and propose the source version under
  `.devkit/proposed/<original-path>`. Protected paths: `AGENTS.md`, `CONTEXT.md`, `.gitignore`,
  `docs/agents/domain.md`, `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`.
  Preflight the proposal destination too; a different existing proposal is a conflict.
- Any other differing content, symlink, or obstruction: report the conflict and stop before writes.
  Do not omit conflicting files and call it a complete import.

Capture a baseline of preexisting files for post-import comparison. Respect preview-only mode:
report the plan without creating the target or writing any files within it.

## 2. Record the same import contract

Copy `template/.devkit/project.json`, setting only `name` and `profile` to the selected values.
Use a nonempty name without control characters and a profile listed in the contract.
Preserve all other keys and types; null commands mean setup remains incomplete.
This configuration is the one intentional transformation of a template during import.

Generate `.devkit/import.json`:

- `schema_version`: 1.
- `kit_version`: the source lockfile version.
- `pending_manual_merges`: sorted original protected paths requiring proposals.
- `files`: mapping of each final copied/generated relative path to its actual SHA-256 hash.
  For a protected conflict, track the proposal path, not the untouched user file.
  Include generated `.devkit/project.json`; exclude the import manifest itself and later setup notes.

Use stable JSON formatting (two-space indentation, trailing newline, sorted file keys).
Preserve the project name as UTF-8. Preflight generated destinations too.
The import manifest is a baseline, not a claim that project behavior has been tested.

## 3. Apply and check

Recheck destination conditions immediately before writing. Use exclusive creation or an equivalent
no-overwrite primitive; do not rely on a recursive force copy. Preserve source bytes, including
binary files. Stop on unexpected changes or write errors and report any partial state accurately.
This is not an atomic transaction and does not protect against arbitrary concurrent writers.

Hash all recorded destination files and compare against the manifest. Compare preexisting files
to the baseline; they must remain unchanged at this stage. Confirm no application code, runtime,
Git metadata, or external service was changed. Report exact tool failures rather than a pass.

Then return to the entry skill to merge compatible instruction proposals and write setup notes.
Keep original import hashes; edits to tracked files remain visible as drift. Protected user files
are not tracked when their proposals are imported, so record their merges explicitly in setup notes.
Never rewrite the baseline to conceal local modifications. Use file/hash tools for later inspection and report only checks actually performed.
