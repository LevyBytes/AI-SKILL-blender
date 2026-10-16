# Convex Hull

## Convex Hull

### Convex Hull 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Convex Hull

Wraps the selected vertices in a convex hull. Original edges and faces lying on that hull may get
reused.

This operator also works as a stand-in for Bridge Edge Loops.

Input mesh, loose vertices, and Convex Hull result for both. 

### Options 

Delete Unused
Clears out vertices, edges, and faces that were selected but didn't end up in the hull. Note that
anything used by other, unselected edges and faces survives.

Use Existing Faces
Reuse existing faces lying on the hull where it can, which lets the hull hold n-gons rather than
only triangles and quads.

Make Holes
Delete the edges and faces that got reused — handy when bridging, to clear faces between the
existing mesh and the hull.

Join Triangles
The hull starts out as pure triangles; this option attempts to fuse them into quads. It carries
all the same controls as the Triangles to Quads operator (angle limit, compare UVs, etc.).

Max Face Angle, Max Shape Angle, Compare
See Triangles to Quads.

[Related references](INDEX.md).
