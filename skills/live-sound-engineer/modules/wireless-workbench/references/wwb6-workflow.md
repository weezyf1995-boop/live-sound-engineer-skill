# WWB 6 coordination workflow

The user runs **Wireless Workbench 6** (latest 6.x is 6.15.4, Oct 2023). This is the default workflow. Use `coordination-workflow.md` (WWB 7) only for concepts, or if the title bar says 7.

UI names below come from Shure's WWB 6 quick start guide and Shure/ProSoundWeb WWB 6 tutorials. Where something isn't confirmed for WWB 6, it says so: look at the screen and adapt rather than hunting for a WWB 7 control.

## Layout

Three main tabs: **Inventory**, **Frequency Coordination**, **Monitor**. On macOS the app menu is **Wireless Workbench 6**.

## 0. Network check

- Preferences: **Wireless Workbench 6 > Preferences** (Windows: **Tools > Preferences**).
- **Preferences > Network tab**: select the interface the Shure devices are on (wired Ethernet).
- **Flash All Devices** (bottom left): every networked unit should blink. Fix any unit that doesn't before going on (see `show-mode-playbooks.md`, "Devices not showing").
- **Reports > Firmware and Network Summary** if anything looks off.

## 1. Inventory

- Networked devices appear on the **Inventory** tab. Green bar = online; grey bar = offline.
- Check Device ID and channel names. Name channels to match the console patch.
- Gear not on the network: **Add New Device** > manufacturer and model > number of channels > band > **Add**. Third-party devices are added the same way. They appear with a grey bar.

## 2. Backups on

- **Wireless Workbench 6 > Preferences > Coordination > General** > enable **Automatically calculate backup frequencies** > **Apply** > save.

## 3. Load the workspace and set priority

- **Frequency Coordination** tab. Five panes: three on top, two on the bottom.
- Bottom right: **Add Frequencies** > **Select Frequencies From Inventory...** > **Coordination Chooser** > **All frequencies from inventory** > OK. This fills the **Coordination Workspace** (bottom left). Click **Expand All**.
- **Order is priority in WWB 6.** It assigns frequencies in the order channels appear, so drag lead vocal, presenter and other priority channels to the top. It can reorder occasionally; check before calculating.

## 4. Scan

- Before scanning: show mics, bodypacks and IEM transmitters **off**; other RF that will run during the show (video walls, LED, comms) **on**. This is a physical step for the user; it is in the pre-flight checklist.
- Top left: cog next to **Recent Scans** > **Live Scan Settings...** > under Microphones pick the receivers covering the widest range (use the Start/Stop columns) > **Start**. Occupied spectrum shows on the **Frequency Plot**.
- External analyser file: run `scripts/clean_scan.py` first, then import. Import location in WWB 6 is not confirmed here; look in the scan area of the Frequency Coordination tab.

## 5. Thresholds and exclusions

- Top right, **Plot Properties**: **Scan Peak Threshold** (orange line) at about -60 dBm. Lower the **Exclusion Threshold (dBm)** to exclude problem ranges (blue shading). Around -80 dBm is a common working figure; excluding too much leaves too little spectrum.
- Add manual exclusions for every range not legal at the venue. Saudi Arabia: `saudi-cst.md`. WWB does not enforce legality.
- TV channels, inclusion groups and compatibility profiles: use them if present on screen; exact WWB 6 locations not confirmed here. WWB 7-only features (ignoring intermod within inclusion groups, custom coordination order controls) do **not** exist in WWB 6; use channel order instead.

## 6. Calculate and analyse

- **Lock** anything already deployed and working first.
- **Calculate** (Coordination Workspace toolbar). Wait for the progress bar to finish.
- Not enough frequencies: raise the exclusion threshold a little and calculate again, then work the "Finding more frequencies" list in `coordination-workflow.md`, skipping WWB 7-only steps.
- **Analyze** any frequency entered by hand.

## 7. Assign and deploy

- **Assign and Deploy** (centre toolbar). Under **Assigned Channels**, the **Rank** and **dBm** columns show quality. Put priority channels on the best-ranked frequencies; drag between Assigned and Unassigned to reorder.
- Make sure **Copy assignment changes to coordination workspace on deployment** is ticked (bottom left).
- **Deploy to Inventory** (bottom right). Units flash as they take the frequencies. The Deploy to Inventory window confirms it: **OK**, then **Close**.
- Then: IR-sync transmitters (user), hand-tune list for non-networked and third-party gear.

## 8. On site with an offline-built show

- Open the show file, then use **settings merging** to push the saved plan onto the online devices. If a **Settings Conflicts** dialog appears, keep the Workbench settings unless the user said the hardware is right.

## 9. Save and hand off

- Save the show file after every major step and at the end. Hand off per the module's Hand-off section.
