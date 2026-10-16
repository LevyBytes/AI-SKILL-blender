# bpy.types.ShaderNodeOutputLight: properties

## ShaderNodeOutputLight(ShaderNode)

### ShaderNodeOutputLight(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeOutputLight ( ShaderNode )

Feeds the computed light data back to a light object.
is_active_output

Set when this node serves as the currently active output (default False)

Type :

bool
target

Picks the renderers and viewport shading modes these shaders apply to (default 'ALL' )

- ALL
All – Use shaders for all renderers and viewports, unless there exists a more specific output.

- EEVEE
EEVEE – Use shaders for EEVEE renderer.

- CYCLES
Cycles – Use shaders for Cycles renderer.

Type :

Literal[‘ALL’, ‘EEVEE’, ‘CYCLES’]

[Related references](INDEX.md).
