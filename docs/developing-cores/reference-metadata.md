!!! warning "The framework is still under development"

    The documentation in this section refers to the Game Bub Core Framework
    as of `v1.1-beta`. The framework is not finalized, and may change
    based on developer feedback.

# Reference: Metadata

When reading a core from the microSD card at `/cores/<core id>`, the host MCU reads core metadata from the following JSON files:

* `core.json`: Info, bitstreams, and hardware requirements (**Required**)
* `files.json`: Files to read/write/persist between the microSD card and the core (*Optional*)
* `settings.json`: User-configurable core settings and actions (*Optional*)

## `core.json`

Contains top-level information about the core and a list of FPGA bitstream files.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `metadata` | Object | **Required** | Core information |
| `metadata.id` | String | **Required** | Unique core identifier (e.g. `"Demo.DemoCore"`), max 32 chars |
| `metadata.name` | String | **Required** |Human-readable core name, max 32 chars |
| `metadata.author` | String | **Required** | Human-readable core author, max 32 chars |
| `metadata.version` | String | `null` | Human-readable version code, max 16 chars |
| `metadata.release_date` | String | `null` | Release date, `"YYYY-MM-DD"` |
| `metadata.url` | String | `null` | URL to website with information, max 64 chars |
| `metadata.license` | String | `null` | SPDX license identifier, max 32 chars |
| `bitstreams` | Array | **Required** | List of bitstream paths / targets |
| `bitstreams[].target` | String | **Required** | Target hardware for the bitstream (e.g. `gamebub_rev4`) |
| `bitstreams[].filename` | String | **Required** | Filename of the bitstream, max 32 chars, ends with `.bit` |
| `hardware` | Object | `{}` | Hardware flags |
| `hardware.cartridge_enable` | String | `"no"` | Whether the cartridge slot should be enabled (`"no"`, `"yes"`, `"if_selected"`) |
| `hardware.cartridge_selectable` | Boolean | `false` | Whether the user can select "Run Cartridge" |

### Example

``` json
{
  "metadata": {
    "id": "Demo.DemoCore",
    "name": "Demo Core",
    "author": "Demo",
    "version": "1.0.0",
    "license": "CERN-OHL-W-2.0",
  },
  "bitstreams": [
    { "target": "gamebub_rev4", "filename": "DemoCore-rev4.bit" },
    { "target": "gamebub_rev2", "filename": "DemoCore-rev2.bit" }
  ]
}
```

## `files.json`

Optional. Defines data files (e.g. ROMs, save files, assets) that need to be loaded into and/or saved out of the core.

A maximum of 8 files may be defined.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `files` | Array | **Required** | List of files, max 8 entries |
| `files[].id` | Integer | **Required** | File ID (`0` to `65535`) |
| `files[].label` | String | **Required** | Human-readable file label, max 16 chars |
| `files[].filename` | String | `null` | Optional fixed path relative to the core directory, max 32 chars |
| `files[].extensions` | Array | `[]` | File extensions for the file, max 4 items, max 8 chars each |
| `files[].optional` | Boolean | `true` | Whether the core will run if the file is missing |
| `files[].read_only` | Boolean | `false` | If `true`, changes will not be saved back to the microSD card |
| `files[].user_selected` | Boolean | `false` | Whether the user is prompted to choose the file |
| `files[].dependent_on_0` | Boolean | `false` | Whether the path is derived from File 0 (see below) |
| `files[].initialize` | Boolean | `false` | If `true` and the file is missing, memory is initialized with `0xFF` |
| `files[].address` | Hex | **Required** | Memory-mapped target base address in core memory |
| `files[].max_size` | Hex | `0` | Maximum allowed file size in bytes (`0` = no limit) |
| `files[].exact_size` | Hex | `0` | Exact required file size in bytes (`0` = no check) |
| `files[].max_transfer_speed` | Integer | `5000` | Maximum transfer rate in KB/s |

Any field marked as "Hex" is either a JSON number or a hexadecimal string, e.g. `"0x0000ABCD"` or `43981`.

If a file has ID 0, it is treated specially. If "Run Cartridge" is selected, neither File 0 nor any file dependent on File 0 will be loaded.

If a file is *dependent* on File 0 (and File 0 is loaded), it will derive its path from File 0, with the first (and only) extension in `extensions` used as its file extension. For example, if File 0 resolves to `/some-path/data.bin`, and its `extensions` is `["sav"]`, the File will be loaded from the path `/some-path/data.sav`.

If a file is given a `filename`, it will be loaded from that filename relative to the core directory. E.g. with a `filename` of `asset.bin`, it could be loaded from `/cores/Demo.DemoCore/asset.bin`.

During core setup, for each file selected (or `0xFF`-initialized):

* `FileWriteStart` command
* The file is written to `address` across the Host memory interface
* `FileWriteEnd` command

Similarly, during core exit, for each file that was loaded (except `read_only` files):

* `FileReadStart` command
* The file is read from `address` across the Host memory interface
* `FileReadEnd` command

### Example

```json
{
  "files": [
    {
      "id": 0,
      "label": "ROM",
      "extensions": ["bin"],
      "user_selected": true,
      "optional": false,
      "read_only": true,
      "address": "0x30000000",
      "max_size": "0x800000"
    },
    {
      "id": 1,
      "label": "Save",
      "extensions": ["sav"],
      "user_selected": false,
      "dependent_on_0": true,
      "optional": true,
      "initialize": true,
      "address": "0x40000000",
      "max_size": "0x10000"
    },
    {
      "id": 2,
      "label": "BIOS",
      "filename": "bios.bin",
      "optional": false,
      "read_only": true,
      "address": "0x10000000",
      "exact_size": "0x100"
    }
  ]
}
```

## `settings.json`

Optional. Defines user-configurable settings, set by the user in the in-core menu. A maximum of 16 settings may be defined.

Settings are written to the core (via the host memory interface) both during setup and whenever the user changes them. Settings are persisted when the core exits.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `settings` | Array | **Required** | List of settings, max 16 entries |
| `settings[].id` | Integer | **Required** | Setting ID (`0` to `65535`) |
| `settings[].label` | String | **Required** | Human-readable setting name |
| `settings[].address` | Hex | **Required** | Memory address (in core) to write setting value |
| `settings[].mask` | Hex | `0` | Mask applied when modifying setting |
| `settings[].default` | Hex | `0` | Default value for the setting |
| `settings[].type` | String | **Required** | Type of setting (see below) |

Any field marked as "Hex" is either a JSON number or a hexadecimal string, e.g. `"0x0000ABCD"` or `43981`.

When a setting is written to the core, it is written as a single 32-bit access over the host memory interface. If `mask` is not `0`, the address is first read, then ANDed with the mask, and then ORed with the new value. This allows multiple settings to be crammed into the same 32-bit register. 

### Setting Types

**`"list"`**

A list of choices, each with a label and associated value:

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `settings[].items` | Array | **Required** | List of selection choices, max 8 items (required when `type` is `"list"`) |
| `settings[].items[].label` | String | **Required** | Human-readable label for this list option |
| `settings[].items[].value` | Hex | **Required** | Value written to `address` when this option is selected |

**`"action"`**

A button, which writes `value` every time it is selected. Not *exactly* a setting.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `settings[].value` | Hex | **Required** | Value written when activated |

**`"checkbox"`**

A yes/no checkbox. When checked, writes `value`. When not checked, writes `0`.

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `settings[].value` | Hex | **Required** | Value written when checked |

### Example

```json
{
  "settings": [
    {
      "id": 0,
      "label": "Reset Core",
      "address": "0x004",
      "type": "action",
      "value": "0x1"
    },
    {
      "id": 1,
      "label": "Slow Mode",
      "address": "0x008",
      "default": "0x0",
      "type": "checkbox",
      "value": "0x1"
    },
    {
      "id": 2,
      "label": "Paddle Color",
      "address": "0x100",
      "default": "0xFFFFFF",
      "type": "list",
      "items": [
        { "label": "White", "value": "0xFFFFFF" },
        { "label": "Red",   "value": "0xFF0000" },
        { "label": "Green", "value": "0x00FF00" }
      ]
    }
  ]
}
```
