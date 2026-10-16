# Extrude Mesh Node: Inputs, Properties, Output, Examples, Attribute Propagation, Vertex Mode

## Extrude Mesh Node

### Extrude Mesh Node

Extrude Mesh builds fresh edges or faces from the selected elements, then pushes them outward along an offset.

Similar to mesh edit-mode extrude tools, but with differences: the node never retains back-faces (they are always removed), and attribute propagation rules may differ.

### Inputs

Mesh
Input geometry.

Selection
Boolean: which elements to extrude.

Offset
Displacement vector per extruded element. Default: element normal.

Tip: If all elements move the same direction, connect a Vector Node to improve performance by skipping normal calculation.

Offset Scale
Multiplier for the displacement vector.

Individual Face Mode Only
Extrude each face separately vs. groups of connected faces.

### Properties

Mode

Vertices:
Add a freestanding edge at each selected vertex.

Edges:
Add a quad face at each selected edge. Vertices shared by selected edges are shared in the duplicated edges.

Note: New-face normals may be arbitrary depending on connectivity. When all selected edges have one adjacent face, consistent orientation is possible; with multiple or zero adjacent faces, normals may need manual correction.

Faces:
Extrude contiguous selected-face regions or each face individually (based on Individual input). Connected-face boundaries spawn "side" faces. Interior vertices/edges/faces move but don't duplicate. A fully-selected manifold mesh simply scales outward.

### Output

Mesh
Output geometry.

Top
Boolean: "top" elements in the extrusion. Vertices mode: new vertices; Edges mode: new edges; Faces mode: moved faces.

Side
Boolean: "side" elements. Vertices mode: new edges; Edges and Faces modes: newly-created faces (moved faces excluded in Faces mode).

### Examples

Selection outputs set materials on certain faces. A Random Value Node limits extrusions to random faces.

### Attribute Propagation

Attributes transfer to new elements under specific rules. An attribute never changes domains. The id attribute has no special handling.

Boolean attributes generally propagate with "or" logic: any "true" connection causes the new value to be "true."

### Vertex Mode

New edges use the average of all connected edges.

- New vertices copy from originals.

- New edges average from any connected original edges. Booleans: selected if any connected edge was selected.

[Related references](INDEX.md).
