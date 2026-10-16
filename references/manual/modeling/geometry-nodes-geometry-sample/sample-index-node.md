# Sample Index Node

## Sample Index Node

The Sample Index node retrieves values from a source geometry at a specific index.
Tip: when the input Geometry is the same as the geometry from the field context, this node is equivalent to the Evaluate at Index Node, which is usually preferable — avoiding the geometry socket makes the whole setup easier to reuse and share in other situations.
Tip: the Point domain is shared across components (Mesh, Point Cloud, Curve); this node simply samples the Value from the first non-empty component, checked in the order Mesh, Point Cloud, Curve. Use the Separate Components Node to sample directly from a specific component.

Inputs:
Geometry — the geometry to retrieve the attribute from.
Value — a field to evaluate on the source Geometry; the values are then retrieved from specific indices for the output.
Index — which index to use when retrieving data from the input Value field; any index can be connected, resulting in a "shuffling" of the values.

Properties:
Data Type — the data type to use for the retrieved values.
Domain — the attribute domain the attribute is transferred from — in other words, the domain used to evaluate the input; for example, it is possible to transfer data from the faces of one geometry to the points of another.
Clamp — clamp the indices to the size of the attribute domain instead of outputting a default value for invalid indices.

Outputs:
Value — the data retrieved from the source Geometry input.

Examples: here the node copies the positions of one object to another, recreating the behavior of the Transfer Attribute node from Blender versions before 3.4; it works best when the geometries have the same number of points and the same Topology.

[Related references](INDEX.md).
