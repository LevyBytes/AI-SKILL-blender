# Extrude Faces

## Extrude Faces

### Extrude Faces 

Reference

Mode :

Edit Mode

Menu :

Face ‣ Extrude Faces ,
Mesh ‣ Extrude ‣ Extrude Faces

Shortcut :

E

This builds new faces around the edge of your selection, then lets you drag the selected faces
along an axis with the cursor. The result is an extrusion — a square turns into a box, a disc into
a cylinder, and so on. Modeling leans on it constantly, for adding limbs to characters, branches
to trees, and the like.

When the faces sit where you want them, press LMB or Return to confirm. RMB or Esc cancels the
move and returns the selected faces to where they began, though the new faces remain.

The extrusion axis defaults to the average of the face normals, but you can override this
Axis Locking by tapping an axis key ( X , Y , or Z ):

- Press once to use the corresponding global axis.

- Press twice to use the average of the faces' local axes.

- Press three times to disable axis locking (allows moving the faces anywhere).

| Description | Description | Description |
| --- | --- | --- |
| Selected face.  | During extrude.  | Using the global Z axis.  |

Once extruded, the Adjust Last Operation panel exposes these options:

Flip Normals
Reverses the normals on the new faces, since they can wind up backward depending on which way you
extruded. Check them against the 3D Viewport's Face Orientation overlay.

Dissolve Orthogonal Edges
Turn this on and new faces merge into adjacent existing ones — possibly forming n-gons — wherever
they make up a flat surface together.

Orientation
Determines the extrusion axis to use.

Mirror Editing
This shifts the matching faces on the mesh's other half without extruding them, so it's of little
use here.

Proportional Editing
This drags the surrounding unselected faces along with the extruded ones, so it's of little use
here.

[Related references](INDEX.md).
