# Show-mode playbooks

First line is always the safest action. Explanation after, only if there is time.

## A channel is dropping out

Safe first move: hand the performer the spare transmitter already on a coordinated backup, or patch the spare channel. Diagnose after the song.

Triage by what the Monitor tab shows:

| Symptom | Likely cause | Action |
|---|---|---|
| RF bars drop, one channel, follows the performer's position | Range, body blocking, antenna line of sight | Move or raise antennas, check performer's pack placement |
| RF bars fine, audio drops | Battery, pack fault, mic cable/capsule, mute | Check battery level and transmitter, swap pack |
| Several channels drop together | Antenna, cable, distro, or strong interferer | Check antenna distribution and cables first, then scan |
| RF present with transmitter off | Interference on that frequency | Move to backup (below) |
| Drops when a specific other system keys up | Intermod or untracked transmitter | Find it, add to inventory, recalculate with everything else locked |

Check the Timeline and Event Log for the moment it happened; mini-timelines show RF and audio history per channel.

## Interference event (AD4D, AD4Q, some ADX5D)

Event colours: white non-active, yellow Alert (present, not yet causing dropouts), red Detected (can cause dropouts).

1. **Switch** moves the channel to a clean backup. Only works with a Spectrum Manager and a compatible frequency list.
2. No Spectrum Manager: **Select from frequency list**, pick a backup, then IR-sync or let ShowLink retune the transmitter.
3. Channel in an inclusion group on an AXT600 system: do not use Switch (AXT600 ignores inclusion groups); use Select from frequency list and stay inside the group's range.
4. Remove Inactive Events to clear the list after.

Setup for next time: receiver Properties > Radio tab > Interference Avoidance Mode (Off / Manual / Automatic). Unregistered Transmitter Action: Allow / Warn / Block.

## Devices not showing in WWB

In order, stop at the first fix:

1. Network icon on the receiver display? If not, link LEDs on the jack; swap the cable.
2. WWB is listening on the right network interface (Preferences > Network). A laptop on Wi-Fi and Ethernet together is the usual culprit.
3. Computer IP on the same subnet as the devices. `ping <device IP>`: 0% loss means WWB should see it; 100% loss means subnet or cabling.
4. Firewall allows all WWB components. VPN off.
5. Devices on another subnet: use Remote Device Connection.
6. AXT620 switch: browse to its IP, System > DHCP Server > Client Entries to see what got an address. Shure MACs start 00:0E. (Default login per Shure docs; change it if still default.)
7. Firmware too old or too new for this WWB version: check the Shure compatibility notes before updating anything mid-show. Do not update firmware during a show.

## ShowLink not linking (Axient / Axient Digital only)

1. Access point (AXT610/AD610) is on the network.
2. IR-sync the transmitter; the ShowLink icon should appear on the receiver.
3. Receiver home screen > SHOWLINK TEST > select transmitter to read signal strength.
4. Weak: check antennas on access point and transmitter. Access point at least 2 m high, antenna vertical, on a stand or non-metal wall. Directional antenna: Shure logo side toward the stage.
5. ShowLink shares 2.4 GHz with Wi-Fi. Check the 2.4 GHz spectrum view in WWB and move away from congested Wi-Fi channels.

Losing ShowLink loses remote control only. Audio RF is unaffected. Say so first; it lowers the temperature.
