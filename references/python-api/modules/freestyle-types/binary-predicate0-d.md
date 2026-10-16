# freestyle.types.BinaryPredicate0D

class freestyle.types. BinaryPredicate0D 

The base class for binary predicates that operate on Interface0D objects. A BinaryPredicate0D usually expresses an ordering between two Interface0D objects: it weighs a relation between the pair of Interface0D instances and hands back a boolean (true or false). You invoke it through the __call__() method.
__init__ ( ) 

Default constructor.
__call__ ( inter1 , inter2 ) 

Inheriting classes must override this. It weighs a relation between two Interface0D objects.

Parameters :

- inter1 (Interface0D) – The first Interface0D object.

- inter2 (Interface0D) – The second Interface0D object.

Returns :

True or false.

Return type :

bool
name 

The name of the binary 0D predicate.

Type :

str

[Related references](INDEX.md).
