# Corners of Face Node

## Corners of Face Node

Corners of Face Node

Selects a corner from a face and outputs its index.

This node operates across two domains. It calculates Weight for each corner, then for each context item:

- Picks a face via Face Index.
- Finds corners on the face.
- Ranks corners by weight.
- Selects one using Sort Index (0 = lowest weight, 1 = second-lowest).
- Outputs the corner's geometry-wide index.

Inputs
Face Index: Index of the face for which to find corners. If unconnected, uses the context item index in the Face domain.
Weights: Corner weights in the geometry. Always evaluated in the Face Corner domain. Corners sort ascending by weight, with ties sorted by index.
Sort Index: Zero-based index for selection from sorted corners. Wraps around if out of range.

Outputs
Corner Index: The geometry-wide index of the selected corner. Pass this to Evaluate at Index Node or Sample Index Node (Face Corner domain).
Total: Number of corners in the face, equivalent to the edge count.

[Related references](INDEX.md).
