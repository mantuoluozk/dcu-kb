"""Find user-supplied local manuals; never read or upload their contents."""
import argparse
import json
import os
import sys
from pathlib import Path

def docs_root(skill_root, explicit=None):
    if explicit:
        return Path(explicit).expanduser().resolve()
    if os.environ.get("DCU_KB_DOCS_ROOT"):
        return Path(os.environ["DCU_KB_DOCS_ROOT"]).expanduser().resolve()
    config = skill_root / "config.local.json"
    if config.exists():
        value = json.loads(config.read_text(encoding="utf-8-sig"))["docs_root"]
        if not isinstance(value, str) or not value.strip():
            raise ValueError("config.local.json docs_root must be a nonempty path")
        p = Path(value).expanduser()
        return (p if p.is_absolute() else config.parent / p).resolve()
    return (skill_root / "manuals").resolve()

def find_manuals(root, entries, query=""):
    terms = query.casefold().split()
    result = []
    for entry in entries:
        text = " ".join([entry["id"], entry["title"], entry["purpose"]]).casefold()
        if terms and not any(term in text for term in terms):
            continue
        hits = [str(root / name) for name in entry["filenames"] if (root / name).is_file()]
        result.append({**entry, "found": hits})
    return result

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-root")
    p.add_argument("--query", default="")
    args = p.parse_args(argv)
    skill = Path(__file__).resolve().parents[1]
    try:
        root = docs_root(skill, args.docs_root)
        if not root.is_dir():
            raise ValueError("Manual directory does not exist; set --docs-root or DCU_KB_DOCS_ROOT")
        entries = json.loads((skill / "references/manual-index.json").read_text(encoding="utf-8"))
        rows = find_manuals(root, entries, args.query)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Cannot locate manuals: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"docs_root": str(root), "matched": len(rows),
                      "found": sum(bool(r["found"]) for r in rows), "manuals": rows},
                     ensure_ascii=False, indent=2))
    return 0 if rows and all(r["found"] for r in rows) else 1

if __name__ == "__main__":
    raise SystemExit(main())
