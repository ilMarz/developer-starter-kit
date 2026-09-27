# Developer Starter Kit

**A reusable toolkit for building software with AI agents, from a new idea or inside an existing codebase.**
Install one entry skill, then ask it to add 17 project skills, development conventions, planning templates, and a configurable implementation/review workflow.

**How it works:** install `devkit` once → open a project → ask it to set up the kit → choose your working approach → implement and verify.
The import prepares your project for this workflow; the agent then helps build the application.

## Quick start — install once, use from chat

### 1. Install the entry skill in Codex

Paste this into **Codex chat**:

```text
Use $skill-installer to install the devkit skill from
https://github.com/ilMarz/developer-starter-kit/tree/main/installer/devkit
```

The entry skill is self-contained: you do not need to clone the whole kit first.
It retrieves a source snapshot when setting up a project. You need an agent with file tools
and access to the source repository (or an existing local copy).
**No Python commands are required from you.** When Python is unavailable or excluded,
the agent imports with file/comparison/hash tools. Python remains optional for the CLI.
Git and Bash are required only for the helpers that use them.

Prefer to clone and install manually? From a terminal:

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git
cd developer-starter-kit
skill_dir="${CODEX_HOME:-$HOME/.codex}/skills/devkit"
if [ -e "$skill_dir" ] || [ -L "$skill_dir" ]; then
  echo "devkit already exists; compare before updating."
else
  mkdir -p "$(dirname "$skill_dir")"
  cp -R installer/devkit "$skill_dir"
fi
```

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
The entry skill stays in your personal installation; the 17 workflow skills are local to each project.
For explicit terminal commands and all parameters, see [optional CLI import](docs/CLI-IMPORT.md).

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
| **Bootstrap and verification CLI** | Import files conservatively, verify vendor snapshots, and detect changes after import |
| **Kit CI** | Snapshot verification and bootstrap tests on Python 3.11 and 3.13 |

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

**Verify files (optional Python CLI):** run from a cloned kit directory:

```bash
python3 tools/verify.py                                      # Check vendor snapshot hashes
python3 -m unittest discover -s tests -v                     # Test the bootstrap
python3 tools/verify.py --project "$HOME/Projects/my-store"  # Find changes since import
```

Integrity checks confirm expected file copies, not application quality. Project changes may be intentional. Without Python, ask `$devkit` to inspect the installed state with file/hash tools. Verifier exit codes: `0` unchanged, `1` modified/missing project files, `2` error. Use `--help` for command help.

## Further reading

[Setup guide](template/docs/development/START-HERE.md) ·
[Working agreement](template/docs/development/WORKING-AGREEMENT.md) ·
[Loop and models](template/docs/development/AGENTIC-LOOP.md) ·
[Research sources](docs/SOURCES.md) ·
[Other frameworks](docs/ECOSYSTEM.md) ·
[Validation and limits](docs/VALIDATION.md) ·
[Changelog](CHANGELOG.md) ·
[Licenses](THIRD_PARTY_NOTICES.md)
