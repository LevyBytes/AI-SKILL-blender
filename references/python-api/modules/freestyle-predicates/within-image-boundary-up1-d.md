# freestyle.predicates.WithinImageBoundaryUP1D

class freestyle.predicates. WithinImageBoundaryUP1D 

Class hierarchy: freestyle.types.UnaryPredicate1D > WithinImageBoundaryUP1D
__init__ ( xmin , ymin , xmax , ymax ) 

Builds an WithinImageBoundaryUP1D object.

Parameters :

- xmin ( float ) – X lower bound of the image boundary.

- ymin ( float ) – Y lower bound of the image boundary.

- xmax ( float ) – X upper bound of the image boundary.

- ymax ( float ) – Y upper bound of the image boundary.
__call__ ( inter ) 

Comes back true when the Interface1D crosses the image boundary.

[Related references](INDEX.md).
