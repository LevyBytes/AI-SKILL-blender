# Mesh to SDF Grid Node

## Mesh to SDF Grid Node

### Mesh to SDF Grid Node

Converts mesh into signed distance field (SDF): each voxel stores shortest distance to surface, signed for inside/outside. Applies to reconstruction, collision, blending, volumetric shape modeling.

Positive = outside, negative = inside, zero = surface.

### Inputs

Mesh: Surface to distance-field.

Voxel Size: Edge dimension. Smaller = finer detail, more memory/compute. Larger = lower precision, faster.

Band Width: Active region width (voxel units). Only voxels near surface store distances; wider band = more overhead.

### Outputs

SDF Grid - Float grid. Each voxel: signed distance to nearest surface point.

[Related references](INDEX.md).
