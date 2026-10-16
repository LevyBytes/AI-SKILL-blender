# SDF Grid Boolean Node

## SDF Grid Boolean Node

Performs boolean operations on two or more Signed Distance Field grids. Combines, subtracts, or intersects volumetric shapes directly in grid space with smooth, continuous results. Preserves the SDF property (each voxel stores shortest distance to nearest surface).

Inputs:
- Grid Intersect: Input for intersection operations; keeps overlapping regions only
- Grid 1 (Union/Difference): Base grid for boolean combination
- Grid 2 (Union/Difference): Grid to add or subtract from Grid 1

Operations:
- Intersect: Keeps overlapping region where both grids contain interior (negative) values
- Union: Combines by taking minimum distance at each voxel; merged shape of both inputs
- Difference: Inverts Grid 2's sign then takes maximum distance; carves one SDF out of another

Outputs:
- Grid: Resulting SDF after operation; maintains valid signed distance values; usable with Grid to Mesh or further volumetric operations

[Related references](INDEX.md).
