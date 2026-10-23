# Volume to Mesh Node

## Volume to Mesh Node

Builds a mesh at the volume surface. A threshold value specifies the surface boundary; voxels exceeding the threshold count as interior.

Inputs:
- Volume: Standard geometry input

Resolution Mode - Controls final mesh resolution:
- Grid: Resolution depends on converted grid resolution; higher grids yield higher-resolution meshes; often most efficient
- Voxel Amount: Specifies approximate final mesh resolution; voxel size adapts to volume size
- Voxel Size: Uses fixed resolution independent of volume changes

Voxel Amount: Approximate final mesh resolution; voxel size adapts to volume dimensions

Voxel Size: Fixed resolution unaffected by volume changes

Threshold: Voxels > threshold are inside; mesh generates on inside/outside boundary ("iso value")

Adaptivity: Reduces final face count by simplifying geometry where detail is unnecessary (similar to decimation)

Outputs:
- Mesh: Standard geometry output

[Related references](INDEX.md).
