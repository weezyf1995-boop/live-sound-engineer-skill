#!/usr/bin/env python3
"""Find official manual/datasheet URLs in references/manuals/.

Usage:
    python3 find_manual.py <search terms...>
    python3 find_manual.py KSL8
    python3 find_manual.py "d&b" rigging
    python3 find_manual.py axient receiver
    python3 find_manual.py --list            # list every product file

All terms must match (case-insensitive) somewhere in the entry.
Searches the JSON inventory first, then every product .md file
(the .md files cover more brands than the JSON — Meyer, Martin, Sennheiser).
Prints matching table rows with their URLs, plus the file each came from.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "references" / "manuals"
SKIP = {"master_inventory.md", "README.md"}


def product_files():
    return sorted(
        p for p in ROOT.rglob("*.md") if p.name not in SKIP
    )


def matches(text, terms):
    t = text.lower()
    return all(term in t for term in terms)


def search_json(terms):
    path = ROOT / "master_inventory.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for e in data.get("entries", []):
        blob = " ".join(
            str(e.get(k, "")) for k in
            ("brand", "series", "model", "document_type", "description")
        ) + " " + " ".join(e.get("tags", []))
        if matches(blob, terms):
            out.append(
                f"{e.get('brand')} | {e.get('series')} | {e.get('model')} | "
                f"{e.get('document_type')} | v{e.get('version','?')} "
                f"{e.get('release_year','')}\n    {e.get('official_url')}"
            )
    return out


def search_md(terms):
    out = []
    for f in product_files():
        text = f.read_text(encoding="utf-8", errors="ignore")
        # Heading context + table rows carrying a URL
        section = ""
        hits = []
        for line in text.splitlines():
            if line.startswith("#"):
                section = line.lstrip("# ").strip()
            if "http" in line and "|" in line:
                if matches(f"{f.as_posix()} {section} {line}", terms):
                    url = re.findall(r"\((https?://[^)]+)\)", line)
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    label = " | ".join(cells[:-1]) if cells else line
                    hits.append(f"  {section} — {label}\n    {url[0] if url else line}")
        if hits:
            rel = f.relative_to(ROOT).as_posix()
            out.append(f"[{rel}]\n" + "\n".join(hits))
    return out


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--list":
        for f in product_files():
            print(f.relative_to(ROOT).as_posix())
        return 0
    terms = [a.lower() for a in argv]
    j = search_json(terms)
    m = search_md(terms)
    if not j and not m:
        print(f"No entries match {' + '.join(argv)!r}. "
              "Not in the directory — search the manufacturer site instead.")
        return 1
    if j:
        print("== master_inventory.json ==")
        print("\n".join(j))
    if m:
        print("\n== product files ==")
        print("\n\n".join(m))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
