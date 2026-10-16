# Edges of Vertex Node

## Edges of Vertex Node

Edges of Vertex Node

Selects a neighboring edge from a vertex and outputs its index.

This node operates across two domains. It evaluates a Weight for each edge, then for each context item:

- Picks a vertex via Vertex Index.
- Locates edges connected to the vertex.
- Sorts these edges by weight.
- Picks an edge using Sort Index (0 = lowest weight, 1 = second-lowest).
- Outputs the geometry-wide edge index.

Inputs
Vertex Index: Index of the vertex for which to find edges. If unconnected, uses the context item index in the Point domain.
Weights: Edge weights in the geometry. Always evaluated in the Edge domain. Edges sort ascending by weight, with ties sorted by index.
Sort Index: Zero-based index for selection from sorted edges. Wraps around if out of range.

Outputs
Edge Index: The geometry-wide index of the selected edge. Pass this to Evaluate at Index Node or Sample Index Node (Edge domain). Zero if the vertex has no connected edges.
Total: Number of edges connected to the selected vertex.

Example: Creating Vertical-Aligned Cones on Cube Vertices

This example places a cone at each cube vertex, aligned to the most vertical neighboring edge.

First, each cube edge receives a "verticality score" by subtracting vertex positions for the direction vector, normalizing, and computing the Z-axis dot product. The absolute value gives a 0–1 range (0 = fully horizontal, 1 = fully vertical).

Since edges sort by ascending weight, set weight = 1 − verticality so the most vertical edge ranks first.

Next, in the point domain, calculate cone rotation using Align Rotation to Vector Node, requiring only the direction vector.

The cone's direction is the midpoint of the most vertical neighboring edge minus the vertex position. Edges of Vertex selects that edge (Sort Index = 0), then Evaluate at Index Node retrieves its midpoint.

Finally, Instance on Points Node creates the cones using the calculated rotations.

[Related references](INDEX.md).
