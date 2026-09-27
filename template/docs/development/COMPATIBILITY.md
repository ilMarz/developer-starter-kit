# Skill and client compatibility

Vendor skills are preserved byte for byte. These are proposed local project conventions;
they do not claim to rewrite upstream skills and cannot override explicit user instructions
or client constraints.

| Difference | Kit convention |
| --- | --- |
| A vendor skill prescribes a step excluded by the user | The selected subset takes precedence; adapt the procedure or execute directly without invoking excluded skills |
| Matt uses behavior tickets; SDD expects tasks and files | Derive an execution plan from tickets, preserving IDs and criteria; do not change the specification |
| to-tickets defaults to .scratch | Use the configured tracker: persistent, versioned docs/work |
| SDD resolves ambiguity; the user approves requirements | Decide reversible details within scope; ask about criteria, tradeoffs, and scope expansion |
| Repeated confirmation requirements | Reuse existing decisions; ask only about new, unauthorized material matters |
| Finishing always requires a menu | Carry out the already authorized destination; otherwise prepare a reviewable result and ask |
| SDD and worktree cleanup | Save durable summaries/evidence first; use native archival tools when available |
| superpowers:skill references and the Skill tool | Resolve the local name in .agents/skills; read the skill file if the client has no loader |
| executing-plans mentioned as an alternative | Not included: use the kit's coordinated direct path and disclose the missing skill |
| Matt TDD defers refactoring until review | Use red/green for behavior; perform justified refactoring after verification, keeping tests green |
| Matt requires agreement on test interfaces | Reuse agreement in the specification; do not block on confirmation already recorded |
| Duplicate review | SDD task review covers requirements and quality; final review covers integration without unnecessary repetition |
| tdd references Matt's code-review skill | Not included: use the requesting-code-review/SDD reviewer for that stage, without claiming to have used the missing skill |
| Skill model defaults | Check availability; role configuration expresses preferences, while the client determines what can run |
| Generic shell setup examples | Use actual manifests and lockfiles; pyproject.toml does not imply Poetry |

## Portability

The kit does not install plugins, MCP servers, credentials, hooks, schedulers, or application runtimes.
Codex reads local skills; for other clients, verify discovery, permissions, tools, and metadata.
If subagents are unavailable, do not pretend contexts are separate: implement directly and disclose
that review is not independent, or request a human reviewer when the risks require one.
Use native worktree tools when available; manual Git is a fallback.
A worktree is not an execution sandbox. SDD helpers require Bash and Git.

Global skills with the same names are not removed. Specify project copies when invoking skills;
disable global copies only when the user requests it.
