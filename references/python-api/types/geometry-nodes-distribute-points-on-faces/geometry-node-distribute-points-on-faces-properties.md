# bpy.types.GeometryNodeDistributePointsOnFaces: properties

## GeometryNodeDistributePointsOnFaces(GeometryNode)

### GeometryNodeDistributePointsOnFaces(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeDistributePointsOnFaces ( GeometryNode )

Scatter points across the surface of a mesh.
distribute_method

Picks the scattering method for the points (default 'RANDOM' )

- RANDOM
Random – Scatter the points at random over the surface.

- POISSON
Poisson Disk – Scatter the points at random over the surface while honoring a minimum spacing between them.

Type :

Literal[‘RANDOM’, ‘POISSON’]
use_legacy_normal

Emit the older normal and rotation values from before the node began honoring smooth normals (default False)

Type :

bool

[Related references](INDEX.md).
