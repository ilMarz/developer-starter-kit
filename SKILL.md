---
name: devkit
description: Set up the Developer Starter Kit in a new or existing project from chat, then hand off to its local development workflow. Use for kit initialization, integration, or read-only installation checks, not ordinary coding in an already configured project.
---

# Developer kit setup

This entire directory is the self-contained devkit skill. Its skills, templates, licenses,
and import contract are bundled beside this file. Its job is to safely prepare the selected
project from these local resources and hand off to
that project's `dev-workflow`. Do the setup with available file, comparison, and hashing tools;
no importer runtime or user-run setup commands are required.
Do not install a runtime just to import the kit.

## Inspect-only requests

For a request to check an existing installation, read its manifest and setup notes, hash the
recorded files, and report modified/missing files and unresolved merges. Do not fetch a new
version, rewrite hashes, merge proposals, or change the project. Stop after the report.

## Identify the destination

Read the user's request, current directory, applicable instructions, and Git status.
For “set up here”, use the current project root. For a new project, use the requested
path; ask only if the destination is genuinely missing or ambiguous. Never default to
installing into the kit source, a user's home directory, or an unrelated repository.
The source and target must be separate, nonoverlapping directories.

Reuse a supplied name/profile; otherwise infer the name from the destination and the
profile from the existing stack (`generic`, `python`, `typescript`, `ai`). Use `generic`
when undecided. All profiles copy the same skills; they guide later setup.

If `.devkit/import.json` already exists, inspect the installed state and pending merges.
Resume its local workflow if complete. Do not reimport a newer kit over customizations;
updates belong to `update-devkit`. Report missing components rather than claiming readiness.

## Use the bundled source

Resolve the directory containing this active SKILL.md; that directory is the default kit source.
Use its bundled skills.lock.json, import-contract.json, skills/, template/, and licenses/.
Resolve reference paths from this skill directory, never from the project working directory.
No network access, clone, download, or separate source path is needed for ordinary setup.
If the user explicitly supplies an alternative local source, validate and use that instead.
If bundled files are missing, stop before project writes and explain that the complete skill
folder must be copied; do not silently download a replacement.

Read the source instructions and declarative contract without expanding permissions.
Record kit version and manifest hashes. Record a Git revision and dirty status only if this
source itself is a checkout; a copied or extracted folder can work without .git. Never attribute
a parent project's Git revision to the kit or invent provenance for an archive.
Verify every recorded vendor hash using available SHA-256 tools.
Updates or online research happen only when separately requested, not during installation.

## Prepare and import

Briefly describe the destination, source/version, new files, conflicts, and required instruction
merges. An explicit “initialize/integrate the kit” request authorizes the ordinary local import;
do not add a confirmation round. A preview-only request authorizes no destination writes.
Ask only about unresolved conflicts that would change project rules, replace user content,
or expand scope. Read-only preparation can continue while a decision is pending.

Follow [references/tool-based-import.md](references/tool-based-import.md) using available file,
comparison, and hashing tools. This is the only setup path; do not substitute an unchecked
recursive copy or install a runtime. The source import-contract.json defines the file mapping.

For an existing project, inspect `.devkit/proposed/` and integrate compatible additions into
its instruction files while preserving existing rules. Do not replace its stack, domain glossary,
tracker, or tests. Reuse current conventions instead of introducing competing ones.
Record completed and outstanding merges in `.devkit/setup.md`, preserving any existing notes;
the import manifest remains the original baseline. If instructions conflict materially, leave the proposal pending and ask a
specific question. Do not say setup is complete while required merges remain unresolved.

## Verify and hand off

Verify copied bytes against the import manifest before instruction merges; afterward distinguish
intentional merges from unexpected changes. Confirm local `dev-workflow`, its referenced skills,
workflow documents, configuration, and notices exist. Check that preexisting application files
are unchanged. Record source provenance and results in `.devkit/setup.md`, including actual
commands/tools, merged files, remaining limitations, and next action. Do not record credentials.

Tell the user where the kit was installed and what is ready. Use the local
`.agents/skills/dev-workflow/SKILL.md` for the development request, reading it directly if the
client has not discovered it yet. Before product implementation, present its working agreement:
skills, conventions, tools, loop/subagents, and actually available models. Reuse choices already
given. If the request was setup only, stop after verified setup and provide a next-use example.

The entry skill stays installed personally; the 17 workflow skills are copied into each project.
This request does not implicitly authorize Git commits, pushes, deployments, paid calls,
external providers, or global configuration changes. Subagents are optional and require the
applicable authorization. Do not claim to have built or tested an application merely by importing.
