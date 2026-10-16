# Store Named Grid Node

## Store Named Grid Node

Stores a voxel grid in a volume geometry under a specified name. Volumes hold multiple grids (density, temperature, velocity, etc.); accessible later via Get Named Grid. Replaces existing grids with same name; enables grid updates during geometry node evaluation.

Inputs:
- Volume: Volume geometry receiving the grid
- Name: Storage name for grid (used later with Get Named Grid or Spreadsheet Volume Grids section); reuses name replaces existing
- Grid: Grid to store (must have compatible resolution/transform; data type must match node Data Type property)

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines Grid input type and storage correctness.

Outputs:
- Volume: Volume with newly stored grid; replaces same-named predecessor or adds as new entry

[Related references](INDEX.md).
