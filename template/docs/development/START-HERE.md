# Getting started

If you arrived through the personal `devkit` entry skill, inspect `.devkit/setup.md` for
source provenance, checks, and instruction merges already performed. Reuse that work.
`devkit` prepares the project; the local `dev-workflow` below handles development.

1. Check `.devkit/import.json`: any `pending_manual_merges` require merging proposals in
   `.devkit/proposed/` with existing instructions. Do not overwrite them.
2. Open the project directory in Codex. Use the local `dev-workflow`. If global copies share
   its name, specify the local path; the client may show both.
3. Explain the objective, users, example outcomes, constraints, and exclusions. For an existing
   repository, the agent first inspects implementation, Git, instructions, and tests.
4. Select the stack and versions based on the project; read `PROFILES.md` for your profile.
   Create suitable manifests/lockfiles and configure commands in `.devkit/project.json`.
   The kit import has not installed application runtimes or dependencies.
5. For a new project, initialize Git and record a baseline when the content is ready.
   Check the diff and secrets before committing. Do not add remotes or publish without authorization.
6. Define criteria, the first slice, budgets, and limits in `.devkit/loop.json`. Configure roles
   in `.devkit/models.json` after checking models available in the client.
7. Execute the first slice through actual behavior, add necessary checks to stack-appropriate CI,
   and record the result in `docs/progress.md`.

Before coding, the agent presents the working agreement in `WORKING-AGREEMENT.md`: you can change
skills, conventions, tools, loop, subagents, and models. If you already specified your choices
and asked to proceed, no further confirmation is needed. Task-specific choices do not automatically
become permanent preferences.

`setup-matt-pocock-skills` is included to reconfigure tracker and layout. The kit import already
provides the minimal local files; no need to repeat the questionnaire if the conventions suit you.

## Ready-to-use prompts

**New project**
> Use $dev-workflow. Objective: [...]. Constraints: [...]. Reference outcome: [...].
> Prepare the specification, criteria, and first slice. Clarify only decisions not inferable from context.

**Authorized implementation**
> Implement slice [ID] using $dev-workflow and subagents. Approved criteria are in [file].
> Use the agreed budgets and update evidence and the log. Continue until completion or a justified stop.

**Resume**
> Resume from docs/progress.md. Check commits, diffs, and evidence, recover the plan and SDD ledger
> if present, then continue the first incomplete task without repeating verified work.

**Bug**
> Use $dev-workflow and diagnosing-bugs. Input [...] produces [...] but should produce [...].
> Reproduce the case, fix within [...], and verify the original case and regressions.
