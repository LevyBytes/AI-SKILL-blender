# freestyle.chainingiterators.pyChainSilhouetteGenericIterator

class freestyle.chainingiterators. pyChainSilhouetteGenericIterator 

A natural chaining iterator that traces edges sharing the same nature along an object's topology, favouring silhouettes first, then borders, then suggestive contours, and finally every remaining edge type.
__init__ ( self , stayInSelection = True , stayInUnvisited = True ) 

Builds a pyChainSilhouetteGenericIterator object.

Parameters :

- stayInSelection ( bool ) – True when leaving the selection is permitted

- stayInUnvisited ( bool ) – Whether one ViewEdge may be chained more than once
init ( )
traverse ( iter )

[Related references](INDEX.md).
