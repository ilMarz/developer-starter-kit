# Development workflow

## Choose the right amount of process

- Typo/small reversible configuration change: focused diff and relevant verification.
- Bug: reproduce, verify the cause, fix, and check the original case and regressions.
- Multistep feature: specification, slices, execution plan, implementation, and review.
- Costly or disputed decision: analyze alternatives and write an ADR. Do not create ADRs for routine work.

## From problem to software

1. **Understand**: gather facts from code and sources; ask only about open decisions. Distinguish
   observations, hypotheses, and proposals. Specify examples, negative criteria, and exclusions.
2. **Choose verification interfaces**: observable behavior and expected outcomes independent of the
   implementation. Reuse approved interfaces.
3. **Vertical slices**: each crosses the layers needed for demonstrable behavior. Do not build all
   models first, then all services, then all tests. Large migrations may use expand → migrate → contract
   while preserving compatibility.
4. **Plan**: derive tasks from slices. Specification = what and why; plan = how and which files.
   Check interface/dependency conflicts before assigning tasks. Use `### Task 1: ...` headings compatible
   with SDD task-brief. The template is in templates/plan.md.
5. **Execute**: controlled environment, baseline, meaningful tests, small changes, and the loop in
   AGENTIC-LOOP.md. Subagents are not mandatory for tiny tasks.
6. **Review**: check criteria, correctness, regressions, relevant security, migrations, and operations.
   The reviewer must be able to challenge the plan and implementation with evidence.
7. **Deliver**: verify the final result, disclose limitations, update documents, record commits/diffs,
   and integrate into the authorized destination. No implicit deployment.

## Consistency and observed conventions

Before starting and closing a feature, compare specification criteria, slices/tasks, and evidence:
every required criterion needs identifiable verification. A document mentioning a criterion does not
prove the behavior works. Also verify the integrated path when multiple slices work together.

In existing projects, record only useful, actually observed conventions in a `docs/standards.md` index:
scope, source file/symbol, rationale, and exceptions. Create it when reusable conventions emerge,
without copying whole manuals. An existing pattern may be technical debt; do not automatically
promote it to a rule.

## Definition of ready

Usable objective and criteria; resolved or explicit dependencies; test surface; environment and
permissions; agreed budget and execution mode. A blocked task is not ready.

## Definition of done

Required behavior observed; relevant original, negative, and regression cases checked; review
addressed; residual errors and missing verification explicit; docs/ADRs updated where needed;
logs free of secrets; destination and activation consistent with authorization.
A feature missing essential verification is not done. It may remain a candidate with stated limitations.

## Memory and context

`docs/progress.md` preserves summaries and links to evidence, commits, and decisions. The SDD ledger
in `.superpowers/sdd/` is Git-ignored scratch: useful for recovering work in a session, but insufficient
as an archive. Before cleanup/handoff, move useful redacted evidence to `docs/reports/`.
Do not copy full transcripts or secrets into the repository.
