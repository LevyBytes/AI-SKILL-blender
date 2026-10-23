# bpy.types.ShaderNodeAmbientOcclusion: properties

## ShaderNodeAmbientOcclusion(ShaderNode)

### ShaderNodeAmbientOcclusion(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeAmbientOcclusion ( ShaderNode )

Measure how much the hemisphere over the shading point is blocked, handy for adding wear to corners.
Note: in Cycles this can noticeably increase render time
inside

Cast rays toward the object's interior (default False)

Type :

bool
only_local

Restrict the AO computation to the object on its own (default False)

Type :

bool
samples

How many rays each shader evaluation traces (in [1, 128], default 0)

Type :

int

[Related references](INDEX.md).
