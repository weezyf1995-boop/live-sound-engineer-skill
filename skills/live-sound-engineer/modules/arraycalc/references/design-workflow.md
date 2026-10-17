# Prep-mode design workflow (ArrayCalc V12)

Contents: 0 Before you start · 1 Venue · 2 Sources: line arrays · 3 Point sources and fills · 4 SUB array · 5 Alignment · 6 3D plot and headroom · 7 ArrayProcessing · 8 Devices: amps and patch · 9 Rigging plot · 10 Ready for R1 and hand-off · Glossary

View names are from the ArrayCalc V10–V12 release notes: Home, Venue, Sources, Alignment, 3D plot, Devices, Rigging plot, HeadroomCalc, Soundscape. The V12 tab order isn't documented publicly. Detailed help is in the app (F1), not in a public PDF. Labels marked *(V8 name)* come from the last public UI walkthrough (TI 385 6.0); if the user's screen shows something different, trust their screen and say so.

Each step has a **Why** line. Keep it in your answer when you're working with a junior.

## 0. Before you start

- Version: current line is 12.8.x (07/2026). Windows 10+ with Vulkan, macOS 12+ with Metal. Old Windows PC without Vulkan → ArrayCalc 11.8.1 (OpenGL) from the d&b software archive.
- Files: project **.dbpr** (shared with R1), venue **.dbacv**, rigger app export **.dbev**. Older: .dbac2 / .dbac.
- Compatibility: files only open in the same or newer software. ArrayCalc 12.8.x files need R1 ≥ 3.46. 12.4 → 3.44, 12.2 → 3.42, 12.0 → 3.40, 11.8 → 3.38. Check what R1 version the system tech runs **before** you design.
- Run the grilling intake (`modules/arraycalc/references/grilling-intake.md`) and `modules/arraycalc/scripts/design_brief.py` first.

## 1. Venue

**Why:** every prediction, Auto splay and ArrayProcessing (AP) target uses the listening planes. Wrong venue, wrong design.

- Venue view. Build listening planes for every audience area: floor, tiers, balconies. Shapes: quadrangle, arc segment, superelliptic plane *(V8 names)*, plus cuboid / structure / joined elements and venue element groups (V10+).
- **Listener height** per plane: 1.7 m standing, 1.2 m seated. Easy to forget, and it shifts every angle.
- Leave planes **Transparent** unless you need balcony shadowing. Absorbent planes calculate much slower.
- Obstacles: video screens, structure, anything that blocks line of sight.
- No drawing? The measurement helpers build a plane from laser rangefinder plus inclinometer readings ("Measurements – Plane" / "Measurements – Arena" *(V8 names)*).
- Imports: the d&b **Venue database** (Venue view ">>" menu or Home view), or **SketchUp + ArrayCalc Exchange** extension → .dbacv. There's no direct DWG/DXF import. Importing offers "Replace current venue" or "Add venue elements".
- V12.8.1+: add **Rigging point** venue elements and use "Snap arrays to rigging point".
- Save now, and after every major step.

## 2. Sources view: line arrays

**Why:** this is the mechanical design. AP and EQ only polish it; they can't rescue a bad hang.

1. Add a line array and pick the series. Mounting: flown or stacked (pullback and compression frames for KSL/XSL where available).
2. Position: **Position x/y** (top front of the array), **Pair** for L/R mirror, **Frame height front** (trim height of the top front edge of the frame), **Horizontal aiming**, **Frame angle**.
3. **No. of cabinets** and the type per position in the cabinet table.
4. **Auto splay** gives *start values*: the frame angle goes to the farthest listener and the splays spread down the planes. No Auto splay for stacked arrays.
   - Large splays that barely grow from top to bottom → you need more boxes.
5. Refine by hand with the **Level over distance** diagram:
   - Use the 4 kHz curve for hi/mid and match it to the low/mid curve.
   - Opening a splay drops HF in that box's target zone; closing it raises HF.
   - Aim for a sensible 2–4 kHz level distribution before thinking about AP.
6. Splay limits: GSL 0–7°, KSL 0–10°, XSL/V/Y/CCL 0–14°, J 0–7°, AL 20–40°. Minimum length: 6 boxes for GSL/KSL/J, 4 for XSL/V/Y. Full table: `modules/arraycalc/references/systems-and-amps.md`.
7. Switches (non-AP):
   - **Line/Arc**: Line for 3+ consecutive splays of 0/1° (GSL, J) or 0/1/2° (KSL, XSL, V, Y, Vi), Arc for curved sections. Both can be used in one array.
   - **HFC** (HF compensation for distance) needs air absorption on in ArrayCalc. HFC1/HFC2: SL +40/+80 m, J >40/>80 m, V >30/>60 m, Y +25/+50 m, T 25/50 m.
   - **CPL** (coupling: tames the LF build-up in long arrays): one value for the whole array, 0 to −9 dB on J/V/Y. Start by matching the 500 Hz curve to 1 kHz. SL-Series has two-stage Coupling (low/mid).
   - **CUT**: tops high-passed when you have enough subs.
8. Cabinet level trims: last resort, a few dB max. Shape with splay. Boxes sharing an amp channel must have identical level and switches.
9. **Load section:** total mass, single pick point hole/position, front/rear pick loads, height of the lowest edge, centre of gravity (blue in the side view).
   - Yellow warning = outside the DGUV V17 limits (replaced BGV-C1 in V10.26.2). Red = absolute load limit exceeded.
   - **HARD STOP:** never accept a yellow or red load warning. Reduce boxes or total splay, and get the system tech / head rigger to sign off any hang before it goes on a rigging plot.
10. Horizontal: where neighbouring columns differ, keep pick points at least 3 m apart *(V8 guidance)*.

## 3. Point sources and fills

**Why:** the mains can't reach everywhere. Front rows under the hang, the sides at the front and seats behind pillars need their own boxes.

- Front fills on the stage lip for the rows below the array's lowest box coverage. `modules/arraycalc/scripts/design_brief.py` flags a wide first-row angle.
- Out fills for wide rooms. Delays where the mains run out of level or HF.
- Each fill gets a test point in its own target area at the alignment step.

## 4. SUB array

**Why:** subs from two L/R stacks cancel in stripes across the room ("power alley"). Where and how you place and delay them decides whether the floor gets even bass.

Full detail: `modules/arraycalc/references/subs-and-alignment.md`. In short:
- Sources view > SUB array. Automatic placement: enter width and x → "Source spacing" and **"Max freq. for pattern control"**. For INFRA mode keep pattern control up to at least 75 Hz.
- Automatic delay proposal: enter the target (−6 dB) dispersion. 50–70° from a stage-wide array is about L/R-equivalent. ArrayCalc computes the delays; use those, not hand maths.
- Keep per-sub levels identical. Shape with delay and rotation, not level.
- Cardioid: J-SUB cardioid by default, HCD in front of walls; SL-SUB has built-in rear rejection; CSA in stacks of 3 for Q-SUB/B2-SUB (TI 330).

## 5. Alignment view

**Why:** boxes that arrive at different times smear the sound and cancel bass. Alignment makes them arrive together where it matters.

- Place a **test point** (10 cm arrow steps). The **Arrival times** diagram shows each source's first arrival there. Add delay to the earlier one.
- Main ↔ out fill: align where both give equal level. ArrayCalc 10.22+ marks suitable test-point areas.
- Sub ↔ top: pick a source with similar dispersion to the sub array, test point typically at FoH, both delays at minimum, then add delay to whichever arrives first until the phase traces match over about **55–120 Hz**. Do this after the sub arc delays and main delays are final.
- Within one column: same input signal and identical delay on every channel.
- Formula: Δt = Δx / c, with c = 343 m/s (d&b; R1 uses 343.5 m/s since 3.44).

## 6. 3D plot and headroom

**Why:** this is where you check the design actually covers the audience evenly and gets loud enough.

- Pick bands (32 Hz–12.5 kHz) or broadband (pink noise / IEC60268 / EIA426B, lin/A/C).
- Interference (complex summation) is only available ≤ 163 Hz; above that it's an energy sum.
- Colour scale is fixed at **6 dB per division**. Don't misread it as auto-scaled.
- Resolution: High 1 m / Mid 2 m / Low 5 m; each step quadruples the time. Use Mid for stadiums.
- Memory slots to compare versions A/B.
- **Headroom:** raise the input level until **GR** LEDs (gain reduction: amp limiters working) light. **GR isn't applied to the SPL map**, so SPL shown with GR lit may be unreachable. Use the **IEC60268** spectrum for rock/pop, not octave bands, which overstate headroom.
- **HeadroomCalc** (enable it in Project settings > Advanced features): load a WAV of real programme, up to 5 measuring points, Gain trim / Auto trim, Calculate. GR colours: green 0–3 dB, yellow 3–12 dB, red > 12 dB.
- Indoors, the LF prediction is free-field and can be well off. Verify by measurement.

## 7. ArrayProcessing (optional)

**Why:** AP calculates a filter set per box so the whole audience gets the same tonal balance and a level distribution you choose. It does not fix a bad mechanical design.

Requirements (all must be true): SL, J, V, Y or T series (A-Series also has AP); amps D80, D40/40D, D20, 30D, or 10D (Y and T only); J-Series AP on D80 or 30D; **one amp channel per box**; **OCA/AES70 Ethernet** remote (not CAN, not R70); meaningful from 6–8 boxes deep; T-Series needs at least 6.

1. Finish splays and CUT/INFRA/100 Hz/70 Hz switches first. **Enabling AP locks the mechanics.**
2. Array's ArrayProcessing section > **Enable** > **Process** opens the dialog.
3. Press **«Intrinsic»** first. It matches the array's natural level curve and fixes tonality without changing level distribution.
4. Adjust **Level drop** (dB per doubling of distance) for Front / Central / Rear, with the area borders. Plane types: Listening (± offset), Reflecting (cuts level above about 800 Hz to the cabinets hitting it), Level avoidance (expert; disables the Realizer).
5. **Realizer**: green fine, yellow/orange near the limit (ease off "Glory"), **red = blocked**: relax the targets or change the array.
6. **Power/Glory** fader: Power = max SPL and headroom, Glory = closest match to target. Centre is usually right.
7. Set temperature/humidity per slot. Name the slot (max 15 characters; it shows in R1 and on the amp).
8. **«Recalculate»**: about 1 minute for a 20-box array over 100 m.
9. Prepare alternative slots: up to 9 user slots; slot 1 is Bypass. Examples: "grandstand in" / "grandstand out", a hotter-day slot.
10. Same **CPL** on all AP arrays. Processed arrays carry **6.2 ms** latency, and Bypass keeps it. Non-AP sources (subs, fills) must account for it.
11. AP is meant for even tonality, not flat SPL everywhere. d&b advises only moderate changes from Intrinsic, chosen by ear on site.

## 8. Devices view: amps and patch

**Why:** in V12 nothing reaches R1 or the amps unless it's patched here.

- **V12 doesn't create amps automatically.** Devices view > **Configure amps** or the **Patch plan**. Option "Use remaining channels".
- "Link cabinets" puts the recommended number of boxes on one channel; the recommended and maximum link depend on the amp (11.4+). AP arrays: one box per channel, no linking.
- Assign **Remote IDs**: format subnet.device, 0–99 . 1–63 on OCA (CAN only 0–7). In the Cabinets patching table, CTRL/CMD+Enter auto-increments (12.8.1+).
- Check the Unused channels table. Export the Patch plan as PDF, a CSV patch export, and a Dante preset or Milan Manager file where used (Milan Manager export is a known issue from 12.6.3).
- Parts list (separate window): cabinets, rigging, amps once patched.

## 9. Rigging plot

**Why:** this is what the riggers and the system tech work from. Errors here are physical.

- Per array: shape, required space, pick point x/y, loads per pick, frame height front, height of lowest edge. Collision view for clearance between sources.
- Share with riggers through the free **ArrayCalc Viewer** app (.dbev; QR code per source since 11.2): splays, amp channel and cabling, heights, angles, pick points, weight, load status.
- **HARD STOP:** the rigging plot goes to the head rigger / system tech for sign-off. A junior never hands it straight to the riggers.

## 10. Ready for R1 and hand-off

- Toolbar flag → **Project report** → Validate. Fix everything that blocks **"Ready for R1"**: duplicate Remote IDs, patch errors, function groups without matrix outputs.
- Save the .dbpr. Hand-off pack: .dbpr, Patch plan PDF, rigging plot printout, .dbev, a summary table (below), and the list of assumptions still open.
- On site, R1 takes over. Hand to the R1 module (`modules/r1/MODULE.md`) for going online, System check, Array verification and loading AP slots.

## Glossary (first-use definitions for juniors)

- **Trim / Frame height front**: height of the top front edge of the flying frame.
- **Splay**: the angle between two neighbouring boxes.
- **Frame angle**: tilt of the whole array. The top box points where the frame points.
- **CPL**: coupling filter. Reduces the LF build-up you get from many boxes coupling together.
- **HFC**: high-frequency compensation for air absorption over distance (non-AP arrays).
- **CUT**: high-pass on tops so subs do the low end.
- **INFRA / 100 Hz / 70 Hz**: sub operating modes that set the sub's upper frequency.
- **CSA / HCD**: cardioid sub array (a rear-facing box cancels sound behind) / hypercardioid mode.
- **GR**: gain reduction, the amp limiter working. Lit GR in a prediction means "can't actually get this loud".
- **AP / Realizer / Power–Glory**: see step 7.
- **Remote ID**: the address R1 uses to find each amp.
- **DGUV V17**: the German safety standard ArrayCalc's load warnings refer to (formerly BGV-C1).
