# Smooth Modifier

## Smooth Modifier

The Smooth modifier flattens the angles between adjacent faces, equivalent to the Smooth tool in Edit Mode. Vertex count stays constant—no subdivision occurs.

The modifier can do more than smoothing. Adjusting the control factor outside the 0.0–1.0 range, including negative values, produces interesting deformations.

Axis toggles deformation in X, Y, and/or Z directions.

Factor controls smoothing intensity. Higher values increase the effect. Values beyond the 0.0–1.0 range distort the mesh.

Repeat sets the iteration count, equivalent to applying Smooth multiple times.

Vertex Group restricts the effect to group vertices, enabling selective real-time smoothing via weight painting.

Invert reverses the group influence.

The algorithm is straightforward: each vertex moves toward the average position of its topologically connected neighbors—a geometric equivalent of image blurring.

[Related references](INDEX.md).
