# Show-mode playbooks (R1)

The first line is always the safest action. If you're a junior and the show is running, **tell the system tech before you change anything in R1.** Explanation after, only if there's time.

Rules while programme is running:
- **Never switch AP slots**: audio drops out for a few tenths of a second.
- **Never update firmware, re-run AutoCreate, go offline/online, or reopen the project.**
- **Never recall a Snapshot or System settings without the system tech.** Recalls are logged, but they hit every amp at once.
- Prefer the smallest change: one channel's mute, one group's level.

## Amps not found / grey in R1

Safe first move: **nothing is wrong with the audio just because R1 can't see an amp.** Amps keep running their settings without R1 (this is how amps normally behave; d&b doesn't state it explicitly). Diagnose calmly.

Read the pattern first. It usually names the cause:
- **All amps grey** → the laptop side: wrong network adapter, Wi-Fi on, IP range, firewall, or the project was opened **offline** and never taken online.
- **One rack or a block of amps grey** → their shared switch, its power or uplink, or a D80 daisy chain broken by an amp switched off.
- **A single amp grey** → that amp's cable or port, its Remote ID (conflict), or its firmware.

Project still offline and doors are close: going online writes the project to the amps. **HARD STOP**: only with the system tech, and only if the project is known to match the tuned amps. If audio is already passing, treat it as programme running: leave R1 offline and fix it at changeover.

In order, stop at the first fix:
1. Amp powered and display on? Link LEDs on the network jack? On D40/D90 the cable must be in **ETH1/PRI** (ETH2 carries no remote control).
2. D80 daisy chain (max 3): an amp switched off mid-chain cuts off the ones after it.
3. Laptop IP in the same range as the amps. Amps on DHCP+LL with no DHCP server → laptop on automatic (169.254.x.x). One DHCP router → both on DHCP. Exactly one DHCP server. Laptop on Wi-Fi and Ethernet at once is the usual culprit; turn Wi-Fi off.
4. Firewall allows **mDNSResponder.exe**. VPN off.
5. Mac USB-C adapter with the ASIX AX88179A chipset: swap the adapter.
6. ID conflict dialog → two amps share a Remote ID. Fix only on connected devices; check the rack label against the Patch plan.
7. Device present but blocked: firmware below R1's minimum (5D < V5.0.5 blocks R1). **Don't update mid-show**; take the device out of the project, or wait for the changeover.
8. CAN-only amps (D6/D12/E-PAC): R60/R70 interface connected, bus terminated at both ends.

## Amp went offline mid-show

1. Is there audio from it? If yes, leave it running and fix the control link at the next break.
2. Check the Log view and OS notifications (Show mode). Amp error 124 = "OCA remote error".
3. Check the cable and switch port. Don't power-cycle an amp that's passing audio unless the system tech says so.

## A channel or zone has gone quiet

| Symptom in R1 / on the amp | Likely cause | Action |
|---|---|---|
| Channel muted, nobody touched it | Override with mute-on-override, output mode change, speaker setup cleared, error mute | Check the amp display error; unmute only after you know why |
| Error 94 "Overtemperature" mute; 99/100 temp warnings | Cooling: blocked vents, hot rack, sun | Open the rack, add airflow, reduce level on that zone |
| Errors 97/98 (rail loss, mains loss), 37–41 (mains range) | Power | Check the distro; tell the system tech |
| Error 160 Fallback / 161–168 Input monitoring fault | Input signal lost | Check the upstream feed (DS10, console, Milan/Dante). Auto fallback may already be on backup inputs; reset with «Regular» once the main feed is back |
| Error 150 "Speaker imp. fault" / LM impedance error | Speaker or cable fault | Listen to that box; mute it if it's distorting; swap the cable at the break |
| Milan labels show «---unmapped---» or PRI/SEC down | Milan stream | Check Milan Manager / the network. Startup "sequence number mismatch" warnings are harmless |
| DS labels show the Dante input missing | Dante → DS10 path | Check the Dante controller subscriptions and the DS10 |

## Limiting, clipping, running out of headroom

- GR/OVL lit, Gainred/Headr meter high: the system is at its limit. Bring the input down; don't add EQ boost.
- MCL (mains current limiter) reduces all channels evenly when the mains limit is hit → power problem, not a tuning one.
- EcoMode switch-back can compress the first 300 ms. Turn EcoMode off for the show.
- If a zone is always in GR, the design is short of boxes or amps. Note it for the ArrayCalc revision; don't fix it with gain.

## Sounds different from soundcheck

1. Has the temperature or humidity changed a lot (an outdoor evening, a room filling up)? AP arrays: adjust **THC** (type values, Apply). Non-AP: HFC/HF Trim per the system tech.
2. Someone changed something? Check the Log view (recalls and syncs are logged). Group controls showing "Different values"?
3. A box failed? Load monitoring / Channel diagnostics.
4. Don't switch AP slots to "try" something during programme.

## Someone changed something by accident

- Check the Log view for what was recalled or synced.
- Restore from the stored System settings only with the system tech.
- Afterwards: set the project to start in Show mode, set a project password and device passwords, lock amp front panels (change the "dbaudio" default), and confirm Master Power/Mute (built in since 3.46.1).

## AP problems on site

| Symptom | Cause | Fix |
|---|---|---|
| No AP slots on a source | AP not in the ArrayCalc design; amp not AP-capable; boxes linked on one channel; amp on CAN/R70 | AP needs OCA Ethernet and one channel per box. Fix in ArrayCalc, then reopen |
| Import AP slots fails / file won't match | Something in AN 161's "breaks pairing" list changed (box count, type, series, mounting, Pair, recreated array) | Rebuild the R1 side from the new file (system tech decision) |
| Rig re-angled after AP | Old filters no longer match | ArrayCalc: disable with "Keep current AP settings" → fix → «Recalculate all slots» → save → R1: Import AP slots → send → clear old slots. Never during programme |
| Pink noise check sounds odd | AP filters active | Recall slot 1 Bypass for pink-noise checks (not during a show) |
