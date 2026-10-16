# Vertex Weight Edit Modifier: Options, Falloff

## Vertex Weight Edit Modifier

### Vertex Weight Edit Modifier

This modifier's job is to edit the weights a vertex group holds.

Broadly, here is what it runs through for each vertex:

- (Optional) Does the mapping, either through one of the built-in functions or a custom mapping curve.

- Brings the influence factor to bear, optionally alongside the vertex group or texture mask
(0.0 keeps the original weight, 1.0 takes the fully mapped weight).

- Writes the weight back onto the vertex, and may optionally drop the vertex
from the group when its weight falls below a set threshold, or add it when its weight climbs above one.

Important

Weight values get implicitly clamped by this modifier into the usual (0.0 to 1.0) span.
Anything under 0.0 snaps to 0.0, and anything over 1.0 snaps to 1.0.

Note

The reworked weights can be inspected in Weight Paint Mode.
By the same token, you'll need to switch off the Vertex Weight Edit modifier
to see the vertex group's original weights as you edit them.

### Options

The Vertex Weight Edit modifier panel.

Vertex Group
The vertex group that gets affected.

Default Weight
The weight handed by default to every vertex outside the given vertex group.

Group Add
Pulls vertices whose final weight tops Add Threshold into the vertex group.

Group Remove
Drops vertices whose final weight sits under Remove Threshold from the vertex group.

Normalize Weights
Rescales the vertex group's weights so their relative spacing holds
while the lowest and highest values stretch across the full 0 - 1 range.

### Falloff

Falloff Type
The kind of mapping used.

Linear
No mapping applied.

Custom Curve
Lets you shape the mapping yourself with a curve.

Sharp, Smooth, Root and Sphere
The standard mapping functions, running from spikiest through to roundest.

Random
Hands each vertex a random value.

Median Step
Produces binary weights (0.0 or 1.0), splitting at 0.5.

Invert
Turns the falloff inside out.

[Related references](INDEX.md).
