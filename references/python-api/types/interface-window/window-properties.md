# bpy.types.Window: properties

## Window(bpy_struct)

### Window(bpy_struct)

base class — bpy_struct
class bpy.types. Window ( bpy_struct )

An open window.
height

Window height (in [0, 32767], default 0, readonly)

Type :

int
modal_operators

The modal operators that are running right now (default None, readonly)

Type :

bpy_prop_collection[Operator]
parent

This window's active workspace and scene track this one (readonly)

Type :

Window
scene

Scene currently being edited in this window (never None)

Type :

Scene
screen

Workspace screen currently shown in this window (never None)

Type :

Screen
stereo_3d_display

Settings for stereo 3D display (readonly, never None)

Type :

Stereo3dDisplay
support_hdr_color

True when the window provides an HDR graphics buffer that accepts wide-gamut, high-dynamic-range colors in extended sRGB space. (default False, readonly)

Type :

bool
view_layer

View layer of the active workspace shown in this window (never None)

Type :

ViewLayer
width

Window width (in [0, 32767], default 0, readonly)

Type :

int
workspace

Workspace currently shown in this window (never None)

Type :

WorkSpace
x

The window's horizontal position (in [-32768, 32767], default 0, readonly)

Type :

int
y

The window's vertical position (in [-32768, 32767], default 0, readonly)

Type :

int

[Related references](INDEX.md).
