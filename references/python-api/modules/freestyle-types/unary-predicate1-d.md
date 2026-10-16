# freestyle.types.UnaryPredicate1D

class freestyle.types. UnaryPredicate1D 

Serves as the parent type for unary predicates operating on Interface1D. A UnaryPredicate1D is a functor that checks a condition on an Interface1D and reports true or false according to whether that condition holds. You use a UnaryPredicate1D by calling its __call__() method, and any derived class must override __call__().
__init__ ( ) 

Default constructor.
__call__ ( inter ) 

Must be overload by inherited classes.

Parameters :

inter (Interface1D) – The Interface1D on which we wish to evaluate the predicate.

Returns :

True if the condition is satisfied, false otherwise.

Return type :

bool
name 

The name of the unary 1D predicate.

Type :

str

[Related references](INDEX.md).
