# bpy.utils: bpy.utils. smpte_from_seconds ( time , * , fps = None , fps_base = None )

bpy.utils. smpte_from_seconds ( time , * , fps = None , fps_base = None ) 

Give back an SMPTE-formatted string built from the time :
HH:MM:SS:FF .

When fps and fps_base are omitted, the active scene supplies them.

Parameters :

- time ( int | float | datetime.timedelta ) – time in seconds.

- fps ( float | None ) – Frames per second, if not given the current scene is used.

- fps_base ( float | None ) – Frames per second base, if not given the current scene is used.

Returns :

the frame string.

Return type :

str

[Related references](INDEX.md).
