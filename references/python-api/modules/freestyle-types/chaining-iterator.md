# freestyle.types.ChainingIterator

class freestyle.types. ChainingIterator 

Class hierarchy: Iterator > ViewEdgeIterator > ChainingIterator

The base class for chaining iterators. It is meant to be subclassed so you can spell out chaining rules, which it makes more straightforward to describe. The two key methods to override are traverse() and init(). traverse() decides which ViewEdge to take next among the adjacent ones. Any restriction rules you set (for instance, "chain only ViewEdges in the selection") get folded into the adjacency iterator, so that iterator will halt solely on "valid" edges.
__init__ ( restrict_to_selection = True , restrict_to_unvisited = True , begin = None , orientation = True ) 

__init__ ( brother )

Constructs a Chaining Iterator from the seed ViewEdge iteration begins on plus its orientation, or through the copy constructor.

Parameters :

- restrict_to_selection ( bool ) – Whether chaining is kept confined to the pool of selected ViewEdges or allowed to leave it.

- restrict_to_unvisited ( bool ) – Whether a ViewEdge already used in a chain should be skipped or reused.

- begin (ViewEdge | None) – The ViewEdge the chain starts from.

- orientation ( bool ) – Which way to head when exploring the graph; when true, the direction set by the first ViewEdge is taken.

- brother (ChainingIterator)
init ( ) 

Sets up the iterator's context. It runs at the start of every new chain and is the place to clear any history you may wish to retain.
traverse ( it ) 

Walks across the candidate next ViewEdges and hands back the one chaining should proceed with. The result is either the upcoming ViewEdge or None once the chain has run out.

Parameters :

it (AdjacencyIterator) – The iterator covering the ViewEdges next to the end vertex of the active ViewEdge. Because the adjacency iterator honors the restriction rules, it only visits ViewEdges that qualify.

Returns :

The following ViewEdge to chain to, or None once there is nothing left to chain.

Return type :

ViewEdge | None
is_incrementing 

Set to True whenever the present pass is moving forward by incrementing.

Type :

bool
next_vertex 

The ViewVertex marking the crossing that comes up next.

Type :

ViewVertex
object 

Whatever ViewEdge this iterator is sitting on right now.

Type :

ViewEdge

[Related references](INDEX.md).
