# Editing Normals: Flip, Recalculate

## Editing Normals

### Editing Normals 

Press Alt - N to open the Normals menu as a popover.

Most operators here act on custom split normals — normal vectors tied to face corners rather than
vertices. You can select those corners in several ways:

- In Vertex or Edge selection mode, picking a vertex or edge also picks the nearest corners of the
faces it belongs to.

- In Face mode, picking a face also picks its corners.

- With both Vertex and Face modes on, picking a vertex and then adding a face selects only the
matching face corner.

- Likewise, with both Edge and Face modes on, picking an edge and then adding a face selects only
the two matching face corners.

See also

- The 3D Viewport overlay for visualizing normals.

- The Geometry Data panel of the mesh properties for
clearing custom normals.

- Mesh Data Transfer (operator
or modifier) for copying normals from
another mesh.

- The Normal Edit Modifier and the
Weighted Normal Modifier for calculating or changing normals
based on certain criteria.

### Flip 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Flip

Reverses the orientation of the selected faces, swapping their "front side" for their "back side"
and vice versa. Custom split normals are untouched.

The 3D Viewport's Face Orientation overlay makes wrongly oriented faces easy to catch.

### Recalculate 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Recalculate Outside and
Mesh ‣ Normals ‣ Recalculate Inside

Shortcut :

Shift - N and Shift - Ctrl - N

Flips the orientation of selected faces wherever needed so they all face outward (or inward). The
mesh doesn't have to be a closed volume for this to work.

Like Flip, this leaves custom split normals untouched.

[Related references](INDEX.md).
