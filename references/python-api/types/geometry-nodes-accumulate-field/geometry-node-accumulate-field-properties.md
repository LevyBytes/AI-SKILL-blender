# bpy.types.GeometryNodeAccumulateField: properties

## GeometryNodeAccumulateField(GeometryNode)

### GeometryNodeAccumulateField(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeAccumulateField ( GeometryNode )

Sums the values of an evaluated field and reports the running tally for every element.
data_type

Kind of data being accumulated (default 'FLOAT' )

- FLOAT
Float – Add floating point values.

- INT
Integer – Add integer values.

- `FLOAT_VECTOR`
Vector – Add 3D vector values.

- TRANSFORM
Transform – Multiply transformation matrices.

Type :

Literal[‘FLOAT’, ‘INT’, ‘`FLOAT_VECTOR`’, ‘TRANSFORM’]
domain

(default 'POINT' )

Type :

Literal[Attribute Domain Items]

[Related references](INDEX.md).
