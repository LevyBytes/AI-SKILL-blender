# bpy.ops.object.geometry_node_bake_unpack_single

bpy.ops.object. geometry_node_bake_unpack_single ( * , session_uid = 0 , modifier_name = '' , bake_id = 0 , method = '`USE_LOCAL`' ) 

Write cached simulation data from the .blend file out to the file system

Parameters :

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- modifier_name ( str ) – Modifier Name, Name of the modifier that contains the node (optional, never None)

- bake_id ( int ) – Bake ID, Nested node id of the node (in [0, inf], optional)

- method ( Literal [ '`USE_LOCAL`' , '`WRITE_LOCAL`' , '`USE_ORIGINAL`' , '`WRITE_ORIGINAL`' ] ) – Method, How to unpack (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
