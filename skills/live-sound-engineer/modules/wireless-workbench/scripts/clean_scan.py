#!/usr/bin/env python3
"""Clean an RF scan export into a file Wireless Workbench will import.

Output: headerless CSV, one "frequency_MHz,level_dBm" pair per line, sorted,
step >= 25 kHz (finer data is max-held into 25 kHz bins so no peak is lost).

Usage:
  clean_scan.py INPUT [-o OUTPUT] [--unit auto|hz|khz|mhz]
                [--flag-ranges 617-652,663-698] [--flag-threshold -80]
"""
import argparse
import math
import re
import sys

MIN_STEP_MHZ = 0.025
NUM = re.compile(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?")


def read_pairs(path):
    pairs, skipped = [], 0
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            nums = NUM.findall(line.replace(";", ",").replace("\t", ","))
            if len(nums) < 2:
                skipped += 1
                continue
            # Lines with letters before the first number are headers/metadata.
            first = line.strip().split(",")[0].split(";")[0].split("\t")[0]
            if re.search(r"[A-Za-z]", first) and not NUM.fullmatch(first.strip()):
                skipped += 1
                continue
            pairs.append((float(nums[0]), float(nums[1])))
    return pairs, skipped


def detect_unit(freqs):
    med = sorted(freqs)[len(freqs) // 2]
    if med >= 1e7:
        return "hz"
    if med >= 1e4:
        return "khz"
    return "mhz"


def to_mhz(value, unit):
    return {"hz": value / 1e6, "khz": value / 1e3, "mhz": value}[unit]


def bin_maxhold(pairs):
    bins = {}
    for f, lvl in pairs:
        key = round(math.floor(f / MIN_STEP_MHZ + 1e-9) * MIN_STEP_MHZ, 3)
        if key not in bins or lvl > bins[key]:
            bins[key] = lvl
    return sorted(bins.items())


def parse_ranges(text):
    out = []
    for part in text.split(","):
        lo, hi = part.split("-")
        out.append((float(lo), float(hi)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    ap.add_argument("--unit", default="auto", choices=["auto", "hz", "khz", "mhz"])
    ap.add_argument("--flag-ranges", help="comma list of lo-hi MHz ranges to report energy in")
    ap.add_argument("--flag-threshold", type=float, default=-80.0, help="dBm level counted as energy (default -80)")
    args = ap.parse_args()

    raw, skipped = read_pairs(args.input)
    if not raw:
        sys.exit("No frequency/level pairs found. Check the file is a scan export.")

    unit = detect_unit([f for f, _ in raw]) if args.unit == "auto" else args.unit
    pairs = [(to_mhz(f, unit), lvl) for f, lvl in raw]
    pairs.sort()

    steps = [b[0] - a[0] for a, b in zip(pairs, pairs[1:]) if b[0] - a[0] > 0]
    min_step = min(steps) if steps else 0.0
    dupes = len(pairs) - len({f for f, _ in pairs})

    if min_step and min_step < MIN_STEP_MHZ - 1e-9 or dupes:
        out = bin_maxhold(pairs)
        binned = True
    else:
        out = [(round(f, 3), l) for f, l in pairs]
        binned = False

    lines = [f"{f:.3f},{l:.1f}" for f, l in out]
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")

    peak_f, peak_l = max(out, key=lambda p: p[1])
    print(f"input lines skipped (headers/blank): {skipped}")
    print(f"readings in: {len(raw)}  unit detected: {unit}" + ("  <-- raw file was not MHz" if unit != "mhz" else ""))
    print(f"range: {out[0][0]:.3f}-{out[-1][0]:.3f} MHz")
    print(f"min raw step: {min_step * 1000:.1f} kHz  duplicates: {dupes}")
    print(f"max-held into 25 kHz bins: {'yes' if binned else 'no'}  readings out: {len(out)}")
    print(f"strongest reading: {peak_f:.3f} MHz at {peak_l:.1f} dBm")

    if args.flag_ranges:
        for lo, hi in parse_ranges(args.flag_ranges):
            hits = [(f, l) for f, l in out if lo <= f <= hi and l >= args.flag_threshold]
            if hits:
                top = max(hits, key=lambda p: p[1])
                print(f"FLAG {lo:g}-{hi:g} MHz: {len(hits)} readings >= {args.flag_threshold:g} dBm, peak {top[0]:.3f} MHz at {top[1]:.1f} dBm")
            else:
                print(f"clear {lo:g}-{hi:g} MHz: nothing >= {args.flag_threshold:g} dBm")

    if not args.output:
        sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
