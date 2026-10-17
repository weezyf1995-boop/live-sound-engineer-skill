# Subs, fills and time alignment

Sources: TI 385 10.10 (series SUB sections, §11), TI 330 (CSA), TI 385 6.0 (V8 SUB array and Alignment chapters), AN 161, the d&b amplifier/software brochure. Where d&b publishes nothing, this file says so. General physics is labelled as such.

## Choosing a sub layout

| Layout | Gains | Costs | d&b note |
|---|---|---|---|
| L/R ground stacks | Max efficiency (ground coupling), simple | Power alley: stripes of cancellation across the room | TI 385 §2.6.1, §3.3 |
| Flown subs (on top of / behind the array) | More even level front-to-back, less LF at the front, longer LF throw | Less LF at the barrier; rigging load | Add ground subs if the front needs LF (loud stage). TI 385 §3.4–3.5 |
| Horizontal SUB array across the stage front, delay-shaped | Most even horizontal coverage; no L/R cancellation zones | Needs stage width; nearfill timing gets trickier | "Alignment of array dispersion and internal delays … performed using ArrayCalc" (TI 385 §2.6.3) |
| Cardioid (J-SUB, CSA, SL-SUB) | Less LF on stage and behind | More boxes (CSA), spacing rules | See below |

TOP:SUB ratios d&b gives: J-SUB : J8/J12 about 1:2 (2:3 for distributed sub arrays); Q-SUB : Q1 1:1 small, 2:3 large; SL table in TI 385 §2.5 (e.g. GSL 3:1 L/R, 2:1 SUB array). Other series: check TI 385.

## Building the SUB array in ArrayCalc

Sources view > SUB array:
- **Automatic placement**: enter the width ("equally spaced along") and x, then Apply. Read **Source spacing** and **Max freq. for pattern control**. In INFRA mode keep pattern control ≥ 75 Hz.
- **Automatic delay proposal**: enter the nominal −6 dB dispersion you want; ArrayCalc sets the delays. 50–70° from a stage-wide array ≈ L/R coverage.
- Group controls: Mute, **relative delay** (moves the whole sub array against the mains while keeping the arc delays), level in 0.5 dB steps, Switch 1 (INFRA / 70 Hz / 100 Hz), Switch 2 (HCD).
- Per position: count, type, level, x/y, **Rotation**, **Total delay** = arc + alignment. Total delay is the value that goes to the amps.
- Keep per-position levels identical. Never shape the pattern with level.
- Rotating cardioid subs: progressive (e.g. 60° outermost, 30° next), not beyond 90°, about the centre axis. Single-sub rotation works for all systems since 11.2.
- The SUB-array map on the Sources view is *relative* level and doesn't change with input level.
- Mixed arrays: e.g. 3 J-SUB alternating with 2 J-INFRA, or 2 V-SUB + 1 J-INFRA. Flown J-SUB with ground J-INFRA: use the J-INFRA 70 Hz setting.

**End-fire, gradient, "virtual arc":** d&b publishes no named ArrayCalc feature or rules for these. You can build them by hand with x positions, rotation and delays, then check the map. `modules/arraycalc/scripts/design_brief.py` gives the general-physics numbers (end-fire delay = spacing / c; rear cancellation lowest at c / 4·spacing; delay-arc per sub). Label them as general physics, and let ArrayCalc's map be the judge.

## Cardioid rules

- **J-SUB**: cardioid by default, max rejection at 180°. **HCD** (hypercardioid) gives max rejection at 135°/225°; use it in front of walls.
- **SL-SUB**: frequency-constant rear rejection over a wide angle, so no cardioid/HCD choice is needed.
- **CSA (TI 330)**, Q-SUB / B2-SUB / B22 / B6 families:
  - Stacks of 3 (or multiples of 3), with the **rear-facing box in the middle**. On the floor, rotate the bottom box to use the floor mirror source.
  - The rear box gets its own channel set to CSA. The front boxes may share a channel. Don't daisy-chain front and rear boxes together.
  - Same input gain, signal, delay and EQ on all sub amps; only the CSA channel differs.
  - Result: about 180° dispersion and at least 15–20 dB rear rejection, with front phase nearly unchanged.
  - Tonal balance moves lower (about +2 dB very low LF). d&b suggests the higher crossover: Q-SUB 130 Hz instead of 100 Hz, B6-SUB 140 Hz instead of 110 Hz/INFRA, B2/B22-SUB 100 Hz instead of INFRA 70 Hz.
  - Keep ≥ 60 cm from walls and obstacles, and 60 cm between stacks. **CSA directly against a rear wall is pointless; use a conventional stack.**
- Keep 60 cm between adjacent stacks of different types (J-INFRA/J-SUB, Q-SUB/J-SUB).

## Time alignment

**The rules d&b states:**
- One column = same input signal and identical delay on every channel.
- Main ↔ out fill: align where both produce equal level (Alignment view; 10.22+ marks suitable test-point areas). If that adds delay to the array the subs are aligned to, compensate the sub array. On site, mute the out fill while measuring sub-to-main.
- Nearfills on sub stacks take the sub delay. With heavily delay-shaped sub arrays, nearfill timing (imaging) matters more, and a local phase mismatch to the subs is acceptable.
- Δt = Δx / c, c = 343 m/s (R1 uses 343.5 m/s).
- AP arrays carry 6.2 ms latency, and Bypass keeps it. R1 defaults AP loudspeaker delay controls to 6.2 ms. Whether ArrayCalc's Alignment view compensates automatically isn't documented, so check the arrival times plot with AP active.

**Sub-to-top procedure (Alignment view):**
1. Geometry final first: positions, trim, sub arc delays, main delays.
2. Pick a flown source with dispersion similar to the sub array.
3. Test point: d&b says FoH "can be used". Beyond that it publishes no rule for where. Choose where the most audience sits and where sub and top levels are similar, and state the choice.
4. Set both delays to minimum (0.3 ms), see which arrives first, and add delay to it until the phase traces match over about **55–120 Hz**.
5. L/R stacks: set the sub source count to 1 and enter the left stack's x/y.
6. Re-check after any main delay change.

**On site:** if geometry or chain latency is unknown, measure, using FoH as reference. **Don't use an automatic "delay finder" on impulse responses between subs and tops**; they cover different bands, so the result is wrong. Compare the flown array against a full-range box placed on the sub stack instead.

**Not published by d&b** (say so if asked): a Haas/precedence offset for delay lines, an SPL variance target, a sub polarity-check procedure. Common practice exists (e.g. adding a few ms so the mains lead), but present it as general practice, not d&b guidance.

## Delay lines and fills

- Each fill or delay gets a test point in its own target area, with its own delay.
- AP extends throw ("the need for delay systems is greatly reduced", TI 385 §12.1). Processed outfills, rear fills and delays share one tonal target above about 140 Hz, except T-Series, which has its own target.
- `modules/arraycalc/scripts/design_brief.py --delay-at <m>` gives the acoustic delay to a delay line; `--precedence-ms` adds an offset of your choosing.
