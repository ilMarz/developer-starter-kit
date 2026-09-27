#!/usr/bin/env python3
"""Import a pinned, offline development kit without overwriting project files."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FIRST_PARTY_SKILLS = {'dev-workflow', 'update-devkit'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_path(path):
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise ValueError(f"Symlink non supportato nella destinazione: {candidate}")
        if candidate.exists() and candidate != path and not candidate.is_dir():
            raise ValueError(f"Il percorso attraversa un file: {candidate}")


def verify_vendor():
    lock = json.loads((ROOT / 'skills.lock.json').read_text())
    expected = set()
    for source in lock['sources']:
        for record in source['files']:
            rel = record['path']
            path = ROOT / rel
            if path.is_symlink() or not path.is_file() or digest(path.read_bytes()) != record['sha256']:
                raise ValueError(f"Snapshot skill alterato o incompleto: {rel}")
            expected.add(rel)
    actual = {p.relative_to(ROOT).as_posix() for base in ('skills', 'licenses')
              for p in (ROOT / base).rglob('*') if p.is_file()
              and not (base == 'skills' and p.relative_to(ROOT / base).parts[0] in FIRST_PARTY_SKILLS)}
    if actual != expected:
        raise ValueError(f"File vendor non registrati: {sorted(actual - expected)}")
    return lock


def collect(name, profile):
    lock = verify_vendor()
    result = {}
    for base, destination in [('template', ''), ('skills', '.agents/skills'), ('licenses', '.devkit/licenses')]:
        for path in sorted((ROOT / base).rglob('*')):
            if path.is_symlink():
                raise ValueError(f"Symlink sorgente non supportato: {path}")
            if path.is_file():
                result[(Path(destination) / path.relative_to(ROOT / base)).as_posix()] = path.read_bytes()
    result['.devkit/skills.lock.json'] = (ROOT / 'skills.lock.json').read_bytes()
    result['.devkit/THIRD_PARTY_NOTICES.md'] = (ROOT / 'THIRD_PARTY_NOTICES.md').read_bytes()
    result['.devkit/project.json'] = (json.dumps({
        'schema_version': 1, 'name': name, 'profile': profile,
        'status': 'needs-project-setup',
        'commands': {'setup': None, 'lint': None, 'typecheck': None, 'test': None, 'build': None, 'e2e': None},
        'commands_note': 'Documentazione: non vengono eseguiti dal bootstrap. Compilare con comandi verificati.',
        'external_effects': 'Require task-specific authorization; existing authorization remains valid.',
        'model_budget': None
    }, indent=2, ensure_ascii=False) + '\n').encode()
    return result, lock


def prepare(target, payload, lock, existing):
    check_path(target)
    target = target.absolute()
    if target == ROOT or ROOT in target.parents or target in ROOT.parents:
        raise ValueError('La destinazione deve essere esterna al repository del kit.')
    if target.exists() and not target.is_dir():
        raise ValueError('La destinazione non è una directory.')
    if target.exists() and any(target.iterdir()) and not existing:
        raise ValueError('Directory non vuota: usa --existing per una importazione conservativa.')
    pending, files, conflicts = [], {}, []
    # These are project-owned documents: offer an explicit merge, never replace them.
    protected = {'AGENTS.md', 'CONTEXT.md', '.gitignore', 'docs/agents/domain.md',
                 'docs/agents/issue-tracker.md', 'docs/agents/triage-labels.md'}
    for rel, data in payload.items():
        dest = target / rel
        check_path(dest)
        if dest.exists() and (not dest.is_file() or dest.read_bytes() != data):
            if rel in protected and dest.is_file():
                pending.append(rel)
                rel = '.devkit/proposed/' + rel
                dest = target / rel
                check_path(dest)
            else:
                conflicts.append(rel)
                continue
        if dest.exists() and (not dest.is_file() or dest.read_bytes() != data):
            conflicts.append(rel)
        files[rel] = data
    manifest = {
        'schema_version': 1, 'kit_version': lock['kit_version'],
        'pending_manual_merges': sorted(pending),
        'files': {p: digest(data) for p, data in sorted(files.items())}
    }
    rel = '.devkit/import.json'
    data = (json.dumps(manifest, indent=2) + '\n').encode()
    check_path(target / rel)
    if (target / rel).exists() and (not (target / rel).is_file() or (target / rel).read_bytes() != data):
        conflicts.append(rel)
    files[rel] = data
    if conflicts:
        raise ValueError('Conflitti: nessun file scritto. Confrontare manualmente:\n' + '\n'.join(sorted(conflicts)))
    return files, pending


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, type=Path)
    parser.add_argument('--name', required=True)
    parser.add_argument('--profile', choices=['generic', 'python', 'typescript', 'ai'], default='generic')
    parser.add_argument('--existing', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    try:
        if not args.name.strip() or any(ord(c) < 32 for c in args.name):
            raise ValueError('Nome progetto vuoto o con caratteri di controllo.')
        # Resolve the user-selected root (macOS /var and /tmp are system aliases).
        # Reject symlinks inside that root when preparing every destination file.
        if args.target.is_symlink():
            raise ValueError('La destinazione stessa è un symlink: indica il percorso reale.')
        target = args.target.resolve()
        payload, lock = collect(args.name, args.profile)
        files, pending = prepare(target, payload, lock, args.existing)
        new = [rel for rel in files if not (target / rel).exists()]
        print(f"{'ANTEPRIMA' if args.dry_run else 'IMPORT'}: {target}")
        print(f'{len(new)} file nuovi, {len(files) - len(new)} identici; profilo {args.profile}.')
        if pending:
            print('MERGE MANUALE necessario: ' + ', '.join(pending))
            print('Proposte in .devkit/proposed/. Integrare prima di usare il workflow.')
        if args.dry_run:
            return 0
        for rel in new:
            path = target / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('xb') as stream:
                stream.write(files[rel])
        print('Copia completata. Nessun git init, install, test applicativo, hook o servizio eseguito.')
        print('Apri docs/development/START-HERE.md nel progetto.')
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
