# bpy.types.StudioLight: properties

## StudioLight(bpy_struct)

### StudioLight(bpy_struct)

base class: bpy_struct
class bpy.types. StudioLight ( bpy_struct )

A studio light.
has_specular_highlight_pass

Studio light image file has separate “diffuse” and “specular” passes (default False, readonly)

Type :

bool
index

(in [-inf, inf], default 0, readonly)

Type :

int
is_user_defined

(default False, readonly)

Type :

bool
light_ambient

Color of the ambient light that uniformly lit the scene (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Color
name

(default “”, readonly, never None)

Type :

str
path

(default “”, readonly, never None)

Type :

str
solid_lights

Lights used to display objects in solid draw mode (default None, readonly)

Type :

bpy_prop_collection[UserSolidLight]
type

(default 'STUDIO' , readonly)

Type :

Literal[‘STUDIO’, ‘WORLD’, ‘MATCAP’]

[Related references](INDEX.md).
