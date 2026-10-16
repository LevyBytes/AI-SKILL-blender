# mathutils.kdtree.KDTree

class mathutils.kdtree. KDTree ( size ) 

KDTree(size) -> new kd-tree initialized to hold up to size items.

Parameters :

size ( int ) – Maximum number of items.

Note

KDTree.balance() must have been called before using any of the find methods.
balance ( ) 

Rebuild and balance the tree.

Note

Constructing the whole tree happens here, so don't run it per insert.
find ( co , * , filter = None ) 

Locate the single point closest to co .

Parameters :

- co ( Sequence [ float ] ) – 3D coordinate.

- filter ( Callable [ [ int ] , bool ] | None ) – callable fed an index that returns True to keep that index in the search.

Returns :

Yields the triple (position, index, distance), falling back to (None, None, None) if nothing matches.

Return type :

tuple[ Vector , int, float] | tuple[None, None, None]
find_n ( co , n ) 

Locate the n points nearest to co .

Parameters :

- co ( Sequence [ float ] ) – 3D coordinate.

- n ( int ) – Number of points to find.

Returns :

Yields a list whose entries are (position, index, distance) triples.

Return type :

list[tuple[ Vector , int, float]]
find_range ( co , radius ) 

Gather every point lying no further than radius from co .

Parameters :

- co ( Sequence [ float ] ) – 3D coordinate.

- radius ( float ) – Furthest reach within which points still count.

Returns :

Yields a list whose entries are (position, index, distance) triples.

Return type :

list[tuple[ Vector , int, float]]
insert ( co , index ) 

Add a single point to the KDTree.

Parameters :

- co ( Sequence [ float ] ) – Point 3d position.

- index ( int ) – Identifier tag for the point; zero or positive only.

[Related references](INDEX.md).
