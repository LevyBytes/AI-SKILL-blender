# Hair Curves Noise

## Hair Curves Noise

### Hair Curves Noise

Hair Curves Noise deforms strands with procedural noise, yielding believable randomness or turbulence — wind buffeting, wave and curl, or faint groom imperfection.

### Inputs

Geometry
Geometry: the hair-curve geometry fed in for noise deformation.

Cumulative Offset
On, every point's offset takes cues from the points ahead of it along the strand — gentler, continuous bending instead of each point moving on its own.

Factor
The overall punch of the noise deform. At 0.0 the effect is off; at 1.0 the displacement applies fully.

Distance
A multiplier on noise amplitude. Raise it and strands stray farther from their starting shape.

Shape
How the effect changes across the strand. At 0.0 the deform is even; at 0.5 it tapers linearly from root to tip.

Scale
The noise-texture scale relative to each strand's root position. Lower values give broad, smooth waves; higher values give fine detail.

Scale along Curve
Noise frequency running along an individual strand. Higher values pack in tighter, more frequent variation down the hair.

Offset per Curve
Throws a random offset into each strand's noise pattern, so every hair varies.

Seed
The random seed that initializes the noise pattern. Shift it for different random results under the same settings.

Preserve Length
On, each curve segment holds its original length. Off, the noise may stretch or squeeze the curve a touch.

### Outputs

Geometry
Output geometry carrying the noise deform on the hair curves.

Offset Vector
A vector field marking the displacement applied at each point down the strands.

[Related references](INDEX.md).
