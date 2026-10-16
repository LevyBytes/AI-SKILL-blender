# bpy.types.ToolSettings: plane_axis, plane_axis_auto, plane_depth, plane_orientation

plane_axis 

Axis along which the base region is placed (default 'Z' )

Type :

Literal[Axis Xyz Items]
plane_axis_auto 

Pick the nearest axis when placing objects, with surfaces taking priority (default True)

Type :

bool
plane_depth 

Starting depth applied when placing the cursor (default 'SURFACE' )

- SURFACE
Surface – Start placing on the surface, using the 3D cursor position as a fallback.

- `CURSOR_PLANE`
Cursor Plane – Start placement using a point projected onto the orientation axis at the 3D cursor position.

- `CURSOR_VIEW`
Cursor View – Start placement using a point projected onto the view plane at the 3D cursor position.

Type :

Literal[‘SURFACE’, ‘`CURSOR_PLANE`’, ‘`CURSOR_VIEW`’]
plane_orientation 

Starting depth applied when placing the cursor (default 'SURFACE' )

- SURFACE
Surface – Use the surface normal (using the transform orientation as a fallback).

- DEFAULT
Default – Use the current transform orientation.

Type :

Literal[‘SURFACE’, ‘DEFAULT’]

[Related references](INDEX.md).
