# imbuf

## Image Buffer (imbuf)

### Image Buffer (imbuf)

This module hands you Blender's image manipulation API.

It lets you work with image buffers that sit outside the
bpy.types.Image data-block context.
imbuf. load ( filepath )

Read an image in from a file.

Parameters :

filepath ( str | bytes ) – The filepath of the image.

Returns :

The newly loaded image.

Return type :

ImBuf
imbuf. load_from_buffer ( buffer )

Read an image in from a buffer.

Parameters :

buffer ( collections.abc.Buffer ) – A buffer containing the image data.

Returns :

The newly loaded image.

Return type :

ImBuf
imbuf. new ( size )

Make a fresh image.

Parameters :

size ( tuple [ int , int ] ) – The size of the image in pixels.

Returns :

The newly created image.

Return type :

ImBuf
imbuf. write ( image , * , filepath = None )

Save an image out.

Parameters :

- image ( ImBuf ) – The image to write.

- filepath ( str | bytes | None ) – Optional filepath of the image (fallback to the image’s file path).

[Related references](INDEX.md).
