# Distribute Points in Volume

## Distribute Points in Volume

Distribute Points in Volume

Creates points inside volume grids in two modes: random or regular grid. Both work on all float grids.

Inputs
Volume: Standard volume geometry input.
Mode:
  Random: Random placement inside the volume. Local count = Density × voxel value. Distribution destabilizes as the volume deforms.
  Grid: Grid pattern inside the volume. Voxel value determines whether to place a point.
Density (Random): Points per unit volume.
Seed (Random): Random number generator seed.
Spacing (Grid): Distance between grid points.
Threshold (Grid): Minimum cell value for a grid point.

Outputs
Points: Standard point cloud geometry output.

[Related references](INDEX.md).
