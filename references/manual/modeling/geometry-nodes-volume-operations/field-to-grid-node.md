# Field to Grid Node

## Field to Grid Node

Creates new voxel grids by sampling geometry fields on an existing grid's topology. Evaluates input fields at voxel positions, producing grids that match resolution, transform, and domain.

Inputs:
- Topology: Reference grid defining voxel layout, resolution, and transform
- Fields: Additional sockets for each field to evaluate (add by dragging into blank area)

Note: Color fields evaluate as Vector data type (color grids not yet supported)

Properties:
Configure each field individually: set data type (Float, Vector, Boolean) and evaluation order

Outputs:
- One grid per field input, each containing sampled voxel data aligned with input topology

[Related references](INDEX.md).
