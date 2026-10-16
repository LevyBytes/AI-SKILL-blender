# Points to SDF Grid

## Points to SDF Grid

Points to SDF Grid

Generates a Signed Distance Field (SDF) grid from input points. Each voxel stores the shortest signed distance to the nearest point, representing them as smooth, volumetric shapes.

Positive values = outside point influence, negative = inside, zero = surface of the implicit sphere.

Useful for constructing volumetric fields or collision volumes from particles, instances, or procedural clouds.

Inputs
Points: Input points defining the SDF centers.
Radius: Influence radius per point. Each point is a sphere; distance extends this far. Defines how far signed distance reaches.
Voxel Size: Voxel size in object units. Smaller = higher resolution, finer detail, more memory and time.

Outputs
SDF Grid: A scalar float grid of the signed distance field. Each voxel holds the shortest distance to any point's surface—negative inside the spheres, positive outside.

[Related references](INDEX.md).
