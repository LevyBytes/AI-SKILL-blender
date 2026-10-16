# bpy.types.ShaderNodeTexVoronoi: properties

## ShaderNodeTexVoronoi(ShaderNode)

### ShaderNodeTexVoronoi(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexVoronoi ( ShaderNode )

Produces Worley noise from the distance to scattered random points — a common way to make stone, water, or organic cell patterns.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
distance

The distance metric used to compute the texture (default 'EUCLIDEAN' )

- EUCLIDEAN
Euclidean – Euclidean distance.

- MANHATTAN
Manhattan – Manhattan distance.

- CHEBYCHEV
Chebychev – Chebychev distance.

- MINKOWSKI
Minkowski – Minkowski distance.

Type :

Literal[‘EUCLIDEAN’, ‘MANHATTAN’, ‘CHEBYCHEV’, ‘MINKOWSKI’]
feature

The Voronoi feature that the node will compute (default 'F1' )

- F1
F1 – Computes the distance to the closest point as well as its position and color.

- F2
F2 – Computes the distance to the second closest point as well as its position and color.

- `SMOOTH_F1`
Smooth F1 – Smoothed version of F1. Weighted sum of neighbor voronoi cells..

- `DISTANCE_TO_EDGE`
Distance to Edge – Computes the distance to the edge of the voronoi cell.

- `N_SPHERE_RADIUS`
N-Sphere Radius – Computes the radius of the n-sphere inscribed in the voronoi cell.

Type :

Literal[‘F1’, ‘F2’, ‘`SMOOTH_F1`’, ‘`DISTANCE_TO_EDGE`’, ‘`N_SPHERE_RADIUS`’]
normalize

Normalize output Distance to 0.0 to 1.0 range (default False)

Type :

bool
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping
voronoi_dimensions

Number of dimensions to output noise for (default '1D' )

- 1D
1D – Use the scalar value W as input.

- 2D
2D – Use the 2D vector (X, Y) as input. The Z component is ignored..

- 3D
3D – Use the 3D vector (X, Y, Z) as input.

- 4D
4D – Use the 4D vector (X, Y, Z, W) as input.

Type :

Literal[‘1D’, ‘2D’, ‘3D’, ‘4D’]

[Related references](INDEX.md).
