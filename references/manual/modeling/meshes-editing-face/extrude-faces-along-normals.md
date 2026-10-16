# Extrude Faces Along Normals

## Extrude Faces Along Normals

### Extrude Faces Along Normals 

Reference

Mode :

Edit Mode

Tool :

Toolbar ‣ Extrude Along Normals

Menu :

Face ‣ Extrude Faces Along Normals ,
Mesh ‣ Extrude ‣ Extrude Faces Along Normals

This works much like Extrude Faces, except every vertex travels along its own normal instead of
all of them following one shared axis. So pushing outward on a convex surface enlarges the faces,
for example.

| Description | Description | Description |
| --- | --- | --- |
| Before extrusion  | Regular extrusion  | Extrusion along normals  |

Once extruded, the Adjust Last Operation panel exposes these options:

Flip Normals
Reverses the normals on the new faces, since they can wind up backward depending on which way you
extruded. Check them against the 3D Viewport's Face Orientation overlay.

Dissolve Orthogonal Edges
Turn this on and new faces merge into adjacent existing ones — possibly forming n-gons — wherever
they make up a flat surface together.

Offset
Distance to move the vertices.

Offset Even
Disabled, each vertex moves the same distance. Enabled, each face moves the same distance instead.

You can also flip this mid-extrusion by pressing S or holding Alt . (Those shortcuts show in the
status bar.)

| Description | Description | Description |
| --- | --- | --- |
| Before extrusion  | Offset Even off (default)  | Offset Even on  |

Mirror Editing
This shifts the matching vertices on the mesh's other half without extruding any faces, so it's
of little use here.

Proportional Editing
This also drags the surrounding unselected vertices along their normals, so it's of little use
for extrusion.

See also

Shrink/Fatten for moving vertices along their
normal without extruding.

[Related references](INDEX.md).
