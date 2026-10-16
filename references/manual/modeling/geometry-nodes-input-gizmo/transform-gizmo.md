# Transform Gizmo

## Transform Gizmo

### Transform Gizmo

A compound gizmo, the Transform Gizmo node can steer position, rotation, and scale together.

### Inputs

Value
Special gizmo value socket. Whatever feeds in here changes as the gizmo is adjusted.

Position
Where the gizmo sits in the object's local space.

Rotation
The gizmo's local orientation.

Note

The 3D viewport ignores the rotation input when the transform orientation is set to global.

### Properties

The node carries sidebar properties that let you disable parts of the gizmo. Handy when, for instance, controlling only a translation or only a rotation.

### Outputs

Transform
Meant to be joined into the geometry this gizmo controls.

[Related references](INDEX.md).
