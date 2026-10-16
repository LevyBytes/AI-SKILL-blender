# freestyle.chainingiterators.pySketchyChainSilhouetteIterator

class freestyle.chainingiterators. pySketchyChainSilhouetteIterator 

A natural chaining iterator with a sketchy, repeated-pass touch: the same ViewEdge is chained several times over to produce a sketch-like look.
__init__ ( self , nRounds = 3 , stayInSelection = True ) 

Builds a pySketchyChainSilhouetteIterator object.

Parameters :

- nRounds ( int ) – How many passes each ViewEdge is chained for.

- stayInSelection ( bool ) – when False, edges beyond the selection are eligible for chaining.
init ( )
make_sketchy ( ve ) 

Produces the sketchy look by sending the chain back to run from its start once more. (loops over itself again)
traverse ( iter )

[Related references](INDEX.md).
