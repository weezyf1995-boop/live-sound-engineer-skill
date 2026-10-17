# Module: R1

Part of the live-sound-engineer skill. Load this module when the task involves d&b audiotechnik R1 Remote control: opening an ArrayCalc project in R1, going online with d&b amps, amps not showing up, Remote IDs and IP settings, firmware updates, System check / Array verification / Load monitoring, loading or importing ArrayProcessing slots, THC and HF Trim, group EQ/level/delay, input routing and fallback, d&b amp errors or mutes during a show, or protecting a running system from accidental changes.

All paths below are relative to the skill root.

R1 V3 (current 3.46.1, 26 May 2026; Windows 10+ / macOS 12+). Check the user's version when a feature matters. The detailed manual is the in-app Help (F1); there's no public V3 manual PDF, so exact click paths for project creation and device matching aren't published. The job is getting the designed system onto the real amps correctly, and keeping it running.

Written for system-tech capability, but juniors will use it most. Give exact numbers, add a one-line "why" to each step, and define jargon the first time it appears (OCA, Remote ID, AP slot, THC, Fallback).

## Route by the opening question

The skill's gig-or-research question already decides the route.

- **At a gig** (doors open, something dropped, an amp is red): answer in the first line, safest action first. No grilling: one question at most. Read `modules/r1/references/show-mode-playbooks.md`.
- **Researching or prepping** (advance, load-in, line check): **grill first** (step 0 of the workflow), then walk the full workflow. Read `modules/r1/references/prep-workflow.md`.

## Grill before working (prep mode)

Harvest what's already supplied (.dbpr, rack labels, network sheet) and ask only about gaps, one question per message, each with a "why" and a recommended default: ArrayCalc project and version → amps and Remote IDs → network layout → AP in the design? → who else touches the system → CAN-only amps. "Skip" turns the rest into labelled assumptions.

## Hard rules

These are wrong often enough elsewhere that they must never be wrong here.

- **R1 builds itself from the ArrayCalc .dbpr.** It won't open a project that isn't "Ready for R1", or one saved by a newer ArrayCalc (12.6/12.8 → R1 3.46; 12.4 → 3.44; 12.2 → 3.42; 12.0 → 3.40; 11.8 → 3.38). Fix in ArrayCalc, not in R1.
- **Save a `<name>_remote.dbpr` copy the moment you first open it** and run R1 on that. ArrayCalc keeps the original; AP changes arrive via **Import AP slots** (R1 stays online).
- **Laptop and amps must share an IP range.** DHCP+LL on the amps plus an automatic laptop works with no DHCP server. One DHCP server only. Allow mDNSResponder.exe. D40/D90 remote control is on **ETH1/PRI only**.
- **Remote IDs (subnet.device) must be unique and match the Patch plan.** 0–99 . 1–63 on Ethernet; 0–7 . 1–63 if CAN is used. Conflicts can only be fixed on connected devices.
- **HARD STOP before going online on a running or tuned system.** Confirm with the system tech whether the project or the amps should win.
- **Never during programme:** switching AP slots (audio drops for tenths of a second), firmware updates, AutoCreate, going offline/online, recalling Snapshots or System settings without the system tech.
- **AP needs OCA Ethernet and one amp channel per box.** Slot 1 is Bypass (keeps 6.2 ms latency). AP delay controls default to 6.2 ms. Same CPL on all AP arrays. After re-angling: recalculate in ArrayCalc → Import AP slots → send → clear old slots.
- **THC adjusts AP air absorption live without recalculation** (needs amp firmware ≥ V2.20.00). HF Trim is live-only.
- **System check is only valid against a calibration** made with the load connected and no programme. Default tolerance −20 % / +30 %. Hot voice coils read up to +50 % high after a show. Nothing in R1 checks splay angles.
- **Firmware:** one version across the system; 5D below V5.0.5 blocks R1 3.38+; update over Ethernet (ETH1); never on show day without the system tech.
- **No invented specs or click paths.** Unpublished: exact V3 device-matching steps, a full OCA port list (only mDNSResponder is documented), factory default IP mode. Say so, and point to R1 Help (F1) or the d&b release notes. Run `scripts/find_manual.py R1` for the documents.

## Prep workflow at a glance

1. Grill. Check R1 version against the ArrayCalc file, plus firmware.
2. Network: IP scheme, one DHCP server, ETH1, firewall, DS10 for Dante.
3. Remote IDs on every amp, matching the Patch plan; rack labels.
4. Open the .dbpr, save `_remote` copy, AutoCreate, own controls on separate views.
5. **HARD STOP**, then go online; resolve ID/Device conflicts; Wink to confirm.
6. Firmware to one version if needed.
7. System calibration → System check → Array verification. Load monitoring on.
8. AP slots and THC; HF Trim.
9. Tune with group controls; EQ 1 for the system tech, EQ 2 for the guest.
10. Protect: System settings backup, start in Show mode, passwords, front-panel locks, input monitoring and fallback.
11. Save and hand-off sheet.

## Reference files

Read only the one the task needs.

- `modules/r1/references/prep-workflow.md`: grilling table, versions, network, Remote IDs, project/AutoCreate, going online, firmware, System check and Array verification, AP/THC, tuning controls, protection, hand-off.
- `modules/r1/references/show-mode-playbooks.md`: amps not found, amp offline mid-show, quiet channel with amp error IDs, limiting, sounds different from soundcheck, accidental changes, AP problems on site.

Design questions (box count, splay, sub layout, alignment design) go to `modules/arraycalc/MODULE.md`.

## R1 output

- Show mode: the safe action first, then numbered steps only if order matters. Name the amp error ID and its meaning when one is shown.
- Prep: a table per amp: model, rack, Remote ID, IP mode/address, firmware, channels → sources/groups.
- System check results: channel, measured vs reference, in/out of tolerance, likely cause.
- State what wasn't verified: firmware not checked, no calibration file, AP slots not matching the rig, untested network paths.
