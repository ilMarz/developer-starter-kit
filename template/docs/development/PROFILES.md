# Project profiles

The selected profile is in `.devkit/project.json`. Apply only the relevant profile, using current
versions verified during setup. No framework is mandatory.

| Profile | Setup to complete |
| --- | --- |
| generic | Runtime, manifest/lockfile, relevant install/lint/test/build commands, first observable test |
| python | Python version, virtual environment, pyproject, consistent package manager and lockfile, pytest or existing runner, lint/typecheck where useful |
| typescript | Node runtime, package manager and lockfile, tsconfig, lint, tests, and build; browser/e2e if there is a UI |
| ai | Everything required by the stack, plus rubrics, separate datasets, redacted traces, errors/not-evaluable outcomes, and live tests distinguished from doubles |

For every profile: reproducible setup from a clean checkout, secret/dependency checks, CI with tests
appropriate to the change, and observability/release procedures proportionate to the product.
Blocking CI and branch protection are project decisions; the kit does not enable them.
For persistence/migrations, verify compatibility, test data, and feasible backup/recovery.
For web apps, include accessibility and empty/error states; for APIs, contracts and errors;
for jobs, idempotency, timeouts, bounded retries, and reconciliation. Apply checks where relevant.

For AI products, separate product evals from software tests and skill evals.
Use positive, negative, incomplete, and adversarial cases, with separate development/calibration/test sets.
Semantic graders require calibration and human checks; measure false passes, errors, coverage,
and total cost. An agent saying 'completed' is not evidence of the outcome.
