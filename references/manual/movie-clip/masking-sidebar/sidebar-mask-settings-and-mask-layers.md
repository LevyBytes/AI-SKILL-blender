# Sidebar: Mask Settings, Mask Layers, Example, Active Spline

## Sidebar

### Sidebar

### Mask Settings

Start Frame, End Frame
Pin down the mask's frame range for the Sequencer .

### Mask Layers

Mask Layer panel.

A mask layer collects one or more splines so that operations treat them as a single group.
With layers you can build up complex shapes and set how the splines play off one another.
Splines sharing a layer can be animated as a unit — driven, say, by an item
from motion tracker footage.
Such tooling might parent the whole batch of splines to a single piece of motion tracking data, or
simply transform them all at once.

Opacity
Dials in how opaque the mask layer is.

Invert
Flips the values (colors) of the mask layer.

Blend
Which blending operation the layer performs. See Color Blend Modes.

Modes Merge Add and Merge Subtract
hold up better than plain mathematical addition and subtraction
when a Feather is in play on overlapping masks.

Falloff
Which Feather falloff type to use; it shapes how the transition from black to white runs.

Overlap
Fills in the areas where the spline crosses itself.

Holes
Splines that overlap within the same layer will punch holes into the mask.

| Description | Description |
| --- | --- |
| The Overlap option example. | The Holes option example. |

### Example

A concrete scenario makes the point of mask layers clearer.
Imagine the footage has two people you'd rather hide, one walking left to right and
the other heading the opposite way. Put each on its own mask layer, both within
one mask data-block, and you can mask them separately. Where the two shapes cross, they add together rather than
punching a hole: which is what would happen if they shared a layer. When the motion is straightforward enough,
one motion-tracked point can drive the whole mask layer's position.

### Active Spline

Active Spline panel.

Feather Offset
Which method works out the offset of the mask spline's feather.

Even :

Holds the feather's thickness steady, though it can throw unwanted loops into the feather curve.

Smooth :

Produces a cleaner, smoother shape,
yet may leave an unwanted sharp feather wherever a curve segment bends into an S.

Weight Interpolation
Which way the weight (feather thickness) is interpolated from one point to the next —
Linear or Ease (that is, the change eases in slowly at the start and the end).

Cyclic
Whether the spline is closed or left open.

Fill
Builds splines with their interiors filled in.
Switch it off and Blender draws curves with a thickness instead, to mask thin objects like wires or hair.

Self Intersection Check
Keeps the feather (not the curve itself) from crossing over itself.

[Related references](INDEX.md).
