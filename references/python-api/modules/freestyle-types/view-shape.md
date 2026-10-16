# freestyle.types.ViewShape

class freestyle.types. ViewShape 

Brings together the ViewMap elements (namely ViewVertex and ViewEdge) that all stem from one and the same input shape.
__init__ ( ) 

__init__ ( brother )
__init__ ( sshape )

Constructs a ViewShape with the default constructor, the copy constructor, or from an SShape.

Parameters :

- brother (ViewShape) – A ViewShape object.

- sshape (SShape) – An SShape object.
add_edge ( edge ) 

Appends a ViewEdge onto the list of ViewEdge objects.

Parameters :

edge (ViewEdge) – A ViewEdge object.
add_vertex ( vertex ) 

Appends a ViewVertex onto the list of ViewVertex objects.

Parameters :

vertex (ViewVertex) – A ViewVertex object.
edges 

The list of ViewEdge objects held within this ViewShape.

Type :

List of ViewEdge
id 

The Id of this ViewShape.

Type :

Id
library_path 

The library path of the ViewShape.

Type :

str, or None if the ViewShape is not part of a library.
name 

The name of the ViewShape.

Type :

str
sshape 

The SShape that this ViewShape is built on top of.

Type :

SShape
vertices 

The list of ViewVertex objects held within this ViewShape.

Type :

List of ViewVertex

[Related references](INDEX.md).
