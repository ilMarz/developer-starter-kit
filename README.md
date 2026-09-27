# Developer Starter Kit

**A reusable toolkit for building software with AI agents, from a new idea or inside an existing codebase.**
Copy this whole repository into your skills directory, then ask it to add 17 project skills, development conventions, planning templates, and a configurable implementation/review workflow.

**How it works:** install `devkit` once → open a project → ask it to set up the kit → choose your working approach → implement and verify.
The import prepares your project for this workflow; the agent then helps build the application.

## Quick start — install once, use from chat

### 1. Copy the whole repository into Codex skills

Download this repository as a ZIP and extract it. Rename the extracted folder to **devkit**
and copy the **entire folder** into **~/.codex/skills/** (or your custom CODEX_HOME/skills).

The result should be:

```text
~/.codex/skills/devkit/
├── SKILL.md
├── agents/
├── references/
├── skills/                 # 17 bundled project skills
├── template/
├── licenses/
├── import-contract.json
└── skills.lock.json
```

Keep the other repository files too; this diagram shows the main parts.
**Everything needed for kit setup is included. No additional downloads or source path are needed.**
The agent uses this installed folder directly, even without Git metadata or network access.
It needs file/comparison/hash tools, not Python or an installation runtime.
Git and Bash are needed only for development helpers that use them.

Alternatively, clone directly into the destination if it does not already exist:

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git "${CODEX_HOME:-$HOME/.codex}/skills/devkit"
```

If devkit is already installed, preserve customizations and compare versions before replacing it.
Do not copy only SKILL.md or create an extra nested repository folder inside devkit.

### 2. Create a project from scratch

Send in **Codex chat**, replacing the destination with your preferred path:

```text
Use $devkit. Create a new project at ~/Projects/my-store for an ecommerce store.
Set up the kit, then help me clarify requirements and choose the stack.
Before implementation, propose the skills, tools, agents, loop, and models to use.
```

The agent prepares the destination and then reads its local `dev-workflow` skill.
Importing the kit does not itself build the store or install application dependencies.

### 3. Or add it to an existing project

Open your project in Codex and send:

```text
Use $devkit. Integrate the kit into this project, preserving its code, stack,
tests, and existing instructions. Set up only; do not implement features yet.
```

The agent previews the import, preserves existing files, and merges compatible instruction
additions. Conflicting rules require a decision; other file conflicts stop the import.
For a preview without project writes, add **“Preview only; do not modify the project.”**
Already configured projects resume their existing workflow; they are not silently upgraded.

### 4. Develop with the project skills

```text
Use $dev-workflow. Add percentage discount codes with expiration dates.
Inspect the checkout and tests, then propose the first slice and working approach.
```

**`devkit` sets up the project; `dev-workflow` guides development afterward.**
The complete kit stays in your personal installation; the 17 workflow skills are local to each project.
See the [import procedure](references/tool-based-import.md) for preservation and verification rules.

## What's included

| Capability | What it gives you |
| --- | --- |
| **1 entry + 17 project skills** | Reusable instructions for requirements, design, implementation, debugging, review, and kit maintenance |
| **Optional multi-agent development** | A coordinator, scoped implementer tasks, and separate review; independent work can run in parallel when authorized and supported |
| **Optional agentic loop** | Implement → test → review → fix, with agreed attempt/time budgets and stop conditions |
| **Models by role** | Choose available models for planning, implementation, review, debugging, and research |
| **Vertical slices** | Small increments that deliver testable behavior across the required layers |
| **Specs and ADRs** | Acceptance criteria and architecture decision records for significant choices |
| **Progress and handoff** | A durable log of decisions, evidence, limitations, and the next task |
| **Agent-driven import** | Preserve existing files, verify vendor hashes, and record the imported baseline |
| **Kit CI** | Verify vendor snapshots, import metadata, and maintenance checks |

Multi-agent execution uses your client's tools. The kit does not ship an agent runtime, provider credentials, background service, or technical spending cap. Project test runners and browser tools are selected from what is actually available.

### Skill inventory

| Purpose | Skills | Source |
| --- | --- | --- |
| Set up a new or existing project | `devkit` (installed personally) | Original |
| Start or resume work | `dev-workflow` | Original |
| Clarify requirements and domain | `grilling`, `domain-modeling`, `grill-with-docs` | Matt Pocock |
| Write specifications and slices | `to-spec`, `to-tickets` | Matt Pocock |
| Design, test, and debug | `codebase-design`, `tdd`, `diagnosing-bugs` | Matt Pocock |
| Configure tracker and domain docs | `setup-matt-pocock-skills` | Matt Pocock |
| Plan and isolate changes | `writing-plans`, `using-git-worktrees` | Superpowers |
| Coordinate implementation and review | `subagent-driven-development`, `requesting-code-review` | Superpowers |
| Verify and integrate completed work | `verification-before-completion`, `finishing-a-development-branch` | Superpowers |
| Discover and propose kit improvements | `update-devkit` | Original |

Third-party skills are pinned snapshots with recorded hashes and licenses. See [provenance](THIRD_PARTY_NOTICES.md) and [compatibility rules](template/docs/development/COMPATIBILITY.md).

## Choose your working approach

Before substantial implementation, the agent proposes a subset of skills, conventions, tools, agents, loop, and models. Accept it or change it in chat:

```text
Proceed with the proposed approach. Use subagents and at most two fix attempts.
```

```text
Skip to-spec; the ticket already defines the requirements.
No subagents or loop for this task: implement directly and run the agreed checks.
```

```text
Use [available model ID] for implementation and [another available ID] for review.
```

You can also request direct implementation without skills. Existing choices are reused; task preferences become permanent only when requested. Model selection depends on client support.

To resume later:

```text
Use $dev-workflow. Resume from docs/progress.md, verify the current state,
and continue the first incomplete task using our agreed choices.
```

### Files added to your project

| Location | Contents |
| --- | --- |
| `.agents/skills/` | The 17 local skills |
| `AGENTS.md`, `CONTEXT.md` | Agent instructions and domain glossary |
| `.devkit/` | Project commands, workflow preferences, model roles, loop budgets, and import records |
| `docs/development/` | Setup guidance, workflow conventions, and spec/ADR/slice/plan/report/eval templates |
| `docs/agents/`, `docs/progress.md` | Tracker conventions and durable progress log |

## Maintain the kit

**Discover improvements:** open the **kit directory** in Codex and ask:

```text
Use $update-devkit. Find useful new skills, tools, conventions, and updates.
Propose what to integrate, why, and how to verify it.
```

Reports go into `docs/updates/`. Select what to apply with `Use $update-devkit. Apply U-01 from [report path].` No automatic adoption or propagation to existing projects. If discovery fails, ask the agent to read `skills/update-devkit/SKILL.md` directly.

**Verify an installation:** ask in chat:

```text
Use $devkit. Check this installation against its recorded hashes and report changes.
Do not modify or update anything.
```

Integrity checks confirm expected copies, not application quality. Changes may be intentional.
Repository maintainers can run `node tools/check-kit.mjs` and `node --test tests/*.test.mjs`;
these are read-only maintenance checks, not installation requirements.

## Further reading

[Setup guide](template/docs/development/START-HERE.md) ·
[Working agreement](template/docs/development/WORKING-AGREEMENT.md) ·
[Loop and models](template/docs/development/AGENTIC-LOOP.md) ·
[Research sources](docs/SOURCES.md) ·
[Other frameworks](docs/ECOSYSTEM.md) ·
[Validation and limits](docs/VALIDATION.md) ·
[Changelog](CHANGELOG.md) ·
[Licenses](THIRD_PARTY_NOTICES.md)
