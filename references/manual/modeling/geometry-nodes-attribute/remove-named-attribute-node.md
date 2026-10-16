# Remove Named Attribute Node

## Remove Named Attribute Node

The Remove Named Attribute node strips a named attribute from geometry.

All geometry-based attributes propagate automatically when the geometry updates, which can be expensive. This node optimizes by removing unneeded attributes, improving node-tree performance and scene memory.

Most named attributes can be deleted. For some Built-In Attributes, removal causes Blender to use a default. For instance, removing cyclic on curves makes all curves non-cyclic.

Geometry: Standard input.

Pattern Mode: Selection method.

Exact: Delete only the named attribute.
Wildcard: Delete all attributes matching the pattern (single * allowed).

Name: The attribute to delete.

Geometry: Standard output.

[Related references](INDEX.md).
