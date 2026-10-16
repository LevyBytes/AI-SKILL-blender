# freestyle.types.AdjacencyIterator

class freestyle.types. AdjacencyIterator 

Class hierarchy: Iterator > AdjacencyIterator

The class behind the adjacency iterators that the chaining process relies on. A ChainingIterator spins one up inside its increment() and decrement() methods and hands it off to the ChainingIterator's traverse() method.
__init__ ( ) 

__init__ ( brother )
__init__ ( vertex , restrict_to_selection = True , restrict_to_unvisited = True )

Constructs an AdjacencyIterator via the default constructor, the copy constructor, or the overloaded one.

Parameters :

- brother (AdjacencyIterator) – An AdjacencyIterator object.

- vertex (ViewVertex) – The vertex that forms the next crossing.

- restrict_to_selection ( bool ) – Whether chaining is kept confined to the pool of selected ViewEdges or allowed to leave it.

- restrict_to_unvisited ( bool ) – Whether a ViewEdge already used in a chain should be skipped or reused.
is_incoming 

True when the current ViewEdge runs toward the iteration vertex, False otherwise.

Type :

bool
object 

The ViewEdge this iterator currently points at.

Type :

ViewEdge

[Related references](INDEX.md).
