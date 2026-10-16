# freestyle.chainingiterators.ChainSilhouetteIterator

class freestyle.chainingiterators. ChainSilhouetteIterator 

Class hierarchy: freestyle.types.Iterator >
freestyle.types.ViewEdgeIterator >
freestyle.types.ChainingIterator >
ChainSilhouetteIterator

A ViewEdge iterator built to track ViewEdges in the most natural way, for instance continuing along visible ViewEdges that share the same nature. The moment either the nature or the visibility shifts, iteration halts (the pointed ViewEdge is set to 0). Where a ViewEdge counts as both Silhouette and Crease, the silhouette criterion takes priority over the crease one.
__init__ ( restrict_to_selection = True , begin = None , orientation = True )
__init__ ( brother )

Constructs a ChainSilhouetteIterator from the seed ViewEdge that iteration begins on plus its orientation, or through the copy constructor.

Parameters :

- restrict_to_selection ( bool ) – Whether chaining is kept confined to the pool of selected ViewEdges or allowed to leave it.

- begin (freestyle.types.ViewEdge | None) – The ViewEdge at which iteration kicks off.

- orientation ( bool ) – When true, the search for the next ViewEdge runs among those surrounding the ending ViewVertex of begin; when false, it runs over the ViewEdges around that same ending ViewVertex of begin.

- brother (ChainSilhouetteIterator) – A ChainSilhouetteIterator object.

[Related references](INDEX.md).
