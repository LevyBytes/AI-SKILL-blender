# bpy.types.Area: properties

## Area(bpy_struct)

A region of subdivided screen space.

base class — bpy_struct
class bpy.types. Area ( bpy_struct )

One subdivision of a screen displaying an editor.
height

Area height (in [0, 32767], default 0, readonly)

Type :

int
regions

Regions this area is subdivided in (default None, readonly)

Type :

bpy_prop_collection[Region]
show_menus

Show menus in the header (default True)

Type :

bool
spaces

Spaces contained in this area, the first being the active space (NOTE: Useful for example to restore a previously used 3D view space in a certain area to get the old view orientation) (default None, readonly)

Type :

AreaSpaces[Space]
type

Current editor type for this area (default '`VIEW_3D`' )

Type :

Literal[Space Type Items]
ui_type

Current editor type for this area

Type :

str
width

Area width (in [0, 32767], default 0, readonly)

Type :

int
x

The window relative vertical location of the area (in [-inf, inf], default 0, readonly)

Type :

int
y

The window relative horizontal location of the area (in [-inf, inf], default 0, readonly)

Type :

int

[Related references](INDEX.md).
