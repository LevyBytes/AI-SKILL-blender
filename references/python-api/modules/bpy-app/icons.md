# bpy.app.icons

## Application Icons (bpy.app.icons)

### Application Icons (bpy.app.icons)
bpy.app.icons. new_triangles ( range , coords , colors )
Creates a new icon from triangle geometry.
Parameters:
- range ( tuple [ int , int ] ) – Pair of ints.
- coords ( bytes ) – Sequence of bytes (6 floats for one triangle) for (X, Y) coordinates.
- colors ( bytes ) – Sequence of bytes (12 for one triangle) for RGBA.
Returns: Unique icon value (pass to the interface icon_value argument).
Return type: int
bpy.app.icons. new_triangles_from_file ( filepath )
Creates a new icon from triangle geometry.
Parameters: filepath ( str | bytes ) – File path.
Returns: Unique icon value (pass to the interface icon_value argument).
Return type: int
bpy.app.icons. release ( icon_id )
Releases the icon.
Parameters: icon_id ( int ) – The icon id to release.

[Related references](INDEX.md).
