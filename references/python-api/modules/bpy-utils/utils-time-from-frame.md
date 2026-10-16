# bpy.utils: bpy.utils. time_from_frame ( frame , * , fps = None , fps_base = None )

bpy.utils. time_from_frame ( frame , * , fps = None , fps_base = None ) 

Gives back the time that corresponds to a frame number.

When fps and fps_base are omitted, the active scene supplies them.

Parameters :

- frame ( int | float ) – number.

- fps ( float | None ) – Frames per second, if not given the current scene is used.

- fps_base ( float | None ) – Frames per second base, if not given the current scene is used.

Returns :

the time in seconds.

Return type :

datetime.timedelta

[Related references](INDEX.md).
