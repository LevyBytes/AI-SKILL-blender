# Editing Masks: Transform, Clear Feather Weight, Toggle Cyclic

## Editing Masks

### Editing Masks

Whichever of the two editors you happen to be in, mask editing uses the same panels and tools.
Working with mask splines plays out much like editing Bézier curves or paths in GIMP and similar curve editors.

Tip

For live feedback on how the mask turns out,
wire a Mask node straight into a Viewer node in the Compositor,
and the compositing result will refresh as you edit.

### Transform

Reference

Mode :

Mask Mode

Menu :

Mask ‣ Transform

Move G
Shifts control points to a new location. You can also drag control points with LMB .
Drag the center dot with LMB to move the whole spline at once.

Rotate R
Repositions control points by turning them around a pivot point.

Scale S
Repositions control points by widening or narrowing the gaps between them.

To Sphere Shift - Alt - S
Bends the control points into the shape of a circle.

Shear Shift - Ctrl - Alt - S
Slides control points along a chosen axis so that parallel ones slip past each other.

Push/Pull
Draws the control points nearer together (Push) or pushes them apart (Pull).

Scale Feather Alt - S
Resizes the feather.

### Clear Feather Weight

Reference

Mode :

Mask Mode

Menu :

Mask ‣ Clear Feather Weight

Drops the feather weight back to zero.

### Toggle Cyclic

Reference

Mode :

Mask Mode

Menu :

Mask ‣ Toggle Cyclic

Shortcut :

Alt - C

Flip between a closed curve and an open one.
Closing the mask ties the final control point back to the first.

[Related references](INDEX.md).
