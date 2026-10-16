# bpy.types.PreferencesSystem: image_draw_method

image_draw_method

How images are drawn on the screen (default 'AUTO' )

- AUTO
Automatic – Let the GPU and image decide the method.

- 2DTEXTURE
2D Texture – Do the display transform on the CPU and show the image as a 2D texture.

- GLSL
GLSL – Do the display transform with GLSL shaders and show the image as a 2D texture.

Type :

Literal[‘AUTO’, ‘2DTEXTURE’, ‘GLSL’]

[Related references](INDEX.md).
