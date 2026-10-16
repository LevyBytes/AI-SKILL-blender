# freestyle.types.Operators: static recursive_split ( func , pred_1d , sampling = 0.0 )

static recursive_split ( func , pred_1d , sampling = 0.0 ) 

static recursive_split ( func , pred_0d , pred_1d , sampling = 0.0 )

Breaks up the present set of chains recursively. Each chain's points are scanned (at the chosen sampling) to locate the point that minimizes a given function; the chain is cut in two there, and both halves are then handled the same way. A 1D predicate, stating a stopping condition on the chain about to be handled, governs how deep the recursion goes.

You may additionally hand in a 0D predicate to pre-filter which points are eligible for splitting. Any point that fails the 0D predicate is excluded from the search for the minimum.

Parameters :

- func (UnaryFunction0DDouble) – The Unary Function evaluated at each point of the chain.
The splitting point is the point minimizing this function.

- pred_0d (UnaryPredicate0D) – A 0D predicate that narrows down which points
are eligible to be split on. Often, say, you would prefer a chain to break near
its center rather than at either tip; a 0D predicate keyed on the curvilinear
abscissa is how you impose constraints of that sort.

- pred_1d (UnaryPredicate1D) – A 1D predicate stating when recursion should halt.
Before any curve is cut, this predicate runs against it; once pred_1d(chain)
comes back true, that curve is left whole and split no further.

- sampling ( float ) – The spacing at which the chain is sampled while the
predicates are evaluated. (No real resampling happens; a virtual point merely
advances along the curve at this spacing.)

[Related references](INDEX.md).
