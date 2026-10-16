# Clean Up: Delete Loose, Decimate Geometry, Degenerate Dissolve

## Clean Up

### Clean Up 

This set of operators can tidy several kinds of messy geometry on their own.

### Delete Loose 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Delete Loose

Removes the selected vertices, edges, and — if you want — faces that connect to nothing.

### Decimate Geometry 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Decimate Geometry

Cuts the face count of the selected geometry while keeping shape changes to a minimum.

Ratio
Target ratio for the triangle count. Enter 0.4, for instance, to keep collapsing edges until only
40% of the original triangles remain.

Vertex Group
Steer edge collapsing by the active vertex group. Heavier vertex weights on an edge raise its
odds of being collapsed, even ahead of otherwise "better" (shorter) candidates.

Weight
A multiplier applied to the vertex weights.

Invert
Flips the vertex weights, so lighter-weighted edges collapse first.

Symmetry
Hold the result symmetric across the X , Y , or Z axis.

See also

The Decimate Modifier in Collapse mode
performs the same operation non-destructively.

### Degenerate Dissolve 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Clean up ‣ Degenerate Dissolve

Collapses selected edges below a set length, which also clears out small faces along the way.

Two vertices close together but not joined by an edge won't merge; see Merge By Distance for
that case.

Merge Distance
Any edge below this length gets collapsed away.

[Related references](INDEX.md).
