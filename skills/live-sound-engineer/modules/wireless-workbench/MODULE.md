# Module: Wireless Workbench

Part of the live-sound-engineer skill. Load this module when the task involves Shure Wireless Workbench (WWB), frequency coordination for Shure wireless (Axient Digital, ADX, ULX-D, QLX-D, SLX-D, PSM 1000/900), show files or show packs, scan files, AD600/AXT600 Spectrum Managers, backup frequencies, interference events, ShowLink, devices missing from WWB, mid-show RF dropouts on Shure systems, or Saudi Arabia (CST) frequency legality.

All paths below are relative to the skill root.

Shure Wireless Workbench 7 (release line 7.x; check the version the user is running when a feature matters). The job is a frequency plan that survives the show, and fast fixes when it doesn't.

## Route by the opening question

The skill's gig-or-research question already decides the route.

- **At a gig** (live, doors open, something just dropped): answer in the first line. Safest action first, explanation after. Numbered steps only when order matters. One risk flag at most. Read `modules/wireless-workbench/references/show-mode-playbooks.md`.
- **Researching or prepping** (advance, load-in, rehearsals): walk the full workflow with UI paths. Read `modules/wireless-workbench/references/coordination-workflow.md`.

## Hard rules

These are wrong often enough elsewhere that they must never be wrong here.

- **WWB only calculates intermod against what is in the coordination workspace.** Any transmitter left out (IEMs, a guest band's packs, a broadcast truck, comms, third-party mics) produces uncalculated IM. Before calculating, ask what else is transmitting in the venue.
- **Coordinate mics and IEMs in the same workspace.** They share the spectrum and intermodulate with each other.
- **A clean calculation is bounded by the scan.** Old, partial or wrong-antenna scans produce confident nonsense. A scan from the actual antennas at show conditions beats anything else.
- **Never hand-pick "the next free frequency".** Every manual frequency goes through Analyze; picking by eye skips the IM maths.
- **Calculate is randomised.** Pressing it again returns a different solution. Lock what is already deployed before recalculating, or working channels move.
- **ShowLink is Axient and Axient Digital (ADX) only**, runs at 2.4 GHz via an AXT610/AD610 access point, and is separate from the audio RF. ULX-D, QLX-D, SLX-D have no ShowLink.
- **AD600 and AXT600 are Spectrum Managers (scanners/coordination hardware), not receivers.** AD600 tunes 174 MHz–2 GHz and supersedes AXT600.
- **Automatic backup switching needs a Spectrum Manager.** Without one, backup status is unknown and the switch is manual. The AXT600 ignores inclusion groups when it auto-assigns.
- **Interference detection** (Interference Avoidance Mode) exists on AD4D, AD4Q and some ADX5D only.
- **Non-networked Shure gear** (BLX, GLX-D) and all third-party gear must be tuned by hand after deploy. List those channels explicitly in the output so nobody forgets them.
- **ULX-D in HD mode** drops transmitter power to 1 mW after resync. Range expectations change; say so.
- **Legality is regional and WWB does not enforce it.** Before calculating, confirm the band is legal where the show is. For Saudi Arabia read `modules/wireless-workbench/references/saudi-cst.md` and exclude prohibited ranges manually.
- **No invented specs.** No made-up guard bands, spacings, ranges or firmware behaviour. Run `scripts/find_manual.py` for the Shure document and read it, or say which document to check.

## Prep workflow at a glance

1. Show file: venue, location, RF zones. Save early.
2. Inventory: every transmitting channel, correct model, band, Tx profile or transmission mode. Virtual devices for gear not yet on the network.
3. Scan: from show antennas where possible. Set exclusion and peak thresholds. Clean external scan files with the scan cleaner before import.
4. Define spectrum: TV channels, regulatory exclusions, inclusion groups, compatibility profile per device type.
5. Calculate, analyse, lock, add backups.
6. Assign and deploy. Hand-tune non-networked and third-party channels.
7. Merge virtual devices with hardware on site. Walk test. Export a show pack.

## Reference files

Read only the one the task needs.

- `modules/wireless-workbench/references/coordination-workflow.md`: full prep workflow with exact WWB 7 menu paths, compatibility profiles, backups, show files vs show packs, merging devices, finding more frequencies.
- `modules/wireless-workbench/references/show-mode-playbooks.md`: dropout triage, interference events, devices not discovered, ShowLink failures.
- `modules/wireless-workbench/references/products-and-scanning.md`: product families and WWB support, Spectrum Manager roles, scan file formats and import rules.
- `modules/wireless-workbench/references/saudi-cst.md`: CST PMSE bands, power limits, licensing lead time, prohibited ranges. Read for any show in Saudi Arabia.

## Scan cleaner

`modules/wireless-workbench/scripts/clean_scan.py` turns any analyser export into a file WWB will import: strips headers, normalises frequency to MHz, sorts, merges duplicates, max-holds anything finer than 25 kHz into 25 kHz bins, and can flag energy in prohibited ranges.

```bash
python3 modules/wireless-workbench/scripts/clean_scan.py raw_scan.csv -o clean_scan.csv
python3 modules/wireless-workbench/scripts/clean_scan.py raw_scan.csv -o clean_scan.csv --flag-ranges 617-652,663-698
```

Read its printed summary. A detected unit of Hz or kHz, or a step under 25 kHz, means the raw file would have imported wrong or not at all.

## Frequency plan output

- Exact values: MHz to three decimals, dBm, mW. No "around".
- Table: channel name, device, band, frequency, zone, backup, deploy method (WWB / hand-tune).
- State what the plan does not cover: untracked transmitters, unscanned zones, unverified legality.
