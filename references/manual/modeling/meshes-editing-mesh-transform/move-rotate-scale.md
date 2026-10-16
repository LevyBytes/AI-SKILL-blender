# Move, Rotate, Scale

## Move, Rotate, Scale

### Move, Rotate, Scale

Reference

Mode:

Edit Mode

Tool:

Toolbar → Move, Rotate, Scale

Menu:

Mesh → Transform → Move, Rotate, Scale

Shortcut:

G , R , S

Displace G, rotate R, or expand S selected vertices, edges, or faces.
Gizmos for transformation provide an alternative.

See also

- Manipulation in 3D Space

- Transform Orientation

- Transform Pivot Point

Proportional Editing influences these transformations.

Pressing G twice launches Vertex Slide or Edge Slide based on the current selection.

### Transform Panel

Reference

Mode:

Edit Mode

Panel:

Sidebar region → Item → Transform

This panel displays the selected vertex or edge properties.
When several items are selected, averages display instead.

X/Y/Z
Coordinates for the selected vertex. (With multiple selected vertices, the label reads "Median," though technically the panel computes geometric center rather than geometric median.)

Space
Coordinate display: Local Space or Global Space.

### Vertex Data

Bevel Weight
Commonly paired with the Bevel Modifier (with Affect as Vertices). The modifier normally applies identical bevel to all vertices, but when Limit Method is Weight, each vertex's Bevel Weight acts as a multiplier. This enables smaller or absent bevels on specific vertices.

Internally stored as an attribute called bevel_weight_vert. The Named Attribute Node in geometry nodes can also read this.

Crease
Higher Crease values make corners at the vertex appear more acute when using the Subdivision Surface Modifier.

Stored internally as an attribute named crease_vert.

Radius X/Y
The radii for the Skin Modifier.
Only displays when the mesh uses this modifier.

### Edge Data

When an edge is selected, these appear:

Bevel Weight
Commonly paired with the Bevel Modifier (with Affect as Edges). See vertex Bevel Weight above.

Stored internally as an attribute named bevel_weight_edge.
Also configurable through the Edge Bevel Weight operator.

Crease
Higher Crease values make corners at the edge appear more acute when using the Subdivision Surface Modifier.

Stored internally as an attribute named crease_edge.
Also configurable through the Edge Crease operator.

[Related references](INDEX.md).
