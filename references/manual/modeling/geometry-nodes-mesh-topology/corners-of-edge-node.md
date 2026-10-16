# Corners of Edge Node

## Corners of Edge Node

Corners of Edge Node

Selects a neighboring face corner from an edge and outputs its index.

This node operates across two domains. It calculates Weight for each corner, then for each context item:

- Selects an edge via Edge Index.
- Finds face corners touching the edge.
- Ranks these corners by weight.
- Picks one using Sort Index (0 = lowest weight, 1 = second-lowest).
- Outputs the corner's geometry-wide index.

Warning: Only one corner per face connects through this node. An edge has four neighboring corners total, but Corner Index retrieves only two. Use Offset Corner in Face Node to access the rest.

Inputs
Edge Index: Index of the edge for which to find connected corners. If unconnected, uses the context item index in the Edge domain.
Weights: Corner weights in the geometry. Always evaluated in the Face Corner domain. Corners sort ascending by weight, with ties sorted by index.
Sort Index: Zero-based index for selection from sorted corners. Wraps around if out of range.

Outputs
Corner Index: The geometry-wide index of the selected corner. Pass this to Evaluate at Index Node or Sample Index Node (Face Corner domain). Zero if the edge has no connected corners.
Total: Number of faces connected to the edge.

[Related references](INDEX.md).
