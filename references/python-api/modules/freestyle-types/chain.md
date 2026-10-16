# freestyle.types.Chain

class freestyle.types. Chain 

Class hierarchy: Interface1D > Curve > Chain

A class standing for a 1D element produced by the chaining process. A Chain is the final stage ahead of the Stroke and feeds into the Splitting and Creation processes.
__init__ ( ) 

__init__ ( brother )
__init__ ( id )

Constructs a Chain through the default constructor, the copy constructor, or from an Id.

Parameters :

- brother (Chain) – A Chain object.

- id (Id) – An Id object.
push_viewedge_back ( viewedge , orientation ) 

Appends a ViewEdge onto the end of the Chain.

Parameters :

- viewedge (ViewEdge) – The ViewEdge that must be added.

- orientation ( bool ) – The orientation with which the ViewEdge must be processed.
push_viewedge_front ( viewedge , orientation ) 

Prepends a ViewEdge at the start of the Chain.

Parameters :

- viewedge (ViewEdge) – The ViewEdge that must be added.

- orientation ( bool ) – The orientation with which the ViewEdge must be
processed.

[Related references](INDEX.md).
