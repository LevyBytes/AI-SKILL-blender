# freestyle.predicates.ShapeUP1D

class freestyle.predicates. ShapeUP1D 

Class hierarchy: freestyle.types.UnaryPredicate1D > ShapeUP1D
__init__ ( first , second = 0 ) 

Builds a ShapeUP1D object.

Parameters :

- first ( int ) – The first Id component.

- second ( int ) – The second Id component.
__call__ ( inter ) 

Comes back true when the shape the Interface1D belongs to carries the same freestyle.types.Id that the user named.

Parameters :

inter (freestyle.types.Interface1D) – An Interface1D object.

Returns :

True if Interface1D belongs to the shape of the
user-specified Id.

Return type :

bool

[Related references](INDEX.md).
