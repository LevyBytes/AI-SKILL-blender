# bpy.types.GeometryNodeDistributePointsInGrid: properties

## GeometryNodeDistributePointsInGrid(GeometryNode)

### GeometryNodeDistributePointsInGrid(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeDistributePointsInGrid ( GeometryNode )

Place points throughout a volume grid.
mode

Picks the scattering method for the points (default '`DENSITY_RANDOM`' )

- `DENSITY_RANDOM`
Random – Scatter the points at random throughout the volume.

- `DENSITY_GRID`
Grid – Lay the points out on a regular grid throughout the volume.

Type :

Literal[‘`DENSITY_RANDOM`’, ‘`DENSITY_GRID`’]

[Related references](INDEX.md).
