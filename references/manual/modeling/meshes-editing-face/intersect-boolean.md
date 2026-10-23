# Intersect (Boolean)

## Intersect (Boolean)

### Intersect (Boolean) 

Reference

Mode :

Edit Mode

Menu :

Face ‣ Intersect (Boolean)

Runs Boolean operations between your selected geometry and the unselected geometry.

Selecting a sphere and performing an Intersection, Union, and Difference
with a cube. 

Tip

Hide geometry by pressing H to exclude it from the operation,
then Alt - H afterwards to unhide it again.

See also

The Boolean Modifier can perform these same operations
non-destructively between different mesh objects.

The Adjust Last Operation panel offers the following options:

Boolean Operation

Intersect :

Keep only the volume sitting inside both the selected and unselected geometry.

Union :

Strip out the interior faces between the selected and unselected geometry.

Difference :

Carve the selected geometry out of the unselected, then discard the selected geometry.

Solver
Algorithm used to perform the Boolean operation.

Float :

A lightweight solver: fast, but with no support for overlapping geometry.

Merge Threshold
How close two faces must be to count as touching. Raising it can help when intersections that
ought to register don't, or when stray geometry appears because edges aren't read as overlapping.

Warning

A threshold approaching the size of faces may cause very slow calculation.
In general, keep this value small.

Exact :

A heavier solver: slowest of the two, but it gives the best results and fully supports
overlapping geometry.

Swap
With Difference , this carves the unselected geometry out of the selected geometry rather than the
reverse.

Self Intersection
Handles self-intersection in the participating geometry properly, trading away some performance.

[Related references](INDEX.md).
