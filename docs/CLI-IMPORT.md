# Optional command-line import

This path requires Python 3.9+. For setup from chat without Python commands, see the [README](../README.md).

## Clone and import

Requires **Python 3.9+** and an AI coding client. The instructions below target Codex; other clients require compatibility checks. Git and Bash are needed for the Superpowers helpers. No Python packages need installing.

```bash
git clone https://github.com/ilMarz/developer-starter-kit.git
cd developer-starter-kit
```

Run the following commands from this kit directory. Replace the example project paths as needed; the destination must be outside the kit.

### Create a project from scratch

Preview the import, then create the project directory with the kit inside:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/my-store" --name my-store --profile typescript
```

Open **`$HOME/Projects/my-store`** in Codex and send this in chat:

```text
Use $dev-workflow. Build an ecommerce store for handmade products.
Clarify the requirements, set up the stack, and prepare the first working slice.
Before coding, suggest the skills, conventions, tools, agents, and models to use.
```

The destination must be empty or nonexistent. The bootstrap copies the kit; stack selection, dependencies, application code, and tests are handled with the agent afterward.

### Add the kit to an existing project

Use `--existing` to import alongside your current code:

```bash
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --existing --dry-run
python3 tools/bootstrap.py --target "$HOME/Projects/existing-store" --name existing-store --existing
```

Open **your existing project** in Codex and send:

```text
Use $dev-workflow. Add percentage discount codes with expiration dates.
Merge any kit instruction proposals with the existing instructions first.
Inspect the checkout and tests, preserve the stack, and propose the first slice and working approach.
```

Existing instruction files are preserved; merge proposals go into `.devkit/proposed/`. The command lists required merges. Other conflicting files stop the import before any writes; identical files are reused. `--existing` is not an upgrade command.

### Import options

| Option | Purpose |
| --- | --- |
| `--target PATH` | Required. Destination directory, absolute or relative |
| `--name NAME` | Required. Project name in configuration; does not rename the directory |
| `--profile generic\|python\|typescript\|ai` | Setup guidance; default: `generic`. Choose one value |
| `--existing` | Allow a conservative import into a nonempty project |
| `--dry-run` | Preview and validate without writing files |
| `--help` / `-h` | Show command help |

All profiles include the same skills. `ai` means the **product** uses AI at runtime; AI-assisted development works with every profile. Import does not initialize Git, install dependencies, or publish anything.


The entry skill can run these commands for you when Python is available. Without Python, it uses the documented file-tool import procedure.
