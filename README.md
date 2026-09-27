# Developer Starter Kit

Version **0.2.1** · research dated September 27, 2026.
A standalone kit for developing with AI agents: 17 skills, specification/ADR/slice templates,
a development loop, configurable skills and models, conservative imports, and verification.
You can move this directory. It does not depend on any other project.

## 1. Open a terminal in the kit directory

Clone the public repository on another computer:

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git
cd developer-starter-kit
```

No GitHub authentication is required to clone it. If you already have a local copy, do not clone it again.
All Python commands below run from the directory containing this README.
If you are in its parent directory:

```bash
cd developer-starter-kit
```

Check Python and inspect the supported arguments:

```bash
python3 --version
python3 tools/bootstrap.py --help
```

Requires **Python 3.9 or later**. The Superpowers development helpers also require Git and Bash.
The bootstrap uses only the Python standard library: no `pip install` or `npm install` is needed to import the kit.

## 2. Import the kit

Examples use `$HOME/Projects/…`: your terminal expands `$HOME` to your home directory.
Replace the destination as needed. Keep the quotes if the path contains spaces.
The destination must be outside the kit directory.

### New project — stack not selected yet

First preview the files that would be copied, without writing anything:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-project" --name my-project --profile generic --dry-run
```

Then perform the import:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-project" --name my-project --profile generic
```

The destination is created if missing. It must be empty or nonexistent for this command.
Skills, templates, and configuration are copied; no application has been implemented yet.

### New Python project

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-backend" --name my-backend --profile python --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/my-backend" --name my-backend --profile python
```

### New TypeScript project

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript
```

### New product using AI models at runtime

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-assistant" --name my-assistant --profile ai --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/my-assistant" --name my-assistant --profile ai
```

`ai` describes the product you are building. AI-assisted development is available in every profile.

### Existing project

Replace `existing-store` with your actual project directory:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --profile generic --existing --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --profile generic --existing
```

`--existing` permits a nonempty destination; it **does not authorize overwrites**.
Existing instruction files remain intact; proposed additions are saved under `.devkit/proposed/`.
The command lists files requiring a merge before using the workflow.
Other conflicting files stop the import before any writes. Identical files are reused.
Existing application code is preserved.

### All bootstrap arguments

| Argument | Required | Default | Meaning |
| --- | --- | --- | --- |
| `--target PATH` | Yes | — | Destination project directory, absolute or relative to the current directory |
| `--name NAME` | Yes | — | Name recorded in configuration; does not rename the directory |
| `--profile generic` | No | `generic` | Stack not selected yet, or another stack |
| `--profile python` | No | — | Python project |
| `--profile typescript` | No | — | TypeScript project |
| `--profile ai` | No | — | Product using AI models at runtime |
| `--existing` | No | Off | Allow a conservative import into a nonempty directory |
| `--dry-run` | No | Off | Validate and show the copy plan without creating files or directories |
| `--help` / `-h` | No | — | Show command help |

Choose **one value** for `--profile`. It is recorded in `.devkit/project.json` and helps the agent
select setup guidance. **Every profile copies the same skills**. It does not install runtimes,
frameworks, dependencies, or services, and does not configure application tests automatically.

The bootstrap does not initialize Git, create commits/remotes/PRs, or execute application workflows.
An identical second import with `--existing` is supported. After customization it may stop on conflicts:
do not use it to upgrade an existing project to a newer kit version.

## 3. Open your project in Codex

Open the directory specified by `--target`, rather than the kit directory.
The following messages belong in **Codex chat**, not in the terminal.

### Start from an idea

```text
Use $dev-workflow. I want to build an ecommerce store for handmade products.
Check the environment, clarify missing requirements, and prepare the first verifiable slice.
Before coding, propose the skills, conventions, tools, loop/subagents, and models you would use.
```

### Change an existing project

```text
Use $dev-workflow. I want to add percentage discount codes with expiration dates.
Merge any proposed kit instructions with the existing ones without replacing them.
Inspect the existing checkout and tests, preserve the stack, and propose criteria and a working subset.
Do not change production.
```

### Accept the proposed approach

```text
Proceed with the proposed subset for this slice. Use the approved criteria and agreed budget.
```

### Change skills, conventions, loop, and models

```text
For this task, skip to-spec: the requirements are already in the ticket.
Do not use subagents or an agentic loop: implement directly and perform the agreed verification.
```

```text
Use the loop with at most two fix attempts. Before dispatch, show me the models actually available
and suggest which ones to use for implementation and review.
```

```text
Use [available model ID] for implementation and [another available ID] for review.
Do not use the [name] skill. This preference applies only to this task.
```

Replace bracketed values. The kit does not prescribe universal model names.
If you already chose an approach and asked to proceed, the agent does not request a second confirmation.
You can also ask to go directly to code without skills. Exclusions apply to subagents and indirect
dependencies too; the agent still reports actual verification and limitations.

### Resume the next day

```text
Use $dev-workflow. Resume from docs/progress.md; check code, commits, and evidence.
Keep the choices already agreed and continue the first incomplete task.
```

### Fix a bug

```text
Use $dev-workflow and diagnosing-bugs. Checkout loses the discount when I change quantities.
Reproduce the problem and propose a fix that verifies the original case and regressions.
```

## 4. Discover improvements and update the kit

Open **the kit directory** in Codex and write in chat:

```text
Use $update-devkit. Search for updates and new skills, tools, and conventions that could improve
this kit. Propose what to integrate, why, and how to verify it.
```

Research includes opportunities outside the current inventory. Proposals with IDs are saved in
`docs/updates/`; this mode leaves operational skills and dependencies unchanged.
It may also suggest removing unnecessary steps, or conclude that no discovery is useful enough.
You do not need to name a technology in advance.

After reading the report, select a proposal and its actual path in chat:

```text
Use $update-devkit. Apply U-01 from [report path].
Preserve customizations, run the relevant checks, and leave U-02 deferred.
```

There is no shell auto-update command: the skill coordinates research and changes through the agent's
tools. It does not monitor in the background. Existing project imports do not update themselves;
compare and merge the authorized changes separately for each project.

The repository exposes the skill through `.agents/skills/update-devkit`, a relative link to
`skills/update-devkit`. If it does not appear in your client, ask:

```text
Read skills/update-devkit/SKILL.md and use it to discover useful improvements for this kit.
```

Imported projects contain regular skill directories under `.agents/skills/`. If global skills share
the same names, the client may show both: specify the project copy.

## 5. Verification commands — run from the kit directory

Check that the 15 third-party skills match the recorded snapshots:

```bash
python3 tools/verify.py
```

Run bootstrap tests:

```bash
python3 -m unittest discover -s tests -v
```

Inspect changes in a project relative to its imported copy:

```bash
python3 tools/verify.py --project "$HOME/Projects/my-project"
```

Show verifier help:

```bash
python3 tools/verify.py --help
```

| Argument/result | Meaning |
| --- | --- |
| No arguments | Verify the hashes of the third-party skills shipped with the kit |
| `--project PATH` | Compare files recorded in `.devkit/import.json` with the current project |
| `--help` / `-h` | Show help |
| Exit code `0` | Check completed with no differences detected |
| Exit code `1` | Project files have changed or are missing since import |
| Exit code `2` | Check/import could not run, conflicts were found, or vendor integrity failed |

**Integrity** means comparing file fingerprints: it confirms expected copies, not their quality or
safety. **Drift** indicates changes since import, often intentional customizations. The verifier
neither fixes them nor proves that the application works. Application tests are configured during setup.

## Project configuration

| Imported file | Contents |
| --- | --- |
| `.devkit/project.json` | Name, profile, and setup/lint/typecheck/test/build/e2e commands to verify |
| `.devkit/workflow.json` | Preferences for skills, conventions, tools, execution, and the initial working agreement |
| `.devkit/models.json` | Models and reasoning by role, selected from available options |
| `.devkit/loop.json` | Budgets and stop conditions; initial values are proposals, not approved limits |
| `AGENTS.md` | Short agent instructions |
| `CONTEXT.md` | Domain glossary |
| `docs/progress.md` | Durable status, evidence, limitations, and next step |
| `docs/development/templates/` | Specification, ADR, slice, plan, report, and eval templates to use when needed |

You can express preferences in chat; no manual JSON editing is required. Task-specific choices become
permanent only when you request it. These files are read by the agent: they are not a runtime,
do not enable a provider, and do not enforce spending limits themselves.

## Contents and documentation

- **Matt Pocock (9):** grilling, domain-modeling, grill-with-docs, to-spec, to-tickets,
  codebase-design, tdd, diagnosing-bugs, setup-matt-pocock-skills.
- **Superpowers (6):** using-git-worktrees, writing-plans, subagent-driven-development,
  requesting-code-review, verification-before-completion, finishing-a-development-branch.
- **Original (2):** dev-workflow, update-devkit.

Third-party copies and licenses are pinned with hashes in `skills.lock.json`. The four local
Superpowers snapshots have no attributed upstream commit; their provenance is explicit.
The client skills skill-creator/skill-installer/openai-docs are not kit dependencies.

- [Getting started](template/docs/development/START-HERE.md)
- [Working agreement and subset selection](template/docs/development/WORKING-AGREEMENT.md)
- [Agentic loop and models](template/docs/development/AGENTIC-LOOP.md)
- [Procedure compatibility](template/docs/development/COMPATIBILITY.md)
- [Sources and practices](docs/SOURCES.md)
- [Spec Kit, BMAD, GSD, and Agent OS comparison](docs/ECOSYSTEM.md)
- [Actual validation and limitations](docs/VALIDATION.md)
- [Changelog](CHANGELOG.md)
- [Licenses and provenance](THIRD_PARTY_NOTICES.md)

The kit's CI in `.github/workflows/check-kit.yml` runs snapshot verification and bootstrap tests on
Linux with Python 3.11 and 3.13; see [validation evidence](docs/VALIDATION.md).
The bootstrap does not configure remotes, publication, or licensing for your future product.
Use it to import the required material rather than copying this entire repository into an application.
