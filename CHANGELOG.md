# Changelog

## 0.5.0 — September 27, 2026

- Package the entire repository as the devkit skill, with SKILL.md at the root.
- Use bundled resources automatically; ordinary setup needs no download or source path.
- Support copied/extracted folders without Git metadata; preserve truthful provenance.
- Remove the separate installer-only layout and document whole-folder installation.

## 0.4.0 — September 27, 2026

- Remove the Python bootstrap, verifier, tests, and CLI import guide.
- Make agent file-tool setup the only import path; no installation runtime is required.
- Define file mappings in import-contract.json and ship project configuration as a template.
- Use dependency-free Node maintenance checks in CI; Node is not needed to use the skills.
- Preserve existing import manifests and keep the Python application profile as an optional stack.

## 0.3.0 — September 27, 2026

- Add standalone `devkit` entry skill under `installer/devkit`: install once, initialize or
  integrate projects from chat, and hand off to their local `dev-workflow`.
- Support agent-executed import without Python using file/comparison/hash tools; retain the
  deterministic Python CLI as an optional path. No runtime is installed by the entry skill.
- Preserve existing instructions and application files, record source provenance and merges,
  and distinguish preview-only, setup-only, and development requests.
- Keep the 17 project skills and 15 vendor snapshots unchanged; the entry skill is installed separately.
- Lead the README with chat-based setup; move detailed terminal instructions to docs/CLI-IMPORT.md.

## 0.2.1 — September 27, 2026

- Translate all original documentation, templates, skills, and CLI messages into English.
- Update cloning instructions for the public repository and document successful GitHub CI.
- Preserve third-party snapshots and their hashes; command arguments and behavior are unchanged.

## 0.2.0 — September 27, 2026

- Add `update-devkit`: discover opportunities beyond the current inventory, produce evidence-based
  proposals, apply selected IDs, and preserve customizations.
- Add an initial working agreement with configurable skills, conventions, tools, loop, and models;
  reuse existing choices, pass exclusions to subagents, and support direct implementation.
- Reports include sources, expected benefit, impact, compatibility, and an experiment.
- Repository discovery uses a relative link; new projects receive regular copies.
- 17 skills total: 15 unchanged vendor skills and 2 original skills. Vendor hashes unchanged.
- Standalone, portable directory without references to specific projects.
- No new technology adopted; previously imported projects remain unchanged.

## 0.1.0 — September 27, 2026

Initial bootstrap, templates, 15 vendor skills, and dev-workflow.
