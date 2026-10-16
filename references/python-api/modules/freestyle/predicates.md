# freestyle.predicates

### Freestyle Predicates (freestyle.predicates) 

The predicates gathered here act on vertices (0D elements) and on polylines (1D elements). The module additionally serves as a set of worked samples for defining your own predicates in Python.

Any predicate you write yourself derives from one of the base classes below, the choice turning on whether it works on a 0D or 1D object and on its arity (unary or binary):

- freestyle.types.BinaryPredicate0D

- freestyle.types.BinaryPredicate1D

- freestyle.types.UnaryPredicate0D

- freestyle.types.UnaryPredicate1D

[Related references](INDEX.md).
