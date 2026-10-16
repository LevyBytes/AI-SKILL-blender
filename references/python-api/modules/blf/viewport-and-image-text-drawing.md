# blf viewport and image text drawing

## Font Drawing (blf)

### Font Drawing (blf) 

This module provides access to Blender's text drawing functions.

### Hello World Text Example 

Example of using the blf module. For this module to work we
need to use the GPU module gpu as well.

```python
# Import stand alone modules.
import blf
import bpy

font_info = {
    "font_id": 0,
    "handler": None,
}


def init():
    """init function - runs once"""
    import os
    # Create a new font object, use external TTF file.
    font_path = bpy.path.abspath('//Zeyada.ttf')
    # Store the font index - to use later.
    if os.path.exists(font_path):
        font_info["font_id"] = blf.load(font_path)
    else:
        # Default font.
        font_info["font_id"] = 0

    # Set the font drawing routine to run every frame.
    font_info["handler"] = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback_px, (None, None), 'WINDOW', 'POST_PIXEL')


def draw_callback_px(self, context):
    """Draw on the viewports"""
    # BLF drawing routine.
    font_id = font_info["font_id"]
    blf.position(font_id, 2, 80, 0)
    blf.size(font_id, 50.0)
    blf.draw(font_id, "Hello World")


if __name__ == '__main__':
    init()
```

### Drawing Text to an Image 

Example showing how text can be drawn into an image.
This can be done by binding an image buffer (imbuf) to the font's ID.

```python
import blf
import imbuf

image_size = 512, 512
font_size = 20

ibuf = imbuf.new(image_size)

font_id = blf.load("/path/to/font.ttf")

blf.color(font_id, 1.0, 1.0, 1.0, 1.0)
blf.size(font_id, font_size)
blf.position(font_id, 0, image_size[1] - font_size, 0)

blf.enable(font_id, blf.WORD_WRAP)
blf.word_wrap(font_id, image_size[0])

with blf.bind_imbuf(font_id, ibuf, display_name="sRGB"):
    blf.draw_buffer(font_id, "Lots of wrapped text. " * 50)

imbuf.write(ibuf, filepath="/path/to/image.png")
```

[Related references](INDEX.md).
