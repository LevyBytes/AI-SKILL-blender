# bpy.types.ShaderNodeVectorRotate: properties

## ShaderNodeVectorRotate(ShaderNode)

### ShaderNodeVectorRotate(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeVectorRotate ( ShaderNode )

Turns a vector about a chosen pivot (center) point.
invert

Reverse the sign of the rotation angle (default False)

Type :

bool
rotation_type

How the rotation angle is supplied (default '`AXIS_ANGLE`' )

- `AXIS_ANGLE`
Axis Angle – Spin the point about an arbitrary axis by an angle.

- `X_AXIS`
X Axis – Spin the point about the X axis.

- `Y_AXIS`
Y Axis – Spin the point about the Y axis.

- `Z_AXIS`
Z Axis – Spin the point about the Z axis.

- `EULER_XYZ`
Euler – Spin the point using XYZ-order Euler angles.

Type :

Literal[‘`AXIS_ANGLE`’, ‘`X_AXIS`’, ‘`Y_AXIS`’, ‘`Z_AXIS`’, ‘`EULER_XYZ`’]

[Related references](INDEX.md).
