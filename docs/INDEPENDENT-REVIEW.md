# Independent kit review

Date: September 27, 2026. Scope: kit 0.1.0 on the filesystem; no Git revision was available in the
inspected directory. A separate agent reviewed the author's work without further subagents,
external providers, or changes to user projects. This is a historical review of that snapshot.

## Outcome

No blocking defect was reproduced in the bootstrap or inspected integration rules. The offline
import is usable as a snapshot of procedures and templates. End-to-end effectiveness of an agent
team and automatic budget/model enforcement were not demonstrated; the kit correctly states these limits.

## Actual executions

- `PYTHONDONTWRITEBYTECODE=1 python3 tools/verify.py`: exit 0; 15 vendor skills verified.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`: exit 0; 12 tests passed.
  Observed coverage: dry run, new/existing imports, preservation, conflicts before writes,
  idempotency, edited configuration, symlinks, path obstructions, drift, SDD helper, and vendor tampering.
- Copied the entire kit to an external temporary directory, then imported from that copy into a
  temporary project with spaces in its path: exit 0; 70 files imported. Original `AGENTS.md`
  preserved with a separate proposal recorded. Import required no dependency on the original directory.
- Repeated the same fixture import with `--existing`: exit 0; zero new files; byte-for-byte content
  unchanged, including proposals for existing instructions.
- Initialized Git and committed a baseline only in the temporary fixture. Actually ran `sdd-workspace`
  with absolute and relative paths to the same plan: same workspace; ledger preserved Task 1 as
  complete and Task 2 as undergoing fixes.
- Applied an actual `smal` → `small` fix to the fixture README: `git diff --name-only` returned only
  `README.md`; numstat 1/1. Import verification exited 0 because README was not a managed file,
  consistent with the verifier's stated scope.

Fixtures were automatically removed. No application workflow, service, or provider was called.
The helper execution verifies file persistence, not that an agent resumes correctly.

## Tabletop evaluation of procedures

These are reasoned decision simulations, separate from the executions above; they are not live
behavioral benchmarks. References describe the reviewed 0.1.0 snapshot, not current line numbers.

| Realistic request / state | Text inspected | Simulated decision |
| --- | --- | --- |
| “Resume”: Task 1 committed and complete, Task 2 in review | START-HERE resume prompt; WORKFLOW memory; SDD Setup | Check Git/evidence, recover the correct plan ledger, continue Task 2 without redispatching Task 1. Relative/absolute workspace behavior was also tested with the script. |
| “Fix this README typo” | dev-workflow; WORKFLOW process sizing | Direct edit and diff check; no interview, ADR, or delegation needed. A minimal fixture diff was also executed, without treating it as live evidence of skill selection. |
| Reviewer configured with nonexistent ID, fallback unauthorized | AGENTIC-LOOP; models.json | Check client capabilities, do not claim successful dispatch, record the limitation and await a choice. If inherited fallback is already authorized, disclose the actual model. No API invoked in review. |
| Two attempts authorized, second still fails | AGENTIC-LOOP; AGENTS autonomy; loop.json | Preserve candidate/evidence and stop without a third attempt. The stricter local limit takes precedence over the vendor SDD five-round cap. Do not mark the failed requirement complete. |
| Approved specification with two independent behaviors | WORKFLOW; spec/slice/plan templates; issue-tracker; COMPATIBILITY | Derive vertical increments and a plan preserving IDs/criteria; write tickets to docs/work rather than upstream scratch. ADRs only for material decisions. |

Vendor differences matter: SDD proposes rulings, five fixes, and model choices; local integration
rules preserve approved criteria, stricter budgets, and actual client capabilities. Using only the
vendor skill without project instructions is not following the kit workflow.

## Limitations and next verification

No mandatory corrective finding emerged in the reviewed scope. Cases in `evals/scenarios.md`
still need execution in a real client with local discovery and authorized dispatch, recording
revisions, actual model, prompts, outcomes, and usage. In particular, resume after compaction,
unavailable models, and budget stops remain **unverified live** until tested.
This review does not certify universal compatibility, future software quality, or hard spending limits.
