# bpy.types.Image: gl_touch, gl_load, gl_free

gl_touch ( * , frame = 0 , layer_index = 0 , pass_index = 0 )

Hold off purging the image from the cache for being idle.

Parameters :

- frame ( int ) – Frame, Frame of image sequence or movie (in [0, inf], optional)

- layer_index ( int ) – Layer, Index of layer that should be loaded (in [0, inf], optional)

- pass_index ( int ) – Pass, Index of pass that should be loaded (in [0, inf], optional)

Returns :

Error, OpenGL error value (in [-inf, inf])

Return type :

int
gl_load ( * , frame = 0 , layer_index = 0 , pass_index = 0 )

Bring the image into an OpenGL texture. When it works, image.bindcode holds the OpenGL texture bindcode. Texture reads come back in scene-linear color space with premultiplied or straight alpha to match the image's alpha mode.

Parameters :

- frame ( int ) – Frame, Frame of image sequence or movie (in [0, inf], optional)

- layer_index ( int ) – Layer, Index of layer that should be loaded (in [0, inf], optional)

- pass_index ( int ) – Pass, Index of pass that should be loaded (in [0, inf], optional)

Returns :

Error, OpenGL error value (in [-inf, inf])

Return type :

int
gl_free ( )

Release the image from OpenGL graphics memory.

[Related references](INDEX.md).
