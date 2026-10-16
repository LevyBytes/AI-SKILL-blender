# bpy.types.BlendData: static temp_data

static temp_data ( * , filepath = None ) 

A context manager that temporarily creates blender file data.

Parameters :

filepath ( str | bytes | None ) – The file path for the newly temporary data. When None, the path of the currently open file is used.

Returns :

Blend file data which is freed once the context exits.

Return type :

bpy.types.BlendData

[Related references](INDEX.md).
