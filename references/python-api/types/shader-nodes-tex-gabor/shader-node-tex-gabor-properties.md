# bpy.types.ShaderNodeTexGabor: properties

## ShaderNodeTexGabor(ShaderNode)

### ShaderNodeTexGabor(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexGabor ( ShaderNode )

Produces Gabor noise.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
gabor_type

The type of Gabor noise to evaluate (default '2D' )

- 2D
2D – Use the 2D vector (X, Y) as input. The Z component is ignored..

- 3D
3D – Use the 3D vector (X, Y, Z) as input.

Type :

Literal[‘2D’, ‘3D’]
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).
