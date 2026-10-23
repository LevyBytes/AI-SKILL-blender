# bpy.types.ShaderNodeOutputLineStyle: properties

## ShaderNodeOutputLineStyle(ShaderNode)

### ShaderNodeOutputLineStyle(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeOutputLineStyle ( ShaderNode )

Governs how texture data is blended onto the base color of a line style.
blend_type

(default 'MIX' )

Type :

Literal[Ramp Blend Items]
is_active_output

Marks whether this node acts as the active output (default False)

Type :

bool
target

Chooses which renderers and viewport shading modes get these shaders (default 'ALL' )

- ALL
All – Use shaders for all renderers and viewports, unless there exists a more specific output.

- EEVEE
EEVEE – Use shaders for EEVEE renderer.

- CYCLES
Cycles – Use shaders for Cycles renderer.

Type :

Literal[‘ALL’, ‘EEVEE’, ‘CYCLES’]
use_alpha

Folds the alpha of the second input into this operation (default False)

Type :

bool
use_clamp

Holds the node's result inside the 0.0–1.0 range (default False)

Type :

bool

[Related references](INDEX.md).
