# Agentic loop and models by role

The kit describes a cycle carried out by the agent in its client. It does not include a
background service, an API orchestrator, or a technical mechanism that caps a bill.

```text
approved criteria → ready slice → plan/environment
 → implementation → observed execution → review
 → [success] report/authorized integration
 → [fixable defect + budget] diagnosis → patch → tests/regressions → focused review
 → [uncertainty, budget, or missing authorization] candidate + explained stop
```

## Operating conditions

Before execution, agree on scope, criteria, commands, time/attempt budgets, and cost if measurable.
Record authorization and destination. Values in loop.json are initial proposals to confirm per task,
not budgets already approved by the user. Do not increase budgets or change criteria to obtain a pass.

Each iteration records slice/task ID, actual model, commit/diff, commands, exit codes, evidence,
review, known usage, and next step. A tool error is an error, not a pass.
After an interruption, reconcile state before repeating actions with side effects.

Stop when the objective is verified, the budget is exhausted, repetition produces no new evidence
or improvement, a criterion is inconsistent/ambiguous, an essential capability is unavailable,
or an effect is unauthorized. The effective fix limit is the stricter of the project and skill limits.
Do not start another iteration if its estimate exceeds the remaining budget. If usage cannot be
measured, disclose that limitation and do not promise a spending cap; agree on an alternative limit
before paid calls. Configure technical limits with the provider when needed.

## Roles and models

`.devkit/models.json` contains roles, optional IDs, and fallback policy. It is not a native Codex
configuration file. The coordinator reads it and translates preferences into available tool calls.

| Role | Starting preference | When to use more capability |
| --- | --- | --- |
| planner | Model capable of design reasoning | Ambiguous requirements, architecture, tradeoffs |
| implementer | Balanced model | Broad integrations and difficult debugging |
| reviewer | Balanced or strong model, separate context | Security, concurrency, migrations, final review |
| debugger | Balanced model | Complex hypotheses and intermittent problems |
| researcher | Fast model for bounded retrieval | Technical synthesis with conflicting sources |

Before dispatch, verify IDs exposed by the client; select and record them for the task.
Different models per role are optional: two agents using the same model can still have separate
contexts. A different model does not guarantee independent errors.
The kit embeds no universal provider ID or 'latest' model name.

If the client supports per-subagent selection, explicitly pass supported model and reasoning values.
You may inherit the model already configured in the client, but disclose this rather than claiming
a different model was used. An unauthorized fallback requires a decision.
Changing the main chat's model may require user action in the client.
External providers require runtime, credentials, and data policies; a JSON preference neither
enables another provider nor authorizes sending data.

## Coordination

One implementer at a time in a shared checkout. Independent research/review may run in parallel
when appropriate. A brief includes objective, constraints, files/interfaces, expected verification,
and output rather than the entire chat history. Check concurrency limits in the client;
the kit does not prescribe a universal limit. The coordinator maintains the log;
subagents do not assign additional reviews to themselves.

## Two different loops

This is the software development loop. If the product itself contains agents, its runtime loop
needs its own implementation: persistent state, permissions, tools, timeouts/retries,
observability, and evals. Do not confuse the kit with those product capabilities.
