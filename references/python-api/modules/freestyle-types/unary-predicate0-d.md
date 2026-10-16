# freestyle.types.UnaryPredicate0D

class freestyle.types. UnaryPredicate0D 

Serves as the parent type for unary predicates operating on Interface0DIterator. A UnaryPredicate0D is a functor that checks a condition on an Interface0DIterator and reports true or false according to whether that condition holds. You use a UnaryPredicate0D by calling its __call__() method, and any derived class must override __call__().
__init__ ( ) 

Default constructor.
__call__ ( it ) 

Must be overload by inherited classes.

Parameters :

it (Interface0DIterator) – The Interface0DIterator pointing onto the Interface0D at
which we wish to evaluate the predicate.

Returns :

True if the condition is satisfied, false otherwise.

Return type :

bool
name 

The name of the unary 0D predicate.

Type :

str

[Related references](INDEX.md).
