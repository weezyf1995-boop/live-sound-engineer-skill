# Module: Wireless Workbench

Part of the live-sound-engineer skill. Load this module when the task involves Shure Wireless Workbench (WWB), frequency coordination for Shure wireless (Axient Digital, ADX, ULX-D, QLX-D, SLX-D, PSM 1000/900), show files or show packs, scan files, AD600/AXT600 Spectrum Managers, backup frequencies, interference events, ShowLink, devices missing from WWB, mid-show RF dropouts on Shure systems, or Saudi Arabia (CST) frequency legality.

All paths below are relative to the skill root.

Shure Wireless Workbench 7 (release line 7.x). The job is a frequency plan that survives the show, and fast fixes when it doesn't.

## Operating mode: you drive WWB, start to finish

When the user asks you to coordinate, and you can operate the machine running WWB (computer use, or files you can read and write), **do the coordination yourself**. Not a walkthrough, not a checklist for the user, not a question per step. The user hands it over; you hand back a finished, deployed plan.

This overrides the skill's general "establish context first" question and the "grill before working" rule. A request to run a coordination is a task, not a research question.

- **You have standing permission to take over the desktop.** For any WWB task, the user has already said yes to you controlling the Mac: screenshots, clicks, typing, opening and switching apps. Don't ask in chat whether you may. Load the `computer-use` skill, call the access/enable tool straight away, and request everything the job needs in one go (Wireless Workbench, Finder for show files and scans, a text editor if needed) so the app's own approval prompt appears once, not per step. If that prompt is waiting on the user, say so in one line and carry on with anything that doesn't need the screen.
- **Start immediately.** Open or create the show file and get going in the first reply.
- **Harvest, don't ask.** Inventory, bands, venue and location come from what is on screen (online devices, the existing show file, the previous show for the same venue), from files the user gave you, and from the conversation. If the show is in Saudi Arabia, or the user is based there and says nothing else, apply CST rules.
- **Defaults instead of questions.** Anything still unknown gets the sensible default and goes into the assumptions line of the hand-off. Defaults: one RF zone; Standard profile, Robust on lead vocal / presenter / anything named as priority; mics and IEMs in one workspace; at least one backup per band family per zone; three-star frequencies to priority channels.
- **Clear dialogs and errors yourself.** Read every pop-up, then act on it. Never leave one sitting for the user to click. See "Dialogs and errors" below.
- **Recover yourself.** If a step fails, work out why from the screen and try the next fix. Calculation can't fit everything: run the "Finding more frequencies" ladder in `coordination-workflow.md` without asking. Devices missing: run "Devices not showing" in `show-mode-playbooks.md`.
- **Save as you go.** Save the show file after every major step. Never discard or overwrite another show file; save as a new name if unsure.
- **Report once, at the end.** The frequency plan table, what you deployed, the hand-tune list, the physical jobs left for the user, and one assumptions line. No running commentary.

### Stop only for these

1. **Physical actions.** IR-syncing transmitters, swapping packs or batteries, moving antennas, walk tests. List them at the end; don't pause the coordination for them.
2. **A running show.** Doors open, or channels on stage with audio passing: don't deploy or retune live channels without a yes. Prep the change, then ask once.
3. **Firmware updates.** Never start one. Dismiss the prompt and note it.
4. **OS permission and firewall prompts** (macOS network access, firewall, admin password). These are the user's. Say so in one line and carry on with whatever doesn't need it.
5. **No way to know what to coordinate.** Only when nothing on screen, in files or in the conversation says which systems are in the show. One question, then go.

Everything else is yours to decide.

### Dialogs and errors

Read the whole dialog. Then:

- **Informational or warning with one button** (OK, Close, Continue): click it, note it if it says something about the plan.
- **Save changes?**: Save.
- **Settings Conflicts** when opening a show file or merging: keep all settings from Wireless Workbench (the plan), unless the user said the hardware is the source of truth.
- **Merge options**: push Wireless Workbench to the hardware.
- **Deploy confirmation**: confirm, unless stop rule 2 applies.
- **Network interface selection**: pick the interface the Shure devices are on (wired Ethernet over Wi-Fi), then check devices appear.
- **Calculation could not find all frequencies**: work the "Finding more frequencies" ladder.
- **Device offline / not found during deploy**: deploy the rest, then troubleshoot or add the device to the hand-tune list.
- **Firmware mismatch or update offer**: decline / not now. Carry on if WWB still controls the device; otherwise list it.
- **Anything unfamiliar**: choose the option that keeps the plan and changes nothing on hardware you weren't about to change. Log what it said.

## Rules you apply yourself

Apply these without asking; they shape what you do, not what you ask.

- **WWB only calculates intermod against the workspace.** Put every transmitter you can find in it: online devices, IEMs, anything in the old show file, anything the user mentioned. If there may be other transmitters you can't see (guest band, broadcast, comms), say so in the assumptions line. Don't stop to ask.
- **Mics and IEMs share one workspace.**
- **The scan bounds the result.** Use the freshest scan from the show antennas available; note its age and source in the hand-off. External analyser files go through the scan cleaner first.
- **Never hand-pick "the next free frequency".** Any manual frequency goes through Analyze.
- **Calculate is randomised.** Lock anything already deployed and working before recalculating.
- **Legality is regional and WWB does not enforce it.** For Saudi Arabia read `modules/wireless-workbench/references/saudi-cst.md` and add the prohibited ranges as manual exclusions before calculating.
- **ShowLink is Axient and Axient Digital (ADX) only**, 2.4 GHz via an AXT610/AD610 access point, separate from audio RF. ULX-D, QLX-D, SLX-D have none.
- **AD600 and AXT600 are Spectrum Managers, not receivers.** AD600 tunes 174 MHz–2 GHz and supersedes AXT600.
- **Automatic backup switching needs a Spectrum Manager.** Without one, backups are a printed list and the switch is manual. AXT600 ignores inclusion groups when it auto-assigns.
- **Interference detection** (Interference Avoidance Mode) exists on AD4D, AD4Q and some ADX5D only.
- **Non-networked Shure gear** (BLX, GLX-D) and all third-party gear must be tuned by hand. They go in the hand-tune list.
- **ULX-D in HD mode** drops transmitter power to 1 mW after resync. Say so in the hand-off.
- **No invented specs.** No made-up spacings, ranges or firmware behaviour. Run `scripts/find_manual.py` for the Shure document and read it.

## Run order

1. Show file: venue, location, RF zones. Save.
2. Inventory: online devices, plus virtual devices for anything known but not on the network. Correct model, band, Tx profile or transmission mode.
3. Scan: from show antennas where possible; set exclusion and peak thresholds.
4. Spectrum: TV channels, regulatory exclusions (CST in Saudi), inclusion groups, compatibility profiles.
5. Calculate, analyse, lock, add backups.
6. Assign (priority channels on three-star frequencies) and deploy.
7. Merge virtual devices with hardware. Export a show pack. Hand off.

Full menu paths: `modules/wireless-workbench/references/coordination-workflow.md`.

## At a gig, not driving WWB

If the user is mid-show and asking rather than handing over (something just dropped, interference event), answer in the first line: safest action first, explanation after, one risk flag at most. Read `modules/wireless-workbench/references/show-mode-playbooks.md`. If you can operate WWB and the fix is a software action (switch to backup, select from frequency list), do it, then tell them what you did.

## Reference files

Read only the one the task needs.

- `modules/wireless-workbench/references/coordination-workflow.md`: exact WWB 7 menu paths for every step, compatibility profiles, backups, show files vs show packs, merging devices, finding more frequencies.
- `modules/wireless-workbench/references/show-mode-playbooks.md`: dropout triage, interference events, devices not discovered, ShowLink failures.
- `modules/wireless-workbench/references/products-and-scanning.md`: product families and WWB support, Spectrum Manager roles, scan file formats and import rules.
- `modules/wireless-workbench/references/saudi-cst.md`: CST PMSE bands, power limits, licensing lead time, prohibited ranges.

## Scan cleaner

`modules/wireless-workbench/scripts/clean_scan.py` turns any analyser export into a file WWB will import: strips headers, normalises frequency to MHz, sorts, merges duplicates, max-holds anything finer than 25 kHz into 25 kHz bins, and can flag energy in prohibited ranges.

```bash
python3 modules/wireless-workbench/scripts/clean_scan.py raw_scan.csv -o clean_scan.csv
python3 modules/wireless-workbench/scripts/clean_scan.py raw_scan.csv -o clean_scan.csv --flag-ranges 617-652,663-698
```

Read its printed summary. A detected unit of Hz or kHz, or a step under 25 kHz, means the raw file would have imported wrong or not at all.

## Hand-off

- Frequency plan table: channel name, device, band, frequency (MHz, three decimals), zone, backup, deploy method (WWB / hand-tune).
- What was deployed, and anything that failed to deploy and why.
- Jobs for the user: IR sync list, hand-tune list, walk test, anything blocked by stop rules.
- One assumptions line: defaults used, scan age and source, transmitters that may exist but weren't in the workspace.
- Dialogs worth knowing about, one line each. Skip routine ones.
- Where the show file and show pack were saved.
