# Custom Camera: Metadata, Limitations

### Metadata

Metadata on parameters governs their interface behavior. Supported entries:

[[ string label = "My Label" ]]
Custom display name in the user interface.

[[ string widget = "null" ]]
Conceals the parameter from the interface.

[[ string widget = "boolean" ]] or [[ string widget = "checkbox" ]]
Shows an integer parameter as a checkbox.

[[ string widget = "filename" ]]
Shows the parameter as a file path picker.

[[ string widget = "mapper", string options = "left:0|right:1" ]]
Shows an integer parameter as an enumerated selector. Options contains label-value pairs separated by | .

[[ string vecsemantics = "POINT" ]]
Treats a vector parameter as position (translation).

[[ string vecsemantics = "NORMAL" ]]
Treats a vector parameter as direction (normal).

[[ string unit = "radians" ]]
Designates a float parameter as an angle, shown in radians.

[[ string unit = "m" ]]
Designates a float parameter as distance, shown in meters.

[[ string unit = "mm" ]]
Designates a float parameter as distance, shown in millimeters.

[[ string unit = "s" ]] or [[ string unit = "sec" ]]
Designates a float parameter as time, shown in seconds.

### Limitations

Important

OSL is not supported with GPU rendering unless using the OptiX backend.

When using OptiX, certain OSL capabilities are unavailable:

- Memory optimizations such as on-demand texture loading and mip-mapping are not present.

- Texture operations require OSL to resolve a constant image file path for each lookup.

- Some noise functions absent. Examples: Cell , Simplex , and Gabor .

- The trace function is non-functional.
Due to this, the Ambient Occlusion and Bevel nodes do not work.

[Related references](INDEX.md).
