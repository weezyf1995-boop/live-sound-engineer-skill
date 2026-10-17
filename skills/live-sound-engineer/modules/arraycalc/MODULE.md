# Module: ArrayCalc

Part of the live-sound-engineer skill. Load this module when the task involves d&b audiotechnik ArrayCalc: designing or predicting a d&b PA, line array box count, trim, splay or frame angle, SUB arrays and cardioid subs, time alignment between mains, subs and fills, ArrayProcessing setup, headroom checks, rigging plots and load warnings, .dbpr design files, or a request like "design a PA for this room" with d&b gear.

All paths below are relative to the skill root.

ArrayCalc V12 (current line 12.8.x, 07/2026; a V13 beta with System Auralization exists). Check the user's version when a feature matters. The detailed manual is the in-app help (F1); there's no public step-by-step PDF. The job is a design that is safe to fly, covers the audience evenly, reaches the show level, and lands in R1 without surprises.

Written for system-tech capability, but juniors will use it most. Give exact numbers and real menu names, add a one-line "why" to each step, and define jargon the first time it appears (glossary at the end of `modules/arraycalc/references/design-workflow.md`).

## Route by the opening question

The skill's gig-or-research question already decides the route.

- **At a gig** (rigging going up, doors open, something sounds wrong): answer in the first line, safest action first. No grilling: one question at most. ArrayCalc is a prep tool, so live fixes happen in R1. Read `modules/arraycalc/references/onsite-playbooks.md`, and hand live amp work to `modules/r1/MODULE.md`.
- **Researching or prepping** (advance, design, load-in): **grill first**, then walk the full workflow. Read `modules/arraycalc/references/grilling-intake.md`, then `modules/arraycalc/references/design-workflow.md`.

## Grill before designing (prep mode)

Works with one given or fifty.
- **Harvest** everything the user already supplied (rider, drawing, rigging plot, old .dbpr, photos) into the intake table. Never ask for what's already there.
- **Ask one question per message**, highest impact first: venue/audience area → system inventory → rigging limits → show type/level → … Each question gets a one-line "why" and a recommended default.
- **Run `modules/arraycalc/scripts/design_brief.py` early** with every given it has a key for, and re-run it when answers change. Its checks table catches the classic contradictions: amps short for the box count (with or without AP), a hang over frame or point limits, more than 10 boxes needing an ArrayCalc load check.
- **Contradictions jump the queue.** Check software versions (ArrayCalc file vs R1 on site), amps vs boxes, and hang vs rigging. List them all, then ask the one question that resolves the most decision-changing one.
- **"Skip" / "don't know" / "use defaults"** ends the grilling at once. Open items become labelled ASSUMPTIONS and the design goes ahead. A bare "that's all I know" still gets the top question once, with its default.
- Stop when answers stop changing the design.

## Hard rules

These are wrong often enough elsewhere that they must never be wrong here.

- **d&b line arrays must be designed in ArrayCalc** "for both safety and acoustic reasons". Beyond 10 boxes at any splay, the load must be checked in ArrayCalc.
- **Never accept a yellow or red load warning.** Yellow = outside DGUV V17 limits (formerly BGV-C1), red = absolute load limit. Reduce boxes or total splay. **HARD STOP:** a hang goes to the head rigger / system tech for sign-off before it reaches riggers. A junior never sends a rigging plot directly.
- **Mechanics first, AP second.** Splay for a sensible 2–4 kHz level distribution, set CUT/INFRA/100 Hz switches, then enable ArrayProcessing. **Enabling AP locks the mechanics.** To re-angle: disable with "Keep current AP settings" → edit → re-enable → «Recalculate all slots».
- **AP requirements are all-or-nothing:** SL/J/V/Y/T (plus A, CCL) series, an AP-capable amp (D80, D40/40D, D20, 30D; 10D for Y/T only; J on D80/30D; D90 has AP), **one amp channel per box** (no linking), **OCA/AES70 Ethernet** (not CAN/R70). AP adds **6.2 ms** total latency; Bypass (slot 1) keeps it. Same CPL on all AP arrays.
- **Realizer red = blocked.** Relax the level drop targets (start from «Intrinsic») or change the array. Don't push "Glory" when it's yellow.
- **GR LEDs lit = the SPL shown can't actually be reached.** Gain reduction isn't applied to the map. Judge rock/pop headroom with the IEC60268 spectrum, not octave bands; HeadroomCalc for real programme.
- **The 3D colour scale is fixed at 6 dB per division**, and interference is only calculated ≤ 163 Hz. Indoor LF predictions are free-field; verify by measurement.
- **V12 doesn't create amps automatically.** Devices view → Configure amps / Patch plan. Unique Remote IDs. The project must be **"Ready for R1"** (toolbar flag → Project report) or R1 won't open it.
- **Files only open in the same or newer software.** ArrayCalc 12.6/12.8 → R1 ≥ 3.46 (12.4 → 3.44, 12.2 → 3.42, 12.0 → 3.40, 11.8 → 3.38). Check the R1 version on site before designing.
- **On-site changes that keep the R1 pairing:** venue, position, aiming, splay, new or recalculated AP slots. **Changes that break it:** box count, box type, series, flown ↔ stacked, Pair switch, recreating arrays, enabling AP on new arrays.
- **Sub-to-top alignment by phase match (about 55–120 Hz) at a chosen test point, after the arc and main delays are final.** Never with a "delay finder" between subs and tops; they cover different bands.
- **Shape coverage with splay and delay, not level.** Cabinet level trims are a last resort (a few dB). SUB array levels stay identical.
- **No invented specs.** d&b publishes no Haas offset, SPL-variance target, end-fire/gradient rules or ArrayCalc safety factor. Say so, and label general practice as general practice. Run `scripts/find_manual.py` and read the current document for any number that will be flown or quoted.

## Prep workflow at a glance

1. Grill, then run the design brief. Confirm the R1 version and amp inventory.
2. Venue: listening planes with the right listener height (1.7 m standing / 1.2 m seated), obstacles, rigging points. Import via the d&b Venue database or SketchUp + ArrayCalc Exchange (.dbacv); there's no direct DWG import.
3. Sources: arrays (position, Frame height front, frame angle, Auto splay as a start, refine on Level over distance at 4 kHz), switches, load check. Fills.
4. SUB array: placement, "Max freq. for pattern control", automatic delay proposal, cardioid rules.
5. Alignment: fills to mains where levels are equal; subs to tops by phase.
6. 3D plot and headroom: coverage, GR, IEC60268, HeadroomCalc.
7. ArrayProcessing (if the amps allow): «Intrinsic» → level drops → Realizer → Power/Glory → named slots.
8. Devices: amps, patch, Remote IDs. Rigging plot and Viewer export (.dbev). **HARD STOP for sign-off.**
9. Ready for R1 → save .dbpr → hand to `modules/r1/MODULE.md`.

## Reference files

Read only the one the task needs.

- `modules/arraycalc/references/grilling-intake.md`: the question bank with "why" lines and defaults, how to handle few vs many givens.
- `modules/arraycalc/references/design-workflow.md`: full V12 workflow view by view, AP dialog, Devices/patch, Ready for R1, glossary.
- `modules/arraycalc/references/subs-and-alignment.md`: sub layouts, SUB array tool, cardioid/CSA/HCD rules, alignment procedures, what d&b doesn't publish.
- `modules/arraycalc/references/systems-and-amps.md`: series picker, line array, sub, fill and amp tables, TOP:SUB ratios, switches, rigging frames.
- `modules/arraycalc/references/onsite-playbooks.md`: rig differs from plan, fewer boxes, won't open in R1, prediction vs reality, Realizer red, slow or won't start.

## Design brief script

`modules/arraycalc/scripts/design_brief.py` fills missing inputs with labelled assumptions, then derives the geometry ArrayCalc needs: angles to the first listener and the last floor or tier row, the vertical coverage to span, throws, level-drop bounds (point vs line source), horizontal angles (flags fill needs), delay-line time, sub line length and spacing limit, and general-physics end-fire and delay-arc delays. Given a box type and count, it also checks the hang mass against frame and point limits, flags when an ArrayCalc load check is mandatory, and counts the 4-channel amps needed for tops and subs (Line/Arc vs AP) against what's available. Its trim is the **bottom** of the array; it prints how to match that to ArrayCalc's "Frame height front".

```bash
python3 modules/arraycalc/scripts/design_brief.py --capacity 2000
python3 modules/arraycalc/scripts/design_brief.py --depth 45 --width 30 --trim 9 --array-length 4.5 --temp 28 --delay-at 30 --subs 8 --sub-spacing 1.2
python3 modules/arraycalc/scripts/design_brief.py --depth 48 --width 34 --tier-depth 70 --tier-height 12 --trim 12 --box-type KSL --boxes 14 --point-wll 1500 --ap yes --amps 16 --sub-type SL-SUB --subs 12
python3 modules/arraycalc/scripts/design_brief.py --json givens.json
python3 modules/arraycalc/scripts/design_brief.py --list-keys
```

Its output is a sanity check, not a prediction. ArrayCalc decides.

## Design output

- Lead with the **inputs table** (value, source: given / document / ASSUMED).
- Per array: series and box count, position x/y, Frame height front, frame angle, splays top to bottom, switches (CUT, CPL, Line/Arc or AP slot names), load status and pick points, total mass.
- Subs: layout, count, positions, delays (from ArrayCalc), modes. Fills: model, position, aim, delay.
- Alignment reference point and the delays it produced.
- Amps: model and count, channel assignment, Remote ID range.
- Exact units: m to 0.01, degrees, ms to 0.1, dB. No "around".
- Finish with **To confirm before load-in**: every ASSUMPTION, rigging sign-off, R1 version and amp firmware, and what the design doesn't cover.
