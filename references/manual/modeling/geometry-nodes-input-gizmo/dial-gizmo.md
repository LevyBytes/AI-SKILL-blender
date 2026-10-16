# Dial Gizmo

## Dial Gizmo

### Dial Gizmo

The Dial Gizmo node is well suited to building gizmos that control angles.

### Inputs

Value
Special gizmo value socket. Anything wired into this socket gets modified as the gizmo is rotated.

Position
Where the gizmo sits in the object's local space.

Up
The gizmo's up or normal direction in the viewport.

Screen Space
On, the gizmo holds the same on-screen size whatever the zoom level. This shifts what the radius input means.

Radius
In screen-space mode, a factor layered on top of the default radius. Otherwise, the gizmo's radius in Blender units.

### Properties

Color
Sets which theme color this gizmo uses.

### Outputs

Transform
Meant to be joined into the geometry this gizmo controls.

[Related references](INDEX.md).
