# bpy.types.MovieTrackingStabilization: filter_type

filter_type

Which interpolation handles the sub-pixel shifts and rotations introduced by stabilization (default 'NEAREST' )

- NEAREST
Nearest – No interpolation, use nearest neighbor pixel.

- BILINEAR
Bilinear – Simple interpolation between adjacent pixels.

- BICUBIC
Bicubic – High quality pixel interpolation.

Type :

Literal[‘NEAREST’, ‘BILINEAR’, ‘BICUBIC’]

[Related references](INDEX.md).
