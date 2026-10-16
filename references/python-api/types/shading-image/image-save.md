# bpy.types.Image: save_render, save

save_render ( filepath , * , scene = None , quality = 0 )

Write the image to a chosen path with a scene's render settings.

Parameters :

- filepath ( str ) – Output path (never None)

- scene (Scene) – Scene to take image parameters from (optional)

- quality ( int ) – Quality, Quality for image formats that support lossy compression, uses default quality if not specified (in [0, 100], optional)
save ( * , filepath = '' , quality = 0 , save_copy = False )

Write the image.

Parameters :

- filepath ( str ) – Output path, uses image data-block filepath if not specified (optional, never None)

- quality ( int ) – Quality, Quality for image formats that support lossy compression, uses default quality if not specified (in [0, 100], optional)

- save_copy ( bool ) – Save Copy, Save the image as a copy, without updating current image’s filepath (optional)

[Related references](INDEX.md).
