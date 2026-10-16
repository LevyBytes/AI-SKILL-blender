# bpy.types.ShaderNodeUVMap: properties

## ShaderNodeUVMap(ShaderNode)

### ShaderNodeUVMap(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeUVMap ( ShaderNode )

Fetches a UV map off the geometry, falling back to the default when none is named.
from_instancer

Where possible, take it from the instance object's parent (default False)

Type :

bool
uv_map

Which UV coordinates serve as the mapping source (default “”, never None)

Type :

str

[Related references](INDEX.md).
