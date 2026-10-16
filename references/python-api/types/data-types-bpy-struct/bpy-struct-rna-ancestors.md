# bpy.types.bpy_struct: rna_ancestors

rna_ancestors ( )

Hands back the chain of data that contains this struct, when it is known.
The list opens with the root (usually an ID) and closes with the immediate parent.
It can come back empty.

Returns :

a list of this object's ancestors.

Return type :

list[bpy.types.bpy_struct]

[Related references](INDEX.md).
