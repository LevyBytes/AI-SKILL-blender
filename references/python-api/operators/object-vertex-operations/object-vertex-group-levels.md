# bpy.ops.object.vertex_group_levels

bpy.ops.object. vertex_group_levels ( * , group_select_mode = '' , offset = 0.0 , gain = 1.0 )

Introduce a displacement and apply a multiplication factor to the weights of the working vertex cluster

Parameters :

- group_select_mode ( str ) – Subset, Identify which portion of clusters to employ (optional)

- offset ( float ) – Offset, Quantity to introduce to weights (in [-1, 1], optional)

- gain ( float ) – Gain, Quantity to increase weights by (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
