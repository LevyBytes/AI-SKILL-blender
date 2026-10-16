# bpy.types.NodeTree: bl_rna_get_subclass, bl_rna_get_subclass_py

classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default (bpy.types.Struct | None) – Fallback returned if no match is found.

Returns :

Either the matching RNA type or the supplied fallback when nothing matches.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default (type | None ) – Fallback returned if no match is found.

Returns :

Either the matching class or the supplied fallback when nothing matches.

Return type :

type

[Related references](INDEX.md).
