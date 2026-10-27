# Module: R1

Part of the live-sound-engineer skill. Load this module when the task involves d&b audiotechnik R1 Remote control: opening an ArrayCalc project in R1, going online with d&b amps, amps not showing up, Remote IDs and IP settings, firmware updates, System check / Array verification / Load monitoring, loading or importing ArrayProcessing slots, THC and HF Trim, group EQ/level/delay, input routing and fallback, d&b amp errors or mutes during a show, or protecting a running system from accidental changes.

All paths below are relative to the skill root.

R1 V3 (current 3.46.1, 26 May 2026; Windows 10+ / macOS 12+). Check the user's version when a feature matters. The detailed manual is the in-app Help (F1); there's no public V3 manual PDF, so exact click paths for project creation and device matching aren't published. The job is getting the designed system onto the real amps correctly, and keeping it running.

When advising rather than driving, give exact numbers, a one-line "why" per step, and define jargon the first time it appears (OCA, Remote ID, AP slot, THC, Fallback).

## Operating mode: you drive R1, start to finish

When the user asks you to bring a system up, check it, load AP slots or fix something in R1, and you can operate the machine running R1, **do it yourself**. Not a walkthrough, not a question per message. The user hands it over; you hand back a system online, checked and protected, with the hand-off sheet.

This overrides the skill's general "establish context first" question and the "grill before working" rule.

- **You have standing permission to take over the desktop** for any R1 task. Don't ask in chat whether you may. Load the `computer-use` skill, call the access/enable tool straight away, and request everything the job needs in one go (R1, ArrayCalc if AP slots need recalculating, Finder for the .dbpr) so the app's approval prompt appears once.
- **Pre-flight warning, then go.** When the user tells you to take over, send the checklist below before you touch the screen and wait for "go". If they already confirmed it in the same message, go.
- **Check versions on take-over:** R1 (title bar or Help > About) against the ArrayCalc version of the .dbpr. Adapt to what's on screen; never hunt for a control that isn't there.
- **Harvest, don't ask.** Amps, Remote IDs, IP mode and patch come from the .dbpr Patch plan, what R1 discovers on the network, rack labels in photos, and the conversation. Use the defaults in step 0 of `modules/r1/references/prep-workflow.md` for the rest and label them.
- **Clear dialogs and errors yourself.** Read every pop-up and act on it (see below). Never leave one waiting for the user.
- **Recover yourself.** Amps not found: work "Amps not found" in `show-mode-playbooks.md` from the laptop side (interface, IP range, mDNSResponder) before telling the user what to check physically. Remote ID conflicts: resolve on the connected devices to match the Patch plan.
- **Save as you go.** Save `<name>_remote.dbpr` the moment you open the project, and after every major step. Never overwrite the ArrayCalc original.
- **Report once, at the end**, in the R1 output format below.

### Stop only for these

1. **A running or tuned system.** Programme playing, or someone else's tuning already on the amps: before going online, ask once whether the project or the amps should win. Prep everything first.
2. **During programme:** no AP slot switches, going offline/online, AutoCreate, Snapshot or System-settings recalls. Prep the change, then ask once.
3. **Firmware updates.** Never start one without a yes. If versions are mixed, list amps and versions and ask once; carry on with everything that doesn't need it.
4. **Physical actions:** cables, rack ID switches, front-panel locks, swapping amps. List them; don't pause the rest of the work.
5. **OS permission, firewall or login prompts.** These are the user's. Say so in one line and carry on.

### Pre-flight checklist (send before taking over)

> Taking over R1 now. Before I start, check:
> 1. VPN off.
> 2. Antivirus / security software off, or R1 allowed through it.
> 3. Firewall allows R1 and mDNSResponder (Bonjour), or off for the session.
> 4. Laptop on wired Ethernet to the amp network (D40/D90 on ETH1/PRI). Wi-Fi off unless you need it; if you do, tell me.
> 5. Amps powered, one DHCP server at most on the network.
> 6. No other R1 or R90 controlling this system right now.
> 7. No programme through the PA if I'm calibrating or running System check.
> 8. Sleep and screen lock off for the session.
> 9. Hands off the mouse and keyboard while I work.
> Say "go" when ready.

### Dialogs and errors

- **Save changes?**: Save (to the `_remote` copy).
- **Project won't open (not Ready for R1 / newer version)**: fix in ArrayCalc if you can drive it (Ready for R1 → save → reopen); otherwise say what's needed.
- **Device or ID conflicts when going online**: match devices to the Patch plan; never rename the plan to fit the rack.
- **Master Power/Mute confirmation**: only confirm if you initiated it and stop rule 2 doesn't apply.
- **Firmware mismatch / update offer**: decline; stop rule 3.
- **System check out of tolerance**: record it, re-check cabling hints in `show-mode-playbooks.md`, list it.
- **Anything unfamiliar**: choose the option that changes nothing on the amps you weren't about to change. Log what it said.

## At a gig, not driving R1

If the user is mid-show and asking rather than handing over (an amp is red, something dropped), answer in the first line, safest action first, one question at most. Read `modules/r1/references/show-mode-playbooks.md`. If you can operate R1 and the fix is a software action outside stop rule 2, do it, then say what you did.

## Hard rules

These are wrong often enough elsewhere that they must never be wrong here.

- **R1 builds itself from the ArrayCalc .dbpr.** It won't open a project that isn't "Ready for R1", or one saved by a newer ArrayCalc (12.6/12.8 → R1 3.46; 12.4 → 3.44; 12.2 → 3.42; 12.0 → 3.40; 11.8 → 3.38). Fix in ArrayCalc, not in R1.
- **Save a `<name>_remote.dbpr` copy the moment you first open it** and run R1 on that. ArrayCalc keeps the original; AP changes arrive via **Import AP slots** (R1 stays online).
- **Laptop and amps must share an IP range.** DHCP+LL on the amps plus an automatic laptop works with no DHCP server. One DHCP server only. Allow mDNSResponder.exe. D40/D90 remote control is on **ETH1/PRI only**.
- **Remote IDs (subnet.device) must be unique and match the Patch plan.** 0–99 . 1–63 on Ethernet; 0–7 . 1–63 if CAN is used. Conflicts can only be fixed on connected devices.
- **Before going online on a running or tuned system,** ask once whether the project or the amps should win (stop rule 1). A fresh rig you were handed: go online.
- **Never during programme:** switching AP slots (audio drops for tenths of a second), firmware updates, AutoCreate, going offline/online, recalling Snapshots or System settings without the system tech.
- **AP needs OCA Ethernet and one amp channel per box.** Slot 1 is Bypass (keeps 6.2 ms latency). AP delay controls default to 6.2 ms. Same CPL on all AP arrays. After re-angling: recalculate in ArrayCalc → Import AP slots → send → clear old slots.
- **THC adjusts AP air absorption live without recalculation** (needs amp firmware ≥ V2.20.00). HF Trim is live-only.
- **System check is only valid against a calibration** made with the load connected and no programme. Default tolerance −20 % / +30 %. Hot voice coils read up to +50 % high after a show. Nothing in R1 checks splay angles.
- **Firmware:** one version across the system; 5D below V5.0.5 blocks R1 3.38+; update over Ethernet (ETH1); never on show day without the system tech.
- **No invented specs or click paths.** Unpublished: exact V3 device-matching steps, a full OCA port list (only mDNSResponder is documented), factory default IP mode. Say so, and point to R1 Help (F1) or the d&b release notes. Run `scripts/find_manual.py R1` for the documents.

## Prep workflow at a glance

1. Harvest and default. Check R1 version against the ArrayCalc file, plus firmware.
2. Network: IP scheme, one DHCP server, ETH1, firewall, DS10 for Dante.
3. Remote IDs on every amp, matching the Patch plan; rack labels.
4. Open the .dbpr, save `_remote` copy, AutoCreate, own controls on separate views.
5. Go online (stop rule 1 if the system is running or tuned); resolve ID/Device conflicts; Wink to confirm.
6. Firmware to one version if needed.
7. System calibration → System check → Array verification. Load monitoring on.
8. AP slots and THC; HF Trim.
9. Tune with group controls; EQ 1 for the system tech, EQ 2 for the guest.
10. Protect: System settings backup, start in Show mode, passwords, front-panel locks, input monitoring and fallback.
11. Save and hand-off sheet.

## Reference files

Read only the one the task needs.

- `modules/r1/references/prep-workflow.md`: harvest-and-default table, versions, network, Remote IDs, project/AutoCreate, going online, firmware, System check and Array verification, AP/THC, tuning controls, protection, hand-off.
- `modules/r1/references/show-mode-playbooks.md`: amps not found, amp offline mid-show, quiet channel with amp error IDs, limiting, sounds different from soundcheck, accidental changes, AP problems on site.

Design questions (box count, splay, sub layout, alignment design) go to `modules/arraycalc/MODULE.md`.

## R1 output

- Show mode: the safe action first, then numbered steps only if order matters. Name the amp error ID and its meaning when one is shown.
- Prep: a table per amp: model, rack, Remote ID, IP mode/address, firmware, channels → sources/groups.
- System check results: channel, measured vs reference, in/out of tolerance, likely cause.
- State what wasn't verified: firmware not checked, no calibration file, AP slots not matching the rig, untested network paths.
