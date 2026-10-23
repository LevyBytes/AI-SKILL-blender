# bpy.types.UDIMTile: properties

## UDIMTile(bpy_struct)

### UDIMTile(bpy_struct) 

base class: bpy_struct
class bpy.types. UDIMTile ( bpy_struct ) 

Properties belonging to a UDIM tile.
channels 

How many channels the tile’s pixel buffer holds (in [0, inf], default 0, readonly)

Type :

int
generated_color 

Color used to fill the generated image (array of 4 items, in [0, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
generated_height 

Height of the generated image (in [1, 65536], default 0)

Type :

int
generated_type 

Kind of image to generate (default 'BLANK' )

Type :

Literal[Image Generated Type Items]
generated_width 

Width of the generated image (in [1, 65536], default 0)

Type :

int
is_generated_tile 

Whether this image tile was generated (default False, readonly)

Type :

bool
label 

Label of the tile (default “”, never None)

Type :

str
number 

Index of the position covered by this tile (in [-inf, inf], default 0)

Type :

int
size 

Pixel width and height of the tile buffer, reported as zero when the image data cannot load (array of 2 items, in [-inf, inf], default (0, 0), readonly)

Type :

bpy_prop_array[int]
use_generated_float 

Produce a floating-point buffer (default False)

Type :

bool

[Related references](INDEX.md).
