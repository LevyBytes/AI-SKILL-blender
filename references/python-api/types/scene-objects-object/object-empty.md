# bpy.types.Object: empty_display_size, empty_display_type, empty_image_depth, empty_image_offset, empty_image_side

empty_display_size 

Viewport draw size for empties (in [0.0001, 1000], default 1.0)

Type :

float
empty_display_type 

The viewport drawing style for empties (default '`PLAIN_AXES`' )

Type :

Literal[Object Empty Drawtype Items]
empty_image_depth 

Sets which surrounding objects hide the image (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’, ‘FRONT’, ‘BACK’]
empty_image_offset 

Distance the origin is shifted (array of 2 items, in [-inf, inf], default (-0.5, -0.5))

Type :

bpy_prop_array[float]
empty_image_side 

Choose whether the front or back side is shown (default '`DOUBLE_SIDED`' )

Type :

Literal[‘`DOUBLE_SIDED`’, ‘FRONT’, ‘BACK’]

[Related references](INDEX.md).
