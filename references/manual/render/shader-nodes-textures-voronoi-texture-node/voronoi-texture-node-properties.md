# Voronoi Texture Node: Properties

### Properties

Dimensions
Which space the noise is evaluated in.

1D :

Evaluate the noise in 1D space at the input W.

2D :

Evaluate the noise in 2D space at the input Vector. The Z component is ignored.

3D :

Evaluate the noise in 3D space at the input Vector.

4D :

Evaluate the noise in 4D space, using the input Vector plus the input W as the fourth dimension.

Higher dimensions cost more render time, so stay with lower ones unless you genuinely need more.

Feature
Which Voronoi feature the node computes.

F1 :

Distance to the nearest feature point, plus that point's position and color.

| Description | Description | Description |
| --- | --- | --- |
| Distance. | Color. | Position. |

F2 :

Distance to the second-nearest feature point, plus that point's position and color.

| Description | Description | Description |
| --- | --- | --- |
| Distance. | Color. | Position. |

Smooth F1 :

A smooth version of F1.

| Description | Description | Description |
| --- | --- | --- |
| Distance. | Color. | Position. |

Distance to Edge :

The distance to the edges of the Voronoi cells.

| Description | Description |
| --- | --- |
| Distance. | Distance smaller than 0.05. |

N-Sphere Radius :

Radius of the n-sphere that fits inside the Voronoi cells — equivalently, half the gap separating the nearest feature point from the one nearest to it.

| Description | Description |
| --- | --- |
| The n-sphere radius can be used to create tightly packed n-spheres. | Node tree for the shader to the left. |

Distance Metric
The distance metric used to compute the texture.

Euclidean :

Use the Euclidean distance metric.

Manhattan :

Use the Manhattan distance metric.

Chebychev :

Use the Chebychev distance metric.

Minkowski :

Use the Minkowski distance metric. Minkowski generalizes the metrics above, taking an Exponent as a parameter. An exponent of one matches the Manhattan distance metric, two matches the Euclidean distance metric, and an infinite exponent matches the Chebychev distance metric.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Minkowski Exponent: 0.5 (Minkowski 1/2). | Minkowski Exponent: 1.0 (Manhattan). | Minkowski Exponent: 2.0 (Euclidean). | Minkowski Exponent: 32.0 (approximation of Chebychev). |

Normalize
On, it keeps the output within 0.0 to 1.0. On rare occasions the value can fall outside that range when Feature is F2 .

[Related references](INDEX.md).
