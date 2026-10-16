# bpy.utils: bpy.utils. blend_paths ( * , absolute = False , packed = False , local = False )

bpy.utils. blend_paths ( * , absolute = False , packed = False , local = False ) 

Gives back the list of external file paths that the open .blend file references.

Parameters :

- absolute ( bool ) – When true the paths returned are made absolute.

- packed ( bool ) – When true include file paths for packed data.

- local ( bool ) – When true skip linked library paths.

Returns :

path list.

Return type :

list[str]

[Related references](INDEX.md).
