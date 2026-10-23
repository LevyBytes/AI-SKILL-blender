# bpy.types.Image: overview

class bpy.types. Image ( ID )

An Image data-block that points at an external or packed image.
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
## Image(ID)

### Image(ID)
### Image Data

An Image data-block is a thin layer wrapping one or more image or video files (held on disk, packed inside, or generated).

The real payload — pixel data, dimensions, resolution and so on — lives in an imbuf.types.ImBuf image buffer (or in several of them, as happens with UDIM textures, multi-views or animations…).

Because of this, a number of the Image data-block's properties and methods actually read from or write to its image buffer rather than to the data-block.

Warning

A notable catch: image buffers are never shared across separate Image data-blocks, nor are they copied when an image is duplicated.

That means edits to an image buffer stay confined until the buffer is written to disk; duplicating the Image data-block beforehand will not carry the buffer changes over to the new Image.

The script below builds an Image data-block at a chosen size, alters its first pixel, resizes it, then makes a duplicate.

The copy keeps the dimensions and colors the original had when it was first made; every edit to the original's buffer is ‘lost’ in the duplicate.

```python
import bpy

image_src = bpy.data.images.new('src', 1024, 102)
print(image_src.size)
print(image_src.pixels[0:4])

image_src.scale(1024, 720)
image_src.pixels[0:4] = (0.5, 0.5, 0.5, 0.5)
image_src.update()
print(image_src.size)
print(image_src.pixels[0:4])

image_dest = image_src.copy()
image_dest.update()
print(image_dest.size)
print(image_dest.pixels[0:4])
```

base classes: bpy_struct, ID

[Related references](INDEX.md).
