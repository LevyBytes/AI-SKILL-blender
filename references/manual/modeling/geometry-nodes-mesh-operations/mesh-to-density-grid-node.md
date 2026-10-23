# Mesh to Density Grid Node

## Mesh to Density Grid Node

### Mesh to Density Grid Node

Transforms mesh surface into a volumetric density grid where each voxel holds a scalar for distance to surface (inside vs. outside). Useful for fog volumes, deformable bodies, or volumetric effects.

Output grids feature smooth transitions: high density inside, low outside. Enables continuous blending and field sampling.

### Inputs

Mesh: Surface to voxelize.

Density: Voxel value inside mesh. Convention: 1.0 full, 0.0 empty; any range works.

Voxel Size: Edge length in object units. Smaller = higher detail, more memory. Larger = faster, coarser.

Gradient Width: Transition zone thickness (object units). Controls falloff steepness; wider = softer edge.

### Outputs

Density Grid: Float grid. Interior voxels high, exterior low; smooth ramp controlled by Gradient Width.

[Related references](INDEX.md).
