# Smooth Corrective Modifier

## Smooth Corrective Modifier

The Smooth Corrective modifier reduces distortion in highly warped mesh areas, particularly useful after armature deformation where joint compression is difficult to avoid through weight painting alone.

Understanding its workings is essential for effective use.

Rest State serves as a reference to identify distorted regions, using original vertex positions by default.

Smoothing internally corrects distorted areas using multiple relaxation strategies.

Factor controls smoothing intensity. Higher values amplify the effect. Values beyond 0.0–1.0 distort the mesh.

Repeat sets the number of smoothing iterations, equivalent to applying the Smooth tool multiple times.

Scale adds additional enlargement, compensating for volume loss that sometimes occurs, especially with rigged geometry.

Smooth Type selects the relaxation method:

Simple relaxes vertices toward their connected edge neighbors.

Length Weight applies distance-weighted relaxation, preserving shape better in some cases.

Vertex Group restricts the effect to a specific group, enabling selective, real-time smoothing via weight painting.

Only Smooth previews smoothing before correction applies, for comparison.

Pin Boundaries prevents boundary vertices from shifting.

Rest Source determines the reference vertex positions:

Original Coordinates uses the unmodified input positions, requiring the same vertex count in input and output.

Bind Coordinates optionally references a stored state, necessary when prior modifiers (Subdivision Surface, Mirror) add geometry.

[Related references](INDEX.md).
