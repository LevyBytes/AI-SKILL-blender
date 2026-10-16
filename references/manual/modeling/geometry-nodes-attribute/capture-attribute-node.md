# Capture Attribute Node

## Capture Attribute Node

This node preserves one or more fields across a geometry, making them available to downstream nodes.

This differs from Store Named Attribute in that capture generates anonymous attributes (no name needed, no name-collision risk), making it ideal for temporary values.

The new attribute only exists in the geometry this node outputs, not in upstream or sibling branches.

Geometry: Standard input.
Capture Items: The fields to keep. Connect new outputs or use the Properties panel list. Rename by Ctrl+LMB clicking in the node or double-clicking in the list.

Domain: Which attribute category to store the data on.

Capture Items List

Reference

Menu: Sidebar ‣ Node ‣ Properties ‣ Capture Items

A list for adding, removing, reordering, and renaming inputs.

Data Type: The data kind of the active input.

Geometry: Standard output.
Attribute: One output per captured field.

Common scenario: Convert a Curve to a Mesh while preserving curve-specific information. The Spline Parameter node works only on curves, not meshes. Capture Attribute solves this by storing the parameter on each control point before conversion. The Curve to Mesh node then propagates these values to mesh vertices. Later, you reconnect to the same Capture Attribute node to retrieve them.

[Related references](INDEX.md).
