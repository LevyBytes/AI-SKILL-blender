# bpy_extras.id_map_utils

## bpy_extras submodule (bpy_extras.id_map_utils)

### bpy_extras submodule (bpy_extras.id_map_utils)
bpy_extras.id_map_utils. get_id_reference_map ( ) 

Hand back a dictionary of direct data-block references for each data-block in the blend file.

Returns :

Each datablock of the .blend file mapped to the set of IDs they directly reference.

Return type :

dict[bpy.types.ID, set[bpy.types.ID]]
bpy_extras.id_map_utils. get_all_referenced_ids ( id , ref_map ) 

Hand back the set of IDs that id references either directly or through other IDs.

Parameters :

- id (bpy.types.ID) – Datablock whose references we're interested in.

- ref_map ( dict [ bpy.types.ID , set [ bpy.types.ID ] ] ) – The global ID reference map, retrieved from get_id_reference_map()

Returns :

Set of datablocks referenced by id .

Return type :

set[bpy.types.ID]

[Related references](INDEX.md).
