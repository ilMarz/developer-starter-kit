# Kit validation

Verified on September 27, 2026, on macOS with local Python.

- `python3 tools/verify.py`: PASS; 15 vendor snapshots match their recorded hashes.
- `python3 -m unittest discover -s tests -v`: PASS; 12 tests covering paths with spaces,
  dry runs without writes, user-file preservation, merge proposals, conflict detection before
  writes, idempotency, rejection of internal symlinks, drift, and vendor tampering.
- Actual SDD task-brief execution against the plan template in a temporary Git repository:
  PASS; task extracted and scratch excluded from Git.
- Structural name/description frontmatter and directory check for all 17 skills: PASS.
- During initial validation, the official quick_validate.py validator was attempted but could not run: PyYAML was absent
  from the two available Python runtimes. No global installation was performed. The structural
  check above is more limited and is not presented as equivalent.
- Independent review: no blocking defect reproduced; additional portability, repeated import,
  and ledger preservation checks. See `INDEPENDENT-REVIEW.md` for the protocol.

Testing uncovered and fixed an incorrect rejection of macOS temporary paths:
the chosen root is resolved, while symlinks inside the destination are rejected.

## Limitations

Resume, unavailable-model, and exhausted-budget cases include documented tabletop evaluations,
not certification of live agent behavior. The `evals/` suite still needs systematic execution
on real projects with comparable measurements.
No provider was called; no generated product was tested end to end. Other clients are not guaranteed.
GitHub CI passed snapshot verification and 12 tests on Linux with Python 3.11 and 3.13 at
revision `08698acd31f5f6bd48404a78bb901e3657e6549c`:
[verified run](https://github.com/ilMarz/developer-starter-kit/actions/runs/36317957804).
Import is designed for one execution at a time: it does not provide filesystem transactions or
protect against concurrent processes changing paths during copying.
Model/budget JSON files are operational instructions, not technical spending or permission enforcement.

## 0.2.0 update

The 12 tests and verification of 15 vendor snapshots passed again after relocation to the standalone
directory. The two original skills are dev-workflow and update-devkit.
The relative `.agents/skills/update-devkit` link is present.
The README documents actual bootstrap parameters and separates terminal commands from chat prompts.
Subset selection before changes is documented in the working agreement; its operational effectiveness
still needs evaluation with agents on real tasks.

## 0.2.1 English translation

All 12 bootstrap tests and vendor integrity checks passed after translation. The two original
skills passed the official quick_validate.py validator using PyYAML in a temporary virtual
environment, removed afterward; no global Python package installation was required.
The CLI changes were also compared at the Python AST level: only string constants changed.
Third-party skill and license bytes remain identical to their pinned snapshots.
This validates structure and import behavior, not live agent behavior in English.

## 0.3.0 standalone entry skill

- The entry skill passed the official quick_validate.py validator in a temporary environment.
- All 12 bootstrap tests and verification of 15 vendor snapshots passed.
- An independent agent actually followed the no-Python procedure in an isolated existing-project
  fixture, using available Node v26.9.0 file/crypto tools. No runtime was installed.
- It verified 45 vendor/license hashes, imported 74 manifest files, and confirmed all 17 project
  skills. Original application/package files remained byte-identical. Existing AGENTS rules were
  preserved verbatim and compatible additions merged, with no pending decisions.
- Preview-only mode left the fresh destination nonexistent. A conflicting workflow configuration
  stopped preflight with identical before/after file inventories and hashes.
- The existing Python verifier independently accepted the resulting import manifest afterward.
  That cross-check was separate from the agent's no-Python import.

The source was an uncommitted 0.3.0 candidate based on `78c1cd4`; dirty provenance was recorded.
These are executed skill evaluations, not an additional automated importer or guarantees for all
clients. Live network retrieval, future upstream changes, and clients without file/hash tools were
not covered by that fixture. No application was implemented or tested.
