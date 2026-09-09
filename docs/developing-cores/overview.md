!!! warning "The framework is still under development"

    The documentation in this section refers to the Game Bub Core Framework
    as of `v1.1-beta`. The framework is not finalized, and may change
    based on developer feedback.

# Overview

## Game Bub Framework

In addition to the built-in Game Boy and Game Boy Advance cores, Game Bub allows third-party cores to be developed, using the [**Game Bub Framework**](https://github.com/gamebub/framework/). Developers can create cores that run on the FPGA, and users can install and run those cores by copying them to their microSD cards.

The framework is a library that abstracts over hardware, implements critical system functions, and manages communication with the host microcontroller (MCU). It exposes a set of well-defined interfaces for different aspects of the system (video, audio, input, etc.), which are versioned and may evolve over time while preserving backwards compatibility.

Because the framework implements critical system functionality, the framework itself must not be modified. This also helps preserve backwards compatibility as hardware and software change. If there's a missing interface, please file feature requests (or make contributions) to the Game Bub project.

The framework is written in a mix of the [Chisel HDL](https://www.chisel-lang.org/) and Verilog, although no knowledge of Chisel is required to use it. Cores may be written entirely in Verilog or VHDL.

## Hardware Overview

For Game Bub Rev4 (horizontal):

* AMD Xilinx XC7A100T FPGA
* 720x480 24-bit display
* Stereo speakers
* 64 MiB SDRAM (split across 2 chips), 16-bit bus
* 512 KiB asynchronous SRAM, 16-bit bus
* GB/GBA cartridge slot
* GBA link port
* PMOD expansion header
* 12 buttons

The framework takes care of scaling the core video to the display, or an external display when docked.

## System Setup

### Prerequisites

* Xilinx Vivado 2023.2 or later, with support for Artix-7 FPGAs
* Python 3.12 or later

The framework is developed on Linux. Vivado supports Windows as well, although this flow hasn't been tested.

## Template

The https://github.com/gamebub/core-example repository serves as both an example and template for building your own cores.

To build the bitstream for `gamebub_rev4`, run:

``` sh
./mill root.buildCore --target gamebub_rev4
```

And keep reading for a detailed dive into the structure of a core and framework interfaces.
