# Trim Gesture Tools: Tool Settings

### Tool Settings

Solver
The computational approach for calculating Boolean intersections.

Exact :

Uses an intricate algorithm providing superior outcomes and complete handling of overlapping topology; however, computation is substantially slower.

Float :

Employs a streamlined algorithm with strong speed characteristics; however, it does not fully support overlapping topology.

Manifold :

Typically the quickest option but restricted to Manifold geometries (with the exception of Difference using planes).

Trim Mode
Determines whether geometry is introduced or subtracted.

Difference :

Subtracts geometry and fills any resulting gaps.

Union :

Introduces geometry and connects intersections with pre-existing geometry.

Join :

Comparable to Union but merges the mesh without Boolean interactions.

Shape Orientation
Determines how the trimming shape gets aligned.

View :

Align the trimming shape toward the viewport.

Surface :

Align the trimming shape along surface normals.

Extrude Mode

Fixed :

Generates new geometry with 90-degree angles perpendicular to depth.

Project :

Generates new geometry following viewport perspective for a tapered appearance.

Use Cursor for Depth
Employs cursor placement and scale for trimming dimensions and positioning. If disabled, the operation spans the object's complete depth from the camera view.

[Related references](INDEX.md).
