# Corners of Vertex Node

## Corners of Vertex Node

Corners of Vertex Node

Selects a neighboring face corner from a vertex and outputs its index.

This node operates across two domains. It calculates Weight for each corner, then for each context item:

- Selects a vertex via Vertex Index.
- Finds face corners touching the vertex.
- Ranks corners by weight.
- Picks one using Sort Index (0 = lowest weight, 1 = second-lowest).
- Outputs the corner's geometry-wide index.

Inputs
Vertex Index: Index of the vertex for which to find corners. If unconnected, uses the context item index in the Point domain.
Weights: Corner weights in the geometry. Always evaluated in the Face Corner domain. Corners sort ascending by weight, with ties sorted by index.
Sort Index: Zero-based index for selection from sorted corners. Wraps around if out of range.

Outputs
Corner Index: The geometry-wide index of the selected corner. Pass this to Evaluate at Index Node or Sample Index Node (Face Corner domain).
Total: Number of adjacent corners, equivalent to the face count.

[Related references](INDEX.md).
