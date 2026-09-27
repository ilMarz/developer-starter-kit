# Kit validation

## Current checks — 0.4.0

The kit has no bundled importer or Python tooling. Setup is performed by the agent using
file/comparison/hash tools, following import-contract.json and the entry skill.

- `node tools/check-kit.mjs`: passed; 45 vendor/license files, 15 vendor skills, 18 total skills.
- `node --test tests/*.test.mjs`: 9 tests passed, covering vendor tampering, added/missing files,
  legacy manifests, drift, read-only inspection, symlinked parents, traversal, and malformed hashes.
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
