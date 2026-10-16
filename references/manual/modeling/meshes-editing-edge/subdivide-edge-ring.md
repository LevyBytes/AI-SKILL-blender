# Subdivide Edge-Ring

## Subdivide Edge-Ring

### Subdivide Edge-Ring 

Reference

Mode :

Edit Mode

Panel :

Edge ‣ Subdivide Edge-Ring

Cuts an edge ring into more loops, with interpolation if you want it.

Note

To Blender, an edge ring is any run of edges lying across a strip of joined faces and running
crosswise to that strip. The strip may close into a loop, but needn't — a "ribbon" counts just as
well as a "ring."

See also Select Edge Rings.

### Options 

Number of Cuts
The number of edge loops to create along the edge ring.

Interpolation
How to place the new edge loops.

Linear
Place the new edge loops in a straight line.

Blend Path
Lays the new loops along a Bézier spline, ignoring the surrounding surface entirely.

Blend Surface
Lays the new loop vertices along Bézier splines while accounting for the normals of the
surrounding surface.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Before subdividing  | Linear  | Blend Path  | Blend Surface  |

Smoothness
Controls smoothness for the Blend Path and Blend Surface interpolations. At 1 you get full Bézier
splines; at 0 the result is effectively Linear .

Profile Factor
Strength of the Profile Shape . Go negative to pinch the ring's middle inward, positive to bulge
it outward.

Profile Shape
How the ring's thickness varies between its middle and its ends.
See the Proportional Editing page
for a description of each option.

[Related references](INDEX.md).
