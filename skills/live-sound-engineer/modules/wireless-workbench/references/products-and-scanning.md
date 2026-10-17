# Products, hardware roles, scan files

## Product families in WWB

| Family | Networked in WWB | Notes |
|---|---|---|
| Axient Digital (AD4D, AD4Q, ADX5D; AD/ADX transmitters) | Yes | Flagship. ShowLink with ADX transmitters. Interference detection on AD4D/AD4Q, some ADX5D. Quadversity. |
| Axient (AXT) | Yes | Older flagship. ShowLink via AXT610. |
| ULX-D | Yes | HD mode for dense channel counts; 1 mW after resync in HD. No ShowLink. |
| QLX-D | Yes | No ShowLink. |
| SLX-D | Yes | No ShowLink. |
| PSM 1000 | Yes | Coordinate in the same workspace as mics. |
| PSM 900 / PSM 300 | Check per model; treat as hand-tuned unless the user confirms network control | Still must be in the coordination workspace. |
| UHF-R | Limited in WWB 7 | Full support was in WWB 6.15. |
| BLX, GLX-D | No | Not networkable. Tune by hand. GLX-D is 2.4 GHz and auto-frequency; it still matters for ShowLink/Wi-Fi congestion. |
| Third-party (Sennheiser, Audio-Technica, etc.) | No control | Built-in profiles for coordination; tune by hand. Sennheiser's equivalent software is WSM. |

When a product's WWB support is in doubt, check the Supported Features page of the WWB online help rather than guessing.

## Hardware roles

- **AD600** Axient Digital Spectrum Manager: 174 MHz–2 GHz, six antenna inputs, real-time scanning, AD600 Live Plot in WWB, holds compatible frequency lists for automatic backup switching.
- **AXT600** Axient Spectrum Manager: predecessor. Ignores inclusion groups when auto-assigning.
- **AXT610 / AD610**: ShowLink access points (2.4 GHz control link).
- **AXT620**: Ethernet switch with DHCP server.
- Receivers with scan capability can scan their own band; check Supported Features for which ones.

## Scan files

Import path: Scan data section > import icon > File / Hardware / Scan Library.

Rules for file imports:
- Formats: .csv, .txt, .spa. Native support for WiNRADiO (.35s), TTi (.csv), RF Explorer (.csv), Sennheiser (.csv), Anritsu (.spa), Rohde & Schwarz (.csv).
- Plain files: no header lines. One reading per line: frequency, comma, level.
- Minimum step size 25 kHz.
- Frequency in MHz, level in dBm is the safe form. `modules/wireless-workbench/scripts/clean_scan.py` produces exactly that.

Common failure modes the script catches:
- Header rows or metadata from analyser exports (import fails or mis-parses).
- Frequency in Hz or kHz (plot lands at absurd frequencies or nothing shows).
- Step finer than 25 kHz (import rejected). The script max-holds into 25 kHz bins, which keeps every peak.
- Unsorted or duplicate frequencies from multi-pass exports.

## Scan Library

Online database of user-contributed scans by location. Useful for an advance on an unfamiliar venue; never a substitute for an on-site scan. Note the scan date and who uploaded it.
