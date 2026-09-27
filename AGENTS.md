# Developer Starter Kit maintenance

This directory is a standalone, general-purpose artifact. Keep adopting projects' data and rules separate.
Project imports come from `template/` and `skills/`; the remaining files maintain the kit.
Do not change vendor snapshots without explicitly recording provenance and the diff.
After bootstrap changes, run `python3 tools/verify.py` and
`python3 -m unittest discover -s tests -v`. Test in temporary directories outside the kit,
never in user projects. Script tests do not prove skill effectiveness; also use `evals/scenarios.md`.
Preserve existing project files; do not perform silent updates or global changes.

To discover improvements and update this kit, use `skills/update-devkit/SKILL.md`.
The discovery path `.agents/skills/update-devkit` points to the same skill.
The default mode produces evidence-based proposals, including opportunities outside the inventory.
