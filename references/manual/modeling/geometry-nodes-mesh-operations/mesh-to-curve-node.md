# Mesh to Curve Node

## Mesh to Curve Node

### Mesh to Curve Node

Converts mesh geometry into one or more curve splines using two modes:

- Edges: Each connected sequence of edges becomes a poly spline. Intersecting edge chains split into separate splines.
- Faces: Each face becomes a closed spline. Much faster than Edges because it parallelizes and avoids attribute duplication.

Isolated vertices are excluded. Both named and unnamed attributes transfer to output splines. If a radius attribute exists, it applies automatically; alternatively use Set Curve Radius Node.

### Inputs

Mesh: Standard mesh input.

Selection: Boolean field on edges; determines which edges convert to curves. More efficient than pre-deleting parts.

### Properties

Mode: Conversion strategy.

Edges: Poly splines from edge chains.

Faces: Closed splines from faces.

### Outputs

Curve: Generated curve.

[Related references](INDEX.md).
