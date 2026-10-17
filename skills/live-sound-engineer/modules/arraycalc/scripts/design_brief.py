#!/usr/bin/env python3
"""Turn whatever givens exist into an ArrayCalc design brief.

Fills every missing input with a labelled assumption, then derives the
geometry ArrayCalc will need: vertical coverage the array must span, throw,
level-drop bounds, speed of sound, delay-line times, and sub-array delays.
It does not predict SPL or pick splay angles; that is ArrayCalc's job.

Usage:
  modules/arraycalc/scripts/design_brief.py [--json givens.json] [--key value ...]
  modules/arraycalc/scripts/design_brief.py --capacity 2000 --venue arena
  modules/arraycalc/scripts/design_brief.py --depth 45 --width 30 --trim 9 --audience standing \
                  --temp 28 --delay-at 30 --subs 8 --sub-spacing 1.2
  modules/arraycalc/scripts/design_brief.py --list-keys

All distances in metres, temperature in deg C. Any key accepted on the CLI
is also accepted in the JSON file (use the long name without dashes).
"""
import argparse
import json
import math
import sys

# Rule-of-thumb defaults, used only when the user gives nothing better.
# Every one of them is printed as an ASSUMPTION so it can be challenged.
VENUE_DEFAULTS = {
    #           depth, width, trim (bottom of array), stage height
    "club":     (20.0, 15.0, 5.0, 1.0),
    "theatre":  (30.0, 25.0, 7.0, 1.0),
    "ballroom": (35.0, 25.0, 5.0, 0.6),
    "arena":    (60.0, 45.0, 12.0, 1.8),
    "outdoor":  (80.0, 60.0, 10.0, 1.8),
}
EAR_HEIGHT = {"standing": 1.7, "seated": 1.2}
# Rough floor area per person, m^2. Used only to guess depth from capacity.
AREA_PER_PERSON = {"standing": 0.5, "seated": 0.8}

# From d&b product pages / manuals (see references/systems-and-amps.md).
# box: (cabinet kg, boxes per 4-ch amp Line/Arc, boxes per 4-ch amp with AP,
#       frame, frame SWL kg, max boxes per frame, any-splay limit (boxes, kg) or None)
TOPS = {
    "GSL": (80, 2, 2, "Z5701", 2000, 24, (10, 800)),
    "KSL": (58, 4, 2, "Z5722", 1500, 24, (10, 685)),
    "XSL": (39, 4, 2, "Z5771", 1000, 24, None),
    "J":   (60, 4, 2, "Z5300", 1500, 24, (10, 665)),
    "V":   (34, 8, 4, "Z5380", 860, 24, (10, 340)),
    "Y":   (20, 8, 4, "Z5390", 540, 24, (10, 220)),
    "CCL": (None, 8, 4, "Z5820", 500, 24, None),
}
# sub: boxes per 4-ch amp
SUBS = {"SL-SUB": 2, "SL-GSUB": 2, "KSL-SUB": 2, "XSL-SUB": 4, "J-SUB": 2,
        "J-INFRA": 2, "V-SUB": 8, "Y-SUB": 8, "CCL-SUB": 8, "B22-SUB": 4, "B6-SUB": 8}

KEYS = {
    "venue": "club | theatre | ballroom | arena | outdoor (sets fallback dims)",
    "capacity": "audience count, used to estimate floor area if no dims",
    "depth": "stage edge to last listener, m",
    "width": "audience width, m",
    "audience": "standing | seated",
    "ear": "ear height above floor, m (overrides audience)",
    "first_row": "stage edge to first listener, m",
    "array_setback": "array position behind stage edge, m",
    "trim": "height of the BOTTOM of the main array above floor, m",
    "array_length": "physical array length, m (if known; refines top angle)",
    "stage_height": "stage deck height, m",
    "temp": "air temperature, deg C",
    "humidity": "relative humidity, % (noted only; ArrayCalc uses it)",
    "delay_at": "distance from main array to a delay line, m",
    "precedence_ms": "extra delay added to delay lines so mains lead, ms (your choice; d&b publishes no value)",
    "tier_depth": "horizontal distance from stage edge to the LAST tier/balcony row, m",
    "tier_height": "floor height of that last row above the main floor, m",
    "box_type": "line array family: " + " | ".join(TOPS),
    "boxes": "boxes per hang (one side)",
    "hangs": "number of main hangs (2 for L/R)",
    "point_wll": "rated load per rigging point, kg",
    "ap": "plan ArrayProcessing: yes | no",
    "amps": "4-channel amps available for this system",
    "sub_type": "sub model: " + " | ".join(SUBS),
    "subs": "number of subwoofers in a front line / arc",
    "sub_spacing": "centre-to-centre spacing of subs, m",
    "arc_angle": "total arc angle for a delay-arced sub line, deg",
    "endfire_rows": "number of end-fire rows",
    "endfire_spacing": "spacing between end-fire rows, m",
}


def speed_of_sound(t_c):
    return 331.3 * math.sqrt(1 + t_c / 273.15)


def parse(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--json", help="JSON file of givens")
    p.add_argument("--list-keys", action="store_true")
    for k, h in KEYS.items():
        typ = str if k in ("venue", "audience", "box_type", "sub_type", "ap") else float
        p.add_argument("--" + k.replace("_", "-"), dest=k, type=typ, help=h.replace("%", "%%"))
    a = p.parse_args(argv)
    if a.list_keys:
        for k, h in KEYS.items():
            print(f"{k:16} {h}")
        sys.exit(0)
    given = {}
    if a.json:
        with open(a.json) as fh:
            given.update({k: v for k, v in json.load(fh).items() if k in KEYS})
    given.update({k: getattr(a, k) for k in KEYS if getattr(a, k) is not None})
    return given


def fill(given):
    v, src = dict(given), {k: "given" for k in given}

    def assume(key, value, why):
        if key not in v:
            v[key], src[key] = value, "ASSUMED: " + why

    venue = v.get("venue")
    if venue and venue not in VENUE_DEFAULTS:
        sys.exit(f"unknown venue '{venue}'; use one of {', '.join(VENUE_DEFAULTS)}")
    assume("audience", "standing", "standing audience (worst case for ear height and SPL)")
    if "capacity" in v and "depth" not in v:
        area = v["capacity"] * AREA_PER_PERSON[v["audience"]]
        w = v.get("width", math.sqrt(area / 1.3))
        assume("width", round(w, 1), f"floor ~1.3x deeper than wide from capacity {int(v['capacity'])}")
        assume("depth", round(area / v["width"], 1), f"{AREA_PER_PERSON[v['audience']]} m2/person")
    if venue and "capacity" in given and "depth" not in given:
        vd = VENUE_DEFAULTS[venue][0]
        if abs(v["depth"] - vd) / vd > 0.5:
            src["depth"] += (f" (typical {venue} is ~{vd:.0f} m; capacity wins here, "
                             "ask for real dimensions)")
    if not venue:
        d = v.get("depth")
        venue = ("club" if d is None or d < 25 else "theatre" if d < 40
                 else "arena" if d < 70 else "outdoor")
        assume("venue", venue, "inferred from depth" if d else "nothing given; small room")
    dd, dw, dt, ds = VENUE_DEFAULTS[v["venue"]]
    assume("depth", dd, f"typical {v['venue']}")
    assume("width", dw, f"typical {v['venue']}")
    assume("stage_height", ds, f"typical {v['venue']} deck")
    assume("trim", dt, f"typical {v['venue']} trim; confirm rigging points and max load")
    assume("ear", EAR_HEIGHT[v["audience"]], f"{v['audience']} ear height")
    assume("first_row", 2.0 if v["audience"] == "standing" else 3.0, "barrier / first row distance")
    assume("array_setback", 1.0, "array hangs ~1 m behind stage edge")
    assume("temp", 20.0, "20 C; re-enter the show temperature on site")
    return v, src


def derive(v):
    out = []
    c = speed_of_sound(v["temp"])
    out.append(("Speed of sound", f"{c:.1f} m/s at {v['temp']:.0f} C"))

    # Horizontal distances measured from the array position.
    x_near = v["first_row"] + v["array_setback"]
    h_bottom = v["trim"] - v["ear"]
    h_top = h_bottom + v.get("array_length", 0.0)
    if "tier_depth" in v:
        # Farthest listener is up the tiers: aim height shrinks by the tier height.
        x_far = v["tier_depth"] + v["array_setback"]
        h_top -= v.get("tier_height", 0.0)
        out.append(("Farthest listener", f"last tier row at {v['tier_depth']:.1f} m, "
                    f"{v.get('tier_height', 0.0):.1f} m above floor"))
    else:
        x_far = v["depth"] + v["array_setback"]
    ang_near = math.degrees(math.atan2(h_bottom, x_near))
    ang_far = math.degrees(math.atan2(h_top, x_far))
    out.append(("Angle down to first listener (from array bottom)", f"{ang_near:.1f} deg"))
    out.append(("Angle down to last listener (from array top; negative = aim above horizontal)", f"{ang_far:.1f} deg"))
    out.append(("Vertical coverage the array must span", f"{ang_near - ang_far:.1f} deg"))
    throw_far = math.hypot(x_far, h_top)
    throw_near = math.hypot(x_near, h_bottom)
    out.append(("Throw, nearest / farthest listener", f"{throw_near:.1f} m / {throw_far:.1f} m"))
    ratio = throw_far / throw_near
    out.append(("Level drop front-to-back, point-source bound (-6 dB/dd)",
                f"{20 * math.log10(ratio):.1f} dB"))
    out.append(("Level drop front-to-back, line-source bound (-3 dB/dd)",
                f"{10 * math.log10(ratio):.1f} dB"))
    half_w = v["width"] / 2
    out.append(("Horizontal angle to audience edge at last row (one hang, centre)",
                f"+/-{math.degrees(math.atan2(half_w, x_far)):.0f} deg"))
    out.append(("Horizontal angle to audience edge at first row (one hang, centre)",
                f"+/-{math.degrees(math.atan2(half_w, x_near)):.0f} deg  (large = needs fills / L-R spread)"))

    if "delay_at" in v:
        prec = v.get("precedence_ms", 0.0)
        t = v["delay_at"] / c * 1000
        line = f"{t:.1f} ms acoustic"
        if prec:
            line += f" + {prec:.1f} ms precedence = {t + prec:.1f} ms"
        out.append((f"Delay line at {v['delay_at']:.1f} m", line))

    if "endfire_spacing" in v:
        rows = int(v.get("endfire_rows", 2))
        step = v["endfire_spacing"] / c * 1000
        delays = ", ".join(f"{i * step:.2f}" for i in range(rows))
        out.append((f"End-fire, {rows} rows at {v['endfire_spacing']} m (general physics, not a d&b feature)",
                    f"delays rear-to-front {delays} ms (rearmost row = 0); "
                    f"cancellation behind lowest at {c / (4 * v['endfire_spacing']):.0f} Hz"))

    if "subs" in v and "sub_spacing" in v:
        n, s = int(v["subs"]), v["sub_spacing"]
        length = (n - 1) * s
        out.append(("Sub line length", f"{length:.2f} m ({n} subs at {s} m)"))
        lam_s = c / s
        out.append(("Frequency above which sub spacing exceeds half a wavelength",
                    f"{lam_s / 2:.0f} Hz (keep it above the sub crossover)"))
        if "arc_angle" in v and v["arc_angle"] > 0 and n > 1:
            # Virtual arc: place subs on a circle of chord length = line length.
            theta = math.radians(v["arc_angle"])
            r = length / (2 * math.sin(theta / 2))
            xs = [-length / 2 + i * s for i in range(n)]
            # Sagitta per element: how far "behind" the line it would sit on the arc.
            sag = [r - math.sqrt(max(r * r - x * x, 0)) for x in xs]
            outer = max(sag)
            delays = [(outer - d) / c * 1000 for d in sag]
            out.append((f"Delay-arc, {v['arc_angle']:.0f} deg total (radius {r:.1f} m; general physics, "
                         "use ArrayCalc's SUB array delay proposal for the real values)",
                        "per sub L-to-R: " + ", ".join(f"{d:.2f}" for d in delays) +
                        " ms (centre gets most delay; outermost = 0)"))
    return out


def checks(v):
    """Inventory and rigging sanity checks. Returns (label, value, flag) rows."""
    rows = []
    bt = v.get("box_type", "").upper()
    if bt and bt not in TOPS:
        rows.append(("box_type", f"unknown '{bt}'", "use one of " + ", ".join(TOPS)))
        return rows
    if bt and "boxes" in v:
        kg, per_amp, per_amp_ap, frame, swl, max_boxes, any_splay = TOPS[bt]
        n, hangs = int(v["boxes"]), int(v.get("hangs", 2))
        if kg:
            mass = n * kg
            rows.append(("Cabinet mass per hang (frame and motors NOT included)",
                         f"{mass} kg ({n} x {kg} kg)", ""))
            if mass > swl:
                rows.append(("Frame", f"{frame} SWL {swl} kg", "OVER FRAME SWL"))
            if "point_wll" in v and mass > v["point_wll"]:
                rows.append(("Rigging point", f"{v['point_wll']:.0f} kg", "CABINETS ALONE EXCEED POINT"))
        if n > max_boxes:
            rows.append(("Boxes per hang", f"{n} > {max_boxes} max on {frame}", "OVER FRAME MAXIMUM"))
        if any_splay and n <= any_splay[0]:
            rows.append(("Load check", f"<= {any_splay[0]} boxes: any splay allowed by the rigging manual",
                         "still confirm in ArrayCalc"))
        else:
            rows.append(("Load check", "beyond the any-splay case", "ArrayCalc load check REQUIRED"))
        rows.append(("Sign-off", "head rigger / system tech", "HARD STOP before anything flies"))
        ap = str(v.get("ap", "no")).lower() in ("yes", "y", "true", "1")
        need = math.ceil(n * hangs / (per_amp_ap if ap else per_amp))
        sub_need = 0
        if v.get("sub_type") and "subs" in v:
            st = v["sub_type"].upper()
            if st in SUBS:
                sub_need = math.ceil(int(v["subs"]) / SUBS[st])
            else:
                rows.append(("sub_type", f"unknown '{st}'", "use one of " + ", ".join(SUBS)))
        mode = "ArrayProcessing (1 box per channel/pair)" if ap else "Line/Arc"
        line = f"{need} for tops ({mode})"
        if sub_need:
            line += f" + {sub_need} for subs = {need + sub_need}"
        flag = ""
        if "amps" in v and need + sub_need > v["amps"]:
            flag = f"SHORT BY {need + sub_need - int(v['amps'])} (have {int(v['amps'])})"
        elif "amps" in v:
            flag = f"ok (have {int(v['amps'])})"
        rows.append(("4-ch amps needed", line, flag))
        if ap:
            rows.append(("AP requirements", "OCA/AES70 Ethernet, AP-capable amp, 6.2 ms latency",
                         "check amp model in systems-and-amps.md"))
    return rows


def main(argv):
    given = parse(argv)
    v, src = fill(given)
    print("# ArrayCalc design brief\n")
    print(f"Givens supplied: {len(given)}. Everything marked ASSUMED must be "
          "confirmed before the design is trusted.\n")
    print("## Inputs\n")
    print("| Input | Value | Source |\n|---|---|---|")
    for k in KEYS:
        if k in v:
            print(f"| {k} | {v[k]} | {src[k]} |")
    print("\n## Derived geometry\n")
    print("| Quantity | Value |\n|---|---|")
    for name, val in derive(v):
        print(f"| {name} | {val} |")
    rows = checks(v)
    if rows:
        print("\n## Inventory and rigging checks\n")
        print("| Check | Value | Flag |\n|---|---|---|")
        for name, val, flag in rows:
            print(f"| {name} | {val} | {flag} |")
    print("\nTrim here = BOTTOM of the array. ArrayCalc's 'Frame height front' is the TOP "
          "front edge of the frame: enter a frame height, then read 'Height of lowest edge' "
          "in the load section and adjust until it matches this trim.")
    missing = [k for k in ("delay_at", "subs", "sub_spacing") if k not in v]
    if missing:
        print(f"\nNot computed (not given): {', '.join(missing)}.")
    print("\nThese are geometric bounds for sanity-checking ArrayCalc, not a prediction. "
          "Speed of sound here follows temperature; d&b documents use 343 m/s, R1 343.5 m/s.")


if __name__ == "__main__":
    main(sys.argv[1:])
