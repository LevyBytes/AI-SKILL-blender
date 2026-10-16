# Laplacian Deform Modifier

## Laplacian Deform Modifier

The Laplacian Deform modifier poses a mesh while maintaining surface detail preservation.

The user marks certain vertices as "anchors," then moves some of them. The modifier keeps unmoved anchors fixed and recalculates all other vertices to preserve the original local geometry—curvature and surface direction based on neighbors.

This works using differential coordinates, which encode local shape information from each vertex and its neighbors.

An Anchors Vertex Group is required; without it the modifier has no effect.

Repeat sets iteration count to refine the solution. More iterations better preserve geometry but take longer. The algorithm seeks optimal rotation of differential coordinates to maintain details.

Anchor Weights specifies the vertex group controlling deformation. Only vertices with weight > 0 participate; their weight values do not affect behavior, only presence.

Invert reverses the group influence.

Bind instructs the modifier to capture the current surface geometry, so moving anchors changes the deformed shape.

Unbind, after binding, allows changing the Anchors Vertex Group. Rebinding is required after group modifications.

Error messages:

"Vertex group X is not valid" appears when the group is deleted or renamed.

"Vertices changed from X to Y" indicates vertex count changes.

"Edges changed from X to Y" indicates edge count changes.

"The system did not find a solution" means the solver failed.

For meshes exceeding 100,000 vertices, nonlinear optimization may fail.

Laplacian Surface Editing, developed by Olga Sorkine et al. in 2004, preserves details during editing operations. Differential coordinates express local shape as the difference between a vertex and the weighted average of its neighbors.

[Related references](INDEX.md).
