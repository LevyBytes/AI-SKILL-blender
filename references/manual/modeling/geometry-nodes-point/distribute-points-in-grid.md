# Distribute Points in Grid

## Distribute Points in Grid

Distribute Points in Grid

Generates points within the active region of a voxel grid. Point count and placement use the grid's density values and distribution parameters.

Useful for procedurally scattering geometry in volumetric regions—distributing particles in fog, populating simulation domains, or sampling SDF/density grid areas.

Inputs
Grid: Input grid defining the volume for point distribution. Values determine placement—typically by density or occupancy.
Density (Random): Scaling factor for voxel values, setting expected points per unit volume. Higher = denser.
Seed (Random): Seed for reproducible results. Change to alter the random distribution.
Spacing (Grid): Distance between points in Grid mode. Controls packing tightness.
Threshold (Grid): Minimum voxel density to place a point. Ignores below-threshold voxels.

Properties
Distribution Method: How to scatter points.
  Random: Random placement weighted by voxel density, creating a natural, stochastic pattern.
  Grid: Regular grid pattern. Spacing input sets point distance.

Outputs
Points: Generated points inside the grid's active volume, distributed per method and parameters.

[Related references](INDEX.md).
