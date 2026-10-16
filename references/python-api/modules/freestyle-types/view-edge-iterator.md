# freestyle.types.ViewEdgeIterator

class freestyle.types. ViewEdgeIterator 

Class hierarchy: Iterator > ViewEdgeIterator

Serves as the parent type for iterators that run over the ViewEdges of the ViewMap Graph. Essentially this class's increment() operator is responsible for deciding, while sitting on a particular ViewEdge, which ViewEdge to move to next.
__init__ ( begin = None , orientation = True ) 

__init__ ( brother )

Constructs a ViewEdgeIterator either from a starting ViewEdge along with its orientation, or via the copy constructor.

Parameters :

- begin (ViewEdge | None) – The ViewEdge from where to start the iteration.

- orientation ( bool ) – If true, we'll look for the next ViewEdge among
the ViewEdges that surround the ending ViewVertex of begin. If
false, we'll search over the ViewEdges surrounding the ending
ViewVertex of begin.

- brother (ViewEdgeIterator) – A ViewEdgeIterator object.
change_orientation ( ) 

Flips the orientation now in effect.
begin 

The first ViewEdge used for the iteration.

Type :

ViewEdge
current_edge 

Whatever ViewEdge this iterator is sitting on right now.

Type :

ViewEdge
object 

Whatever ViewEdge this iterator is sitting on right now.

Type :

ViewEdge
orientation 

The orientation of the ViewEdge pointed at during iteration. When true, the iterator hunts for the next ViewEdge among those circling the ending ViewVertex of the "begin" ViewEdge; when false, it scans the ViewEdges around the ending ViewVertex of the "begin" ViewEdge.

Type :

bool

[Related references](INDEX.md).
