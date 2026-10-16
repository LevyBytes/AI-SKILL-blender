# bpy.ops.object.vertex_group_clean

bpy.ops.object. vertex_group_clean ( * , group_select_mode = '' , limit = 0.0 , keep_single = False ) 

Discard vertex cluster allocations that aren't essential

Parameters :

- group_select_mode ( str ) – Subset, Identify which portion of clusters to employ (optional)

- limit ( float ) – Limit, Strip vertices whose power is at or below this point (in [0, 1], optional)

- keep_single ( bool ) – Keep Single, Safeguard vertices present in a minimum of one cluster when filtering (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
