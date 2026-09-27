# Research and kit decisions

Accessed September 27, 2026. These are selected practices, not a claim to cover every stack or
best practice. Web pages may change; skills are pinned in skills.lock.json.

| Primary source | Relevant guidance | Application in the kit |
| --- | --- | --- |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Precise task, progressive disclosure; repository skills in .agents/skills; same-named skills are not merged | Local copies and a short router; explicit path selection |
| [OpenAI: Best practices](https://learn.chatgpt.com/guides/best-practices) | Repository context and concrete verification | Short AGENTS, commands verified during setup |
| [OpenAI, September 11, 2026: Rethinking skills](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Revisit excessive or overlapping instructions and descriptions | Load only the relevant procedure; lightweight path for small changes |
| [Michael Nygard: ADR](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Short decisions with context, status, and consequences | ADR template; preserve superseded history |
| [Matt Pocock](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills) | Vertical slices, explicit dependencies, interface tests, glossary | to-tickets, tdd, domain-modeling; separate specification and plan |
| [Anthropic: Long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | Increments and artifacts for resuming across sessions | Durable log and handoff; do not rely solely on chat summaries |
| [Anthropic, March 24, 2026: Harness design](https://www.anthropic.com/engineering/harness-design-long-running-apps) | Planning, generation, and evaluation with concrete criteria | Separate roles, feedback from execution; benefit remains to be measured |
| [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Distinguish traces from actual outcomes; repeatable evaluations | Eval template with outcomes, errors, costs, and negative cases |
| [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Scoped delegation, model configuration, care with concurrent writes | One implementer per checkout, briefs and reviewer; explicit fallback |
| [Superpowers](https://github.com/obra/superpowers) | Planning, isolation, review, and verification | Four local copies plus two upstream snapshots; documented integration rules |

## Our proposals, to be measured

The single router, offline import, two-level logging, and model profiles are kit choices,
not standards mandated by these sources. Their effectiveness needs testing across projects.
No universal model, cost threshold, time limit, or provider is claimed to be best.
Refresh sources before substantial procedure, API, or model changes; compare at least a small
change, a complete feature, a bug, and a resumed session.
