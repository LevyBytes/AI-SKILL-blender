# Gabor Texture Node: Inputs

## Gabor Texture Node

The Gabor Texture node samples Gabor noise at the supplied texture coordinates. Visually, Gabor noise reads as randomly interleaved bands whose direction and width you can steer. It can also produce omnidirectional noise much like the standard Noise Texture node, but since it costs more to compute, the Noise Texture node is usually the better pick for that purpose — see the examples for more.

Inputs:
Vector: where the Gabor noise is sampled; in the 2D case the Z component is ignored, and an unconnected socket falls back to Generated texture coordinates.
Scale: overall scale of the Gabor noise.
Frequency: how fast the noise varies across space; unlike Scale, it stretches only perpendicular to the noise's direction.
Anisotropy: how directional the noise is: 1 means fully directional, 0 means omnidirectional.
Orientation — the direction of anisotropic noise — an angle in the 2D case, a unit direction vector in the 3D case.

Properties:
Type: the kind of Gabor noise texture.
- 2D: evaluates the noise in 2D space, ignoring the input vector's Z component.
- 3D: evaluates the noise in 3D space.
Note: higher dimensions cost more render time, so prefer lower dimensions unless higher ones are necessary.

Outputs:
Value: the Gabor noise value carrying both random intensity and phase; it equals the sine of the phase multiplied by the intensity.
Phase: the noise phase, without the random intensity.
Intensity: the noise intensity, without the random phase.

Examples: varying the parameters changes the look. The noise shows interleaved bands generally aligned to one direction, and dropping Anisotropy below 1 makes the band directions more random. Frequency sets how many bands run perpendicular to the noise direction, but Scale also raises the band count globally, so try raising Scale first, since high-frequency noise can suffer from low contrast and poorly interleaved bands. Gabor noise decomposes into Phase and Intensity components, with the Gabor value computed as the sine of the phase multiplied by the intensity (the phase output is normalized to the [0, 1] range). The Phase output's advantage is that it carries no random intensities and none of the low-contrast patches seen in the value output, making it a good base for more structured textures such as sand dunes. The Intensity output mainly reveals where singularities sit in the Phase output — the spots where bands meet (shown in red in the manual's figure), which fall near zero in the Intensity output; if those spots are unwanted, hide them by multiplying with a variant of the Intensity output. Inputs can also be varied across space — for instance varying the frequency and orientation — to produce more interesting patterns.

The Gabor Texture node samples Gabor noise at the input texture coordinates. Visually, Gabor noise reads as randomly interleaved bands whose direction and width you can steer. It can also produce omnidirectional noise much like the standard Noise Texture node, but since it costs more to compute, the Noise Texture node is usually the better pick for that purpose — see the examples for more.
Note: this node is ported from shader nodes, so the manual and images reference the shader version of the node. It accepts field inputs and outputs, and when the Vector input is unconnected it carries an implicit position attribute value.

Inputs:
Vector: where the Gabor noise is evaluated; in the 2D case the Z component is ignored, and an unconnected socket falls back to Generated texture coordinates.
Scale: overall scale of the Gabor noise.
Frequency: how fast the noise changes across space; unlike Scale, it stretches only perpendicular to the noise's direction.
Anisotropy: how directional the noise is: 1 means fully directional, 0 means omnidirectional.
Orientation — the direction of anisotropic noise — an angle in the 2D case, a unit direction vector in the 3D case.

Properties:
Type: the kind of Gabor noise texture.
- 2D: evaluates the noise in 2D space, ignoring the input vector's Z component.
- 3D: evaluates the noise in 3D space.
Note: higher dimensions cost more render time, so prefer lower dimensions unless higher ones are necessary.

Outputs:
Value: the Gabor noise value carrying both random intensity and phase; it equals the sine of the phase multiplied by the intensity.
Phase: the noise phase, without the random intensity.
Intensity: the noise intensity, without the random phase.

Examples: varying the parameters changes the look. The noise shows interleaved bands generally aligned to one direction, and dropping Anisotropy below 1 makes the band directions more random. Frequency sets how many bands run perpendicular to the noise direction, but Scale also raises the band count globally, so try raising Scale first, since high-frequency noise can suffer from low contrast and poorly interleaved bands. Gabor noise decomposes into Phase and Intensity components, with the Gabor value computed as the sine of the phase multiplied by the intensity (the phase output is normalized to the [0, 1] range). The Phase output's advantage is that it carries no random intensities and none of the low-contrast patches seen in the value output, making it a good base for more structured textures such as sand dunes. The Intensity output mainly reveals where singularities sit in the Phase output — the spots where bands meet (shown in red in the manual's figure), which fall near zero in the Intensity output; if those spots are unwanted, hide them by multiplying with a variant of the Intensity output. Inputs can also be varied across space — for instance varying the frequency and orientation — to produce more interesting patterns.

### Gabor Texture Node

This node evaluates Gabor noise at the texture coordinates you feed in. Visually, Gabor noise reads as randomly interleaved bands whose orientation and width you can dial in. It can also produce omnidirectional noise the way the regular Noise Texture node does, but it costs more to compute, so the Noise Texture node is usually the smarter pick for that. The examples go into more detail.

### Inputs

Vector
Coordinates where Gabor noise gets evaluated. In the 2D case the Z component is dropped. With nothing plugged in it falls back to Generated coordinates.

Scale
Scale of the Gabor noise.

Frequency
How fast the Gabor noise varies across space. Unlike Scale, it only stretches the noise perpendicular to its direction.

Anisotropy
How directional the Gabor noise is. At 1 the noise is fully directional; at 0 it is omnidirectional.

Orientation
Which way anisotropic Gabor noise points. It is an angle in the 2D case and a unit direction vector in the 3D case.

[Related references](INDEX.md).
