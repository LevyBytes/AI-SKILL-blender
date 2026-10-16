# Warp

## Warp

### Warp

Reference

Mode:

Edit Modes

Menu:

Object/Mesh/Curve/Surface → Transform → Warp

This transform warps part of the selection into a circular arc.
Compared to Bend, the 3D Cursor sits at the arc center rather than on the arc itself.

### Usage

- Orient the 3D Viewport viewing plane toward the warp plane.

- Locate the 3D Cursor at the warp center.

- Click Warp in the menu.

- Adjust options in the Adjust Last Operation panel.

| Before. | Warp Angle 90°. |
| --- | --- |
| Warp Angle 180°. | Warp Angle 360°. |

Note

Unlike most transform tools, Warp disregards transform orientation and pivot point, always using the viewing plane and 3D Cursor instead.

### Options

Warp Angle
The arc's size into which to deform the selection.

Offset Angle
Direction angle for the line from 3D Cursor to selection center.
0° points straight up; higher values proceed clockwise.

Min/Max
Distance from the centerline to the leftmost/rightmost geometry that enters the arc. Geometry beyond these limits rotates but doesn't curve.

Warping with an Offset Angle of 45°, a Min and Max of -0.5 and 0.5,
and a Warp Angle of 90°.

### Example

Text wrapped around logo.

This was produced by building the Blender logo and text as separate objects.
The text was converted to a mesh and then warped around the logo.

[Related references](INDEX.md).
