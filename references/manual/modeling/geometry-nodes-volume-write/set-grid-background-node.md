# Set Grid Background Node

## Set Grid Background Node

Defines the background value for a voxel grid—the value returned when sampling inactive regions or uninitialized tiles. By default, empty voxels evaluate to zero or an implicit value; this node customizes that behavior. Useful for procedural grid construction or multi-grid combination.

Inputs:
- Grid: Grid whose background value modifies
- Background: Value assigned to inactive/uninitialized voxels and tiles; returned when sampling outside defined region instead of zero
- Update Inactive: Override all values in inactive voxels as well

Properties:
Data Type: Grid data type (determines Background input type and grid value types: Float, Integer, Boolean, Vector)

Outputs:
- Grid: Grid with updated background value; passable to Sample Grid Index or Sample Grid for consistent out-of-region results

[Related references](INDEX.md).
