!!! warning "The framework is still under development"

    The documentation in this section refers to the Game Bub Core Framework
    as of `v1.1-beta`. The framework is not finalized, and may change
    based on developer feedback.

# Packaging

The output of `./mill root.buildCore` is a `.bit` file (FPGA bitstream) for the target you chose. For example, `DemoCore-gamebub_rev4.bit`.

To allow Game Bub to use your core, you have to package the `.bit` file with some metadata `.json` files, and place them on the microSD card in the appropriate location.

A core named `Demo.DemoCore` would be placed in `/cores/Demo.DemoCore/`.

## Metadata Files

Let's take a look at the metadata files used in [the example core](https://github.com/gamebub/core-example).

For full documentation about metadata files, see [Reference: Metadata](reference-metadata) section.

The only required file is `core.json`, which provides basic information about your core and its bitstreams.

``` json title="core.json"
{
	"min_firmware": "1.1.0",
	"metadata": {
		"id": "Demo.DemoCore",
		"name": "Demo Core",
		"author": "Demo"
	},
	"bitstreams": [
		{"target": "gamebub_rev4", "filename": "DemoCore-gamebub_rev4.bit"}
	]
}
```

`min_firmware` specifies the minimum handheld firmware version required to run the core.

The `metadata` section gives the `id` of the core (a short name, of the format `Author.Name`), the user-visible `name`, and the user-visible `author`. There are other available keys for providing other information.

The `bitstreams` section is a list of available bitstreams and the targets they're built for. Each hardware product and revision needs its own bitstream, for example, `gamebub_rev4`, which represents the horizontal Game Bub rev4, sold commercially.

One optional file is `settings.json`, which allows your core to have user-adjustable settings.

``` json title="settings.json"
{
	"settings": [
		{
			"id": 1,
			"label": "Paddle Color",
			"address": "0x00001000",
			"type": "list",
			"items": [
				{"label": "White", "value": "0xFFFFFF"},
				{"label": "Red",   "value": "0xFF0000"},
				{"label": "Green", "value": "0x00FF00"},
				{"label": "Blue",  "value": "0x0000FF"}
			],
			"default": "0xFFFFFF"
		}
	]
}
```

This example core has a single setting, "Paddle Color", with a list of options. On core load, and when a user selects a new option in the in-game settings menu, the `value` for the option is written to the `address` using the `HostV0` memory interface.

## Core Directory

Once your core is packaged (and published as a GitHub release), you can list it in the [Game Bub Core Directory](https://cores.gamebub.net/).

To add your core, open a pull request adding your repository to `repos.toml` in [gamebub/core-directory](https://github.com/gamebub/core-directory):

```toml
[[repos]]
repo = "owner/repo-name"
```

Once merged, the directory automatically tracks your latest GitHub Release.

### Validation

Even if your core loads and runs fine on Game Bub, the directory enforces a few extra publishing requirements and rejects cores that don't meet them:

* **Must be a published, stable GitHub Release:** Drafts and pre-releases (`prerelease: true`) are ignored. Only your latest valid release is indexed.
* **Strict `.zip` layout:** `core.json` must sit at the root of the archive as `<Core ID>/core.json` or `cores/<Core ID>/core.json`. Multiple cores may be packaged in one `.zip`.
* **`metadata.id` naming:** Must follow `Author.CoreName`, and may not be a reserved ID (such as `GameBub.*`)
* **`metadata.version` is required:** Optional on the handheld, but required for the directory
* **Optional metadata is validated strictly:** Optional fields (like `description`, `url`) must be valid if present

When you open a PR to `repos.toml`, CI runs a dry-run sync against your repository and reports any validation warnings in the workflow summary.
