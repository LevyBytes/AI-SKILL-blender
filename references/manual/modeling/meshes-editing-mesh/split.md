# Split

## Split

### Split

Press Alt - M to open the Split menu as a popover.

These tools handle splitting meshes by disconnecting faces from one another.
For cutting faces into smaller pieces, consult the Knife Topology Tool or the Connect Vertex Path operator.

### Split Selection

Reference

Mode:

Edit Mode

Menu:

Mesh → Split → Selection

Shortcut:

Y

Severs the mesh along the border of selected faces, allowing them to be repositioned elsewhere.

This operator also disconnects "wires" (edges not belonging to a face). However, applying it to edges that are part of a face duplicates them instead.

Disconnecting inner faces from their surroundings.

See also

The Separate operator disconnects selection and transfers it into a new mesh object.

### Split Faces by Edges

Reference

Mode:

Edit Mode

Menu:

Mesh → Split → Faces by Edges

Splits the mesh along selected edges, allowing vertices to be pulled apart and forming gaps.

Splitting by selected edges.

See also

Rip Vertices also cuts adjoining unselected edges.

### Split Faces & Edges by Vertices

Reference

Mode:

Edit Mode

Menu:

Mesh → Split → Faces & Edges by Vertices

Cuts the mesh at all adjacent edges of each selected vertex. (This differs from Rip Vertices, which cuts only two edges per vertex.)

Vertices can then be separated to create gaps.

Splitting by selected vertices.

[Related references](INDEX.md).
