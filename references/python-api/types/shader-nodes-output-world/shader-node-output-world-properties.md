# bpy.types.ShaderNodeOutputWorld: properties

## ShaderNodeOutputWorld(ShaderNode)

### ShaderNodeOutputWorld(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeOutputWorld ( ShaderNode )

Sends computed light-color data to the scene's World.
is_active_output

Whether this node is treated as the active output right now (default False)

Type :

bool
target

Selects the renderers and viewport shading modes for which these shaders are used (default 'ALL' )

- ALL
All – Use shaders for all renderers and viewports, unless there exists a more specific output.

- EEVEE
EEVEE – Use shaders for EEVEE renderer.

- CYCLES
Cycles – Use shaders for Cycles renderer.

Type :

Literal[‘ALL’, ‘EEVEE’, ‘CYCLES’]

[Related references](INDEX.md).
