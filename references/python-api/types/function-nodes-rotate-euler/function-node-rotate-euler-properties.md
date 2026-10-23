# bpy.types.FunctionNodeRotateEuler: properties

## FunctionNodeRotateEuler(FunctionNode)

### FunctionNodeRotateEuler(FunctionNode)

base classes: bpy_struct, Node, NodeInternal, FunctionNode
class bpy.types. FunctionNodeRotateEuler ( FunctionNode )

Adds a further Euler rotation on top of an existing Euler rotation.
rotation_type

Method used to describe the rotation (default 'EULER' )

- `AXIS_ANGLE`
Axis Angle – Rotate around an axis by an angle.

- EULER
Euler – Rotate around the X, Y, and Z axes.

Type :

Literal[‘`AXIS_ANGLE`’, ‘EULER’]
space

Base orientation for rotation (default 'OBJECT' )

- OBJECT
Object – Rotate the input rotation in the local space of the object.

- LOCAL
Local – Rotate the input rotation in its local space.

Type :

Literal[‘OBJECT’, ‘LOCAL’]

[Related references](INDEX.md).
