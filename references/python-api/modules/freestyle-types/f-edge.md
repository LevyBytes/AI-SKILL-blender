# freestyle.types.FEdge

class freestyle.types. FEdge 

Class hierarchy: Interface1D > FEdge

Acts as the parent type for feature edges. Such an FEdge may stand for a silhouette, a crease, a ridge or valley, a border, or a suggestive contour. With silhouettes, orientation places the visible face on the edge's left side; borders likewise keep their face on the left. Depending on whether the mesh is smooth or sharp, an FEdge may coincide with an original mesh edge or instead cut across one of its faces. Because their properties differ somewhat, the class branches into a smooth variant and a sharp variant.

FEdge ( ) 

FEdge ( brother )

Constructs an FEdge using the default constructor, the copy constructor, or from a pair of SVertex objects.

Parameters :

- brother (FEdge) – An FEdge object.

- first_vertex (SVertex) – The first SVertex.

- second_vertex (SVertex) – The second SVertex.
first_svertex 

The first SVertex making up this FEdge.

Type :

SVertex
id 

The Id of this FEdge.

Type :

Id
is_smooth 

Set to True when this FEdge happens to be a smooth FEdge.

Type :

bool
nature 

The nature of this FEdge.

Type :

Nature
next_fedge 

Whatever FEdge comes after this one within the ViewEdge. None is reported when this FEdge sits at the end of the ViewEdge.

Type :

FEdge
previous_fedge 

Whatever FEdge comes before this one within the ViewEdge. None is reported when this FEdge sits at the start of the ViewEdge.

Type :

FEdge
second_svertex 

The second SVertex making up this FEdge.

Type :

SVertex
viewedge 

The ViewEdge that this FEdge is part of.

Type :

ViewEdge

[Related references](INDEX.md).
