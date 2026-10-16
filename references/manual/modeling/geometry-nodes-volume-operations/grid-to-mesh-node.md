# Grid to Mesh Node

## Grid to Mesh Node

Converts a voxel grid to a polygonal mesh by extracting an isosurface at a specified threshold (similar to Marching Cubes). The boundary where grid values cross the threshold becomes the mesh surface. Enables conversion of procedural volumetric data (SDFs, density grids) into geometry for rendering or further modeling.

Inputs:
- Grid: Voxel grid to convert (must contain float values from SDF or density field)
- Threshold: Value defining the surface; voxels > threshold are inside, smaller are outside. For SDF, threshold 0.0 typically marks the surface
- Adaptivity: Mesh simplification by curvature; higher values reduce polygon count by merging flat areas; 0.0 disables adaptivity for uniform density

Outputs:
- Mesh: Extracted surface where grid scalar values equal Threshold; usable for rendering or further processing

[Related references](INDEX.md).
