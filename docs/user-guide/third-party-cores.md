# Third-party cores

!!! warning

    Third-party core support is only available on `v1.1-beta` firmware and is still under development.

You can install and run third-party FPGA cores from your microSD card.

The [Game Bub Core Directory](https://cores.gamebub.net/) is a good place to find cores and stay up-to-date with the latest releases.

## Installation

Download the core, and copy the entire directory to a top-level `cores` directory on the microSD card. For example, it may look like `/cores/Author.CoreName`.

Some cores may require additional steps (e.g. copying a BIOS file). Make sure to read the documentation for the core.

## Running cores

When you select **Cores** from the Main Menu, select the core from the list.

Then, select any files needed by the core (such as ROMs or other assets).

When you exit a core, save files and settings are persisted back to the microSD card.

## Developing

Third-party cores are developed with the **Game Bub Framework**. See [Developing Cores](/developing-cores/overview/) for complete information.
