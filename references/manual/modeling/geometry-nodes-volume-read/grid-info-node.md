# Grid Info Node

## Grid Info Node

Retrieves structural and metadata information about a voxel grid. Provides spatial transform and background value details describing grid positioning and inactive-voxel storage. Useful for inspecting or reusing grid parameters in other operations (aligning transforms, matching resolutions, reconstructing fields with consistent background).

Inputs:
- Grid: Voxel grid to query

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines Grid input type and Background Value output type.

Outputs:
- Transform: Transform matrix converting grid index space to object space; defines voxel positioning, scaling, orientation in 3D; passable to Set Grid Transform or alignment operations
- Background Value: Default value for inactive voxels (as set by Set Grid Background or similar); represents empty value in outside regions

[Related references](INDEX.md).
