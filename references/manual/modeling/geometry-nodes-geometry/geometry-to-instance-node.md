# Geometry to Instance Node

## Geometry to Instance Node

Geometry to Instance Node

Wraps every connected input as a separate instance. Visually resembles Join Geometry Node but outputs instances rather than merged data. Faster than Join Geometry on large inputs because data merging is avoided.

Useful with Pick Instances in Instance on Points Node to select among node-tree-generated geometries (vs. picking from Collection Info Node instances).

Inputs:
Geometry: Input geometries to wrap. Multiple links accepted. Muting passes only the first link.

Outputs:
Geometry: Standard geometry output.

Examples:
Paired with Instance on Points Node to randomly pick among primitives.

[Related references](INDEX.md).
