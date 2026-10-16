# Gabor Texture Node: Properties, Outputs, Examples

### Properties

Type
Type of Gabor noise texture.

2D :

Evaluates the noise in 2D space; the Z component of the input vector is dropped.

3D :

Evaluates the noise in 3D space.

Note

Higher dimensions cost more render time, so stay with lower ones unless you genuinely need more.

### Outputs

Value
The Gabor noise value, carrying both a random intensity and a random phase. It equals the sine of the phase times the intensity.

Phase
The phase of the Gabor noise, which carries no random intensity.

Intensity
The intensity of the Gabor noise, which carries no random phase.

### Examples

The table below shows the node's output under various parameters. As you can see, the noise reads as interleaved bands generally pointing one way. Drop Anisotropy below 1 to make those band directions more random. Frequency sets how many bands run perpendicular to the noise direction. Scale can also globally raise the band count, so try bumping the scale first, since high-frequency noise tends to suffer from low contrast and poorly interleaved bands.

| Value output. Frequency = 2. Anisotropy = 1. | Phase output. Frequency = 2. Anisotropy = 1. | Intensity output. Frequency = 2. Anisotropy = 1. |
| --- | --- | --- |
| Value output. Frequency = 3. Anisotropy = 1. | Phase output. Frequency = 3. Anisotropy = 1. | Intensity output. Frequency = 3. Anisotropy = 1. |
| Value output. Frequency = 2. Anisotropy = 0.7. | Phase output. Frequency = 2. Anisotropy = 0.7. | Intensity output. Frequency = 2. Anisotropy = 0.7. |

Gabor noise splits into a Phase and an Intensity part; the Gabor value emerges as sine-of-phase scaled by intensity, while the phase result is rescaled to span [0, 1].

Compute the value output from the phase and intensity outputs.

The Phase output's advantage is that it has no random intensities and none of the low-contrast patches you get in the value output, so it works as a base for more structured textures like sand dunes.

Sand dune-like structures creates using the phase output.

Mostly, the Intensity output earns its keep by pinpointing where singularities sit in the Phase output. Those singularities are the spots at which bands converge — picked out in red in the figure below — and the Intensity output dips toward zero right there. To suppress them, multiply through by some reworked form of that output.

Visualization of the areas where singularities happen.

Varying the inputs across space yields more interesting patterns.

Varying the frequency and orientation across space.

[Related references](INDEX.md).
