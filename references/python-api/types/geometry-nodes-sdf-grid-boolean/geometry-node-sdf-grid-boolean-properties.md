# bpy.types.GeometryNodeSDFGridBoolean: properties

## GeometryNodeSDFGridBoolean(GeometryNode)

### GeometryNodeSDFGridBoolean(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSDFGridBoolean ( GeometryNode )

Carve, subtract, or merge several SDF volume grid inputs together
operation

(default 'DIFFERENCE' )

- INTERSECT
Intersect – Retain only the region shared by all of the operands.

- UNION
Union – Merge the grids additively.

- DIFFERENCE
Difference – Merge the grids subtractively.

Type :

Literal[‘INTERSECT’, ‘UNION’, ‘DIFFERENCE’]

[Related references](INDEX.md).
