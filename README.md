# Live Sound Engineer skill

One Claude skill for live sound work. Install it once and every module comes with it.

## What's inside

The core skill covers PA design, system tuning, consoles, wireless and RF, and troubleshooting, plus a bundled directory of official manufacturer manuals (`scripts/find_manual.py`).

Tool-specific workflows sit under it as modules. Claude loads a module only when the task needs it.

| Module | What it covers | Status |
| --- | --- | --- |
| Wireless Workbench | Shure WWB 7: frequency coordination, show files, scan cleaning (`clean_scan.py`), Spectrum Managers, show-mode playbooks, Saudi CST legality | Ready |
| ArrayCalc | d&b ArrayCalc: array prediction, splay, sub arrays, rigging checks | In development |
| R1 | d&b R1: amp control and monitoring, ArrayCalc import, d&b Remote network | In development |

## Layout

```
skills/live-sound-engineer/
├── SKILL.md                 core skill and module router
├── scripts/find_manual.py   manual lookup
├── references/manuals/      official manual directory
└── modules/
    ├── wireless-workbench/  MODULE.md, references/, scripts/clean_scan.py
    ├── arraycalc/           MODULE.md
    └── r1/                  MODULE.md
```

## Install

```bash
cp -R skills/live-sound-engineer ~/.claude/skills/
```

Already installed the old `wireless-workbench` skill separately? Remove it so the two don't compete:

```bash
rm -rf ~/.claude/skills/wireless-workbench
```
