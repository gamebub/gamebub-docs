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
			]
		}
	]
}
```

This example core has a single setting, "Paddle Color", with a list of options. On core load, and when a user selects a new option in the in-game settings menu, the `value` for the option is written to the `address` using the `HostV0` memory interface.
