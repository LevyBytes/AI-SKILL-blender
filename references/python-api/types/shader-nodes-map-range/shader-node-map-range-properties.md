# bpy.types.ShaderNodeMapRange: properties

## ShaderNodeMapRange(ShaderNode)

### ShaderNodeMapRange(ShaderNode) 

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeMapRange ( ShaderNode ) 

Convert a value from one range onto a destination range
clamp 

Restrict the output to the target range [To Min, To Max] (default False)

Type :

bool
data_type 

(default 'FLOAT' )

- FLOAT
Float – Floating-point value.

- `FLOAT_VECTOR`
Vector – 3D vector with floating-point values.

Type :

Literal[‘FLOAT’, ‘`FLOAT_VECTOR`’]
interpolation_type 

(default 'LINEAR' )

Type :

Literal[Node Map Range Items]

[Related references](INDEX.md).
