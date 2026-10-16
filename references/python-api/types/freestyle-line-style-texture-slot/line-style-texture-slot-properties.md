# bpy.types.LineStyleTextureSlot: properties

alpha_factor 

How much the texture affects alpha (in [-inf, inf], default 1.0)

Type :

float
diffuse_color_factor 

How much the texture affects diffuse color (in [-inf, inf], default 1.0)

Type :

float
mapping 

(default 'FLAT' )

- FLAT
Flat – Map X and Y coordinates directly.

- CUBE
Cube – Map using the normal vector.

- TUBE
Tube – Map with Z as central axis.

- SPHERE
Sphere – Map with Z as central axis.

Type :

Literal[‘FLAT’, ‘CUBE’, ‘TUBE’, ‘SPHERE’]
mapping_x 

(default 'X' )

Type :

Literal[‘NONE’, ‘X’, ‘Y’, ‘Z’]
mapping_y 

(default 'Y' )

Type :

Literal[‘NONE’, ‘X’, ‘Y’, ‘Z’]
mapping_z 

(default 'Z' )

Type :

Literal[‘NONE’, ‘X’, ‘Y’, ‘Z’]
texture_coords 

Which texture coordinates map the texture onto the background (default '`ALONG_STROKE`' )

- WINDOW
Window – Use screen coordinates as texture coordinates.

- GLOBAL
Global – Use global coordinates for the texture coordinates.

- `ALONG_STROKE`
Along stroke – Use stroke length for texture coordinates.

- ORCO
Generated – Use the original undeformed coordinates of the object.

Type :

Literal[‘WINDOW’, ‘GLOBAL’, ‘`ALONG_STROKE`’, ‘ORCO’]
use_map_alpha 

Whether the texture acts on the alpha value (default False)

Type :

bool
use_map_color_diffuse 

Whether the texture acts on the stroke's base color (default True)

Type :

bool

[Related references](INDEX.md).
