# bpy.types.ShaderNodeTexWhiteNoise: properties

## ShaderNodeTexWhiteNoise(ShaderNode)

### ShaderNodeTexWhiteNoise(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexWhiteNoise ( ShaderNode )

From a supplied seed, derives a pseudo-random scalar or color.
noise_dimensions

Selects how many input dimensions feed the noise (default '1D' )

- 1D
1D – Drive the noise from the scalar W value.

- 2D
2D – Drive the noise from the (X, Y) pair; W is dropped.

- 3D
3D – Drive the noise from the (X, Y, Z) triple.

- 4D
4D – Drive the noise from the full (X, Y, Z, W) set.

Type :

Literal[‘1D’, ‘2D’, ‘3D’, ‘4D’]

[Related references](INDEX.md).
