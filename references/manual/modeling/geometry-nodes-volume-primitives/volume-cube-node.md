# Volume Cube Node

## Volume Cube Node

Generates a volume by evaluating a density field on a 3D grid. Grid points space equally between Min/Max bounds. Density field depends only on Position node. Uses grid point extrema as volume bounds.

Inputs:
- Density: Value for new grid at each voxel
- Background: Value outside Min..Max bounds; voxels equaling background are pruned (memory efficient)
- Min: Left-most grid point; voxel volume lower bound
- Max: Right-most grid point; voxel volume upper bound
- Resolution X,Y,Z: Grid point count per axis; full voxel count = grid points - 1

Note: Resolution changes significantly impact performance (default 32 = ~33k evaluations; 100 = ~1M; 1000 = ~1B)

Outputs:
- Volume: Generated volume geometry

[Related references](INDEX.md).
