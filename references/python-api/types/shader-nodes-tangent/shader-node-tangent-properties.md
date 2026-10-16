# bpy.types.ShaderNodeTangent: properties

## ShaderNodeTangent(ShaderNode)

### ShaderNodeTangent(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTangent ( ShaderNode )

Produces a tangent vector for use with the Anisotropic BSDF.
axis

Axis for radial tangents (default 'X' )

- X
X – X axis.

- Y
Y – Y axis.

- Z
Z – Z axis.

Type :

Literal[‘X’, ‘Y’, ‘Z’]
direction_type

Method to use for the tangent (default 'RADIAL' )

- RADIAL
Radial – Radial tangent around the X, Y or Z axis.

- `UV_MAP`
UV Map – Tangent from UV map.

Type :

Literal[‘RADIAL’, ‘`UV_MAP`’]
uv_map

UV Map for tangent generated from UV (default “”, never None)

Type :

str

[Related references](INDEX.md).
