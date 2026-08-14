# Frequently asked questions

## General

#### How do I get a Game Bub?

You can buy a Game Bub from the [official Crowd Supply store](https://www.crowdsupply.com/second-bedroom/game-bub#products).

Game Bub is also open-source, and designed to be able to be built yourself. This isn't recommended for people without prior electronics experience. You can see the project files and instructions [on GitHub](https://github.com/elipsitz/gamebub/blob/be1d65f/docs/building.md).

#### What shell colors are available?

Only transparent colorless shells are available at the moment.

There was a campaign-exclusive transparent purple shell, available only during the duration of the original crowdfunding campaign. This is no longer available for sale.

If you 3D-print your own shell, however, you could make it be any color you want. Some people on the Discord have also discussed the possibility of dyeing a colorless shell to another color.

#### How was Game Bub created?

Game Bub was created by Eli Lipsitz over a few years. If you're curious about the early development process, you can read the following blog posts:

* [Building an FPGA Game Boy emulator](https://eli.lipsitz.net/posts/fpga-gameboy-emulator/)
* [Introducing Game Bub](https://eli.lipsitz.net/posts/introducing-gamebub/)

#### What's the difference between the vertical and horizontal Game Bub?

The first version of Game Bub had a vertical form factor ("rev 2"). For the mass produced Crowd Supply version, this was changed into a horizontal form factor ("rev 4").

Only the later, horizontal version is officially for sale. If you want a vertical Game Bub, you'll need to build it yourself.

The horizontal version has a few other improvements over the vertical version, like a larger, higher-resolution screen, a bigger D-pad, more SDRAM, and some ergonomic and reliability improvements.

#### Is Game Bub an emulator?

**Yes.** [You can read an explanation here](https://eli.lipsitz.net/posts/introducing-gamebub/#a-brief-rant-about-fpga-retrogaming), but in short: Game Bub does not use the original chips from any video game system. Thus, it is inherently an emulator (it emulates the target system).

Unlike most emulation handhelds, or emulation software that runs on a computer, Game Bub uses an FPGA to recreate (not clone) the target systems. This gives some advantages, like significantly lower latency (time between a button press and something happening), and the ability to interface with real hardware, like original game cartridges and other systems via the link port.


## Cores and Systems

#### What systems does Game Bub support?

Game Bub comes with Game Boy / Game Boy Color, and Game Boy Advance cores built-in.

A future firmware update will add the ability to load custom cores, possibly for other systems.

#### Is Game Bub 100% accurate?

No. Game Bub's Game Boy and Game Boy Advance cores have wide compatibility, but they're not 100% accurate (and have known issues in certain games, which could be fixed in the future).

#### Do flashcarts work on the Game Bub?

Game Bub is known to have issues with certain flashcarts and reproduction cartridges. This should be fixable in a future firmware update.

Note, however, that Game Bub has built-in support for running homebrew ROM files off of the microSD card, so flashcarts are not strictly required.

#### Does Game Bub support button remapping?

Firmware 1.0 does not support button remapping, but this may be added in a future firmware update.

#### Is fast-forward supported?

Firmware 1.0 does not support fast forward in either of the built-in cores.

#### Are save states supported?

Firmware 1.0 does not support save states in either of the built-in cores.

#### Does Game Bub support the GBA-GCN adapter link cable?

Yes, Game Bub works with the official GBA-GCN link cable. The shell has notches to allow the adapter to clip on without any modifications.


## Hardware

#### What are the specifications of Game Bub's screen?

The horizontal version has a 720x480, 24-bit IPS LCD, with variable refresh support. The display is laminated with tempered glass.

The vertical version uses a 480x320, 16-bit IPS LCD.

#### Does Game Bub support post-processing filters?

Firmware 1.0 supports [color correction filters](https://www.crowdsupply.com/second-bedroom/game-bub/updates/color-correction-on-the-game-bub). Other filters, like scanlines or pixel grid, are not supported (but they may be added in the future).

#### What scaling modes does the display support?

Firmware 1.0 uses fixed integer scaling for both the Game Boy and Game Boy Advance cores. The Game Bub screen is an exact integer multiple (3x) of the Game Boy Advance, but there's a small black border when playing Game Boy games.

A future update may introduce other scaling modes, such as non-integer scaling for the Game Boy.

#### Are the buttons tactile (clicky) or membrane (soft)?

The face buttons and D-pad use clicky tactile switches, like the Game Boy Advance SP (unlike the original Game Boy Advance, has membrane buttons).


## Dock

#### What is the Game Bub Dock?

The Game Bub Dock is an optional accessory that adds video output and external controller support to the Game Bub. *Game Bub only supports video output through the Dock: a standard USB-C video adapter will not work.*

You can buy a Dock from the [official Crowd Supply store](https://www.crowdsupply.com/second-bedroom/game-bub#products).

#### What is the output resolution of the Dock?

As of Firmware 1.0, the Dock produces 720x480 video output (matching the internal screen). Other output resolutions may be added in the future (e.g. 720p, or "direct" video output for use with scalers).

#### Does the Dock support analog video?

No, the Dock only produces digital video output.

#### Can I use wireless controllers without the Dock?

No, wireless controllers may only be used when Game Bub is plugged into a Dock.

#### Can the link port be used while Game Bub is docked?

Not really, the Dock partially covers the link port. This is purely a mechnical incompatibility: if you were to mod a Dock to have a different form-factor, the link port would work normally.


## Troubleshooting

#### My Game Bub isn't turning on

Make sure your Game Bub's battery is charged.

Also, make sure you aren't holding the <span class="btn btn-home">Home</span> or <span class="btn btn-vol-down">Volume-</span> buttons while turning the device on. If you did, hold the <span class="btn btn-power">Power</span> button for 7 seconds to force the device off, and then try turning on the device again.

#### Game Bub isn't recognizing my game cartridge

Make sure your cartridge's gold contacts are clean, and make sure the cartridge is securely inserted into the device.

To remove light grime, gently scrub the contacts using a cotton swap and 91%+ isopropyl alcohol. Let the contacts dry fully, and try again.

#### I'm encountering an unexpected game bug

Game Bub has very good game compatibility, but it isn't perfect. If you encounter bug with one of the built-in cores, you can [file an issue on GitHub](https://github.com/elipsitz/gamebub/issues), or report it on the Discord.

If you're playing a Game Boy Advance game, you should also make sure you're [using the official BIOS](playing-games/#custom-bios-files) for maximum compatibility.
