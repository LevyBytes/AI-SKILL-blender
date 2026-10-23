# Noise Texture Node

## Noise Texture Node

The Noise Texture node samples a fractal Perlin noise at the input texture coordinates. Use it for a single Perlin evaluation, or to stack multiple octaves (layers) of progressively finer detail.

Inputs (dynamic: they appear as the node's properties require them):
Vector: coordinate to sample the noise at; an unconnected socket defaults to Generated texture coordinates.
W: coordinate to sample the noise at.
Scale: scale of the base noise octave.
Detail: number of noise octaves; a fractional value blends (for example, a Detail of 2.5 gives a 50% blend between 2 and 3 octaves).
Roughness: shifts between a smoother pattern and a rougher one with sharper peaks.
Lacunarity: the scale gap between each pair of consecutive octaves; larger values make higher octaves larger in scale.
Offset: an offset added to each octave, setting the level at which the highest octave appears.
Gain: an extra multiplier for tuning the magnitude of octaves.
Distortion: amount of distortion.

Properties:
Dimensions: the space the noise is evaluated in.
- 1D: in 1D space at the input W.
- 2D: in 2D space at the input Vector; the Z component is ignored.
- 3D: in 3D space at the input Vector.
- 4D: in 4D space at the input Vector with the input W as the fourth dimension.
Note: higher dimensions raise render time, so keep to lower dimensions unless higher ones are necessary.
Type: the Noise texture variety, differing in how octaves combine.
- fBM: fractal Brownian motion — homogeneous and isotropic; octave values are added together.
- Multifractal: more uneven and location-dependent, akin to real terrain; octave values are multiplied together.
- Hybrid Multifractal: peaks and valleys with varying roughness, like real mountains rising from flat plains; combines octaves by both addition and multiplication.
- Ridged Multifractal: sharp peaks — takes the absolute value of the noise to carve "canyons," then flips the surface upside down.
- Hetero Terrain: like Hybrid Multifractal, a heterogeneous terrain but with the likeness of river channels.
Normalize fBM: when enabled, keeps output within 0.0 to 1.0; when disabled, the range reaches at most -(Detail + 1) to Detail + 1 (narrower if Roughness < 1).

Outputs:
Factor: value of the fractal noise.
Color: a color carrying different fractal noise in each component.

Notes: although the noise is random in nature, it follows a pattern that may not yield random values in some setups. Consider a grid of objects whose material samples a noise texture at each object's location — you might expect random values from the differing locations, but you won't get them: every object reads 0.5. The reason appears in a plot of 1D noise with zero detail and zero distortion: with a noise scale of 1, the curve always crosses the 0.5 line at whole numbers, and since the objects sit on a grid at whole-number locations they all evaluate to 0.5. In general, any discrete sampling of noise at integer multiples of the reciprocal of the noise scale lands on 0.5, and samples near those points land close to 0.5; in such cases the White Noise Texture is almost always preferable. You can also work around it by: adjusting the noise scale so it doesn't align with the evaluation domain; adding an arbitrary offset to the texture coordinates to break that alignment; or evaluating the noise in a higher dimension and tuning the extra dimension until the result looks right. A related artifact is banding — alternating bands of high- and low-contrast noise — seen, for example, on planar surfaces slightly tilted along one axis: the slight tilt makes values along the perpendicular axis change very slowly, exposing the noise's grid structure; rotating the coordinates by an arbitrary amount is the easiest fix.

Note: this node is ported from shader nodes, so the manual and images reference the shader version of the node. It accepts field inputs and outputs, and when the Vector input is unconnected it carries an implicit position attribute value.

The Noise Texture node samples a fractal Perlin noise at the input texture coordinates. Use it for a single Perlin evaluation, or to combine multiple octaves (layers) of progressively finer detail.

Inputs (dynamic: they appear as the node's properties require them):
Vector: coordinate to sample the noise at; an unconnected socket defaults to Generated texture coordinates.
W: coordinate to sample the noise at.
Scale: scale of the base noise octave.
Detail: number of noise octaves; the input's fractional part is multiplied by the magnitude of the highest octave, and more octaves mean longer render time.
Roughness: shifts between a smoother pattern and a rougher one with sharper peaks.
Lacunarity: the scale gap between each pair of consecutive octaves; larger values make higher octaves larger in scale.
Offset: an offset added to each octave, setting the level at which the highest octave appears.
Gain: an extra multiplier for tuning the magnitude of octaves.
Distortion: amount of distortion.

Properties:
Dimensions: the space the noise is evaluated in.
- 1D: in 1D space at the input W.
- 2D: in 2D space at the input Vector; the Z component is ignored.
- 3D: in 3D space at the input Vector.
- 4D: in 4D space at the input Vector with the input W as the fourth dimension.
Note: higher dimensions raise render time, so keep to lower dimensions unless higher ones are necessary.
Normalize: when enabled, keeps output values within 0.0 to 1.0; when disabled, output values land in the range -1.0 to 1.0.
Type: the Noise texture variety, differing in how octaves combine.
- FBM: fractal Brownian motion — homogeneous and isotropic; octave values are added together.
- Multifractal: more uneven and location-dependent, akin to real terrain; octave values are multiplied together.
- Hybrid Multifractal: peaks and valleys with varying roughness, like real mountains rising from flat plains; combines octaves by both addition and multiplication.
- Ridged Multifractal: sharp peaks — takes the absolute value of the noise to carve "canyons," then flips the surface upside down.
- Hetero Terrain: like Hybrid Multifractal, a heterogeneous terrain but with the likeness of river channels.

Outputs:
Factor: value of the fractal noise.
Color: a color carrying different fractal noise in each component.

Notes: although the noise is random in nature, it follows a pattern that may not yield random values in some setups. Consider a grid of objects whose material samples a noise texture at each object's location — you might expect random values from the differing locations, but you won't get them: every object reads 0.5. The reason appears in a plot of 1D noise with zero detail and zero distortion: with a noise scale of 1, the curve always crosses the 0.5 line at whole numbers, and since the objects sit on a grid at whole-number locations they all evaluate to 0.5. In general, any discrete sampling of noise at integer multiples of the reciprocal of the noise scale lands on 0.5, and samples near those points land close to 0.5; in such cases the White Noise Texture is almost always preferable. You can also work around it by: adjusting the noise scale so it doesn't align with the evaluation domain; adding an arbitrary offset to the texture coordinates to break that alignment; or evaluating the noise in a higher dimension and tuning the extra dimension until the result looks right. A related artifact is banding — alternating bands of high- and low-contrast noise — seen, for example, on planar surfaces slightly tilted along one axis: the slight tilt makes values along the perpendicular axis change very slowly, exposing the noise's grid structure; rotating the coordinates by an arbitrary amount is the easiest fix.

### Noise Texture Node

This node evaluates fractal Perlin noise at the texture coordinates you feed in. Use it for a single Perlin evaluation, or to stack several octaves (layers) of ever-finer detail.

[Related references](INDEX.md).
