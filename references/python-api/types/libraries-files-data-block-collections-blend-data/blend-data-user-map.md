# bpy.types.BlendData: user_map

user_map ( * , subset = None , key_types = None , value_types = None ) 

Generate a mapping of all ID data-blocks to which other data-blocks reference them.

For list of valid set members for key_types & value_types, see: bpy.types.KeyingSetPath.id_type.

Parameters :

- subset (Sequence[bpy.types.ID] | None) – When passed, only these data-blocks and their users will be included as keys/values in the map.

- key_types ( set [ str ] | None ) – Filter the keys mapped by ID types.

- value_types ( set [ str ] | None ) – Filter the values in the set by ID types.

Returns :

dictionary that maps data-blocks ID's to their users.

Return type :

dict[bpy.types.ID, set[bpy.types.ID]]

[Related references](INDEX.md).
