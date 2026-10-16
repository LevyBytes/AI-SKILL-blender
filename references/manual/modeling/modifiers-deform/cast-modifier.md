# Cast Modifier

## Cast Modifier

The Cast modifier deforms meshes, curves, surfaces, or lattices toward a predefined shape—sphere, cylinder, or cuboid. It is equivalent to the To Sphere tool in Edit Mode, though supporting multiple target shapes.

Pairing Cast with the Smooth modifier improves visual quality, as cast shapes sometimes benefit from smoothing to resolve distortions.

The modifier operates in local space only. Incorrect results may indicate that the object's transformations need application, particularly when casting to cylinders.

Shape selects the target: Sphere, Cylinder, or Cuboid.

Axis toggles the effect along X, Y, Z axes (only X and Y for Cylinder, as Z is unaffected).

Factor controls the blend between original and cast positions. At 0.0, no change occurs; at 1.0, full casting applies. Values outside the 0.0–1.0 range exaggerate results in sometimes interesting ways.

Radius, if nonzero, restricts the effect to vertices inside a spherical zone. Outside vertices remain unaffected.

Size sets an alternative target shape size. When zero, the initial shape and control object (if present) determine it.

Size from Radius, when active, calculates Size from Radius for smoother transitions.

Vertex Group restricts the effect to a specific group, enabling selective, real-time casting via weight painting.

Invert reverses the group effect.

Object names a control object whose origin defines the projection center. Its scale and rotation also transform the cast vertices, allowing animation of the control object to animate casting deformation.

[Related references](INDEX.md).
