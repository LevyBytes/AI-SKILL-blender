# freestyle.types.UnaryFunction1D

class freestyle.types. UnaryFunction1D 

Serves as the parent type for unary functions (functors) operating on Interface1D. A unary function gets invoked by calling __call__() on an Interface1D. Within Python, the particular UnaryFunction1D subclass you use depends on what type the functor returns; for instance, to write a function returning a double you would derive from UnaryFunction1DDouble. The UnaryFunction1D subclasses on offer are:

- UnaryFunction1DDouble

- UnaryFunction1DEdgeNature

- UnaryFunction1DFloat

- UnaryFunction1DUnsigned

- UnaryFunction1DVec2f

- UnaryFunction1DVec3f

- UnaryFunction1DVectorViewShape

- UnaryFunction1DVoid
name 

The name of the unary 1D function.

Type :

str

[Related references](INDEX.md).
