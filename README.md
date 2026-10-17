# Live Sound Engineer skill

One Claude skill for live sound work. Install it once and every module comes with it.

## What's inside

The core skill covers PA design, system tuning, consoles, wireless and RF, and troubleshooting, plus a bundled directory of official manufacturer manuals (`scripts/find_manual.py`).

Tool-specific workflows sit under it as modules. Claude loads a module only when the task needs it. Every module asks one question at a time in prep mode (with a recommended default; "skip" turns the rest into labelled assumptions), so it works with one given or a full advance pack. In show mode it gives the safest action first. Written at system-tech depth, delivered so juniors can follow, with hard stops before rigging, live-amp pushes and mid-show changes.

| Module | What it covers | Status |
| --- | --- | --- |
| Wireless Workbench | Shure WWB 7: frequency coordination, show files, scan cleaning (`clean_scan.py`), Spectrum Managers, show-mode playbooks, Saudi CST legality | Ready |
| ArrayCalc | d&b ArrayCalc V12: grilling intake, full design workflow, SUB arrays and alignment, ArrayProcessing, d&b system/amp/rigging tables, on-site playbooks, design brief script (`design_brief.py`) | Ready |
| R1 | d&b R1 V3: network and Remote IDs, opening ArrayCalc projects, going online, firmware, System check / Array verification, AP slots and THC, show-mode amp fixes | Ready |

## Layout

```
skills/live-sound-engineer/
├── SKILL.md                 core skill and module router
├── scripts/find_manual.py   manual lookup
├── references/manuals/      official manual directory
└── modules/
    ├── wireless-workbench/  MODULE.md, references/, scripts/clean_scan.py
    ├── arraycalc/           MODULE.md, references/, scripts/design_brief.py
    └── r1/                  MODULE.md, references/
```

## Install

```bash
cp -R skills/live-sound-engineer ~/.claude/skills/
```

Already installed the old `wireless-workbench` skill separately? Remove it so the two don't compete:

```bash
rm -rf ~/.claude/skills/wireless-workbench
```
