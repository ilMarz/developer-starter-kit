# Developer Starter Kit maintenance

This directory is a standalone, general-purpose artifact. Keep adopting projects' data and rules separate.
Project imports come from `template/` and `skills/`; the remaining files maintain the kit.
Do not change vendor snapshots without explicitly recording provenance and the diff.
For maintenance checks, run `node tools/check-kit.mjs` and `node --test tests/*.test.mjs`
using an available Node runtime (CI provides one). Node is not required to use the skills.
Test imports in temporary directories outside the kit, never in user projects. Script tests do not prove skill effectiveness; also use `evals/scenarios.md`.
Preserve existing project files; do not perform silent updates or global changes.

To discover improvements and update this kit, use `skills/update-devkit/SKILL.md`.
The discovery path `.agents/skills/update-devkit` points to the same skill.
The default mode produces evidence-based proposals, including opportunities outside the inventory.

The whole repository is the installable `devkit` skill, with `SKILL.md` at its root.
Use bundled resources by default; ordinary setup must not download another copy.
Validate relocation and offline setup in temporary fixtures, without Git metadata.
