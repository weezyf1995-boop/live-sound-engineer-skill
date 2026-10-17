# Show-mode and on-site playbooks

The first line is always the safest action. If you're a junior and the show is running, **tell the system tech before you change anything.** Explanation comes after, only if there's time.

## Doors open and something sounds wrong

Don't open ArrayCalc mid-show. ArrayCalc is a prep tool; live fixes happen in R1 (hand to `modules/r1/MODULE.md`). Safe moves in R1: group level or EQ, mute a faulty element, THC (temperature/humidity) adjustment. **Don't switch AP slots mid-show**: audio drops out for a few tenths of a second.

## Trim height, rigging points or angles differ from the plan

Safe first move: **don't fly until the design matches what's rigged.** Get the real trim, pick points and splays from the riggers (or ArraySight / ArrayCalc Viewer).

No AP on the array:
1. Sources view: update Frame height front, position and splays to what's actually rigged.
2. Check the load section: no yellow/red warning, and the pick point is still valid. **HARD STOP: the system tech / head rigger signs off any change.**
3. Re-check the Level over distance plot and the 3D plot. If the coverage broke, re-splay (only if the riggers can still change it) or add a fill.
4. Re-check Alignment (sub-to-top, fills). Save and update R1 (by hand, or reopen the file in R1).

AP on the array (AN 161 workflow):
1. Disable AP with **"Keep current AP settings"**.
2. Update trim, splay, position or venue.
3. Re-enable AP → **«Recalculate all slots»** (about 1 minute for 20 boxes / 100 m).
4. **Save in ArrayCalc.**
5. In R1 (running on its own `_remote.dbpr` copy): **Import AP slots** from the ArrayCalc file, then send them to the amps. R1 doesn't go offline for this.

**Allowed** without breaking the ArrayCalc ↔ R1 pairing: venue data, position, aiming, splay angles, new or recalculated slots. **Not allowed:** box count, box type (J8 ↔ J12), series, flown ↔ stacked, the Pair switch, deleting/recreating an array, disabling AP without "Keep current AP settings", enabling AP on new arrays, copy/paste or export/import of arrays. Any of these means rebuilding the R1 side (group tree and views) → system tech decision.

## Fewer boxes than designed (a box or amp channel is dead, or the hang was shortened)

- Dead box/channel with AP running: safe move = mute that box in R1 and tell the system tech. The AP filters no longer match the array exactly; d&b offers no "emergency" AP mode beyond Bypass (slot 1, keeps the 6.2 ms latency). Don't switch slots mid-show.
- Planned shorter hang on a tour (AN 161 "approach B"): build the project for the largest hang, open a copy, delete the unused boxes, save, open in R1. Unassigned controls show up, but it works.
- Reused tour file: clear the previous venue's AP slots from the amps, and re-check CPL, level, delay and EQ.

## The project won't open in R1

| Message / symptom | Cause | Fix |
|---|---|---|
| Not "Ready for R1" (toolbar flag) | Duplicate Remote IDs, patch errors, function group without matrix output | Project report → Validate → fix each item |
| No amps in the project after moving to V12 | V12 doesn't auto-create amps | Devices view → Configure amps / Patch plan |
| R1 refuses the file | File newer than R1 (files only open in same or newer) | 12.8 → R1 ≥ 3.46; 12.4 → 3.44; 12.2 → 3.42; 12.0 → 3.40; 11.8 → 3.38. Update R1 (not mid-show) |
| DS100 firmware 3.x conflict | I/O size | Go offline in R1, open in ArrayCalc ≥ 12.0, Devices tab > DS100 > I/O size '128x64', save, reopen in R1 ≥ 3.40 |
| Newer amp firmware features missing (THC, etc.) | Old AP data | Recalculate AP in ArrayCalc, re-run R1 AutoCreate |

## The prediction doesn't match what you hear or measure

In order:
1. Is the rig actually what's in the file? Trim, splays, positions, box types, cabling (R1 Array verification checks the cabling order against ArrayCalc; nothing checks splay angles automatically, so check them with ArraySight or by eye against the Viewer).
2. Temperature/humidity in the file vs. the real conditions → THC in R1 for AP arrays.
3. Indoors, LF is free-field in the prediction, so expect differences. Measure.
4. Was the SPL read with GR LEDs lit? Then it was never reachable.
5. Subs misaligned: re-measure with the flown array vs a full-range box on the sub stack. No delay-finder between subs and tops.

## Realizer red / AP won't calculate

- Red = the array can't do the target. Press «Intrinsic» and start again, relax the level drops, or change the array (more boxes, different splays).
- Yellow/orange = near the limit: back off "Glory".
- AP option missing: series not supported, amp not AP-capable, boxes linked on one channel, or no OCA/Ethernet planned. See the requirements in `modules/arraycalc/references/design-workflow.md` §7.

## ArrayCalc won't start or is slow

- Windows without Vulkan → ArrayCalc 11.8.1 (OpenGL) from the archive. macOS 11 → stay on 12.6.5.
- Slow calculation: turn off Autocalculate, use Mid/Low mapping resolution, make planes Transparent, switch off planes you don't need.
