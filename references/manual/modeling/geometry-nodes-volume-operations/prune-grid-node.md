# Prune Grid Node

## Prune Grid Node

Optimizes voxel grid storage by collapsing uniform regions into coarser tiles or inner nodes (inverse of Voxelize Grid). Detects large uniform areas and replaces them with compact representations. Especially useful after operations creating constant-value regions (filling, clipping, thresholding).

Inputs:
- Grid: Grid to optimize

Pruning methods (Mode):
- Inactive: Turns inactive voxels/tiles into inactive background tiles; basic cleanup for empty regions
- Threshold: Collapses regions where all voxels have approximately same value and active state (within tolerance) into background tiles; good for fog/scalar grids with smooth variations
- SDF: Specialized for signed distance fields; replaces inactive tiles with inactive nodes for faster, targeted pruning without threshold comparison; efficient for narrow-band SDFs with large interior/exterior regions

Threshold parameter: Regions are uniform if voxel values differ by less than this amount; higher thresholds enable aggressive simplification; lower values preserve finer detail

Properties:
Data Type: Grid data type (Float, Integer, Boolean, Vector). Must match input.

Outputs:
- Grid: Optimized grid with uniform regions collapsed into larger tiles/nodes for compact, efficient representation

[Related references](INDEX.md).
