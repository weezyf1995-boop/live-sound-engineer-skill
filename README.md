# Live Sound Engineer skill

Claude skills for live sound work.

| Skill | What it covers |
| --- | --- |
| [`live-sound-engineer`](skills/live-sound-engineer/SKILL.md) | PA design, system tuning, consoles, wireless/RF, troubleshooting, plus a bundled directory of official manuals (`scripts/find_manual.py`). |
| [`wireless-workbench`](skills/wireless-workbench/SKILL.md) | Shure Wireless Workbench 7: frequency coordination, show files, scan cleaning (`scripts/clean_scan.py`), Spectrum Managers, show-mode playbooks, Saudi CST legality. |

`live-sound-engineer` hands RF coordination on Shure systems to `wireless-workbench`; `wireless-workbench` defers general PA and console questions back.

## Install

Copy both folders into your skills directory:

```bash
cp -R skills/* ~/.claude/skills/
```
