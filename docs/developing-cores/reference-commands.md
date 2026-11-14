!!! warning "The framework is still under development"

    The documentation in this section refers to the Game Bub Core Framework
    as of `v1.1-beta`. The framework is not finalized, and may change
    based on developer feedback.

# Reference: Host/Core Commands

As described in [Reference: Interfaces](reference-interfaces), there is a bidirectional Command / Request interface between the Host MCU and the Core.

To begin a request, the initiator raises `request` high, and holds it high for the duration of the request. The receiver then raises the `busy` signal, to indicate it is working on the request. When the receiver is finished, it raises the `done` signal (and the `error` signal, if the command completed in an error). 

After the initiator is done handling the response, they must lower `request`. Then, they may raise `request` again to send a new request, and the whole process repeats.

## Parameters and Results

Request parameters and results are transmitted using the memory bus, in the regions `0xF000_0000` (Host -> Core) and `0xF000_1000` (Core -> Host). Each parameter and result is 32 bits.

Before raising `request`, the host writes its command opcode to `0xF000_0000`, its first parameter (if there is one) to `0xF000_0004`, its second parameter (if there is one) to `0xF000_0008`, etc.

Upon request completion (when `done` goes high), the host will read the first result word from `0xF000_0000`, the second result word from `0xF000_0004`, etc.

For Core -> Host commands, the same interface holds true, but in reverse, at starting at `0xF000_1000`. That is, when `request` is raised by the core, the host will read the opcode from `0xF000_1000`, the first parameter from `0xF000_1004`, etc. And similarly, before it raises `done`, it will write the first result word to `0xF000_1000`, the second to `0xF000_1004`, etc.

## Host -> Core commands

### `GetStatus` (`0x0000`)
Called by the host to request the status of the core. No parameters. The result is a single value, indicating the status:

* `StatusUnknown = 0`: unknown status
* `StatusInitialize = 1`: the core is initializing itself
* `StatusSetup = 2`: the core has initialized, and is ready for the host to transmit commands and memory accesses
* `StatusCoreHalt = 3`: the core has been set up, and is halted in reset 
* `StatusCoreRun = 4`: the core is actively running

### `CoreRun` (`0x0100`)
Called by the host to start core execution (taking it out of reset).

No parameters or results.

The core should transition to `StatusCoreRun`.

### `CoreHalt` (`0x0101`)
Called by the host to halt core execution (putting it into reset).

No parameters or results.

The core should transition to `StatusCoreHalt`.

### `SetupComplete` (`0x0102`)
Called by the host to indicate that it is done setting up the core (files and settings have been transmitted).

No parameters or results.

The core should finalize its setup and transition to `StatusCoreHalt`.

### `NotifyFocus` (`0x0200`)
Called by the host to indicate that the core gained or lost UI focus. When not focused, video may be obscured by a menu, audio may be silenced, and the core will not receive any input.

The core may choose to (but does not have to) pause itself.

One parameter: `1` if the core has gained focus, `0` if the core has lost focus. No results.

### `FileWriteStart` (`0x0300`)
Called by the host before it starts writing a file to the core via the host memory interface.

One parameter: the file ID, defined in `files.json`. No results.

### `FileWriteEnd` (`0x0301`)
Called by the host when it has finished writing the file.

Three parameters:

1. The file ID
2. The total size of the file transferred, in bytes
3. Reserved (0)

No results.

### `FileReadStart` (`0x0302`)
Called by the host before it starts reading a file from the core via the host memory interface.

One parameter: the file ID. One result: the file size in bytes.

### `FileReadEnd` (`0x0303`)
Called by the host when it has finished reading the file.

One parameter: the file ID. No results.


## Core -> Host commands

The `File*` commands allow the core to perform on-demand I/O on files declared with `"on_demand": true` in `files.json`.

All Core -> Host file commands return a status code as their first result word:

* `FileStatusOk = 0`: the command succeeded
* `FileStatusErrInvalidFile = 1`: the specified file is invalid or the operation is not valid for the file
* `FileStatusErrIo = 2`: an I/O error occurred
* `FileStatusErrBounds = 3`: requested size or `offset + length` violates `exact_size` or `max_size` bounds

### `FileGetSize` (`0x0400`)
Called by the core to get the size (in bytes) of an on-demand file.

One parameter:

1. The file ID (as defined in `files.json`)

Three results:

1. Status (`FileStatus*`)
2. Lower 32 bits of the file size, in bytes
3. Upper 32 bits of the file size, in bytes

### `FileSetSize` (`0x0401`)
Called by the core to resize an on-demand file. May shrink (truncate) or grow (zero-fill) the file. The file must not be `read_only`.

Three parameters:

1. The file ID (as defined in `files.json`)
2. Lower 32 bits of the new size, in bytes
3. Upper 32 bits of the new size, in bytes

One result:

1. Status (`FileStatus*`)

### `FileRead` (`0x0402`)
Called by the core to read data from a file into core memory (via the host memory interface).

Attempting to read past the end of the file will lead to a smaller number of bytes read, but the command will still return `FileStatusOk`.

The host writes the data over `host.mem` before raising `done`, so the core's memory interface must remain responsive while waiting for `done`.

Note that there is a performance penalty when switching between different files with `FileRead` and `FileWrite`: for best performance, do as much I/O on one file as possible before switching to another.

Five parameters:

1. The file ID (as defined in `files.json`)
2. Core memory destination address
3. Lower 32 bits of the file offset, in bytes
4. Upper 32 bits of the file offset, in bytes
5. Number of bytes to read

Two results:

1. Status (`FileStatus*`)
2. Number of bytes transferred

### `FileWrite` (`0x0403`)
Called by the core to write data from core memory into a file (via the host memory interface). The file must not be `read_only`.

The host reads the data over `host.mem` before raising `done`, so the core's memory interface must remain responsive while waiting for `done`.

Note that there is a performance penalty when switching between different files with `FileRead` and `FileWrite`: for best performance, do as much I/O on one file as possible before switching to another.

Five parameters:

1. The file ID (as defined in `files.json`)
2. Core memory source address
3. Lower 32 bits of the file offset, in bytes
4. Upper 32 bits of the file offset, in bytes
5. Number of bytes to write

Two results:

1. Status (`FileStatus*`)
2. Number of bytes transferred

### `FileFlush` (`0x0404`)
Called by the core to flush buffered writes for a file to the microSD card.

Note that the host will already persist writes when exiting the core or powering off. However, this command provides some additional guarantees in case of sudden power loss or crash.

One parameter:

1. The file ID (as defined in `files.json`)

One result:

1. Status (`FileStatus*`)
