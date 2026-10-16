# Sample Grid Node

## Sample Grid Node

Retrieves values from a voxel grid at given spatial positions. Evaluates stored data (float, integer, boolean, or vector) and returns interpolated result for each queried position. Useful for reading grids from other nodes (Mesh to SDF Grid, Field to Grid, Points to SDF Grid) and driving procedural effects, geometry deformation, shading.

Inputs:
- Grid: Grid to sample (stores scalar, vector, or color data per data type)
- Position: Spatial positions in object space; each position interpolates based on nearby voxel values

Interpolation method:
- Nearest Neighbor: Returns closest voxel value without interpolation; fastest; can appear blocky/discrete
- Trilinear: Linear interpolation across eight nearest voxels; smooth transitions; suitable for general use
- Triquadratic: Higher-order (quadratic) interpolation; even smoother gradients, more continuous; additional computation cost

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Determines output socket type.

Outputs:
- Value: Interpolated grid value at given positions; output type matches grid Data Type

[Related references](INDEX.md).
