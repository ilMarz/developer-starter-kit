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

The standalone entry skill is in `installer/devkit/`, exposed locally through
`.agents/skills/devkit`. It is installed personally, not copied by the project import.
Validate its setup behavior in isolated temporary fixtures, using the agent file-tool procedure.
