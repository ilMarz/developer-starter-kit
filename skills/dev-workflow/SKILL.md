---
name: dev-workflow
description: Start or resume a feature, bug fix, or project using the local developer starter kit, connecting specifications, slices, implementation, and evidence.
---

# Developer workflow

Read applicable `AGENTS.md` instructions and the project's `docs/development/WORKFLOW.md`.
If they are missing, explain that the kit needs importing; do not invent configuration.
Read `.devkit/project.json` for status and commands. Initial null values are not passed checks.
For first-time setup, follow START-HERE.md.

Before the first substantial change, follow the **working agreement** in
`docs/development/WORKING-AGREEMENT.md`: present suggested skills, conventions, tools,
delegation/loop, and actually available models, then let the user choose.
Choices already provided in the task count; do not request approval twice.
An explicit request to go directly to code or exclude a skill overrides the suggested path below.
Read `.devkit/workflow.json` when present, applying the user's task overrides first.
These are agent-read preferences, not runtime controls.

Suggest an approach proportionate to the request, then use only the selected subset:

- Ambiguous new feature: `grill-with-docs` for open points only, then `to-spec`.
- Approved specification: reuse it; use `to-tickets` if distinct increments are needed.
- Ready slice: execution plan with `writing-plans` for multistep implementation;
  `using-git-worktrees` as appropriate and `subagent-driven-development` if delegation is available and authorized.
- Bug: `diagnosing-bugs`, observed reproduction, fix, and relevant regression verification.
- Small, clear change: execute directly with proportionate verification.

For test-first development, use `tdd`; for interface decisions, use `codebase-design`.
Suggest review, `verification-before-completion`, and `finishing-a-development-branch` when Git
integration is needed. The user may choose direct verification without these skills;
still report what was verified. Do not duplicate SDD reviews.
Do not invoke an excluded skill indirectly through another: disclose the dependency and adapt.
For example, without `grilling`, clarify only essential ambiguities; without subagents,
do not start SDD while pretending to provide independent review.

Included skills live in `.agents/skills/<name>/SKILL.md`. If the client has no Skill tool,
read the file and only its required resources. The upstream `superpowers:` prefix refers
to the same-named skill in this directory; it does not require another plugin.
`grill-with-docs` also requires `grilling` and `domain-modeling`.
Resolve internal relative paths from the skill's directory. Do not replace a local skill
with a global skill of the same name without comparing versions.

For tool constraints, procedure conflicts, durable logging, and existing-project imports,
see `docs/development/COMPATIBILITY.md`. Implementer subagents must not delegate;
the coordinator assigns reviews and tasks. The current task and existing authorization
take precedence over kit conventions.

End each slice by recording verified criteria, commands actually run, limitations,
commit or diff, and the next step in `docs/progress.md`.
