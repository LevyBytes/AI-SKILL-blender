# bpy.types.ShaderNodeDisplacement: properties

## ShaderNodeDisplacement(ShaderNode)

### ShaderNodeDisplacement(ShaderNode) 

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeDisplacement ( ShaderNode ) 

Push the surface outward along its normal direction
space 

Coordinate space the input height is measured in (default 'OBJECT' )

- OBJECT
Object Space – Height is read in object space, so it scales with the object.

- WORLD
World Space – Height is read in world space, independent of object scale.

Type :

Literal[‘OBJECT’, ‘WORLD’]

[Related references](INDEX.md).
