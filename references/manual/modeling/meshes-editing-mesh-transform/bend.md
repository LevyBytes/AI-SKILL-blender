# Bend

## Bend

### Bend

Reference

Mode:

Object and Edit Modes

Menu:

Object/Mesh/Curve/Surface → Transform → Bend

Shortcut:

Shift - W

This transform warps part of the selection into a circular arc. Compared to Warp, the 3D Cursor lies on the arc itself instead of at its center.

| Description | Description | Description |
| --- | --- | --- |
| Before. | Clamp on. | Clamp off. |

### Usage

- Line the 3D Viewport viewing plane with the plane for bending.

- Set the 3D Cursor at the bend's base. Geometry around it stays put.

- Align the mouse with the geometry to bend, so the line between mouse and cursor lies along the bend direction.

- Press Shift - W and drag to bend the geometry.

- The separation between mouse and cursor determines the bend radius and distortion depth (versus pure rotation).
Press Alt to unlock clamping and bend the entire selection without limit.

- The angle from the original line to the new one determines the bend angle.

- Hit LMB or Return to confirm, or RMB or Esc to cancel.

Note

Unlike most transform tools, Bend ignores transform orientation and pivot point, always using the viewing plane and 3D Cursor instead.

Hint

Repeatedly circling the mouse around the 3D Cursor will apply bending through multiple full rotations.

### Options

Unlike other operators, Bend lacks an Adjust Last Operation panel.

### Example

Multiple consecutive bends.

[Related references](INDEX.md).
