# Star Node

## Star Node

Star Node

Generates a star-shaped poly spline by alternating vertices on two concentric circles.

Inputs:
Points: Vertex count on each circle.
Inner Radius, Outer Radius: Distances of the two circles from center. Inner can exceed outer.
Twist: Rotational offset angle. Rotates inner vertices counterclockwise, positioning them between outer vertices.

Outputs:
Curve: The poly spline.
Outer Points: Boolean field marking every second vertex (those on the outer circle).

[Related references](INDEX.md).
