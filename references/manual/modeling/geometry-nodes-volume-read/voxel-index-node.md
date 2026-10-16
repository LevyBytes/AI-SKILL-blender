# Voxel Index Node

## Voxel Index Node

The Voxel Index node outputs the integer index of the voxel the field is currently being evaluated on. Unlike a position in object space, the voxel index gives the discrete cell coordinates inside a voxel grid, so you can reason about neighboring voxels directly in index space without converting through world or object space. Combine it with nodes such as Integer Math and Sample Grid Index to sample values from nearby voxels by offsetting the indices.

Inputs: this node has no inputs.

Outputs:
X, Y, Z — the integer indices of the current voxel in the grid along each axis. They identify which voxel the field is sampling at this evaluation point, and can be offset (for example, add or subtract 1 on X) and passed to Sample Grid Index to read values from neighboring voxels.
Tile:
Is Tile — whether the current evaluation is happening on a tile rather than on a single voxel. For performance, some operations evaluate fields on tiles that cover multiple voxels at once, and then the coordinates from X, Y, and Z alone don't describe the full covered region; if this is false, the extent is always 1.
Extent X, Extent Y, Extent Z — the number of voxels along each axis of the tile. For a normal voxel the extent on each axis is 1; for a tile covering multiple voxels, the extents describe how many voxels are grouped together in X, Y, and Z. Use these to detect and handle cases where an evaluation represents an aggregated region (a tile) instead of an individual voxel, so the result isn't misinterpreted as referring to just one voxel.

[Related references](INDEX.md).
