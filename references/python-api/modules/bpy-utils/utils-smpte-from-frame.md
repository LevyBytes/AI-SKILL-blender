# bpy.utils: bpy.utils. smpte_from_frame ( frame , * , fps = None , fps_base = None )

bpy.utils. smpte_from_frame ( frame , * , fps = None , fps_base = None ) 

Give back an SMPTE-formatted string built from the frame :
HH:MM:SS:FF .

When fps and fps_base are omitted, the active scene supplies them.

Parameters :

- frame ( int | float ) – frame number.

- fps ( float | None ) – Frames per second, if not given the current scene is used.

- fps_base ( float | None ) – Frames per second base, if not given the current scene is used.

Returns :

the frame string.

Return type :

str

[Related references](INDEX.md).
