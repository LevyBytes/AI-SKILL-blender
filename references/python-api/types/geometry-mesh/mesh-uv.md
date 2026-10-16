# bpy.types.Mesh: uv_layer_clone, uv_layer_clone_index, uv_layer_stencil, uv_layer_stencil_index, uv_layers

uv_layer_clone

The UV loop layer that serves as the cloning source

Type :

MeshUVLoopLayer
uv_layer_clone_index

Clone UV loop layer index (in [0, inf], default 0)

Type :

int
uv_layer_stencil

The UV loop layer that masks off the painted area

Type :

MeshUVLoopLayer
uv_layer_stencil_index

Mask UV loop layer index (in [0, inf], default 0)

Type :

int
uv_layers

All UV loop layers (default None, readonly)

Type :

UVLoopLayers[MeshUVLoopLayer]

[Related references](INDEX.md).
