#!/usr/bin/env python3
"""Check vendor integrity or detect drift in a bootstrapped project. No commands run."""
import argparse
import json
from pathlib import Path
import sys
from bootstrap import digest, verify_vendor


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path)
    args = parser.parse_args()
    try:
        if args.project:
            manifest = json.loads((args.project / '.devkit/import.json').read_text())
            changed = []
            for rel, expected in manifest['files'].items():
                path = args.project / rel
                if path.is_symlink() or not path.is_file() or digest(path.read_bytes()) != expected:
                    changed.append(rel)
            print(json.dumps({'modified_or_missing': changed,
                              'pending_manual_merges_at_import': manifest['pending_manual_merges']}, indent=2))
            print('Drift may be intentional; this check does not verify project quality.')
            return 1 if changed else 0
        lock = verify_vendor()
        print(f"Snapshot verified: {sum(len(s['skills']) for s in lock['sources'])} vendor skills.")
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
