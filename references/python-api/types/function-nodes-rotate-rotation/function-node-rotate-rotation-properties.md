# bpy.types.FunctionNodeRotateRotation: properties

## FunctionNodeRotateRotation(FunctionNode)

### FunctionNodeRotateRotation(FunctionNode)

base classes — bpy_struct, Node, NodeInternal, FunctionNode
class bpy.types. FunctionNodeRotateRotation ( FunctionNode )

Layers an extra rotation onto a rotation value already supplied.
rotation_space

Base orientation for the rotation (default 'GLOBAL' )

- GLOBAL
Global – Rotate the input rotation in global space.

- LOCAL
Local – Rotate the input rotation in its local space.

Type :

Literal[‘GLOBAL’, ‘LOCAL’]

[Related references](INDEX.md).
