# bpy.types.MaterialGPencilStyle: fill_color, fill_image, fill_style

fill_color

Color that fills the region enclosed by each stroke (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
fill_image

Type :

Image
fill_style

Choose the style used to fill strokes (default 'SOLID' )

- SOLID
Solid – Fill area with solid color.

- GRADIENT
Gradient – Fill area with gradient color.

- TEXTURE
Texture – Fill area with image texture.

Type :

Literal[‘SOLID’, ‘GRADIENT’, ‘TEXTURE’]

[Related references](INDEX.md).
