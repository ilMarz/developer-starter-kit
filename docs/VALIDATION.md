# Kit validation

## Current checks — 0.5.0

The kit has no bundled importer or Python tooling. Setup is performed by the agent using
file/comparison/hash tools, following import-contract.json and the entry skill.

- `node tools/check-kit.mjs`: passed; 45 vendor/license files, 15 vendor skills, 18 total skills.
- `node --test tests/*.test.mjs`: 10 tests passed, covering vendor tampering, added/missing files,
  legacy manifests, drift, read-only inspection, symlinked parents, traversal, malformed hashes, and whole-folder installation without Git metadata.
- These Node checks are repository-maintenance tools, not prerequisites for installing or using skills.
- CI runs the same read-only checks with Node supplied by the hosted runner.

An independent agent executed a fresh 0.4.0 import from the declarative contract using already
available Node file/hash tools, without a bundled importer or runtime installation:

- 45 vendor/license hashes and 74 imported manifest files verified; all 17 project skills present.
- Project configuration came from the template, changing only name and profile.
- Original application/package files and project rules preserved; compatible AGENTS additions merged.
- Preview left its destination absent; an unrelated file conflict prevented all target writes.
- The maintenance verifier independently accepted the resulting manifest.

The candidate source was based on commit b64e869 with dirty provenance recorded. This is an
executed agent evaluation, not an automated import test or proof of behavior on every client.

## Earlier evidence

The 0.1–0.3 releases included a scripted importer that has now been removed. Their 12-test results
apply to those historical releases, not to the current agent-driven import path.
See the [historical validation record](https://github.com/ilMarz/developer-starter-kit/blob/b64e869/docs/VALIDATION.md)
and [independent 0.1.0 review](INDEPENDENT-REVIEW.md).

In 0.3.0 an independent agent used available Node file/crypto tools, without installing a runtime,
to import 74 manifest files and all 17 project skills, preserving application files and existing rules.
Preview left its target absent; a configuration conflict prevented all writes.
Those results do not certify all clients or future source snapshots.

## Limitations

There is no atomic import transaction or protection from arbitrary concurrent writers.
The agent must preflight the whole plan, preserve existing files, and verify actual hashes.
No application implementation or live provider integration is certified by setup checks.
Model/budget configuration contains instructions, not technical spending or permission enforcement.
Resume after compaction and model/budget behavior still require live evaluations on real tasks.

## 0.5.0 whole-folder offline evaluation

An independent agent copied the full kit into a temporary skills/devkit directory, excluding
Git metadata and caches. It then used only the copied root SKILL.md and its bundled resources:
no source override, original checkout reads during import, downloads, or network access.
The skill resolved its own directory as source and imported 74 recorded files and 17 project
skills after verifying 45 vendor/license hashes. Existing application bytes and conventions
were preserved; compatible instructions merged. The bundled verifier reported no missing or
modified imported files. Archive provenance correctly had no Git revision. Preview/conflict
checks also preserved the destination. This is one actual agent evaluation, not a universal
client guarantee or an application test.
