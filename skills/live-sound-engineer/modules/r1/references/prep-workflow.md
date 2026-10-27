# Prep-mode workflow (R1 V3)

Contents: 0 Harvest and default · 1 Install and versions · 2 Network · 3 Remote IDs · 4 Open the project · 5 Go online · 6 Firmware · 7 System check and Array verification · 8 ArrayProcessing slots and THC · 9 Tuning controls · 10 Protect the show · 11 Save and hand-off

R1 V3, current 3.46.1 (26 May 2026). The detailed manual is the in-app Help (F1). There's no public V3 manual PDF, so exact click paths for project creation and device matching aren't published. Where this file gives a view or tab name, it comes from the R1 release notes or amp manuals. If the user's screen differs, trust the screen and say so.

Each step has a **Why** line. Keep it in your answer when you're working with a junior.

## 0. Harvest and default

When you're driving R1 (the default when the user hands over the job), fill these from the .dbpr, what R1 discovers on the network, rack labels and the conversation, and use the default for anything still unknown. Don't ask; label assumptions in the hand-off. Ask one question per message only if the user wants to be walked through it.

| # | Question | Why | Default |
|---|---|---|---|
| 1 | Is there an ArrayCalc project (.dbpr) for this system? Which ArrayCalc version saved it? | R1 builds its whole interface from it, and files only open in the same or newer software | Yes; check the version against the table in step 1 |
| 2 | Which amps, how many, and their Remote IDs (rack labels)? | R1 finds amps by Remote ID; duplicates block the project | Read them from the ArrayCalc Patch plan |
| 3 | How is the control network built: switch, DHCP router, DS10, direct cable? | Wrong IP scheme is the number one reason amps don't show up | Amps on DHCP+LL, laptop on DHCP/automatic, one switch, no DHCP server |
| 4 | Is ArrayProcessing in the design? | AP needs OCA/Ethernet, one channel per box, and slot management on site | Whatever the .dbpr says |
| 5 | Who else will touch the system (guest engineer, second laptop, R90)? | Decides EQ ownership, passwords, and who's allowed to change what | System tech owns EQ 1; the guest gets EQ 2 |
| 6 | Any CAN-only amps (D6, D12, E-PAC)? | They need an R60/R70 interface and IDs within 0–7 . 1–63 | None |

## 1. Install and versions

**Why:** a version mismatch stops the show file opening on site.

- Windows 10+ or macOS 12+ (Intel or Apple silicon). Wired Ethernet. Download from the d&b R1 page (installers need a My d&b login). In-app updates: Help > Check for updates.
- Project file compatibility (files only open in the same or newer software):

| Saved in ArrayCalc | Needs R1 |
|---|---|
| 12.6.x / 12.8.x | 3.46.x |
| 12.4.x | 3.44.x |
| 12.2.x | 3.42.x |
| 12.0.x | 3.40.x |
| 11.8.x | 3.38.x |

- Files saved in R1 3.22+ don't open in older R1 or ArrayCalc.
- **Don't update R1 or firmware on show day** unless the system tech decides to.

## 2. Network

**Why:** R1 talks to amps over OCA/AES70 on Ethernet. If the laptop and the amps aren't in the same IP range, R1 sees nothing.

- Amp IP modes (D40/D90: «IP settings»; D80: «Remote» tab): **Manual**, **DHCP+FB** (DHCP, falling back to a manual IP), **DHCP+LL** (DHCP, falling back to link-local 169.254.x.x). With no DHCP server, DHCP+LL plus a laptop on automatic addressing gives a working network with nothing to configure.
- Exactly **one DHCP server** per network. A laptop sharing its internet connection becomes a second one.
- D40/D90: remote control only on **ETH1/PRI**. ETH2/SEC is Milan redundancy only. Star topology; daisy-chaining isn't supported.
- D80: star, or a daisy chain of max 3. An amp switched off mid-chain cuts off the ones after it.
- Firewall: allow **mDNSResponder.exe**. On a dedicated production network d&b says turning off the extra firewall "should be safe". VPN off. Wi-Fi only for a tablet during setup, never the show connection.
- Mac: USB-C adapters with the ASIX AX88179A chipset lose devices after re-plugging (R1 3.32+ detects it). Use a different adapter.
- Dante reaches d&b amps as AES3 through a **DS10**, which also gives the laptop a control connection. D90/D40/40D also do Milan natively.
- CAN (legacy amps): R60 USB-CAN or R70 Ethernet-CAN; 120 Ω termination at both ends, max 600 m bus.

## 3. Remote IDs

**Why:** the Remote ID is how R1 recognises each physical amp as the amp in the design.

- Format **subnet.device**: 0–99 . 1–63 on Ethernet; 0–7 . 1–63 if the amp also uses CAN (D80 shows "Remote ID exceeds 7.63, CAN disabled!").
- Set on the amp: Network > «Remote ID». Must match the ArrayCalc Patch plan, and be unique.
- Duplicate IDs: R1 opens an **ID conflict** dialog. Since 3.38.1 you can only change the ID of a device that's actually connected.
- Practice: keep IDs unique across the rental stock and label every rack with them. If the project and the amps disagree, it's usually quicker to change the project than to walk to every amp (system tech's call).

## 4. Open the project

**Why:** R1 builds its group tree and control views from the ArrayCalc data, so there's no manual setup.

- Open the .dbpr from ArrayCalc. If ArrayCalc says it isn't "Ready for R1", R1 won't open it; fix it in ArrayCalc (`modules/arraycalc/references/onsite-playbooks.md`).
- **Immediately save a copy** as `<name>_remote.dbpr` and run R1 on that (d&b AN 161). ArrayCalc keeps the original; later AP changes come across with **Import AP slots** instead of reopening.
- Run **AutoCreate**. It builds the group tree and default Remote views, with relative controls prefixed "rel.". The Overview gets a Master Power/Mute section (confirmation required since 3.46.1).
- Put your own controls on **separate views** (or templates), so regenerating the default views doesn't wipe them (AN 161 approach C).
- Offline mode lets you do all of this before the amps exist.

## 5. Go online

**Why:** online is when R1 starts writing to real amps. Settings in the project get pushed to the hardware.

- Before going online on a system that's already running or already tuned, ask once which side wins: the project or the amps. A fresh rig you were handed: go online.
- Then go online. Watch for the ID conflict and Device conflict dialogs, and devices stuck in "found but not connected".
- Wink (flashes the amp display) to check a device is the one you think it is. Reverse Wink: press Mode on a DN1/DN2/UxN and R1 highlights it.
- Not everything shows up → `modules/r1/references/show-mode-playbooks.md`, "Amps not found".

## 6. Firmware

**Why:** mixed or too-old firmware blocks R1 or silently disables features (THC, Milan, AP data).

- Service view > **Firmware** tab > download the latest > update (several amps at once). Ethernet only, through ETH1 on D40/D90 class. If it gets interrupted, no harm done: restart R1 and repeat.
- Don't run different firmware versions in one system.
- Gates: 5D ≥ V5.0.5 (otherwise R1 3.38+ is **blocked**; update the 5D while it's *not* in the project), D90 ≥ V1.08.00, DS100 FW 3.x needs R1 ≥ 3.40, THC needs amp ≥ V2.20.00. After a firmware update that adds features, recalculate AP in ArrayCalc and re-run AutoCreate.
- Windows R1 3.44+: delete the old `Documents\dbaudio\` firmware folder and re-download.

## 7. System check and Array verification

**Why:** it finds blown drivers, bad cables and swapped channels before the audience does.

View: **System Check & Array Verification**.
1. Verify all connections. Mute everything, then listen to each channel in turn with programme (unmute one at a time from R1).
2. With the load connected and **no programme**, run a **System calibration**. It measures each channel and stores the reference.
3. Compare against the typical d&b impedances (F1 in R1 has the table).
4. Run a **System check** before the show if a calibration for this configuration exists, or after the show. Default tolerance **−20 % / +30 %**.
5. **Array verification** (D20, D80, 10D, 30D listed by d&b): boxes play an LF signal in turn while the others listen, and R1 compares the result with the ArrayCalc order and flags swapped channels or cables. Needs every box and amp connected and online. Symmetrical pair links in ArrayCalc disable it for those groups.
- Reading results: hot voice coils read up to +50 % right after a loud show (cooling takes an hour or more); ambient temperature up to +20 %; with 1 of 4 parallel LF drivers dead, Z only rises about 33 %. Know how many boxes share a channel before you call it fine.
- **Load monitoring** (continuous): inaudible pilot tones every 40–1000 s, doesn't work in standby. Error 150 "Speaker imp. fault" = speaker or cable. Shows as "LM impedance error" in Channel diagnostics.
- Nothing in R1 checks splay angles. Use ArraySight or the ArrayCalc Viewer against the rig.

## 8. ArrayProcessing slots and THC

**Why:** the AP filters are what make the array sound the way it was designed. They have to match the rig exactly.

- Slots come from ArrayCalc. **Slot 1 = Bypass** (filters off, 6.2 ms latency kept). Up to 9 user slots. The amp shows the slot name, version and comment.
- ArrayProcessing view: select the source(s) and choose the slot. **Switching interrupts audio for a few tenths of a second, so never during programme.**
- Rig changed (angles, trim, venue)? ArrayCalc: recalculate and save → R1: **Import AP slots** (R1 stays online) → send to the amps → clear the old venue's slots → re-confirm CPL, level, delay, EQ.
- **THC** (Temperature & Humidity Control): adjusts air absorption for all AP arrays live, with no recalculation. Since 3.46.1, type the values in and press **Apply** (Undo reverts). Measure temperature and humidity at array height if possible (ArraySight and SL frames have sensors readable in R1).
- **HF Trim** 0 / +1 / +2 (+10 % / +20 % target distance, max +30 m): live only, grouped like HFC.
- Same CPL on every AP array. Bypass HF Trim = the Arc HFC filters.

## 9. Tuning controls

**Why:** group controls let you tune the system as zones (mains, subs, fills) instead of channel by channel.

- Group controls set every member to the same value and overwrite individual settings. A "Different values" icon shows when members disagree.
- Relative faders: hold CTRL/CMD while moving to shift the fader without sending values (offset correction).
- **EQ:** two independent 16-band EQs per channel (D90/D80/D40/D25/D20/40D/30D/25D/10D; 8 bands on 5D; 4 on D6/D12). PEQ, Notch, Hi/Lo shelf, Asym; 20 Hz–20 kHz, Q 0.5–25, gain −18 to +12 dB. d&b's suggested split: system tech uses EQ 1 and locks it, the guest engineer gets EQ 2; instant A/B between the curves.
- Delay 0.3–10000 ms, 0.1 ms steps (R1 converts distance at 343.5 m/s). AP loudspeaker delay controls default to 6.2 ms.
- Level −57.5 to +6 dB in 0.5 dB steps. Switches: CUT, 100 Hz, INFRA, HFA, HFC, CSA, CPL (−9…+5), SL Coupling low/mid.
- Input routing (D40/D90): M1–M8 Milan, D1–D4 AES, A1–A4 analog. **Fallback** Off/Manual/Auto (Auto needs Input monitoring); reset with «Regular». **Override** with optional mute-on-override.
- Input monitoring: Pilot / Lock / DS data / Network data. Set it up so input loss raises an alarm instead of silence.

## 10. Protect the show

- Snapshots & System settings view: store a **System settings** backup of the tuned system, and Snapshots for scenes. Don't recall settings files made with different Remote IDs.
- Set the project to **start in Show mode**. Show mode raises OS notifications for device errors (level set in Application preferences).
- Passwords: project password, device passwords (Service view), amp front-panel Lock (factory password "dbaudio", so change it).
- AmpPresets on the amps: 9 user presets, plus remote-only Alarm and Backup presets that protect settings from local changes.

## 11. Save and hand-off

- Save `<name>_remote.dbpr`. Keep the ArrayCalc original separate.
- Hand-off sheet: amp list with Remote IDs and IPs, network diagram, firmware versions, System check print-out (calibrated reference), AP slot names and the active slot, THC values, who owns which EQ, passwords given to whom.
