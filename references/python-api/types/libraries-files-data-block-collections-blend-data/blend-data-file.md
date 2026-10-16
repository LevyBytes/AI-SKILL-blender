# bpy.types.BlendData: file_path_foreach, file_path_map

file_path_foreach ( visit_path_fn , * , subset = None , visit_types = None , flags = {'`SKIP_PACKED`', '`SKIP_WEAK_REFERENCES`'} ) 

Invoke a callback function for all file-path references within data blocks.

For list of valid set members for visit_types, see: bpy.types.KeyingSetPath.id_type.

Parameters :

- visit_path_fn (Callable[[bpy.types.ID, str, Any], str|None]) – function that takes three parameters: the data-block, a file path, and a placeholder for future use. The function should return either None or a str . In the latter case, the visited file path will be replaced with the returned string.

- subset ( set [ str ] | None ) – When given, only these data-blocks and their used file paths will be visited.

- visit_types ( set [ str ] | None ) – When given, only visit data-blocks of these types. Ignored if subset is also given.

- flags ( set [ str ] ) – Set of flags that influence which data-blocks are visited. See File Path Foreach Flag Items.
file_path_map ( * , subset = None , key_types = None , include_libraries = False ) 

Generate a mapping of all ID data-blocks to their external file dependencies.

For list of valid set members for key_types, see: bpy.types.KeyingSetPath.id_type.

Parameters :

- subset (Sequence[bpy.types.ID] | None) – When given, only these data-blocks and their used file paths will be included as keys/values in the map.

- key_types ( set [ str ] | None ) – When given, filter the keys mapped by ID types. Ignored if subset is also given.

- include_libraries ( bool ) – Include library file paths of linked data. False by default.

Returns :

dictionary of bpy.types.ID instances, with sets of file path strings as their values.

Return type :

dict[bpy.types.ID, set[str]]

[Related references](INDEX.md).
