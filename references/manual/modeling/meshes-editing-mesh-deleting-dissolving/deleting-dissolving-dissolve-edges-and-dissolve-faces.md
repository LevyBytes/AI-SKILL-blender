# Deleting & Dissolving: Dissolve Edges, Dissolve Faces

### Dissolve Edges 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete ‣ Dissolve Edges

Shortcut :

X , Delete , or Ctrl - X

Removes each selected edge and fuses its surrounding faces into one, but only for edges with
exactly two neighboring faces.

The Adjust Last Operation panel offers the following options:

Dissolve Vertices
Dissolve the selected edges' vertices too, not merely the edges.

Angle Threshold
With Dissolve Vertices on, this preserves vertices at corners while still dissolving those in
flattish areas. Two faces count as a corner when the angle between their normals tops this value —
so coplanar faces register as 0°, not 180°.

Face Split
Where possible, splits surrounding faces so only a corner triangle merges rather than the whole
face. This shrinks the final "hole-filling" faces and evens them out.

### Dissolve Faces 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete ‣ Dissolve Faces

Shortcut :

X , Delete , Ctrl - X , or F

Collapses each patch of connected faces down to one face.

Note

The F shortcut is normally used for creating faces, but when run on a selection of existing faces,
it dissolves them instead. See Dissolve Existing Faces.

| Description | Description |
| --- | --- |
| Before dissolving.  | After dissolving.  |

[Related references](INDEX.md).
