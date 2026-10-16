# freestyle.chainingiterators.pyNoIdChainSilhouetteIterator

class freestyle.chainingiterators. pyNoIdChainSilhouetteIterator 

A natural chaining iterator that traces edges sharing the same nature along an object's topology, favouring silhouettes first, then borders, then suggestive contours, and finally every remaining edge type. The same ViewEdge is never chained twice.
__init__ ( self , stayInSelection = True ) 

Builds a pyNoIdChainSilhouetteIterator object.

Parameters :

stayInSelection ( bool ) – True when leaving the selection is permitted
init ( )
traverse ( iter )

[Related references](INDEX.md).
