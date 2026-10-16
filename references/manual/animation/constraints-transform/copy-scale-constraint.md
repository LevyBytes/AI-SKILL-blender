# Copy Scale Constraint

## Copy Scale Constraint

The Copy Scale constraint forces an object or bone to match a target's scale. Options: Target (the object or bone whose scale to copy); Axis (which axes to copy); Power (raise the target's scales to this power, before Offset); Make Uniform (instead of per-axis scaling, apply a single uniform scale to all axes that gives the same volume change); Offset (when on, the target's current scale is multiplied with the owner's original scale from preceding constraints rather than copied over); Additive (with Offset on, add the owner's scales minus 1 rather than multiplying — kept for backwards compatibility, generally pointless and best unused); Target/Owner (the spaces for reading scales and applying them); and Influence. Tips: depending on the settings, Power can give a better-looking result than Influence; and to copy one target axis's scale to all the owner's axes, disable the other axes, enable Make Uniform, and set Power to 3.

[Related references](INDEX.md).
