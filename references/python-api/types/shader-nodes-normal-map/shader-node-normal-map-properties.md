# bpy.types.ShaderNodeNormalMap: properties

## ShaderNodeNormalMap(ShaderNode)

### ShaderNodeNormalMap(ShaderNode) 

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeNormalMap ( ShaderNode ) 

Build a perturbed normal from an RGB normal map image, a common trick for simulating fine surface detail
base 

The surface the normal map is referenced against once displacement is in play (default 'DISPLACED' )

- ORIGINAL
Original Base – Reference the normal map against the smooth, undisplaced surface, suited to normal maps that pair with the displacement map.

- DISPLACED
Displaced Base – Reference the normal map against the displaced surface, suited to normal maps layered on top of the displacement map.

Type :

Literal[‘ORIGINAL’, ‘DISPLACED’]
convention 

OpenGL or DirectX (default 'OPENGL' )

- OPENGL
OpenGL – Follows the OpenGL convention, where the green channel encodes the Y axis pointing up.

- DIRECTX
DirectX – Follows the DirectX convention, where the green channel encodes the Y axis pointing down.

Type :

Literal[‘OPENGL’, ‘DIRECTX’]
space 

Coordinate space the input normal is given in (default 'TANGENT' )

- TANGENT
Tangent Space – Normal mapping in tangent space.

- OBJECT
Object Space – Normal mapping in object space.

- WORLD
World Space – Normal mapping in world space.

- `BLENDER_OBJECT`
Blender Object Space – Object-space normal mapping that works with Blender render baking.

- `BLENDER_WORLD`
Blender World Space – World-space normal mapping that works with Blender render baking.

Type :

Literal[‘TANGENT’, ‘OBJECT’, ‘WORLD’, ‘`BLENDER_OBJECT`’, ‘`BLENDER_WORLD`’]
uv_map 

The UV Map used by tangent-space maps (default “”, never None)

Type :

str

[Related references](INDEX.md).
