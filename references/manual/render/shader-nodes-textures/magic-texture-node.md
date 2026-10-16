# Magic Texture Node

## Magic Texture Node

The Magic Texture node adds a psychedelic color texture — usable for "thin film interference" by assigning a Reflection Texture Coordinate to the Vector input with a relatively high Turbulence — generating the RGB components independently with a sine formula. Inputs: Vector (the coordinate to sample at, defaulting to Generated coordinates if unconnected); Scale (the texture scale); and Distortion (the amount of distortion). Properties: Depth (the number of iterations). Outputs: Color (the texture color) and Factor (the texture intensity).

Magic Texture Node

Note: Ported from shader nodes; manual references shader version. Accepts field inputs/outputs. Vector defaults to implicit position.

Produces psychedelic color texture.

Inputs
Vector: Sample coordinate; defaults to Generated if unconnected.
Scale: Texture scale.
Distortion: Distortion amount.

Properties
Depth: Number of iterations.

Outputs
Color: Texture color output.
Factor: Texture intensity output.

Examples: Magic texture with Depth 10, Distortion 2.0.

### Magic Texture Node

This node lays down a psychedelic colour texture. Feed a Reflection Texture Coordinate into Vector and crank the Distortion fairly high and you get a "Thin Film Interference" look. Each RGB component is generated on its own from a sine formula.

### Inputs

Vector
Where the texture is sampled; with nothing plugged in it falls back to Generated coordinates.

Scale
Scale of the texture.

Distortion
Amount of distortion.

### Properties

Depth
Number of iterations.

### Outputs

Color
Texture color output.

Factor
Texture intensity output.

### Examples

Magic texture: Depth 10, Distortion 2.0.

[Related references](INDEX.md).
