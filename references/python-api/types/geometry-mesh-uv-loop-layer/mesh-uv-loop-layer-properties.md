# bpy.types.MeshUVLoopLayer: properties

## MeshUVLoopLayer(bpy_struct)

### MeshUVLoopLayer(bpy_struct)

base class — bpy_struct
class bpy.types. MeshUVLoopLayer ( bpy_struct )
active

Set the map as active for display and editing (default False)

Type :

bool
active_clone

Set the map as active for cloning (default False)

Type :

bool
active_render

Set the UV map as active for rendering (default False)

Type :

bool
data

Deprecated, use ‘uv’, ‘vertex_select’, ‘edge_select’ or ‘pin’ properties instead (default None, readonly)

Type :

bpy_prop_collection[MeshUVLoop]
name

Name of UV map (default "", never None)

Type :

str
pin

UV pinned state in the UV editor (default None, readonly)

Type :

bpy_prop_collection[BoolAttributeValue]
uv

UV coordinates on face corners (default None, readonly)

Type :

bpy_prop_collection[Float2AttributeValue]

[Related references](INDEX.md).
