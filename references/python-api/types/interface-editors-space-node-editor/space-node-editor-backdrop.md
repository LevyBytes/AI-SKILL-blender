# bpy.types.SpaceNodeEditor: backdrop_channels, backdrop_offset, backdrop_zoom

backdrop_channels

Which channels of the image get drawn (default 'COLOR' )

- `COLOR_ALPHA`
Color & Alpha – Display image with RGB colors and alpha transparency.

- COLOR
Color – Display image with RGB colors.

- ALPHA
Alpha – Display alpha transparency channel.

- RED
Red.

- GREEN
Green.

- BLUE
Blue.

Type :

Literal[‘`COLOR_ALPHA`’, ‘COLOR’, ‘ALPHA’, ‘RED’, ‘GREEN’, ‘BLUE’]
backdrop_offset

Backdrop offset (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
backdrop_zoom

Backdrop zoom factor (in [0.01, inf], default 1.0)

Type :

float

[Related references](INDEX.md).
