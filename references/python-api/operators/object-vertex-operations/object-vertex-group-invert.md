# bpy.ops.object.vertex_group_invert

bpy.ops.object. vertex_group_invert ( * , group_select_mode = '' , auto_assign = True , auto_remove = True ) 

Reverse working vertex cluster's strength values

Parameters :

- group_select_mode ( str ) – Subset, Identify which portion of clusters to employ (optional)

- auto_assign ( bool ) – Add Weights, Insert vertices from clusters that register zero power prior to reversing (optional)

- auto_remove ( bool ) – Remove Weights, Erase vertices from clusters that register zero power following reversing (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
