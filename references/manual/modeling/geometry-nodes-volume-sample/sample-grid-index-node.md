# Sample Grid Index Node

## Sample Grid Index Node

Retrieves values directly from a voxel grid at specific integer indices rather than arbitrary spatial positions. Unlike Sample Grid (interpolates in object space), this node reads exact stored voxel values at specified coordinates. Useful for index-space work (voxel neighborhood lookups, procedural filtering, sampling from Voxel Index).

Inputs:
- Grid: Voxel grid to sample (stores scalar, vector, color, or boolean data per type)
- X, Y, Z: Integer voxel coordinates in index space; specifies voxel to retrieve along each axis

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines Grid input type and Value output type.

Outputs:
- Value: Voxel value at specified indices; output type matches grid Data Type; no interpolation—values sampled exactly as stored

[Related references](INDEX.md).
