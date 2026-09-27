# Working agreement and user-selected subset

Before the first implementation or substantial change in a task, present a short proposal for
the approach you intend to use. This selects a working method; it does not authorize external effects.
During preparation and research, you may read code, verify facts, and prepare the proposal without
changing the product.

## Suggested working agreement

> **Objective:** add discount codes to checkout.
> **Skills:** to-spec for unresolved criteria; tdd for tests; requesting-code-review for a separate
> review. No full interview if the specification is already approved.
> **Conventions:** one verifiable slice; an ADR only if a significant decision arises; update the log.
> **Tools:** file reading/search, terminal, Git, and the existing test runner; browser only if available
> and needed to verify checkout.
> **Execution:** a bounded implementation/test/fix loop with an agreed budget; one implementer and
> one reviewer if subagents are authorized.
> **Models:** the current model, or available IDs proposed for each role.
> **Choice:** proceed with this approach, change the subset, or implement directly?

Adapt this to the task; it is not a mandatory list of tools to execute. Name only verified available
tools and models; label missing capabilities as requiring configuration. 'Strong model' is a preference,
not an actual model selection.

## How to choose

The user can reply in natural language without editing JSON:

- “Proceed with this approach.”
- “Skip to-spec: the requirements are already in the ticket.”
- “No skills or subagents; go directly to implementation.”
- “Use the loop, but stop after two fix attempts.”
- “Use [available ID] to implement and [another ID] for review.”
- “No browser; verify from the CLI.”
- “No ADR this time; keep the rationale in the report.”

If the initial request already specifies choices and asks to proceed, briefly summarize them and work.
Do not introduce another confirmation wait. If the user only requests a proposal, or has not selected
an approach for a substantial change, present the agreement and wait for their choice before dependent
changes. Silence or elapsed time is not acceptance. For explicitly requested typos and minimal edits,
one line describing a proportionate approach followed by execution is enough; no questionnaire.

## Persistence and precedence

Project preferences live in `.devkit/workflow.json`, roles/models in `.devkit/models.json`, and budgets
in `.devkit/loop.json`. Initial files are proposals. Record task choices in the plan or log before
executing them. Update permanent preferences only when the user says they apply to future tasks too.
A choice for 'this time' does not automatically change project defaults.

Operational precedence: client instructions and applicable authorization, the user's current request,
previously agreed preferences, then kit suggestions. The kit cannot make a rejected skill mandatory.
Do not reopen the same choice for every task, compaction, or agent handoff; recover it from the log.

Disabling a skill removes that procedure; it does not allow invented results. If a choice prevents
essential verification, explain the limitation and agree on an alternative; do not weaken acceptance
criteria yourself. Without a loop, perform the agreed change and verification and report the outcome;
no open-ended correction/escalation cycles. Without subagents, disclose direct review.

## Dependencies and changes of approach

Pass exclusions, models, and budgets to subagents. Vendor instructions do not reactivate excluded
skills or tools. If a workflow depends on a disabled skill, adapt it or propose an alternative first.
Ask for a new choice only for material changes: an unavailable model without an agreed fallback,
new effects/tools, scope expansion, or an exhausted budget.
JSON does not technically block tools or spending; the agent must respect these constraints and,
where necessary, configure them in the runtime too.
