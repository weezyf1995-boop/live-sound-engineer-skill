# d&b systems, amps, switches and rigging (for design decisions)

All values come from official d&b product pages, manuals, rigging manuals and TI 385 10.10 (09/2026), as researched on 2026-10-17. Product data dates quickly, so before a value goes onto a rigging plot or a quote, run `scripts/find_manual.py <model>` and check the current document. Where the manual and the product page disagree, the newer product page wins.

**Max SPL isn't comparable across families.** SL-Series and CCL are quoted with an IEC 60268 broadband signal; J/V/Y/A/E/T/xS with pink noise, crest factor 4. Don't rank them against each other on these numbers.

## Picking a series (rule-of-thumb by job)

| Job | Usual candidates | Why |
|---|---|---|
| Stadium / large festival main | GSL (+ SL-SUB) | Highest output, 24 per frame, 2000 kg frame |
| Arena / large festival | KSL, J | Long throw, AP, 24 per frame |
| Theatre, mid-size venue, tour | V, XSL, CCL | Lighter, 0–14° splay for close coverage |
| Small venue, fills, delays | Y, CCL, T, A-Series | Light frames, short throws |
| Out fills / delays to a big main | Same family one size down | AP arrays share one tonal target above about 140 Hz (except T-Series) |

## Line arrays

| | GSL8/12 | KSL8/12 | XSL8/12 | J8/J12 | V8/V12 | Y8/Y12 | CCL8/12 | AL60/AL90 |
|---|---|---|---|---|---|---|---|---|
| Horizontal | 80°/120° | 80°/120° | 80°/120° | 80°/120° | 80°/120° | 80°/120° | 80°/120° | 60°/90° (×30° v) |
| Splay | 0–7° | 0–10° | 0–14° | 0–7° | 0–14° | 0–14° | 0–14° | 20–40° in 5° steps |
| Min array (TI 385) | 6 | 6 | 4 | 6 | 4 | 4 | — | max 4 (6 custom with AP) |
| Max per frame | 24 | 24 | 24 (12 on top mounting frame) | 24 | 24 | 24 | 24 | 4 |
| Weight | 80 kg | 58 kg | 39 kg | 60 kg | 34 kg | 20 kg | — | — |
| Freq std / CUT (−5 dB) | 45 Hz / 70 Hz–18 kHz | 54 / 75 Hz–18 kHz | 60 / 90 Hz–18 kHz | 48 / 85 Hz–17 kHz | 67 / 100 Hz–18 kHz | 54 / 100 Hz–19 kHz | 60 / 90 Hz–18 kHz | 60 / 95 Hz–18 kHz |
| Amps | D90, D80 | D90, D80, D40, 40D | D90, D80, D40, 40D | D80, D90, 30D (D12 legacy) | D80, D40, 40D, D20, 30D (D90 on SPL line) | D80, D40, D90, 40D, D25/25D, 10D (AP), D20 | D40, D80, D90, 40D, D25/25D | 4-ch amps except 10D |
| Boxes per amp, Line/Arc → AP | 2 → 2 per 4-ch amp (2-way active, 1 per channel pair) | 4 → 2 | 4 → 2 | 4 → 2 | 2 → 1 per channel | 2 per channel | 2 → 1 per channel | 2 → 1 per channel |
| AP | Yes | Yes | Yes | Yes (D80, 30D) | Yes | Yes (also 10D) | Yes | Yes |
| Matching subs | SL-SUB / SL-GSUB | SL-SUB, KSL-SUB/GSUB | KSL-SUB, XSL-SUB | J-SUB, J-INFRA | V-SUB / V-GSUB, J-INFRA | Y-SUB, J-INFRA | CCL-SUB | V-SUB |

Cabinet heights aren't in this table. To convert a bottom-of-array trim to ArrayCalc's "Frame height front", enter a frame height and read "Height of lowest edge" in the load section.

T10: 105° horizontal, splay to 15°, 3–20 per array, 4 per channel, AP from 6 boxes, T frame 250 kg / 20 T10.

**2-way active** cabinets (GSL, KSL, XSL, J8/J12, J-SUB, J-INFRA, SL-SUB, KSL-SUB) use a **pair** of amp channels. "Boxes per amp" above counts a whole 4-channel amp.

## TOP:SUB ratios (TI 385)

| System | L/R stacks | SUB array |
|---|---|---|
| GSL : SL-SUB | 3:1 | 2:1 |
| KSL : SL-SUB | 4:1 | 3:1 |
| KSL : KSL-SUB | 3:1 | 2:1 |
| XSL : KSL-SUB | 4:1 | 2:1 |
| XSL : XSL-SUB | 2:1 | 3:2 |
| J8/J12 : J-SUB | 2:1 | 3:2 (distributed) |
| V8/V12 : V-SUB | 2:1 | 3:2 (distributed) |
| AL : V-SUB | 2:1 | — |

J-INFRA covers 2 J-SUB, 2 V-SUB, or up to 4 Y-SUB. Keep 60 cm between adjacent stacks of different types.

## Subwoofers

| Sub | Pattern | Std / alt mode (−5 dB) | Per amp / channel | Flown | Amps |
|---|---|---|---|---|---|
| SL-SUB | Cardioid (wide, frequency-constant) | 33–84 / 30–65 Hz INFRA | 2 per D80 (2-way active) | Yes, ≤ 14 on GSL frame | D80, D90 |
| SL-GSUB | Cardioid | same | 2 per D80 | Ground only | D80 |
| KSL-SUB | Cardioid | 36–105 / 33–75 Hz | 2 per 4-ch amp | Yes, ≤ 16 | D40, D80, D90, 40D |
| XSL-SUB | Cardioid | 37–110 / 35–85 Hz | 4 per 4-ch amp | Yes, ≤ 15 | D40, D80, D90, 40D |
| J-SUB | Cardioid / HCD | 32–100 / 32–70 Hz INFRA | 1 per channel pair | Yes, ≤ 16 | D80, 30D (D12 legacy) |
| J-INFRA | Cardioid | 27–60 / 27–70 Hz (70 Hz mode) | 2 per D80 | Ground only | D80, D90 |
| V-SUB / V-GSUB | Cardioid | 37–115 / 37–95 Hz (100 Hz) | 2 per channel (1 on D40 for max output) | V-SUB yes, ≤ 13 | D80, D40, D90, 40D, D20 |
| Y-SUB | Cardioid | 39–140 / 39–110 Hz (100 Hz) | 2 per channel | Yes, ≤ 10 | D80, D40, D20 … |
| CCL-SUB | Cardioid (one channel) | 39–150 / 39–100 Hz | 8 per 4-ch amp | Yes, ≤ 10 | D40, D80, D90, 40D, D25/25D |
| B22-SUB | Omni, CSA-capable | 37–90 / 32–68 Hz INFRA | 1 per channel | — | D80, D90, D40, 40D, D20, 30D |
| B6-SUB | Omni, CSA-capable | 37–140 / 37–110 Hz (100 Hz) | 2 per channel | — | D80, D20, 10D, 30D … |
| T-SUB, E15X-SUB, E12X-SUB, 18S/21S (omni), 27S (cardioid) | | see product page | 2 (21S: 1) | | |

## Point sources for fills

| Model | Dispersion | Low end std / CUT | Max SPL | Per ch |
|---|---|---|---|---|
| E4 / E5 | 100° conical | 130 / 85 Hz | 115 / 117 dB | 4 |
| E6 | 100°×55° rotatable | 85 Hz | 123 dB | 5 |
| E8 | 90°×50° rotatable | 62 Hz | 129 dB | 3 |
| E12 | 80°×50° rotatable | 50 Hz | 134 dB | 2 |
| 44S | 90°×30° rotatable | 90 Hz | 123 dB | 4 |
| 24S | 75°×45° rotatable | 55 Hz | 138 dB | 1 |
| 5S / 8S / 10S | 100° / 100° / 75°×50° | 80 / 70 / 60 Hz | 118 / 127 / 130 dB | 4 / 3 / 3 |
| T10 PS | 90°×35° | 68 Hz | 132 dB | 4 |
| Y7P / Y10P | 75° / 110° ×40° | 59 Hz | 137 / 136 dB | 2 |
| V7P / V10P | 75° / 110° ×40° | 59 Hz | 140 / 139 dB | 2 |

Run point sources in CUT when used with subs (TI 385). Rotatable horns have a separate measured dataset per orientation in ArrayCalc.

## Amplifiers

| Amp | Ch | Per channel (CF 12 dB, 4 Ω) | AP | Can't drive |
|---|---|---|---|---|
| D90 | 4 | 5400 W | Yes (own AP chapter in the reference manual) | — (all current setups) |
| D80 | 4 | 4000 W | Yes | — (all setups + LINEAR) |
| D40 / 40D | 4 | 2400 W | Yes | GSL, SL-SUB, J-Series, M2 |
| D20 | 4 | 1600 W | Yes | J-Series, M2, SL-Series |
| 30D | 4 | 1600 W | Yes | SL-Series |
| 10D | 4 | 700 W | Y and T only | A, J, SL, V, M2, B22-SUB |
| 5D | 4 (power sharing) | 600 W | Not stated | Selected E, xS, xC, T only |
| D25 / 25D, 5DM | — | not researched | — | check the product page |
| D6 / D12 | 2 | legacy | No | CAN only; need R60/R70 for R1 |

There's no d&b "D60". If a rider says D60, ask; it's probably D40 or D80.

Output modes on 4-channel amps: **Dual Channel** (independent channels), **Mix TOP/SUB** (A = top, B = sub over one NL4), **2-Way Active** (A+B drive one active cabinet).

AP: 5.9 ms on top of the amp's 0.3 ms = **6.2 ms**. Needs OCA/AES70 Ethernet and one channel (or channel pair) per box.

## Switches and filters

| Switch | What it does | Notes |
|---|---|---|
| CUT | Lowers the box's LF so subs take over | LINEAR setup: 110 Hz 2nd-order Butterworth HP |
| HFC1 / HFC2 | Air-absorption compensation for distant seats | SL +40/+80 m, J >40/>80 m, V >30/>60 m, Y +25/+50 m. Obsolete under AP |
| HF Trim 0/1/2 (AP) | +10 % / +20 % target distance, capped at +30 m | Live in R1 only |
| HFA | Gentle HF roll-off from 1 kHz (≈ −3 dB at 10 kHz) | Point sources close to listeners |
| CPL (line arrays) | Low-shelf cut, 0 to −9 dB, from about 2 kHz, max below 100 Hz; +0 to +5 dB = LF boost for use without subs | Same value on every box in a column; same on all AP arrays. J8/J12: use from 5 boxes up |
| CPL (point sources) | 0 to −9 dB from about 1 kHz, max below 250 Hz | Boundary / monitor coupling |
| Coupling (SL-Series) | Two-stage: Low +5 to −5, Mid 0 to −8, 0.5 steps | Mixed with classic CPL: match classic CPL to Coupling-Mid |
| Line / Arc | Line for 3+ consecutive splays of 0/1° (GSL, J) or 0/1/2° (KSL, XSL, V, Y, Vi); Arc for curved sections | Both in one array allowed. Obsolete under AP |
| INFRA | Narrows a sub to infra duty (J-SUB 100→70 Hz; B22 32–68 Hz; SL/KSL/XSL-SUB INFRA mode) | Extends full-range (non-CUT) arrays downwards |
| 100 Hz | Lowers sub upper limit (V-SUB 115→95, Y-SUB 140→110, B6 140→110 Hz) | With full-range tops |
| 70 Hz (J-INFRA) | For J-INFRA loosely coupled to J-SUB (flown J-SUB, INFRA SUB array) | |
| HCD (J-SUB) | Hypercardioid, max rejection 135°/225° | Side stacks, in front of walls |
| CSA | Rear-facing box in a stack of 3 runs the CSA setup | B22, B6, B2, Q-SUB; TI 330 |
| MDC (A-Series) | "Out" setup on outer boxes, "In" on inner, against low-mid beaming | 2-box array: Out on both |

## Rigging frames

| Frame | System | SWL | Max boxes | Any splay without an ArrayCalc check |
|---|---|---|---|---|
| Z5701 (set Z5708) | GSL | 2000 kg | 24 GSL / 14 SL-SUB | 10 boxes / 800 kg |
| Z5722 (set Z5721) | KSL | 1500 kg | 24 KSL / 16 KSL-SUB | 10 / 685 kg |
| Z5771 (set Z5770) | XSL | 1000 kg | 24 XSL8 / 15 XSL-SUB | not stated |
| Z5300 | J | 1.5 t WLL | 24 J8 / 16 J-SUB | 10 / 665 kg |
| Z5380 | V / Vi | 860 kg | 24 V / 13 V-SUB | 10 / 340 kg |
| Z5387 Vi top frame | Vi | 141 kg (about 4 Vi) | — | — |
| Z5390 | Y | 540 kg | 24 Y / 10 Y-SUB | 10 / 220 kg |
| Z5820 | CCL | 500 kg | 24 CCL / 10 CCL-SUB | not stated |
| Z5370 | T | 250 kg | 20 T10 / 10 T-SUB | 10 / 110 kg |
| Z5455 | AL | 100 kg | 4 AL | — |

- Beyond the "10 boxes, any splay" case, every rigging manual requires a load check in ArrayCalc. "For both safety and acoustic reasons, d&b line arrays must be designed using ArrayCalc."
- d&b rigging is inherently safe up to the top suspension point (DGUV Information 215-313): no secondary safety needed within the array. Above that point is the venue's and rigger's responsibility. With multiple hoists, each must be able to lift the whole array.
- XSL compression rigging: hoist with two independent brakes (D8 Plus), max compression force 750 kg.
- Wind: no overhead flying above 6 Bft. Above 8 Bft, clear the area and lower the array.
- Safety factor: current manuals state SWL/WLL only. Don't quote a factor; the only numbers (12×/10×/5×) come from a 2003 general document.
- **HARD STOP:** never present a hang as safe on the strength of this table. The ArrayCalc load section, the current rigging manual and the head rigger decide.
