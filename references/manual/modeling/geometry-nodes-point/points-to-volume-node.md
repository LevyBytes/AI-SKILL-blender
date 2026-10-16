# Points to Volume Node

## Points to Volume Node

Points to Volume Node

Generates a fog volume sphere around every point. The grid is named "density".

Usually combine with Volume to Mesh Node.

Warning: Point positions should not be extremely large. Billion-scale values give unstable results.

Inputs
Points: Standard geometry input.
Density: Voxel value inside the fog volume.
Resolution Mode: How to specify voxel size.
  Amount: Approximate voxels along the diagonal.
  Size: Voxel side length. Tweaking carefully—small changes affect time significantly.
Voxel Amount (Amount): Approximate voxels along the diagonal.
Voxel Size (Size): Voxel side length.
Radius: Sphere radius generated per point.

Outputs
Volume: Standard geometry output.

[Related references](INDEX.md).
