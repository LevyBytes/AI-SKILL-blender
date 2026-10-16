# Trim Gesture Tools: Box Trim, Lasso Trim, Line Trim, Polyline Trim

## Trim Gesture Tools

### Trim Gesture Tools

Reference

Mode :

Sculpt Mode

These tools introduce or subtract geometry based on a defined selection region. This approach excels when establishing a preliminary mesh foundation for subsequent voxel remesher sculpting.

| Description | Description | Description |
| --- | --- | --- |
| Using Lasso Trim set to Join | The symmetrized mesh. | Sculpting with voxel remeshing. |

Newly added geometry receives a fresh Face Set grouping. When subtracting geometry, the interior surfaces generated along the boundary are assigned a new Face Set instead.

Note

For meshes above 100k vertices, Difference and Union operations using the Exact Solver are not recommended. Since Boolean operations power this tool, processing can require significant time. For higher-resolution geometries, the Line Project tool or Fair Positions mode from Edit Face Set are preferable alternatives.

### Box Trim

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Box Trim

Executes a Boolean operation within a box-defined region.

### Lasso Trim

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Lasso Trim

Executes a Boolean operation within a lasso-defined region.

### Line Trim

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Line Trim

Executes a Boolean operation within a line-defined region.

Note

This tool exclusively supports geometry removal. Only Difference is available.

### Polyline Trim

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Polyline Trim

Executes a Boolean operation within a polyline-defined region.

[Related references](INDEX.md).
