# Intake (prep mode)

Before designing, fill the intake table. **When you're driving ArrayCalc (the default when the user hands over a design), you fill it yourself and don't ask.** Grilling is only for when the user explicitly wants to be walked through it.

## How to fill it

1. **Harvest first.** Messages, rider, CAD/PDF venue drawing, rigging plot, old .dbpr, photos. Never ask for something already given.
2. **Default every gap** from the table and label it ASSUMED. Don't stall on missing information.
3. **The one exception:** if nothing at all says what the room is (no drawing, no dimensions, no capacity, no venue name), ask that one question. Everything else defaults.
4. **Run the brief early and re-run it.** Run `modules/arraycalc/scripts/design_brief.py` as soon as anything is known, with every given it has a key for (`--list-keys`). Its **Inventory and rigging checks** table surfaces contradictions.
5. **Resolve contradictions yourself.** Check three things:
   - **Software versions:** ArrayCalc vs R1 on site. A 12.6/12.8 file needs R1 ≥ 3.46. If R1 is older, say so in To confirm.
   - **Amps vs boxes:** if amps are short for AP, design without AP (or with fewer AP arrays) and say so.
   - **Hang vs rigging:** reduce the box count to fit the frame, point rating and load check.

   Pick the option that is safe and inside the inventory, design it, and list the choice in the output.

## Walk-through mode (only when the user asks to be taught)

One question per message, highest impact first, each with a one-line "why" and a default they can accept with "default". "Skip" ends it; open items become ASSUMPTIONS.

## Intake table, highest impact first

| # | Input | Why it matters | Default if unknown |
|---|---|---|---|
| 1 | **Venue type and audience area** (depth from stage edge to last listener, width, balconies or tiers) | Drives everything: box count, throw, fills | `modules/arraycalc/scripts/design_brief.py` venue default (club / theatre / ballroom / arena / outdoor), or estimated from capacity |
| 2 | **System inventory**: which d&b series and how many boxes, subs and amps actually exist for this show | You can only design what is in the truck. A design for 16 GSL when the shop has 12 KSL is useless | Harvest from the rider, old .dbpr or shop list. If none, design to the room with the series that fits (see `systems-and-amps.md`) and output it as a shopping list |
| 3 | **Rigging**: trim limit, rigging point positions, point load rating, ground stack only? | Safety. Fixes the array position and the maximum box count | Assume flown at the venue default trim; flag "rigging unconfirmed" in the output. **No hang goes to the riggers until this is confirmed** |
| 4 | **Show type and target level** (speech, theatre, rock/pop, EDM; dBA/dBC goals; noise limits) | Sets headroom, the sub count, and whether to check HeadroomCalc | Rock/pop: evaluate with the IEC60268 spectrum |
| 5 | **Audience standing or seated** | Ear height for listening planes: 1.7 m standing, 1.2 m seated | Standing (worst case) |
| 6 | **Stage**: width, height, where FoH is | Sub array width, L/R spacing, alignment reference point | Venue default; FoH on the centre line at about 2/3 of the depth |
| 7 | **Amps and remote network**: which amps, OCA/Ethernet available? | ArrayProcessing needs one amp channel per cabinet plus OCA/AES70 control | Check against the inventory; no AP until confirmed |
| 8 | **ArrayProcessing wanted?** | Locks the mechanics and adds 6.2 ms latency to the processed arrays; needs the amps above | Plan mechanically first and add AP after, if the amps allow it |
| 9 | **Subs**: count and type, ground or flown, cardioid needed (stage spill, wall behind) | Power alley, on-stage LF, ratio to tops | d&b TOP:SUB ratio for the series (see `modules/arraycalc/references/systems-and-amps.md`) |
| 10 | **Fills**: front fill, out fill, delays, balconies | Coverage holes that the mains physically can't reach | Decide after the first 3D plot |
| 11 | **Temperature / humidity at show time** | Air absorption, HF at distance | 20 °C / 60 % RH (ArrayCalc "std"); re-enter on site |
| 12 | **Software versions** (ArrayCalc, R1, amp firmware) | File compatibility: a 12.8 file needs R1 ≥ 3.46 | Assume current; check before go-live |

## When the user dumps a lot of givens

- Build the intake table from the documents and show it with a **Source** column (rider p.3, rigging plot, user message, ASSUMED).
- Default the gaps and resolve the contradictions; list both in the output.
- If a venue drawing exists, note the route into ArrayCalc: the d&b Venue database, or SketchUp + ArrayCalc Exchange → .dbacv. ArrayCalc does not import DWG/DXF directly.

## When the user gives almost nothing

Example: "design a PA for a 2000 cap room". Use the capacity estimate, design with labelled assumptions, and finish with a "To confirm before load-in" list. That list always includes rigging and inventory.
