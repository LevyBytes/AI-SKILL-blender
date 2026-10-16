# Vertex Weight Proximity Modifier: Falloff, Influence, Example

### Falloff

Type
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

### Influence

All three Vertex Weight modifiers hold these settings in common;
see the Vertex Weight Edit modifier page for the rest.

### Example

The example below drives a Wave modifier on the fly through a vertex group
whose values come from distance to a target object:

The blend-file,
`TEST_1` scene.

[Related references](INDEX.md).
