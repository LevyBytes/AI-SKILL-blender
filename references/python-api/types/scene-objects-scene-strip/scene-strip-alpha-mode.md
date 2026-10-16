# bpy.types.SceneStrip: alpha_mode

alpha_mode

How alpha is represented within the RGBA pixels (default 'STRAIGHT' )

- STRAIGHT
Straight – In transparent pixels, the RGB channels stay independent of the alpha channel.

- PREMUL
Premultiplied – In transparent pixels, the RGB channels are scaled by the alpha channel.

Type :

Literal[‘STRAIGHT’, ‘PREMUL’]

[Related references](INDEX.md).
