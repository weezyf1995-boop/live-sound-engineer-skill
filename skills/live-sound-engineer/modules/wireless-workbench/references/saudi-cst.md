# Saudi Arabia: CST PMSE rules for a WWB plan

Source: CST, Regulations on the Use of the Radio Spectrum for PMSE (Annex 8), Decision 563/1447, dated 05/11/2025.
https://www.cst.gov.sa/en/regulations-and-licenses/regulations/Document-1611

Regulations change. If the show date is more than a few months after this file was written (October 2026), re-check the CST page before relying on the table.

## Licensing

- A CST licence is required before use. Apply at least 10 business days before first use.
- Eligible applicants: government entities and companies legally registered in KSA that organise the event or operate the equipment.
- Temporary licence: up to 60 days total including renewals. Longer use: annual licence.
- Application needs: equipment technical documentation and bands, coordinates of every location, start and end dates, serial numbers and manufacturer details.
- First come, first served. PMSE is non-interference, non-protection: you may not interfere, and you are not protected.
- Light licensing for some audio uses and licence-exempt SRD use exist under separate CST rules and technical specification RI044. Check those for small, low-power setups.
- CST issues separate spectrum plans for large-scale events. For festival-scale shows, ask the organiser for the event's CST plan before coordinating.
- WMAS (wideband multichannel audio) is case by case.

## Prohibited for PMSE

- **617–652 MHz**
- **663–698 MHz**

Add both as manual exclusions in every Saudi show file. Any transmitter whose tuning range sits entirely inside these cannot be used.

## Bands for wireless microphones and IEMs (Article 12-1)

| Range (MHz) | Max power | Licence |
|---|---|---|
| 29.7–47 | 10 mW ERP | Annual / temporary |
| 173.965–174.015 | 2 mW ERP | Annual / temporary |
| 174–216 | 50 mW ERP | Annual / temporary |
| 470–614 | 50 mW ERP | Annual / temporary |
| 654–663 | 20 mW EIRP (up to 100 mW EIRP at CST discretion, e.g. body-worn) | Temporary only |
| 733–738 | 50 mW ERP | Temporary only |
| 823–832 | 20 mW EIRP (up to 100 mW EIRP at CST discretion) | Temporary only |
| 1785–1803 | 20 mW EIRP (up to 50 mW EIRP at CST discretion) | Temporary only |

Channel bandwidth 200 kHz per channel (wider on request). Audio links (Article 12-2): 174–216 and 470–614 MHz at up to 5 W ERP, temporary.

## Applying it in WWB

1. Check each device's band label against the table. Flag any band that is wholly or partly in a prohibited range.
2. Add manual exclusions: 614–654, 663–733, 738–823 MHz and anything else outside the permitted list that falls inside a device's tuning range. (614–617 and 652–654 are not listed as permitted either, so exclude the whole gap, not just the prohibited core.)
3. Use inclusion groups to pin each band family to its legal slice.
4. Set transmitter RF power at or under the limit for the slice (e.g. 654–663 MHz is 20 mW EIRP unless CST allowed more).
5. Do not rely on WWB's TV database for Saudi legality. Treat the table as the authority and the scan as the reality check.
6. Output the licensed frequency list in the format CST asked for, alongside the WWB report.

`modules/wireless-workbench/scripts/clean_scan.py --flag-ranges 617-652,663-698` reports scan energy in the prohibited ranges, which is useful evidence when something illegal is already transmitting in the venue.

This is regulatory information, not legal advice. The licence holder is responsible for compliance; when in doubt, ask CST directly (19966, info@cst.gov.sa).
