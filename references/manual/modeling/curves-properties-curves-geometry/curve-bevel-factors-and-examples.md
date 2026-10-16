# Curve bevel factors and examples

Factor Start, End
Percentages along the curve length where geometry begins
and finishes. Default: 0 and 1 (full length);
change to 0.5 and 0.75 to cover just the third quarter.

| Description | Description |
| --- | --- |
| Curve with Factor Start at 0 and End at 1.  | Factor End changed to 0.6.  |

Mapping Start, End
How Factor Start, End percentages map to curve positions.

Resolution :

Count control points only, ignoring spline segment lengths. A three-point spline with Factor Start at 0.5 always starts at the second point,
regardless of its distances to the first and third points.

Segments :

Approximate the percentage along spline length by assuming
all subdivisions in each segment space evenly.

Spline :

Calculate a precise percentage along spline length.

Examples:

Open 2D Curve:

An open (non-cyclic) curve with beveling becomes a tube.

Closed 2D Curve:

A closed (cyclic) curve with beveling becomes a torus by default.
Set Fill Mode to Both for a 2D curve
to fill top and bottom holes with flat discs, making a rounded-edge cylinder.

This doesn't work with 3D curves.

Taper:

Pick a 2D curve as the Taper Object of another (2D or 3D) curve
to vary geometry radius without adding points.

Tilt:

Use the Tilt tool to spin a control point around
its tangent axis, twisting the curve. The example also uses
a custom profile (cross section).

[Related references](INDEX.md).
