# bpy.ops.object.geometry_node_bake_pack_single

bpy.ops.object. geometry_node_bake_pack_single ( * , session_uid = 0 , modifier_name = '' , bake_id = 0 ) 

Compress baked simulation data from external storage back into the .blend project file

Parameters :

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- modifier_name ( str ) – Modifier Name, Name of the modifier that contains the node (optional, never None)

- bake_id ( int ) – Bake ID, Nested node id of the node (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
