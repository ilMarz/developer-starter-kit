# Research for updates and opportunities

Start from the current kit's objectives and difficulties. If there is no observed problem,
label the benefit as a hypothesis. Consider maintenance, new capabilities, and fewer instructions;
do not reward the number of installed skills.

## Starting sources, not an exhaustive list

- Actual origins in `skills.lock.json` and the SOURCES/ECOSYSTEM documents.
- [Matt Pocock](https://github.com/mattpocock/skills) and [Superpowers](https://github.com/obra/superpowers):
  releases, skill code, and referenced resources. Local versions may differ.
- [OpenAI skills](https://learn.chatgpt.com/docs/build-skills),
  [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), and
  [changelog](https://learn.chatgpt.com/docs/changelog): verify actual tools and clients.
- [Anthropic Engineering](https://www.anthropic.com/engineering): harnesses, evals, and context;
  distinguish their results from guarantees for our environment.
- Maintained repositories and primary sources for new proposals. Catalogs such as
  [skills.sh](https://skills.sh/) help discovery; they do not certify quality.

Look beyond these names: debugging, behavioral tests, agent evaluation, execution safety,
memory, model routing, costs, CI, and compatibility. Do not force every category into every update;
select relevant ones.

## Evidence to collect

URL and access date; release/event date; version/commit; files/symbols read; observed license and
maintenance; required dependencies/tools; differences from current adoption; limitations of static
inspection. A README screenshot or star count does not prove compatibility or effectiveness.

## Proportionate experimentation

Compare the current workflow and proposal on the same problem with agreed criteria.
Observe correctness, missed problems, rework, cost/time, and required interventions.
Semantic judgments need reference, negative, and not-evaluable cases; use deterministic checks
for exact properties. If a service requires new data access or costs, first specify how to test
within the authorized scope.

A weak result may suggest improving the question, context, or decomposition; record the experiment
without forcing adoption. A useful improvement can also remove a redundant step or replace two
overlapping skills with one.
