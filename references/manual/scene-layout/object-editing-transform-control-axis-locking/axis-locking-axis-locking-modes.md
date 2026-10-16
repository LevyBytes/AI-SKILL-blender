# Axis Locking: Axis Locking Modes

### Axis Locking Modes 

A single press of a key locks movement to the current transform orientation setting.
A second press of the same key locks movement to the matching world axis
(if the transform orientation is already Global, the Local orientation is selected instead).
A third press removes all limits.

The orientation is configured
in the Transform Orientation
dropdown of the viewport header.

For example, when transform orientation is set to Normal,
hitting G to start moving, then Z locks moving
in the Z direction according to the Normal orientation. Pressing Z
a second time locks moving to the world Z direction.
Pressing Z once more deactivates all limits.
The active mode appears in the left corner of the viewport header.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Z axis locking in world space.  | Z axis locking in object space.  | Z axis locking in world space with vertex selection.  | Z axis locking in Normal space with vertex selection.  |

As shown in the Axis locking modes example,
the movement direction considers the selection too.

Note that using an axis lock doesn't block numerical transform entry.

[Related references](INDEX.md).
