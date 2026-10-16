# freestyle.chainingiterators.ChainPredicateIterator

class freestyle.chainingiterators. ChainPredicateIterator 

Class hierarchy: freestyle.types.Iterator >
freestyle.types.ViewEdgeIterator >
freestyle.types.ChainingIterator >
ChainPredicateIterator

A flexible ViewEdge iterator whose behaviour you steer yourself, assembled out of one unary and one binary predicate. The unary test runs first against every candidate next ViewEdge, retaining only those that meet its constraint. The binary test then compares the current ViewEdge against each survivor of that first pass. Whichever ViewEdge clears both tests becomes the next one in the chain; should no candidate satisfy the pair of predicates, None comes back instead.
__init__ ( upred , bpred , restrict_to_selection = True , restrict_to_unvisited = True , begin = None , orientation = True )
__init__ ( brother )

Constructs a ChainPredicateIterator either from a unary predicate, a binary predicate, a seed ViewEdge and its orientation, or via the copy constructor.

Parameters :

- upred (freestyle.types.UnaryPredicate1D) – The unary test the following ViewEdge is required to pass.

- bpred (freestyle.types.BinaryPredicate1D) – The binary test the following ViewEdge has to pass when paired with the ViewEdge currently pointed at.

- restrict_to_selection ( bool ) – Whether chaining is kept confined to the pool of selected ViewEdges or allowed to leave it.

- restrict_to_unvisited ( bool ) – Whether a ViewEdge already used in a chain should be skipped or reused.

- begin (freestyle.types.ViewEdge | None) – The ViewEdge at which iteration kicks off.

- orientation ( bool ) – When true, the search for the next ViewEdge runs among those surrounding the ending ViewVertex of begin; when false, it runs over the ViewEdges around that same ending ViewVertex of begin.

- brother (ChainPredicateIterator) – A ChainPredicateIterator object.

[Related references](INDEX.md).
