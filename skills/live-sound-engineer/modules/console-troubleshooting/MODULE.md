# Module: Console Troubleshooting

Part of the live-sound-engineer skill. Load this module when a console is passing signal wrong or not at all: **"link is up but no audio at the PA"**, "signal on the channel but no sound", a dead output or mix, a remote-control app that can't find the desk, or a tone/noise nobody can trace. It covers the console side from the source channel to the stagebox outputs; amp-side faults hand off to the amp's own module (`modules/r1/MODULE.md` for d&b).

All paths below are relative to the skill root.

## Brand references

Read only the one for the desk in front of you. If none matches, run the elimination order below on the desk's own screens and web-search the manufacturer's docs for menu paths; never invent one.

| Console | Reference |
| --- | --- |
| Allen & Heath Qu-5/6/7 (+ Qu-MixPad) | `modules/console-troubleshooting/references/allen-heath-qu.md` |

## No audio at the PA: elimination order

Work from the source to the speaker and say what each step rules out. Look first; change nothing on the way unless asked.

1. **Source channel.** Is the programme on the channel you think? (Laptop over the console's USB = the USB channel; an external interface may sit on a mic input.) Check its input meter, mute, fader, and its assignment and level to the main bus. A fader at -inf looks exactly like "signal but no sound".
2. **Main master.** Mute and fader. Matrices and most PA feeds are **post-fader**, which means after the master mute too, so a muted or -inf master kills everything downstream.
3. **Matrix (or output bus) sends** from the main: on, pre/post, level.
4. **Matrix masters:** mute and fader for whatever feeds the PA.
5. **Output patch:** the PA feeds land on the sockets (local, stagebox, network) the amps are actually cabled to. Don't "fix" it by patching the main bus straight out; it still passes the master mute and bypasses the matrix gain structure.
6. **Link and stagebox:** the console sees the expander (link status, socket availability), the cable is in the right port (primary, not cascade/redundant), the clock source is sane.
7. **Prove the downstream half without the master:** console signal generator, **pink noise** around -40 dB, routed to **one PA matrix or output only**, main bus off. Hiss from the PA = console-to-speaker path is good and the fault is upstream (steps 1–2). Silence = stagebox or later: XLRs in the patched outputs, amp input routing, amp mutes.
8. **Clean up:** every signal-generator route off, and check it isn't left on the main bus; a forgotten tone there plays the moment the master is unmuted.

## Hard stops

- Never unmute a master with programme playing and the fader up. Pull the fader to -inf, unmute, bring it up slowly.
- Don't raise channel or master faders, or send a test signal anywhere, while the master is live unless the user says so. Ask once, saying what will come out of the PA.
- Don't repatch, recall a scene or update firmware on a desk that is running a show without a yes.

## Output

At a gig: the cause in the first line, then the fix, then what was ruled out in one line. In research or post-mortem: the full chain as a table of stage, state found and verdict.
