# Arc Node

## Arc Node

The Arc node builds a poly spline arc. Two modes: Radius and Points.

Resolution: Edge count on the arc.
Radius: Arc radius (Radius mode).
Start Angle: Arc beginning angle (Radius mode).
Sweep Angle: Arc length (Radius mode).
Connect Center: Link the arc's center point.
Invert Arc: Draw the opposite arc.
Start, Middle, End: Three arc points (Points mode). Order sets direction (clockwise/counterclockwise). Start-to-End is always via Middle; use Invert Arc to flip.
Offset Angle: Arc angle offset (Points mode).

Note: Finite resolution means the middle point may not lie exactly on the arc.

Mode:

Points: Arc determined by three points; center, radius, and normal are output.
Radius: Arc determined by radius, start angle, and sweep angle.

Curve: Poly spline from inputs.
Center: Arc center (Points mode only).
Normal: Plane normal pointing toward +Z (Points mode only).
Radius: Arc radius (Points mode only).

[Related references](INDEX.md).
