# Edge Slide

## Edge Slide

### Edge Slide 

Reference

Mode :

Edit Mode

Menu :

Edge ‣ Edge Slide

Shortcut :

G twice

Shifts whatever edges you've picked sideways, gliding them over the faces next to them.

Hint

Use Select Edge Loops to quickly select a chain of edges
that goes around the mesh.

### Usage 

Pick at least one edge, tap G twice, drag the cursor, then LMB to lock it in
(or RMB to back out).

Out of the box, every vertex on the chosen edges shifts by an identical percentage toward
its neighbor:

| Description | Description |
| --- | --- |
| Selected edges.  | Repositioned edges.  |

Switch on Even mode and the vertices instead hold a fixed gap from their neighbor.
Which neighbor each one targets is marked by the red dot:

| Description | Description |
| --- | --- |
| Even Mode enabled.  | Even Mode with Flip enabled.  |

### Options 

The Factor reading appears above the 3D Viewport during the operation, with the shortcut keys
listed in the status bar. The settings remain editable in the Adjust Last Operation panel even
once you've committed with LMB .

Factor
How far and which way to slide. Set it to -1 or 1 to push each edge all the way onto
one neighbor.

Even E
Normally a vertex travels a fixed fraction of its edge's length. Turn on Even and every vertex
instead lands at one identical absolute gap from a neighboring vertex. (Factor stays a relative
value regardless.)

Flipped F
While Even runs, picks the vertex's other neighbor instead.

Clamp Alt or C
Stops the edges short of the faces flanking them, so they can't slide past.

Mirror Editing
Slides the equivalent edges across on the mesh's opposite half too.
This requires Mesh Symmetry to be on.

Correct UVs
Adjusts the moved vertices' UVs so the texture doesn't stretch.

See also

Slide Vertices

[Related references](INDEX.md).
