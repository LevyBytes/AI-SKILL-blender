# freestyle.types.BinaryPredicate1D

class freestyle.types. BinaryPredicate1D 

The base class for binary predicates that operate on Interface1D objects. A BinaryPredicate1D usually expresses an ordering between two Interface1D objects: it weighs a relation between the pair of Interface1D instances and hands back a boolean (true or false). You invoke it through the __call__() method.
__init__ ( ) 

Default constructor.
__call__ ( inter1 , inter2 ) 

Inheriting classes must override this. It weighs a relation between two Interface1D objects.

Parameters :

- inter1 (Interface1D) – The first Interface1D object.

- inter2 (Interface1D) – The second Interface1D object.

Returns :

True or false.

Return type :

bool
name 

The name of the binary 1D predicate.

Type :

str

[Related references](INDEX.md).
