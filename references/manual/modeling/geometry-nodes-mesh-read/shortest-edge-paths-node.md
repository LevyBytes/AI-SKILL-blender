# Shortest Edge Paths Node

## Shortest Edge Paths Node

### Shortest Edge Paths Node

Finds paths along edges to target vertices; cost definition customizable. Default: uniform per-edge; typical: edge length.

Output per-vertex; Next Vertex Index encodes path to nearest endpoint. Dijkstra's algorithm.

Tip: Edge length naturally feeds Edge Cost (Edge Vertices Node + Vector Math distance).

See: Edge Paths to Selection Node, Edge Paths to Curves Node for geometry output.

### Inputs

End Vertex: Selection of path endpoints.

Edge Cost: Per-edge weight.

### Outputs

Next Vertex Index: Following vertex on shortest path to nearest endpoint.

Total Cost: Remaining cost to endpoint.

### Examples

Shortest Edge Paths on deformed Icosphere.

Gradient maze: shortest paths to target.

Organic branching on Suzanne.

[Related references](INDEX.md).
