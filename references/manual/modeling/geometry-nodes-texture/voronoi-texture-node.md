# Voronoi Texture Node

## Voronoi Texture Node

The Voronoi Texture node samples a Worley Noise at the input texture coordinates.

Inputs (dynamic — they appear as the node's properties require them):
Vector — coordinate to sample the noise at; an unconnected socket defaults to Generated texture coordinates.
W — coordinate to sample the noise at.
Scale — scale of the noise.
Detail — number of noise octaves; the input's fractional part is multiplied by the magnitude of the highest octave, and more octaves mean longer evaluation time.
Roughness — shifts between a smoother pattern and a rougher one with sharper peaks.
Lacunarity — the scale gap between each pair of consecutive octaves; larger values make higher octaves larger in scale.
Smoothness — how smooth the noise is (illustrated at 0.0, 0.25, 0.5, and 1.0).
Exponent — exponent of the Minkowski distance metric (illustrated at 0.5, 1.0, 2.0, and 32.0).
Randomness — how random the noise is (illustrated at 1.0, 0.5, 0.25, and 0.0).

Properties:
Dimensions — the space the noise is evaluated in.
- 1D: in 1D space at the input W.
- 2D: in 2D space at the input Vector; the Z component is ignored.
- 3D: in 3D space at the input Vector.
- 4D: in 4D space at the input Vector with the input W as the fourth dimension.
Higher dimensions raise render time, so keep to lower dimensions unless higher ones are necessary.
Feature — which Voronoi feature the node computes.
- F1: the distance to the closest feature point, plus its position and color.
- F2: the distance to the second-closest feature point, plus its position and color.
- Smooth F1: a smoothed version of F1.
- Distance to Edge: the distance to the edges of the Voronoi cells.
- N-Sphere Radius: the radius of the n-sphere inscribed in the Voronoi cells — that is, half the distance between the closest feature point and the feature point closest to it (handy for creating tightly packed n-spheres).
Distance Metric — the metric used to compute the texture.
- Euclidean: the Euclidean distance metric.
- Manhattan: the Manhattan distance metric.
- Chebychev: the Chebychev distance metric.
- Minkowski: the Minkowski distance metric, a generalization of the others taking an Exponent as a parameter — an exponent of one is equivalent to Manhattan, two is equivalent to Euclidean, and an infinite exponent is equivalent to Chebychev.
Normalize — when enabled, keeps output within 0.0 to 1.0; in rare cases the value may fall outside that range when Feature is F2.

Outputs:
Distance — distance.
Color — cell color (the color is arbitrary).
Position — position of the feature point.
W — position of the feature point.
Radius — n-sphere radius.

Notes: in some node configurations, especially at low Randomness, rendering artifacts can occur for the same reasons covered in the Notes section of the White Noise Texture page, and they can be fixed in the same way described there.

Examples: the difference between F1 and Smooth F1 can be used to create beveled Voronoi cells, and the node can build a hammered-metal shader.

Note: this node is ported from shader nodes, so the manual and images reference the shader version of the node. It accepts field inputs and outputs, and when the Vector input is unconnected it carries an implicit position attribute value.

The Voronoi Texture node samples a Worley Noise at the input texture coordinates.

Inputs (dynamic — they appear as the node's properties require them):
Vector — coordinate to sample the noise at; an unconnected socket defaults to Generated texture coordinates.
W — coordinate to sample the noise at.
Scale — scale of the noise.
Detail — number of noise octaves; the input's fractional part is multiplied by the magnitude of the highest octave, and more octaves mean longer evaluation time.
Roughness — shifts between a smoother pattern and a rougher one with sharper peaks.
Lacunarity — the scale gap between each pair of consecutive octaves; larger values make higher octaves larger in scale.
Smoothness — how smooth the noise is (illustrated at 0.0, 0.25, 0.5, and 1.0).
Exponent — exponent of the Minkowski distance metric (illustrated at 0.5, 1.0, 2.0, and 32.0).
Randomness — how random the noise is (illustrated at 1.0, 0.5, 0.25, and 0.0).

Properties:
Dimensions — the space the noise is evaluated in.
- 1D: in 1D space at the input W.
- 2D: in 2D space at the input Vector; the Z component is ignored.
- 3D: in 3D space at the input Vector.
- 4D: in 4D space at the input Vector with the input W as the fourth dimension.
Higher dimensions raise render time, so keep to lower dimensions unless higher ones are necessary.
Feature — which Voronoi feature the node computes.
- F1: the distance to the closest feature point, plus its position and color.
- F2: the distance to the second-closest feature point, plus its position and color.
- Smooth F1: a smoothed version of F1.
- Distance to Edge: the distance to the edges of the Voronoi cells.
- N-Sphere Radius: the radius of the n-sphere inscribed in the Voronoi cells — that is, half the distance between the closest feature point and the feature point closest to it (handy for creating tightly packed n-spheres).
Distance Metric — the metric used to compute the texture.
- Euclidean: the Euclidean distance metric.
- Manhattan: the Manhattan distance metric.
- Chebychev: the Chebychev distance metric.
- Minkowski: the Minkowski distance metric, a generalization of the others taking an Exponent as a parameter — an exponent of one is equivalent to Manhattan, two is equivalent to Euclidean, and an infinite exponent is equivalent to Chebychev.
Normalize — when enabled, keeps output within 0.0 to 1.0; in rare cases the value may fall outside that range when Feature is F2.

Outputs:
Distance — distance.
Color — cell color (the color is arbitrary).
Position — position of the feature point.
W — position of the feature point.
Radius — n-sphere radius.

Notes: in some node configurations, especially at low Randomness, rendering artifacts can occur for the same reasons covered in the Notes section of the White Noise Texture page, and they can be fixed in the same way described there.

Examples: the difference between F1 and Smooth F1 can be used to create beveled Voronoi cells, and the node can build a hammered-metal shader.

[Related references](INDEX.md).
