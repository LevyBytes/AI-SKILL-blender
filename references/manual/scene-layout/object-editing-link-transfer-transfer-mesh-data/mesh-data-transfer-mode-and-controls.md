# Transfer Mesh Data: Object Mode, Object ‣ Link/Transfer Data ‣ Transfer Mesh Data

## Transfer Mesh Data

### Transfer Mesh Data

Reference

Mode :

Object Mode

Menu :

Object ‣ Link/Transfer Data ‣ Transfer Mesh Data

This operation duplicates a particular data category from the active mesh to the selected meshes. This could be UV maps, color attributes, custom normals, and more.

For each component (vertex/edge/face) in each destination mesh, the operator identifies one or more matching components in the source mesh, then interpolates between those source component values.

See also

Data Transfer Modifier

The Adjust Last Operation panel offers the following options.

Freeze Operator
Blocks settings changes from re-running data transfer. Helpful when adjusting multiple settings simultaneously with complex geometry.

Data Type
Which data to transfer.

Data types.

Create Data
Introduces any missing data layers to the destination meshes (e.g. create missing vertex groups).

Mapping
The method for finding matching source component(s) for each destination component. Various options are described in the Mapping section.

Auto Transform
When source and destination meshes do not align in world space, enable this option to determine a transformation algorithmically. Though quick and convenient, manual overlap may yield superior results.

Object Transform
Whether to factor in the world space transformations of source and destination objects. Unchecked means all objects are treated as if in the same position with default rotation and scale.

Only Neighbor Geometry
Evaluate only source elements near the destination component.

Max Distance
The highest acceptable distance between source and destination component (for non-topology mappings).

Ray Radius
The initial radius for ray casting operations.

For specified mapping types, the operator executes a series of ray casts from each destination component to locate matching source components. These casts start at the specified radius and progressively increase until a match is found or a limit is reached.

A low starting radius yields higher precision but diminishes performance if overly compact. A high starting radius improves efficiency but may yield suboptimal matches.

Generally, use a low radius for high-density source meshes and a high one for simpler ones.

Islands Precision
Governs the computation preventing destination faces from obtaining UV coordinates from disparate source UV islands (seam-bordered regions). A value of 0.0 skips island handling, while higher values enhance accuracy at the cost of additional computation.

Typically, modest values like 0.02 achieve good outcomes, but when mapping from extremely high-poly sources to extremely low-poly destinations, you may need substantially higher values.

[Related references](INDEX.md).
