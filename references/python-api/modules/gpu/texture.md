# gpu.texture

## GPU Texture Utilities (gpu.texture)

### GPU Texture Utilities (gpu.texture)

This module bundles helpers for working with textures.
gpu.texture. from_image ( image )

Obtain the GPUTexture tied to an Image data-block. That GPUTexture shares its memory with Blender.
Note: Colors read from the texture will be in scene linear color space and have premultiplied or straight alpha matching the image alpha mode.

Parameters :

image (bpy.types.Image) – The Image data-block.

Returns :

The GPUTexture used by the image.

Return type :

[Related references](INDEX.md).
