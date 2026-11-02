# Allen & Heath Qu-5/6/7 and Qu-MixPad

Reference for the console-troubleshooting module. Read when the desk is a current-generation Qu (Qu-5/6/7, "D" = Dante) or the job runs through Qu-MixPad. The generic elimination order and hard stops live in `modules/console-troubleshooting/MODULE.md`; this file maps each step onto Qu screens.

Not the old Qu-16/24/32/Pac/SB: different app (Qu-Pad), different firmware line. Firmware V1.2 (Oct 2026) is current; check the user's version before quoting features.

## The desk in one paragraph

Every model has the same 96 kHz XCVI engine: 38 inputs to mix (32 mono/linkable + ST1, ST2, USB), 12 mixes (1–6 mono/linkable, 7–12 stereo-capable), 4 stereo matrices (splittable to mono), 6 FX engines. Size only changes local I/O and faders (Qu-5: 16 combi in, 12 XLR out, 17 faders). **SLink**: dSnake 40×20+40 ME @48k, **DX 32×32 @96k**, GigaACE/GX 128×128 @96k. **Dante** (D models): 16×16, non-redundant; V1.2 adds a paid 32×32 add-on (needs Dante module firmware ≥ V1.1.0). **USB-C** is a 32×32 audio interface only, never control. SD multitrack 32×32 @48k / 16×16 @96k; USB-A stereo. A Mac on USB-C usually makes the Qu its default output, so Mac playback lands on the **USB input channel**.

## Qu-MixPad: connecting

- Control runs only over the rear **Network** RJ45 port. Not SLink, not Dante, not USB-C.
- Up to 8 app connections, max 2 MixPad (rest Qu4You). App and firmware must share the first two version digits or the app runs in Legacy Mode (no new features, can't push shows). Mac MixPad is Apple Silicon only.
- Desk with no DHCP shows its address with `(*)` and self-assigns 169.254.x.x. Cable Mac ↔ desk directly and the Mac self-assigns too; check with `ifconfig` (adapter `status: active`, 169.254 address) and `ping`.
- If the Mac is also on Wi-Fi, discovery can go out the wrong interface and Choose Unit stays empty. Scroll the list (the unit can appear below Offline/Other…), or use **Other…** with the desk IP.
- **Show Pull** (Data/offline menu) only copies a show off the desk; it is not live control. In offline mode, menu → **Logout** returns to Choose Unit.
- MixPad has **no I/O patch page**. Output patching is on the desk: **I/O → Outputs → SLink/Local/ME/USB/Dante**. A **hatched** output tile is assigned to a socket with no hardware behind it; a non-hatched SLink tile plus "DX" in the desk header means the expander's sockets are seen.
- Useful MixPad pages: Routing → channel → **Main** tab (MainLR assign + level); Routing → MainLR → **Matrix** (sends, pre/post, levels); Processing → Mix, page the bank to reach the matrix masters; Setup → Audio → **SigGen**.

## The elimination order on a Qu

1. **Source channel.** Is the music on the channel you think? (Mac over USB-C = USB channel; an external interface may sit on a mic channel.) Check its mute, its fader, and its MainLR assign/level on Routing → Main. A fader at -inf looks exactly like "signal but no sound".
2. **MainLR master.** Mute and fader. Matrix sends are normally **post**: after the master fader *and* mute, so a muted or -inf master kills every matrix.
3. **Matrix sends** from MainLR: on, pre/post, level.
4. **Matrix masters:** mute and fader for the matrices that feed the PA.
5. **Output patch** (desk I/O screen): the PA matrices land on the SLink sockets the amps are actually cabled to. Don't "fix" it by patching MainLR straight to the outputs; it still passes through the master mute and bypasses the matrix gain structure.
6. **Prove the downstream half without the master:** Setup → Audio → SigGen, **pink noise** around -40 dB, assigned to **one PA matrix only**, MainLR assign **off**. Hiss from the PA = desk-to-speaker path is good and the fault is upstream (steps 1–2). Silence = stagebox or later: link LED, cable in the expander's first DX port (not the cascade port), XLRs in the patched outputs, amp input routing and mutes (d&b amps: `modules/r1/MODULE.md`).
7. **Clean up:** every SigGen assign off. Check SigGen isn't left assigned to MainLR; a forgotten tone there plays the moment the master is unmuted.

## Driving MixPad with computer use (macOS)

- In live mode MixPad ignores background `app_*` clicks; ask for full-screen control. Background screenshots can lag behind the real screen; trust a full-screen screenshot.
- Overlay apps (e.g. **Wispr Flow**) can sit invisibly over the centre of the screen and block full-screen clicks there. Return did not confirm MixPad dialogs; a background `app_*` click on the button did.
- Virtual knobs (SigGen frequency/level) don't respond to scroll or drag. Prefer settings that need no knob (pink noise instead of a tuned sine), or ask the user to turn the desk's screen encoder.
- In screenshots the meter graphics show their full colour scale even with no signal. Read live signal from the brighter lit segment, the desk's PK LEDs, or ask the user.

## Case record: 2 Nov 2026, Qu-5D → SLink → DX → PA

Link "DX" up, patch correct (LR matrix → SLink 1/2, Ff&sub → 3/4), still no PA. Root cause in layers: MainLR muted, MainLR fader at -inf, and the Mac's music arriving on the **USB channel (35) with its fader at -inf**. Pink noise on the LR matrix only proved SLink → DX → amps → tops were fine. Side findings: SigGen had been left assigned to MainLR (33 Hz sine, -38 dB) and was removed; ch32 (external interface) muted; Mix STG patched to SLink 17, hatched (no hardware). Fix: engineer raised USB to -19 dB and master to ~0 dB. USB sitting at -19 means the Mac output is hot; turn the Mac down so the fader works near 0.
