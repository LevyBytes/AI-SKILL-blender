# Curve Modifier

## Curve Modifier

The Curve modifier bends a mesh, curve, surface, or lattice along a path, deforming it as if following a rail.

The modifier works along a dominant axis (X, Y, or Z, selectable). Moving the object along the dominant direction (default X) travels the object along the curve. Moving perpendicular to it shifts the object toward or away from the path.

Beyond the curve's endpoints, deformation continues based on the direction vector at those ends.

The modifier uses global space, so actual geometry position relative to the curve matters. Position the object origin at its geometry center (use Set Origin to Geometry if needed) and align the object's origin with the curve's origin initially (use snap tools).

If the curve is 3D, Tilt values on control points twist the deformed object. The Radius property scales it. These settings are in the Curve panel under Path/Curve-Deform.

Curve Object specifies the path to follow.

Deformation Axis selects which direction the object travels (X, Y, Z, or their negatives).

Vertex Group restricts the effect to a specific group.

Invert reverses the group effect.

[Related references](INDEX.md).
