# Scale Elements Node

## Scale Elements Node

### Scale Elements Node

Scales selected faces or edges individually with per-element scale and pivot. Connected faces/edges scale together using average factor and center.

### Inputs

Geometry: Standard input.

Selection: Boolean; targets elements to scale.

Scale: Factor per element.

Center: Pivot per element.

Axis Single Axis Mode Only: Direction vector (auto-normalized).

Scale Mode

Uniform: Same factor all axes.

Single Axis: Single-direction scaling per Axis input.

### Properties

Domain: Element type.

Face: Faces.

Edge: Edges.

### Output

Geometry: Standard output.

### Examples

Effective with Extrude Mesh Node, especially Individual mode where connected faces don't extrude together.

[Related references](INDEX.md).
