# Grilling intake (prep mode)

Before designing anything, find out what you're designing for. You do that by grilling the user, but in a way that suits a junior who may not know the answers yet.

## How to grill

1. **Harvest first.** Read everything the user has already given you: messages, a rider, a CAD/PDF venue drawing, a rigging plot, an old .dbpr, photos. Fill the intake table below from it. Never ask for something they have already given you.
2. **Ask one question per message.** Take the highest-impact unknown first, using the order of the table. Each question has three parts:
   - the question, in plain words
   - one line on why it matters (it teaches the junior what a system tech would want to know)
   - a recommended default they can accept with "yes" or "default"
3. **Stop asking when answers stop changing the design.** Most shows need 3–6 questions; a festival main stage can need more.
4. **"Skip", "don't know" or "use defaults" ends the grilling straight away.** Every open item becomes a labelled ASSUMPTION, and you design with those. Never stall the user on missing information. A general "that's all I know" at the start is different: still ask the top question once, with its default, because one answer (the room size) changes everything.
5. **Run the brief early and re-run it.** Run `modules/arraycalc/scripts/design_brief.py` as soon as anything is known, and again whenever an answer changes an input. Pass every given it has a key for (`--list-keys`): venue, dimensions, tiers, trim, box type and count, point rating, amps, AP, subs. Its **Inventory and rigging checks** table surfaces contradictions automatically. Show its tables with the first contradiction or with the design, whichever comes first.
6. **Contradictions jump the queue.** Always check three things:
   - **Software versions:** the ArrayCalc version vs the R1 on site. A 12.6/12.8 file needs R1 ≥ 3.46.
   - **Amps vs boxes:** the brief's "4-ch amps needed" against the amps available, with and without AP.
   - **Hang vs rigging:** box count and mass against the frame maximum, the point rating, and the "10 boxes any splay" limit.

   If there are several, list them all in one message, then ask the single question that resolves the most decision-changing one (usually the one that decides AP or no AP, or the box count).

Example of one grilling turn:

> **How high can the bottom of the main hang be (trim)?**
> Why: trim sets how steeply the array has to aim down to reach the front rows, and it decides whether you need front fills.
> Default: 9 m (typical arena with a 1.8 m stage). Say "default" or give the number from the rigging plot.

## Intake table, highest impact first

| # | Input | Why it matters | Default if unknown |
|---|---|---|---|
| 1 | **Venue type and audience area** (depth from stage edge to last listener, width, balconies or tiers) | Drives everything: box count, throw, fills | `modules/arraycalc/scripts/design_brief.py` venue default (club / theatre / ballroom / arena / outdoor), or estimated from capacity |
| 2 | **System inventory**: which d&b series and how many boxes, subs and amps actually exist for this show | You can only design what is in the truck. A design for 16 GSL when the shop has 12 KSL is useless | Ask. If the user truly doesn't know, design to the room, then produce a shopping list |
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
- Ask only about gaps and contradictions.
- If a venue drawing exists, note the route into ArrayCalc: the d&b Venue database, or SketchUp + ArrayCalc Exchange → .dbacv. ArrayCalc does not import DWG/DXF directly.

## When the user gives almost nothing

Example: "design a PA for a 2000 cap room". Ask the top question only, venue type and audience area; if they skip, use the capacity estimate. Then design with clearly labelled assumptions and finish with a "To confirm before load-in" list. That list always includes rigging and inventory.
