# Bevel: Options

### Options

While operating, settings appear at the viewport's top. Pick a setting via keyboard shortcut (status bar shows all), then drag the cursor or type a number. Press Shift while dragging to slow down for finer control, or Ctrl to jump in larger increments.

After applying with LMB, Adjust Last Operation panel preserves further changes.

Affect V

Vertices
Round selected vertices, keeping edges unchanged.

Edges
Round selected edges and vertices where three or more edges join.

Width Type M
What the Width setting represents. In the examples below, Width is 50% for "Percent" and 1.0 for others.

| Before beveling | Offset | Width |
| --- | --- | --- |
| Depth | Percent | Absolute |

Width A
Bevel size/radius. Width Type determines its exact meaning.

Note

When multiple edges are beveled simultaneously, matching widths across all edges may be impossible.
Bevel compromises in such cases.
Disabling Loop Slide (below) sometimes helps.

Segments S
Geometry density. Higher values yield smoother results.

While active, Wheel adjusts this setting even if not selected.

Profile Shape P
A value between 0 and 1 managing the bevel profile shape (viewed from the edge's side).

When Miter Outer or Miter Inner is Arc, this also governs miter shape.

Material Index
The 0-based material slot index for newly created faces.
Use -1 to inherit from neighbors.

Harden Normals H
When on, applies custom split normals to new faces, creating smooth appearance without altering the rest.

Clamp Overlap C
Blocks beveled edges from extending past neighboring face ends.

Loop Slide
Whether new inner edges stay perpendicular to the beveled edge or follow existing inner edge directions.

| Description | Description | Description |
| --- | --- | --- |
| Before beveling. | Loop Slide off. | Loop Slide on. |

Mark

Seams U
When beveling three or more connected edges and two are marked UV Seams, new edges between them get marked too.

Sharp K
Mirrors Mark Seams but for Sharp edges.

| Description | Description | Description |
| --- | --- | --- |
| Before beveling. | Mark Seams off. | Mark Seams on. |

[Related references](INDEX.md).
