# bpy.ops.armature.move_to_collection

bpy.ops.armature. move_to_collection ( * , collection_index = -1 , new_collection_name = '' )

Shift bones to a group.

Parameters :

- collection_index ( int ) – Collection Index, Index of the collection to move selected bones to. When the operator should create a new bone collection, do not include this parameter and pass new_collection_name (in [-1, inf], optional)

- new_collection_name ( str ) – Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and move the selected bones to it. To move to an existing collection, do not include this parameter and use collection_index (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
