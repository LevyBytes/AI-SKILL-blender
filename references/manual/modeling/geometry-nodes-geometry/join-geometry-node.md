# Join Geometry Node

## Join Geometry Node

Join Geometry Node

Merges multiple geometry sources into a single result. Output data type reflects the union of inputs.

Note: Cannot handle multiple volume inputs simultaneously.

Materials:
When inputs carry different material sets, output consolidates all materials from all inputs.

Attributes:
During merging, the highest-complexity data type is chosen. Example: weight boolean on one input and vector on another becomes vector on output.

Note: Vertex groups survive instance realization and geometry joining. If domain and type rules produce vertex domain and float type, the attribute becomes a vertex group on output.

Inputs:
Geometry: Geometries to merge. Multiple links accepted. Muting passes only the first link.

Outputs:
Geometry: Standard geometry output.

[Related references](INDEX.md).
