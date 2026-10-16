# freestyle.types.ViewEdge

class freestyle.types. ViewEdge 

Class hierarchy: Interface1D > ViewEdge

Represents a ViewEdge, an edge belonging to the image graph. It joins a pair of ViewVertex objects and is formed by stringing together a set of FEdges.
__init__ ( ) 

__init__ ( brother )

Constructs a ViewEdge with the default constructor or the copy constructor.

Parameters :

brother (ViewEdge) – A ViewEdge object.
update_fedges ( ) 

Points the Viewedge of every embedded fedge at this one.
chaining_time_stamp 

The time stamp of this ViewEdge.

Type :

int
first_fedge 

The first FEdge that makes up this ViewEdge.

Type :

FEdge
first_viewvertex 

The first ViewVertex.

Type :

ViewVertex
id 

The Id of this ViewEdge.

Type :

Id
is_closed 

Set to True when this ViewEdge closes back on itself into a loop.

Type :

bool
last_fedge 

The last FEdge that makes up this ViewEdge.

Type :

FEdge
last_viewvertex 

The second ViewVertex.

Type :

ViewVertex
nature 

The nature of this ViewEdge.

Type :

Nature
occludee 

The shape hidden by the ViewShape that owns this ViewEdge. When nothing is occluded, this property is None.

Type :
ViewShape
qi 

The quantitative invisibility.

Type :

int

viewshape 

The ViewShape that this ViewEdge is part of.

Type :

ViewShape

[Related references](INDEX.md).
