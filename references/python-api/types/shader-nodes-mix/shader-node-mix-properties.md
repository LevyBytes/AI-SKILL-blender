# bpy.types.ShaderNodeMix: properties

## ShaderNodeMix(ShaderNode)

### ShaderNodeMix(ShaderNode) 

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeMix ( ShaderNode ) 

Blend values according to a factor
blend_type 

(default 'MIX' )

Type :

Literal[Ramp Blend Items]
clamp_factor 

Hold the factor inside the [0,1] range (default False)

Type :

bool
clamp_result 

Hold the result inside the [0,1] range (default False)

Type :

bool
data_type 

(default 'FLOAT' )

Type :

Literal[‘FLOAT’, ‘VECTOR’, ‘RGBA’, ‘ROTATION’]
factor_mode 

(default 'UNIFORM' )

- UNIFORM
Uniform – Apply one shared factor across every component.

- `NON_UNIFORM`
Non-Uniform – Apply a separate factor per component.

Type :

Literal[‘UNIFORM’, ‘`NON_UNIFORM`’]

[Related references](INDEX.md).
