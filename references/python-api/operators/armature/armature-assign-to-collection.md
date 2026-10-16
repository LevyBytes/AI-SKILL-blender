# bpy.ops.armature.assign_to_collection

bpy.ops.armature. assign_to_collection ( * , collection_index = -1 , new_collection_name = '' )

Put all active bones into a group, or extract them, contingent on whether the focused bone is already assigned.

Parameters :

- collection_index ( int ) – Collection Index, Index of the collection to assign selected bones to. When the operator should create a new bone collection, use new_collection_name to define the collection name, and set this parameter to the parent index of the new bone collection (in [-1, inf], optional)

- new_collection_name ( str ) – Name, Name of a to-be-added bone collection. Only pass this if you want to create a new bone collection and assign the selected bones to it. To assign to an existing collection, do not include this parameter and use collection_index (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
