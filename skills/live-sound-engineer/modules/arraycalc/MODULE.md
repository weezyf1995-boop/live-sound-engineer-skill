# Module: ArrayCalc

Part of the live-sound-engineer skill. Load this module when the task involves d&b audiotechnik ArrayCalc: designing or predicting a d&b PA, line array box count, trim, splay or frame angle, SUB arrays and cardioid subs, time alignment between mains, subs and fills, ArrayProcessing setup, headroom checks, rigging plots and load warnings, .dbpr design files, or a request like "design a PA for this room" with d&b gear.

All paths below are relative to the skill root.

ArrayCalc V12 (current line 12.8.x, 07/2026; a V13 beta with System Auralization exists). Check the user's version when a feature matters. The detailed manual is the in-app help (F1); there's no public step-by-step PDF. The job is a design that is safe to fly, covers the audience evenly, reaches the show level, and lands in R1 without surprises.

When advising rather than driving, give exact numbers and real menu names, a one-line "why" per step, and define jargon the first time it appears (glossary at the end of `modules/arraycalc/references/design-workflow.md`).

## Operating mode: you drive ArrayCalc, start to finish

When the user asks for a design, and you can operate the machine running ArrayCalc (computer use, or files you can read and write), **build the design yourself**. Not a walkthrough, not a question per message. The user hands it over; you hand back a saved, R1-ready .dbpr and the design sheet.

This overrides the skill's general "establish context first" question and the "grill before working" rule.

- **You have standing permission to take over the desktop** for any ArrayCalc task. Don't ask in chat whether you may. Load the `computer-use` skill, call the access/enable tool straight away, and request everything the job needs in one go (ArrayCalc, Finder for drawings and .dbpr files, a PDF viewer for riders and rigging plots) so the app's approval prompt appears once.
- **Pre-flight warning, then go.** When the user tells you to take over, send the short checklist below before you touch the screen and wait for "go". If they already confirmed it in the same message, go.
- **Check the version on take-over** (title bar or About). The rules here are written for V12; if the screen differs, adapt to what is there and note it. Never hunt for a control that isn't on screen.
- **Harvest, don't ask.** Pull every given from the conversation, riders, drawings, rigging plots, photos and old .dbpr files into the intake table in `modules/arraycalc/references/grilling-intake.md`. Run `modules/arraycalc/scripts/design_brief.py` with all of it.
- **Defaults instead of questions.** Every gap gets the default from the intake table and becomes a labelled ASSUMPTION. Contradictions (amps short, hang over limits, version mismatch) get resolved by you: pick the option that stays safe and inside the inventory, design it, and say what you chose.
- **Clear dialogs and errors yourself.** Read every pop-up and act on it (see below). Never leave one waiting for the user.
- **Recover yourself.** Yellow or red load warning: reduce boxes or total splay until it clears. Realizer red: relax the level drops from «Intrinsic» or change the array. GR LEDs lit: more boxes, more subs or lower target, then say which.
- **Save as you go.** Save the .dbpr after every major step under a new name if you opened someone else's file; never overwrite the only copy.
- **Report once, at the end**, in the Design output format below.

### Stop only for these

1. **Nothing says what room or system this is.** No drawing, no dimensions, no capacity, no inventory anywhere. One question (the room), then go with the capacity default for everything else.
2. **OS permission, licence or login prompts** (macOS access, admin password, My d&b login). These are the user's. Say so in one line and carry on with what doesn't need it.
3. **Software install or update.** Don't start one; note it.

The rigging sign-off is not a pause: finish the design, then mark the rigging plot **NOT SIGNED OFF**. It goes to the head rigger / system tech before it reaches riggers, never straight from you or a junior.

### Pre-flight checklist (send before taking over)

> Taking over ArrayCalc now. Before I start:
> 1. Venue drawing, rider, rigging plot or old .dbpr: in the chat or tell me the folder.
> 2. Sleep and screen lock off for the session.
> 3. Hands off the mouse and keyboard while I work.
> Say "go" when ready.

### Dialogs and errors

- **Save changes?**: Save (new name if the file isn't one you created this session).
- **Load warning (yellow/red)**: never accept; fix by box count or splay.
- **Realizer / AP warnings**: follow the hard rules below; don't push "Glory" on yellow.
- **Ready for R1 not met**: open the Project report, fix each listed item (amps, patch, Remote IDs), re-check.
- **File saved by a newer version / won't open**: say so; don't install anything.
- **Anything unfamiliar**: choose the option that keeps the design and changes nothing irreversible. Log what it said.

## At a gig, not driving ArrayCalc

If the user is mid-show or rigging is going up and they're asking rather than handing over, answer in the first line, safest action first, one question at most. ArrayCalc is a prep tool, so live fixes happen in R1: read `modules/arraycalc/references/onsite-playbooks.md`, and hand live amp work to `modules/r1/MODULE.md`.

## Hard rules

These are wrong often enough elsewhere that they must never be wrong here.

- **d&b line arrays must be designed in ArrayCalc** "for both safety and acoustic reasons". Beyond 10 boxes at any splay, the load must be checked in ArrayCalc.
- **Never accept a yellow or red load warning.** Yellow = outside DGUV V17 limits (formerly BGV-C1), red = absolute load limit. Reduce boxes or total splay yourself. A hang goes to the head rigger / system tech for sign-off before it reaches riggers; you and a junior never send a rigging plot directly.
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

1. Harvest givens, run the design brief, default the gaps. Note the R1 version and amp inventory (assume current R1 if unknown).
2. Venue: listening planes with the right listener height (1.7 m standing / 1.2 m seated), obstacles, rigging points. Import via the d&b Venue database or SketchUp + ArrayCalc Exchange (.dbacv); there's no direct DWG import.
3. Sources: arrays (position, Frame height front, frame angle, Auto splay as a start, refine on Level over distance at 4 kHz), switches, load check. Fills.
4. SUB array: placement, "Max freq. for pattern control", automatic delay proposal, cardioid rules.
5. Alignment: fills to mains where levels are equal; subs to tops by phase.
6. 3D plot and headroom: coverage, GR, IEC60268, HeadroomCalc.
7. ArrayProcessing (if the amps allow): «Intrinsic» → level drops → Realizer → Power/Glory → named slots.
8. Devices: amps, patch, Remote IDs. Rigging plot and Viewer export (.dbev), marked NOT SIGNED OFF.
9. Ready for R1 → save .dbpr → hand to `modules/r1/MODULE.md`.

## Reference files

Read only the one the task needs.

- `modules/arraycalc/references/grilling-intake.md`: the intake table with defaults; how to fill it from givens without asking.
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
