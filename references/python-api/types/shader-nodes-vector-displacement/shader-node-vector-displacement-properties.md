# bpy.types.ShaderNodeVectorDisplacement: properties

## ShaderNodeVectorDisplacement(ShaderNode)

### ShaderNodeVectorDisplacement(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeVectorDisplacement ( ShaderNode )

Pushes the surface outward along a freely chosen direction.
space

Which space the incoming height is measured in (default 'TANGENT' )

- TANGENT
Tangent Space – Vector displacement evaluated in tangent space.

- OBJECT
Object Space – Vector displacement evaluated in object space.

- WORLD
World Space – Vector displacement evaluated in world space.

Type :

Literal[‘TANGENT’, ‘OBJECT’, ‘WORLD’]

[Related references](INDEX.md).
