# Comparison with public development kits

Research dated **September 27, 2026**. Goal: identify reusable practices for this starter while
retaining Matt Pocock for specifications, slices, TDD, and debugging; local Superpowers for
isolated execution/review; and the kit's conservative import approach.
This is not an effectiveness ranking: stars and activity indicate adoption and maintenance,
not measured correctness, safety, or productivity.

## Verified snapshot

Metadata was read from GitHub APIs: `GET /repos/{owner}/{repo}` and
`GET /repos/{owner}/{repo}/commits/{default_branch}`. Dates are committer timestamps for the
head commit of the default branch, in UTC; they are not release dates.
Counts are mutable observations from this research. Commit links pin code; API links remain dynamic.

| Repository / primary API | Stars | Verified license | Latest observed commit | Status |
| --- | ---: | --- | --- | --- |
| [github/spec-kit](https://api.github.com/repos/github/spec-kit) | 139,060 | MIT | [c00dc055](https://github.com/github/spec-kit/commit/c00dc0551583428a10a94443c58c6a41e5e0138c), September 25, 2026 | Not archived |
| [bmad-code-org/BMAD-METHOD](https://api.github.com/repos/bmad-code-org/BMAD-METHOD) | 53,535 | MIT with a separate trademark notice¹ | [5e33d3c0](https://github.com/bmad-code-org/BMAD-METHOD/commit/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb), September 25, 2026 | Not archived |
| [gsd-build/get-shit-done](https://api.github.com/repos/gsd-build/get-shit-done) | 64,450 | MIT (API) | [bdcaab2c](https://github.com/gsd-build/get-shit-done/commit/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815), May 31, 2026 | **Archived**; README points to GSD Core |
| [open-gsd/gsd-core](https://api.github.com/repos/open-gsd/gsd-core) | 9,893 | MIT | [84ed9b84](https://github.com/open-gsd/gsd-core/commit/84ed9b843d9c383e46144931328676fef929a34c), September 27, 2026 | Referenced successor; not archived |
| [buildermethods/agent-os](https://api.github.com/repos/buildermethods/agent-os) | 5,452 | MIT (API) | [475b0cac](https://github.com/buildermethods/agent-os/commit/475b0cac4c7c5cf2336ad5a663b691a6d3415e05), August 29, 2026 | Not archived |

¹ BMAD's API returns `NOASSERTION`; the [inspected LICENSE](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/LICENSE)
contains MIT terms and a trademark notice. Do not infer licensing solely from badges or API fields.

## Capabilities and practices to select

The capabilities below are documented in the sources, not tested by running the frameworks.
Overlap and adoption assessments are our own judgments.

| System | Evidence and strength | Practice to adopt | Overlap to avoid |
| --- | --- | --- | --- |
| **Spec Kit** | Separates specification, plan, tasks, and convergence; also offers bug and idea-evaluation paths. Analysis compares requirements, plan, and tasks for ambiguity, inconsistencies, and coverage gaps. [README](https://github.com/github/spec-kit/blob/c00dc0551583428a10a94443c58c6a41e5e0138c/README.md), [analyze](https://github.com/github/spec-kit/blob/c00dc0551583428a10a94443c58c6a41e5e0138c/templates/commands/analyze.md) | Explicit requirement → slice/task → evidence checks before completion; distinguish documentary coverage from verified behavior. | Installing the whole system adds a second router, artifacts, and implementation cycle over Matt + Superpowers. Its constitution should not become a competing authority alongside AGENTS and approved criteria. |
| **BMAD Method** | Proportionate planning: small change, Build session, epic, or project. Product/architecture documents help coordinate multiple parts; implemented units need joint verification. [README](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/README.md), [planning path](https://github.com/bmad-code-org/BMAD-METHOD/blob/5e33d3c03ba53187a40ab679d5479cdd4b6ac2fb/docs/plan/choose-a-planning-path.md) | Activate roles/documents for a concrete gap; add integrated verification after multiple slices. | A full PRD and many roles for every fix consume context and interactions without demonstrated benefit. Its backlog and loop duplicate the kit's. |
| **GSD / GSD Core** | The [old README](https://github.com/gsd-build/get-shit-done/blob/bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815/README.md) points to `open-gsd/gsd-core`. The [successor README](https://github.com/open-gsd/gsd-core/blob/84ed9b843d9c383e46144931328676fef929a34c/README.md) describes Discuss/Plan/Execute/Verify/Ship phases, separate contexts, and durable state (`STATE.md`, `CONTEXT.md`). | Compact implementer/reviewer briefs and resuming from state/evidence, consistent with the local approach. Measure resume quality. | Do not layer its orchestrator and parallel waves onto local SDD. README context-size claims do not guarantee the available runtime's capacity. Runtime adaptation requires its installer; copying individual commands does not certify compatibility. |
| **Agent OS** | Extracts code-specific conventions, documents them briefly, and loads relevant ones through an index. [README](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/README.md), [discover-standards](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/commands/agent-os/discover-standards.md), [inject-standards](https://github.com/buildermethods/agent-os/blob/475b0cac4c7c5cf2336ad5a663b691a6d3415e05/commands/agent-os/inject-standards.md) | Lightweight index of observed conventions, code origins, rationale, and exceptions; load by relevance. | Do not make every existing pattern mandatory. Inspected commands assume `AskUserQuestion` and specific paths; they are not portable Codex skills without adaptation. Avoid another standards store duplicating project ADRs/context. |

## Decision for this starter

Keep **one workflow entry point**. These systems are complete alternatives or sources of practices,
not dependencies to stack. Prefer three bounded improvements:

1. Check consistency between requirements, slices, and evidence, inspired by Spec Kit.
2. Size the process to risk and verify integration across slices, as suggested by BMAD.
3. Keep context short, durable, and selective, drawing on GSD and Agent OS.

These are recommendations, not claims of implemented capabilities. Importing code or text requires
snapshots, licenses, diffs, and verification like other kit dependencies. This research did not
install or execute frameworks, installers, hooks, or instructions found in sources.

To determine whether a practice improves the kit, compare current and modified workflows on a small
change, a multislice feature, a bug, and session recovery: same criteria, missed defects, required
interventions, time/cost, and repository integrity. Do not choose a framework solely by star count.
