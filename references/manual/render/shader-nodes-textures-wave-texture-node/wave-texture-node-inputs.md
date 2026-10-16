# Wave Texture Node: Inputs

## Wave Texture Node

The Wave Texture node makes procedural bands or rings carrying noise distortion. Inputs: Vector (the coordinate to sample at, defaulting to Generated coordinates if unconnected); Scale (overall texture scale); Distortion (the wave's distortion amount — and a hint notes that, like distorting any texture by mixing its coordinates with another, the built-in distortion uses the Noise Texture Node's Color output, replicable by centering that range on zero, multiplying by a factor proportional to Distortion / Scale, and adding it to the coordinates, with Detail, Detail Scale, and Roughness here matching the Noise Texture Node's inputs); Detail (the distortion-noise detail); Detail Scale (the distortion-noise scale); Roughness (blend between smoother and rougher with sharper peaks); and Phase Offset (the wave's position along the Bands Direction, usable as an input for more distortion control). Properties: Type (Bands or Rings); Bands/Rings Direction (the axis the bands or rings are perpendicular to — Bands allow a Diagonal axis, Rings allow Spherical to radiate from a point); and Wave Profile (the wave's look — Saw, a sawtooth, or Sine, the standard sine). Outputs: Color (the texture color) and Factor (the texture intensity).

Wave Texture Node

Note: Ported from shader nodes; manual references shader version. Accepts field inputs/outputs. Vector defaults to implicit position.

Produces procedural bands or rings with noise distortion.

Hint: Textures distort by mixing coordinates with another texture. Wave uses Noise Color for built-in distortion. To replicate: zero-center the noise value, multiply by Distortion/Scale, add to coordinates. Wave Detail/Detail Scale/Roughness match Noise Texture inputs.

Inputs
Vector: Sample coordinate; defaults to Generated if unconnected.
Scale: Overall texture scale.
Distortion: Wave distortion amount. (See Hint above for replicating the distortion effect.)
Detail: Distortion noise detail amount.
Detail Scale: Distortion noise scale.
Roughness: Smooth to sharp peaks blend.
Phase Offset: Wave position along Bands Direction. Controls distortion.

Properties
Type: Bands or Rings waves.
Bands/Rings Direction: Axis for propagation (perpendicular axis). Bands allow Diagonal. Rings allow Spherical for radial propagation.
Wave Profile: Wave appearance.
  Saw: Sawtooth profile.
  Sine: Standard sine profile.

Outputs
Color: Texture color output.
Factor: Texture intensity output.

Examples: Wave Texture.

### Wave Texture Node

This node lays down procedural bands or rings carrying noise distortion.

### Inputs

Vector
Where the texture is sampled; with nothing plugged in it falls back to Generated coordinates.

Scale
Overall texture scale.

Distortion
Amount of distortion of the wave.

Hint

As a rule, you can distort textures by mixing their coordinates with another texture. The distortion baked into this node uses the Color output of the
Noise Texture Node.

Reproduce it yourself by shifting that output's range so it centres on zero, multiplying through by a factor in proportion to Distortion / Scale , and folding what you get back into the coordinates. On this node, Detail , Detail Scale , and Roughness map straight onto the matching inputs over on the
Noise Texture Node.

Detail
Amount of distortion noise detail.

Detail Scale
Scale of distortion noise.

Roughness
Slides between smoother noise and rougher noise with sharper peaks.

Phase Offset
Position of the wave along the Bands Direction . Use it as an input for finer control over the distortion.

[Related references](INDEX.md).
