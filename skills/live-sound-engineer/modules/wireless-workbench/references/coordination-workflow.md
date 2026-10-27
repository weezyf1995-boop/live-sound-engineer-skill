# Prep-mode coordination workflow (WWB 7)

Contents: 1 Show file · 2 Inventory · 3 Scan · 4 Define spectrum · 5 Calculate and analyse · 6 Backups · 7 Assign and deploy · 8 On-site merge · 9 Hand-off · Finding more frequencies

Menu paths are WWB 7. Preferences live under Tools > Preferences on Windows and Wireless Workbench > Preferences on macOS. If the screen shows something different, trust the screen, adapt, and note it in the hand-off.

## 1. Show file

- Create the show, set location and show details under File > Show properties.
- Define RF zones if the event has physically separate areas (main stage, second stage, broadcast). Devices in different zones can reuse spectrum only if the zones are genuinely isolated; when in doubt, keep one zone.
- Save immediately and after every major step. A show file holds inventory, coordination and monitoring info. It does **not** hold scan data.

## 2. Inventory

Every transmitting channel goes in, including ones WWB cannot control.

- Online devices (green) appear automatically when on the same network.
- Gear not yet on the network: toolbar > Add new device > manufacturer, model, band > number of devices > RF zone or inclusion group > Add. It lands as a virtual (white) device.
  - Axient / Axient Digital: set Tx profile or Transmission mode.
  - ULX-D: Transmission mode HD for high density. Output power becomes 1 mW after resync.
  - ULX / SLX: pick the master list variant if offered.
- Third-party gear: use the built-in third-party profiles; build a custom equipment profile only if none exists, and send it with the show pack.
- Check for IEMs, guest or support act systems, broadcast, comms, talkback and venue house systems in everything available (screen, old show file, conversation). Add what you find. Don't stop to ask about the rest; list possible untracked transmitters in the hand-off assumptions. Each one left out is uncalculated IM.
- Naming: match the console patch and the RF plot (e.g. "VOX 1 – ADX2"). Names survive into reports and deploy screens.

## 3. Scan

Order of preference: live scan from the show antennas at show time > earlier scan from the same antennas > external analyser scan > Scan Library scan of the venue. Flag the age and source of whatever is used.

- Frequency coordination tab or toolbar Frequency plot > gear next to Scan sources: set Start, Stop, Resolution bandwidth, Step size, Sweep interval (options vary by device). Cover the full tuning range of every band in inventory.
- One sweep (once per antenna) for a snapshot; Continuous (up to 8 hours) for monitoring through load-in. Disable computer sleep for long runs.
- Right-click scan data to save it. An asterisk means unsaved.
- Thresholds:
  - Exclusion threshold line: anything above becomes an exclusion.
  - Peak threshold line: peaks above are treated as active transmitters, given a transmitter profile and buffered in the calculation.
  - Peak hold shows the max across selected scans; Additional exclusions shows what both thresholds generate.
- Only scans selected in the sidebar feed the calculation. Selecting several uses their peak hold.
- Importing: Scan data section > import icon > File, Hardware, or Scan Library. For a Spectrum Manager, save the scan on the hardware first. For PSM 1000, IR-sync the scan to the transmitter first. External files: run `modules/wireless-workbench/scripts/clean_scan.py` first (see `modules/wireless-workbench/references/products-and-scanning.md`).

## 4. Define the spectrum

- TV channels: select occupied channels from the TV database for the location. If the database does not cover the country or looks stale, add manual exclusions from the scan and local knowledge instead.
- Regulatory exclusions: add manual exclusions for every range not legal at the venue. WWB will not do this for you. Saudi Arabia: `modules/wireless-workbench/references/saudi-cst.md`.
- Inclusion groups: restrict channels to ranges (e.g. keep IEMs in one block, mics in another, or confine a band to its licensed slice). WWB 7 can also ignore intermod spacing between frequencies within a group and let you customise coordination order.
- Compatibility profile per device type: in the coordination workspace select the device header (Ctrl-click for several) > Compatibility tab.
  - Standard: default balance of count and stability.
  - Robust: wider spacing. Use for lead vocal, presenter, anything that cannot drop, and for large Tx-to-Rx distances.
  - More frequencies: tighter spacing, shorter working range, needs more Tx-to-Tx separation. Use only when the count demands it and say what it costs.
  - Global defaults: Preferences > Coordination > Compatibility.

## 5. Calculate and analyse

- Frequency coordination tab > Add frequencies > Select frequencies from inventory. Bring in everything, including virtual and third-party channels. Request frequencies for gear not yet in inventory from the drop-downs on the same tab.
- For AD PSM in point-to-point mode, coordinate the receiver channel receiving the ADTD/ADTQ transmission.
- Calculate. It uses scan data, exclusions, TV channels, inclusions and user groups. It is randomised; repeated presses give alternative solutions.
- If anything is already deployed and working, lock it (lock all frequencies icon) before recalculating.
- Any frequency entered by hand: run Analyze before trusting it.
- If the calculation cannot fit everything, see "Finding more frequencies" below before dropping to More frequencies globally.

## 6. Backups

- Automatic: Preferences > Coordination > enable automatically calculate backup frequencies.
- Manual: Add frequencies tab > manufacturer, model, band, RF profile > quantity > Add frequencies as: Backup > Add.
- Primaries are always found before backups. Lock primaries, then Calculate; only unlocked entries get new values.
- Rule of thumb for count: at least one backup per product/band family per zone, more for priority channels. State the number chosen and why.
- Backups only switch automatically with a Spectrum Manager. Deploy the list to it (or add to its compatible frequency list in its Properties). Without one, print the backup list for the RF tech.

## 7. Assign and deploy

- Assign and deploy > preview. Rank column: three stars cleanest, one star usable but near another carrier or a TV channel. Put priority channels on three-star frequencies; drag to swap.
- Deploy to column per RF zone: WWB, or a Spectrum Manager device ID. Choose selected zone or all zones.
- Deploy sets networked devices. Everything else (BLX, GLX-D, third-party, offline) must be tuned by hand. Output a hand-tune list.
- Re-sync transmitters (IR sync) after the receivers change.

## 8. On site: merge virtual devices with hardware

- Drag the virtual/offline device onto the online one (or the reverse). Expand Detailed options and choose per setting:
  - Wireless Workbench: push the plan to the hardware. Normal choice after prep.
  - Online Device: hardware overwrites the plan. Use only if the hardware is known-good and the plan is stale.
  - Ignore: leaves both; remote control is blocked until resolved (device shows in italics).
- Cannot merge two online or two offline devices.
- Opening an older show file can raise Settings Conflicts. To keep the plan, choose to keep all settings from Wireless Workbench.

## 9. Hand-off

- Walk test every channel through the full performance area, including the worst corners and behind the PA.
- Export a show pack: File > Export. It carries show file contents, coordination-workspace scans, custom equipment and compatibility profiles, in-use inclusion groups, TV channels and exclusions. Frequency-plot scans are not included. The receiving machine needs any user-defined profiles at the same file path.
- Generate the report (inventory, coordination, network) for the A2/RF tech.

## Finding more frequencies

Work down this list yourself without asking; note in the hand-off which step solved it:

1. Remove anything in the workspace that is not actually transmitting at this show.
2. Split by RF zone if areas are genuinely isolated.
3. Re-check exclusion threshold; an over-sensitive line excludes noise floor.
4. Inclusion groups so IEMs and mics stop competing for the same slice.
5. Ignore intermod within groups where the products are known to be too weak to matter (e.g. IEMs far from mic receivers). State the assumption.
6. Increase the number of calculations.
7. More frequencies profile on non-critical channels only.
8. ULX-D / Axient Digital HD mode for evenly spaced dense channels (right-click the device profile header). 1 mW on ULX-D.
9. Move some systems to another band, or to 1.8 GHz / VHF where legal.
