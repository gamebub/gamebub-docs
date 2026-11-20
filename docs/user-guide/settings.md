# Settings

To change device settings, open the **Main Menu** and select **Settings**.

<figure markdown="span" style="image-rendering: pixelated;">
  ![Screenshot: Settings](screenshots/ui-settings-menu.png)
</figure>

### About

The *About* section shows information about your device's hardware and software.

If the Game Bub is plugged into a Dock, it will also show information about the Dock.

### General

* **Date and Time (UTC)**: Adjust the system's date and time, in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
    * Press <span class="btn btn-confirm">Confirm</span> to start editing, use the <span class="btn btn-dpad">D-Pad</span> to modify, and press <span class="btn btn-confirm">Confirm</span> again to save the modified time.
* **Startup Action**: change the behavior of the device at boot
    * *Main Menu* (default): open the main menu
    * *Run Cartridge*: skip the menu, immediately run the inserted game cartridge
* **Require long press to power on**:
    * *Off* (default): turn on the device by briefly pressing <span class="btn btn-power">Power</span>
    * *On*: turning the device back on requires holding <span class="btn btn-power">Power</span> for ~1 second

    !!! warning

        Due to a hardware limitation, enabling this feature will drain approximately 1% of your battery per day while powered off.

* **Auto-dim screen on inactivity**: automatically dim the built-in screen after a period of inactivity
    * *1 min* (default)
    * *3 min*
    * *5 min*
    * *Never*

### Dock

This section controls behavior when the Game Bub is inserted into a Dock.

* **Swap A/B and X/Y**: swap the A/B and X/Y face buttons on external controllers when docked
    * *Off* (default): use standard controller button mapping
    * *On*: swap A/B and X/Y on external controllers
* **Use built-in screen when docked**: controls whether the built-in screen or an external screen is used when docked
    * *Off* (default): use the external screen (and turn off the built-in screen)
    * *On*: use the built-in screen when docked 


### Core: GB / GBC

This section controls the built-in Game Boy and Game Boy Color core.

* **Enable GB Mode**: Set the emulated device model
    * *Off* (default): emulate a [Game Boy Color (CGB)](https://en.wikipedia.org/wiki/Game_Boy_Color)
    * *On*: emulate an original [Game Boy (DMG)](https://en.wikipedia.org/wiki/Game_Boy)
* **GBC Color Corrections**: set the color correction profile used in Game Boy Color mode
    * *None*: no color corrections (sRGB)
    * *GBC* (default): Game Boy Color
    * *GBA*: Game Boy Advance
    * *GBA SP*: Game Boy Advance SP
* **GB Color Palette**: set the color palette used in Game Boy mode
    * *Grayscale*: shades of gray
    * *DMG Green* (default): bright green, like the original Game Boy (DMG)
    * *GB Pocket*: soft green, like the Game Boy Pocket

### Core: GBA

This section controls the built-in Game Boy Advance core.

* **Color Corrections**: set the color correction profile
    * *None*: no color corrections (sRGB)
    * *GBA* (default): Game Boy Advance
    * *GBA SP*: Game Boy Advance SP
    * *NDS*: Nintendo DS (original)
    * *NDS Lite*: Nintendo DS Lite
    * *NSO GBA*: alternate Game Boy Advance (from Nintendo Switch Online)
* **Enable Game Boy Player**: Emulate the [Game Boy Player](https://en.wikipedia.org/wiki/Game_Boy_Player). This enables rumble in [supported games](https://en.wikipedia.org/wiki/Game_Boy_Player#Rumble_enabled). However, [GBA Video](https://en.wikipedia.org/wiki/Game_Boy_Advance_Video) cartridges will refuse to work.
    * *Off*: disable Game Boy Player emulation
    * *On* (default): enable Game Boy Player emulation
* **Warn about missing BIOS**: Show a compatibility warning if no GBA BIOS was found when launching a game
    * *Off*: disable the warning
    * *On* (default): enable the warning
