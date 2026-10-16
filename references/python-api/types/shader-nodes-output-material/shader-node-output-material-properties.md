# bpy.types.ShaderNodeOutputMaterial: properties

## ShaderNodeOutputMaterial(ShaderNode)

### ShaderNodeOutputMaterial(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeOutputMaterial ( ShaderNode )

Hands surface material data off to the renderer.
is_active_output

Indicates that this node is the one currently used as output (default False)

Type :

bool
target

Determines the renderers and viewport shading modes that will use these shaders (default 'ALL' )

- ALL
All – Use shaders for all renderers and viewports, unless there exists a more specific output.

- EEVEE
EEVEE – Use shaders for EEVEE renderer.

- CYCLES
Cycles – Use shaders for Cycles renderer.

Type :

Literal[‘ALL’, ‘EEVEE’, ‘CYCLES’]

[Related references](INDEX.md).
