# bpy.types.ShaderNodeVectorTransform: properties

## ShaderNodeVectorTransform(ShaderNode)

### ShaderNodeVectorTransform(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeVectorTransform ( ShaderNode )

Moves a vector, point, or normal across world, camera, and object spaces.
convert_from

The coordinate space being converted out of (default 'WORLD' )

Type :

Literal[‘WORLD’, ‘OBJECT’, ‘CAMERA’]
convert_to

The coordinate space being converted into (default 'WORLD' )

Type :

Literal[‘WORLD’, ‘OBJECT’, ‘CAMERA’]
vector_type

(default 'VECTOR' )

- POINT
Point – Treat the input as a position to transform.

- VECTOR
Vector – Treat the input as a direction to transform.

- NORMAL
Normal – Treat the input as a unit-length normal to transform.

Type :

Literal[‘POINT’, ‘VECTOR’, ‘NORMAL’]

[Related references](INDEX.md).
