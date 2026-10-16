# freestyle.types.UnaryFunction0D

class freestyle.types. UnaryFunction0D 

Serves as the parent type for unary functions (functors) operating on Interface0DIterator. A unary function gets invoked by calling __call__() on an Interface0DIterator. Within Python, the particular UnaryFunction0D subclass you use depends on what type the functor returns; for instance, to write a function returning a double you would derive from UnaryFunction0DDouble. The UnaryFunction0D subclasses on offer are:

- UnaryFunction0DDouble

- UnaryFunction0DEdgeNature

- UnaryFunction0DFloat

- UnaryFunction0DId

- UnaryFunction0DMaterial

- UnaryFunction0DUnsigned

- UnaryFunction0DVec2f

- UnaryFunction0DVec3f

- UnaryFunction0DVectorViewShape

- UnaryFunction0DViewShape
name 

The name of the unary 0D function.

Type :

str

[Related references](INDEX.md).
