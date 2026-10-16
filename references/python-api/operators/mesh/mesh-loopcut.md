# bpy.ops.mesh.loopcut

bpy.ops.mesh. loopcut ( * , number_cuts = 1 , smoothness = 0.0 , falloff = '`INVERSE_SQUARE`' , object_index = -1 , edge_index = -1 , mesh_select_mode_init = (False, False, False) )

Introduce a fresh loop between present loops

Parameters :

- number_cuts ( int ) – Number of Cuts, (in [1, 1000000], optional)

- smoothness ( float ) – Smoothness, Smoothness factor (in [-1000, 1000], optional)

- falloff (Literal[Proportional Falloff Curve Only Items]) – Falloff, Falloff type of the feather (optional)

- object_index ( int ) – Object Index, (in [-1, inf], optional)

- edge_index ( int ) – Edge Index, (in [-1, inf], optional)

- mesh_select_mode_init ( Sequence [ bool ] ) – (array of 3 items, optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
