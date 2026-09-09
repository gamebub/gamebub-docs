!!! warning "The framework is still under development"

    The documentation in this section refers to the Game Bub Core Framework
    as of `v1.1-beta`. The framework is not finalized, and may change
    based on developer feedback.

# Core Structure

This **example core** both shows how the framework is used, and can be used as a template from which to begin developing other cores: https://github.com/gamebub/core-example. To clone the repository, use the following command:

```
git clone --recurse-submodules https://github.com/gamebub/core-example
```

## Key Components

* `framework/`: The Game Bub Framework, as a Git submodule that can be independently updated
* `rtl/`: Directory for the core's Verilog or VHDL code
* `chisel/src/`: Directory for the core's Chisel code
* `metadata/`: JSON metadata files to be packaged with the core
* `mill`: [Mill](https://mill-build.org) bootstrap script, for running framework build commands
* `build.mill`: Mill build file

You'll notice that there are a bunch of additional files that *aren't* just the Verilog/VHDL RTL for the core. If you're building a typical core, you don't need to understand most of this code, but we'll go over the relevant details.

## Building

To build the example core, run:

``` sh
./mill root.buildCore --target gamebub_rev4
```

This uses the Mill build tool to compile the core for the `gamebub_rev4` target. It first compiles the Scala files associated with the framework and any Chisel code, then bundles it up with any other RTL files and passes them over to `Vivado` for building.

## Components

Let's start by taking a look at `build.mill`:

``` scala title="build.mill"
import mill._
import mill.scalalib._

object root extends build.framework.FrameworkModule {
  override def sourcesFolders = Seq("chisel/src")

  override def defaultCoreClass = Some("DemoCore")

  override def mvnDeps = super.mvnDeps() ++ Seq(
    // Optional: add additional Scala dependencies
  )
}
```

The main thing to note here is `defaultCoreClass`, which in this example is set to `DemoCore`. This defines the Scala entrypoint to your core, which is used by the framework for configuration. If you don't know Scala, don't worry! You can pretty much just treat this as a configuration file.

Let's break the main entrypoint `chisel/src/DemoCore.scala` down into pieces. First, it starts by defining the `DemoCore` class (references above in `build.mill`):

``` scala title="chisel/src/DemoCore.scala"
class DemoCore extends Module with Core {
    ...
}
```

### Interfaces

In the class, we have the `val io = IO(new Bundle { ... })` bundle.

``` scala title="chisel/src/DemoCore.scala"
val io = IO(new Bundle {
    val clocks = new ClocksV0(
        clockSystemHz = 10_000_000,
        clockDisplayHz = displayClock,
        clockSpiHz = 200_000_000,
    )
    val video = new VideoV0(
        videoWidth = 240,
        videoHeight = 160,
        colorDepthR = 5,
        colorDepthG = 5,
        colorDepthB = 5,
        framePeriod = 1.0 / 60.0,
    )
    val audio = new AudioV0()
    val host = new HostV0()
    val input = new InputV0()
})
```

This constructs the actual interface between your core and the framework. This is made up of a series of modular interfaces (e.g. `video`). A core selects a specific version of each interface (e.g. `VideoV0`), and configures it as needed (e.g. `videoWidth = 240`).

Some interfaces (like `clocks`) are required. Others (like `input`) aren't. For a full listing of the different interfaces available and their configuration parameters, see the [Reference: Interfaces](reference-interfaces) section.

Certain interfaces also provide information about the specific platform the core is being built for. Although the framework abstracts away many of the details of the underlying hardware, your core may need to know about certain aspects of the hardware.

In this example, the core needs to generate the clock used to drive the display. Since the display could vary on different hardware revisions (and the clock required may vary at different frame rates), the `DemoCore` class does a bit of math to figure out how to configure a PLL divider:

``` scala title="chisel/src/DemoCore.scala"
val (displayClockMin, _) = ClocksV0.getClockDisplayHz(1.0 / 60.0)
val mmcmVcoHz = 800_000_000
val displayDivider = (mmcmVcoHz.toFloat / displayClockMin).floor.toInt
val displayClock = mmcmVcoHz / displayDivider
```

Here, `ClocksV0.getClockDisplayHz` returns the minimum and maximum allowable clock frequency for the given frame period (`1.0 / 60.0`: 60 Hz). Then, it uses the MMCM (a fancy Xilinx PLL) internal VCO frequency (in this example, 800 MHz) to calculate the divider needed to generate the display clock, and the actual value of the display clock.

This value is passed both to the `clocks` interface, as well as the inner Verilog implementation below.


### Verilog / VHDL Bridge

Although the Framework and entrypoint class are written in Chisel, the rest of your core need not be written in Chisel. This example is primarily written in Verilog.

The framework provides a helper utility to easily delegate the majority of the work to a separate Verilog module:

``` scala title="chisel/src/DemoCore.scala"
bindExtModule("demo_core", io, Map(
    "DISPLAY_DIVIDER" -> displayDivider,
))
```

Here, `bindExtModule` is used to bind the `io` variable (the complete interface for the core) to an instantiation of the Verilog module called `demo_core`. The framework automatically uses Verilog modules added to the top-level `rtl/` directory.

`bindExtModule` also provides the means to pass parameters to the module (e.g. `DISPLAY_DIVIDER` here), and while the core is being built, it also **automatically generates a Verilog template** to use, based on the configuration of the core. This template is printed when building the core.

The template generated for this core looks something like this:

``` verilog
module demo_core
#(
  parameter int  DISPLAY_DIVIDER
)
(
  input  logic        clock,
  input  logic        reset,
  ...
  output logic [4:0]  video_data_r,
  output logic [4:0]  video_data_g,
  output logic [4:0]  video_data_b,
  output logic        video_dataEnable,
  output logic        video_vblank,
  output logic        video_hblank,
  ...
);

  // Add module implementation here.

endmodule
```

You can see that the ports for the module have been automatically generated and configured based on the individual interfaces used (and their configurations). This is one way that the framework allows cores with wildly different capabilities to be used on the same (or different) underlying hardware.
