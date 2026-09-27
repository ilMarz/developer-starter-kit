# Developer Starter Kit

**A reusable toolkit for building software with AI agents, from a new idea or inside an existing codebase.**
It adds 17 skills, development conventions, planning templates, and a configurable implementation/review workflow to your project.

**How it works:** import the kit → open your project in Codex → describe the task → choose the suggested skills and tools → implement and verify.
The import prepares your project for this workflow; the agent then helps build the application.

## Quick start

Requires **Python 3.9+** and an AI coding client. The instructions below target Codex; other clients require compatibility checks. Git and Bash are needed for the Superpowers helpers. No Python packages need installing.

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git
cd developer-starter-kit
```

Run the following commands from this kit directory. Replace the example project paths as needed; the destination must be outside the kit.

### Create a project from scratch

Preview the import, then create the project directory with the kit inside:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript
```

Open **`$HOME/Projects/my-store`** in Codex and send this in chat:

```text
Use $dev-workflow. Build an ecommerce store for handmade products.
Clarify the requirements, set up the stack, and prepare the first working slice.
Before coding, suggest the skills, conventions, tools, agents, and models to use.
```

The destination must be empty or nonexistent. The bootstrap copies the kit; stack selection, dependencies, application code, and tests are handled with the agent afterward.

### Add the kit to an existing project

Use `--existing` to import alongside your current code:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --existing --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --existing
```

Open **your existing project** in Codex and send:

```text
Use $dev-workflow. Add percentage discount codes with expiration dates.
Merge any kit instruction proposals with the existing instructions first.
Inspect the checkout and tests, preserve the stack, and propose the first slice and working approach.
```

Existing instruction files are preserved; merge proposals go into `.devkit/proposed/`. The command lists required merges. Other conflicting files stop the import before any writes; identical files are reused. `--existing` is not an upgrade command.

### Import options

| Option | Purpose |
| --- | --- |
| `--target PATH` | Required. Destination directory, absolute or relative |
| `--name NAME` | Required. Project name in configuration; does not rename the directory |
| `--profile generic\|python\|typescript\|ai` | Setup guidance; default: `generic`. Choose one value |
| `--existing` | Allow a conservative import into a nonempty project |
| `--dry-run` | Preview and validate without writing files |
| `--help` / `-h` | Show command help |

All profiles include the same skills. `ai` means the **product** uses AI at runtime; AI-assisted development works with every profile. Import does not initialize Git, install dependencies, or publish anything.

## What's included

| Capability | What it gives you |
| --- | --- |
| **17 skills** | Reusable instructions for requirements, design, implementation, debugging, review, and kit maintenance |
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

**Verify files:** run from the kit directory:

```bash
python3 tools/verify.py                                      # Check vendor snapshot hashes
python3 -m unittest discover -s tests -v                     # Test the bootstrap
python3 tools/verify.py --project "$HOME/Projects/my-store"  # Find changes since import
```

Integrity checks confirm expected file copies, not application quality. Project changes may be intentional. Verifier exit codes: `0` unchanged, `1` modified/missing project files, `2` error. Use `--help` for command help.

## Further reading

[Setup guide](template/docs/development/START-HERE.md) ·
[Working agreement](template/docs/development/WORKING-AGREEMENT.md) ·
[Loop and models](template/docs/development/AGENTIC-LOOP.md) ·
[Research sources](docs/SOURCES.md) ·
[Other frameworks](docs/ECOSYSTEM.md) ·
[Validation and limits](docs/VALIDATION.md) ·
[Changelog](CHANGELOG.md) ·
[Licenses](THIRD_PARTY_NOTICES.md)
