# Get Named Grid Node

## Get Named Grid Node

Retrieves a specific voxel grid from a volume by name. Volumes contain multiple grids (density, color, temperature, velocity, etc.); this node accesses one for further processing.

Inputs:
- Volume: Input volume containing named grids
- Name: Grid name to retrieve (must match stored grid)
- Remove: When enabled, removes grid from volume after retrieval; useful for restructuring without duplication or memory management

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines Grid output type and usage in subsequent nodes.

Outputs:
- Volume: Resulting volume after optional grid removal
- Grid: Extracted grid for Name/Data Type; passable to Sample Grid, Grid to Mesh, or other node manipulation

[Related references](INDEX.md).
