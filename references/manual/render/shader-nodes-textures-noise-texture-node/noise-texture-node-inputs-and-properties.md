# Noise Texture Node: Inputs, Properties

### Inputs

Which inputs appear is dynamic: they show up only as the node properties call for them.

Vector
Where the noise is evaluated; with nothing plugged in it falls back to Generated coordinates.

W
Coordinate at which to evaluate the noise.

Scale
Scale of the base noise octave.

Detail
How many noise octaves there are. A fractional figure blends between counts — a Detail of 2.5, say, gives a 50% mix of 2 and 3 octaves.

Roughness
Slides between smoother noise and rougher noise with sharper peaks.

Lacunarity
The scale gap between any two neighbouring octaves. Larger values push higher octaves to larger scales.

Offset
An offset added to every octave; it sets the level at which the top octave shows up.

Gain
An extra multiplier for fine-tuning octave magnitude.

Distortion
Amount of distortion.

### Properties

Dimensions
Which space the noise is evaluated in.

1D :

Evaluate the noise in 1D space at the input W .

2D :

Evaluate the noise in 2D space at the input Vector . The Z component is ignored.

3D :

Evaluate the noise in 3D space at the input Vector .

4D :

Evaluate the noise in 4D space, using the input Vector plus the input W as the fourth dimension.

Note

Higher dimensions cost more render time, so stay with lower ones unless you genuinely need more.

Type
Type of Noise texture, with different ways to combine octaves.

fBM :

Fractal Brownian motion: a uniform, isotropic result. Octave values are summed.

Multifractal :

Choppier, varying by location like real terrain. Octave values are multiplied.

Hybrid Multifractal :

Peaks and valleys of varying roughness, the way real mountains lift out of flat plains. Combines octaves through both addition and multiplication.

Ridged Multifractal :

Sharp peaks. It takes the absolute value of the noise to carve "canyons", then flips the surface upside down.

Hetero Terrain :

Like Hybrid Multifractal, a heterogeneous terrain, but suggestive of river channels.

Normalize fBM
On, it keeps the output within 0.0 to 1.0. Off, the range runs at most -( Detail + 1) to Detail + 1 (narrower if Roughness < 1).

[Related references](INDEX.md).
