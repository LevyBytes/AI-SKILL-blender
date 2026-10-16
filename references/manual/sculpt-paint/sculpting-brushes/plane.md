# Plane

## Plane

### Plane

Reference

Mode:
Sculpt Mode

Brush:
Sidebar ‣ Tool ‣ Brush Settings ‣ Advanced ‣ Brush Type

Flatten or raise geometry relative to virtual plane.

### Brush Settings

### General

Note

More info at General brush settings
and on Advanced brush settings.

### Unique

Height
Controls influence reach above the plane.
Higher values affect vertices positioned further up.

Depth
Controls influence reach below the plane.
Higher values affect vertices positioned further down.

Inversion Mode
Dictates brush action when inverted.

Invert Displacement
When inverted, geometry moves away from the plane, increasing definition.

Swap Height and Depth
When inverted, Height and Depth roles reverse.

As an example, if Height equals 0.7 and Depth 0.3, inversion causes
effective Height of 0.3 and Depth of 0.7.

Stabilize Normal
Governs plane orientation consistency. The plane normal gets averaged across recent
steps, with quantity and blend factor set by this value.

At 0, orientation updates immediately.

At 1, orientation remains static throughout.

Intermediate settings create gradual transitions via weighted moving average of
surface normals.

Stabilize Plane
Governs plane position consistency. Functions as Stabilize Normal by averaging
position across prior steps.

Position is calculated as interpolation between unstabilized placement and projection
onto the prior step's plane.

[Related references](INDEX.md).
