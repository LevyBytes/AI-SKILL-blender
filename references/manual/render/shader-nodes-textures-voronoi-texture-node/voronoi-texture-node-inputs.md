# Voronoi Texture Node: Inputs

### Voronoi Texture Node

This node evaluates a Worley Noise at the texture coordinates you feed in.

### Inputs

Which inputs appear is dynamic: they show up only as the node properties call for them.

Vector
Where the noise is evaluated; with nothing plugged in it falls back to Generated coordinates.

W
Coordinate at which to evaluate the noise.

Scale
Scale of the noise.

Detail
How many noise octaves there are. The fractional part scales the magnitude of the top octave. More octaves mean longer evaluation.

Roughness
Slides between smoother noise and rougher noise with sharper peaks.

Lacunarity
The scale gap between any two neighbouring octaves. Larger values push higher octaves to larger scales.

Smoothness
The smoothness of the noise.

| Smoothness: 0.0. | Smoothness: 0.25. | Smoothness: 0.5. | Smoothness: 1.0. |
| --- | --- | --- | --- |
| Smoothness: 0.0. | Smoothness: 0.25. | Smoothness: 0.5. | Smoothness: 1.0. |

Exponent
Exponent of the Minkowski distance metric.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Exponent: 0.5. | Exponent: 1.0. | Exponent: 2.0. | Exponent: 32.0. |

Randomness
The randomness of the noise.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Randomness: 1.0. | Randomness: 0.5. | Randomness: 0.25. | Randomness: 0.0. |

[Related references](INDEX.md).
