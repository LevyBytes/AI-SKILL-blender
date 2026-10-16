# Select Linked: Options, Linked Flat Faces

### Options

Edge Tag Edge Mode
What happens to the selected edges:

Select :

Just select them.

Tag Seam :

Flag them as UV Seams.

Tag Sharp :

Flag them as Sharp.

Tag Crease :

Set their Crease to 1.0.

Tag Bevel :

Set their Bevel Weight to 1.0.

Tag Freestyle Edge Mark :

Flag them as Freestyle edges.

Face Stepping
Permits diagonal paths for vertices and faces, and edge rings for edges.

Topology Distance
Favors the route over the fewest edges instead of the shortest spatial distance.

Fill Region Shift - Ctrl - LMB
Grabs every shortest path at once rather than a single one.

Deselected, Selected, Offset
Lets the path come out "dashed" instead of solid, a recurring run of a few skipped elements then a few selected ones. See also Checker Deselect.

### Linked Flat Faces

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Linked ‣ Linked Flat Faces

Spreads the selection across connected faces until it hits a sharp corner.

Sharpness
The widest angle two faces may span and still pass as one flat surface. Read off the face normals, so coplanar faces sit at 0° (not 180°), and the sharper the corner the larger the angle (not the smaller).

| Description | Description | Description |
| --- | --- | --- |
| Initial selection.  | After running Select Linked Flat Faces.  | Comparison to Select Similar ‣ Normal .  |

To halt the selection at edges you manually marked Sharp, use Linked instead.

[Related references](INDEX.md).
