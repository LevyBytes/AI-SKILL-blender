# Intersect (Knife)

## Intersect (Knife)

### Intersect (Knife) 

Reference

Mode :

Edit Mode

Menu :

Face ‣ Intersect (Knife)

Lays new edges everywhere faces cross one another.

| Description | Description |
| --- | --- |
| Before intersect.  | After intersect.  |

See also

Intersect (Boolean) in Union mode doesn't
just create intersection edges, but also removes faces that end up enclosed in a volume.

### Options 

Source

Self Intersect
Cross selected faces against other selected faces.

Selected/Unselected
Cross selected faces against unselected faces.

Separate Mode
Whether faces get disconnected from one another after the edges are made.

All :

Split every face apart at each intersection edge.

Cut :

When Source is Selected/Unselected , detach only the selected faces from the unselected ones.
Otherwise it acts the same as All .

Merge :

Keep every face joined at each intersection edge.

| Description | Description | Description |
| --- | --- | --- |
| Separate All: the cylinder and the plane stay separate and are each split in two.  | Separate Cut: the cylinder and the plane stay separate.  | Merge: the cylinder and the plane are connected to each other.  |

Solver
Algorithm used to calculate the intersections.

Float
A lightweight solver: fast, but with no support for overlapping geometry.

Merge Threshold
How close two faces must be to count as touching. Raising it can help when intersections that
ought to register don't, or when stray geometry appears because edges aren't read as overlapping.

Warning

A threshold approaching the size of faces may cause very slow calculation.
In general, keep this value small.

Exact
A heavier solver: slowest of the two, but it gives the best results and fully supports
overlapping geometry.

[Related references](INDEX.md).
