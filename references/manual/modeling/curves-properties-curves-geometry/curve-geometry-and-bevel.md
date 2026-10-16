# Geometry: Geometry panel., and Bevel applied (gray tube).

## Geometry

The Geometry panel converts a curve from a 1D line into 2D ribbon or 3D tube geometry.

Geometry panel. 

Three copies of the same base curve: one without geometry (bright orange line);
one with Offset and Extrude applied (blue ribbon); and one with Offset, Extrude,
and Bevel applied (gray tube). 

Offset
Move control points along their normals.

Extrude
Convert the curve from a line into a ribbon by pushing it to the "sides":
at each point, the curve normal becomes the "up" direction,
and the curve extends to the "left" and "right."

Hint

Adjust the direction and distance of Offset and Extrude per point
by changing its Tilt (tangent-axis rotation) and
Radius (scale factor).

Taper Object
A separate Curve object, consisting of a single, non-cyclic,
2D spline, controlling the scale along the length of each curve spline.

Note

The "taper" name is misleading: it means "to reduce toward the end,"
while the Taper Object can scale anywhere. A better name might be "Scale Curve."

Picture the Taper Object as a profile graph: how far along the curve you sit is read off the X axis, while the scale factor applied there is read off the Y axis:

- Its opening spline point maps onto the geometry's opening spline point, and the closing ones line up the same way.

- Arrange them so the earliest taper point carries the largest X value and the final one the smallest
(if the scaling looks inverted, apply Switch Direction).
The absolute X span is irrelevant—[-10, 10], [-1, 1], or anything else behaves identically.

- Where Y sits at 1.0 the geometry stays as-is; 0.5 shrinks it by half,
whereas 2.0 enlarges it twofold.

Any Z component on these points goes unused; flip the object's Shape to "2D" if you wish.

Taper Radius
Combine the Taper Object scale graph with control point radii.

Note

This isn't limited to tapering and doesn't define a single radius.
A better name might be "Scale Curve Mode."

Override :

The Taper Object (scale curve) replaces the radii (scales) of the curve's control points.

Multiply :

The Taper Object scale is multiplied by control point scales.

Add :

The Taper Object scale is added to control point scales.

| Description | Description | Description |
| --- | --- | --- |
| Override mode.  | Multiply mode.  | Add mode.  |

Map Taper
When geometry covers only part of the curve (set via
Factor Start/End), enabling Map Taper aligns
Taper Object endpoints with geometry endpoints instead of curve endpoints.

[Related references](INDEX.md).
