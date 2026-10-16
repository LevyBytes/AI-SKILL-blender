# bpy.utils: bpy.utils. make_rna_paths ( struct_name , prop_name , enum_name )

bpy.utils. make_rna_paths ( struct_name , prop_name , enum_name ) 

Build RNA "paths" from the supplied names.

Parameters :

- struct_name ( str ) – Name of a RNA struct (like e.g. "Scene").

- prop_name ( str ) – Name of a RNA struct's property.

- enum_name ( str ) – Name of a RNA enum identifier.

Returns :

A triple of three "RNA paths"
(most_complete_path, "struct.prop", "struct.prop:'enum'").
When enum_name is omitted, the third entry is always empty.

Return type :

tuple[str, str, str]

[Related references](INDEX.md).
