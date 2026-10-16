# mathutils.bvhtree.BVHTree: overlap ( other_tree , / )

overlap ( other_tree , / )

Locate the overlapping indices shared between two trees.

Parameters :

other_tree (BVHTree) – Other tree to perform overlap test on.

Returns :

Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree .

Return type :

list[tuple[int, int]]

[Related references](INDEX.md).
