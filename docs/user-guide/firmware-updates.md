# Firmware updates

You should keep your devices updated to take advantage of the latest bugfixes, features, and
other improvements.

The Game Bub Handheld and Dock can both be updated over USB by connecting them to a computer
with a data-capable USB cable.

## Handheld

You can find the latest update on the [GitHub release page](https://github.com/elipsitz/gamebub/releases).

### Installing an update

1. Start by [powering off the device](/user-guide/getting-started/#power-and-charging).
2. Wait 10 seconds to ensure the device is fully powered off.
3. While holding <span class="btn btn-vol-down">Volume-</span>, press the <span class="btn btn-power">Power</span> button.
4. The purple light will start blinking, two blinks at a time. The screen *will not* turn on.
5. Using a USB-C cable, plug the device into a computer.
6. After a few seconds, a virtual USB drive called **GAME BUB** will appear.
7. Drag the firmware update file (`.uf2`) to the virtual USB drive.
8. Allow up to 30 seconds to install the update.
9. After the file is successfully copied, the device will reboot automatically.
10. After a successful update, `Settings -> About` will show the new firmware version.


## Dock

!!! note

    There are currently no firmware updates available. Please check later!

### Installing an update

1. Unplug the Dock.
2. While holding the rear button, connect the rear USB-C port to a computer using a USB cable.
3. After a few seconds, a virtual USB drive called **GameBubDock** will appear.
4. Drag the firmware update file (`.uf2`) to the virtual USB drive.
5. Allow up to 30 seconds to install the update.
6. After the file is successfully copied, the dock will reboot, and the *red standby light* will turn on.

## Troubleshooting

!!! tip

    After a successful update, the device will reboot automatically. You may see a
    "USB drive not properly ejected!" warning from your operating system. This is
    safe to ignore.

!!! warning

    Windows sometimes fails to properly copy the update file to the virtual USB drive.
    If the copy fails, and the device doesn't automatically reboot, reconnect
    the device and try again.

