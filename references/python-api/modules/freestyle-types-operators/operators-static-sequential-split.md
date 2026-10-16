# freestyle.types.Operators: static sequential_split ( starting_pred , stopping_pred , sampling = 0.0 )

static sequential_split ( starting_pred , stopping_pred , sampling = 0.0 ) 

static sequential_split ( pred , sampling = 0.0 )

Cuts every chain in the present set of chains one after another. A chain's points are handled in order (at the chosen sampling). The opening point of the original chain becomes the opening point of one of the chains produced. Splitting stops once no further chain can begin.

Tip

Supplying both a starting and a stopping predicate lets the resulting chains overlap rather than partition one another.

Parameters :

- starting_pred (UnaryPredicate0D) – A per-point predicate carrying the start
condition. Whenever it holds true, a fresh chain is opened.

- stopping_pred (UnaryPredicate0D) – A per-point predicate carrying the stop
condition. The chain closes the moment this predicate holds true.

- pred (UnaryPredicate0D) – A per-point predicate carrying the split condition.
Whenever it holds true, the chain breaks in two, so the chains produced amount
to a partition of the chain you started with.

- sampling ( float ) – The spacing at which the chain is sampled while the
predicates are evaluated. (No real resampling happens; a virtual point merely
advances along the curve at this spacing.)

[Related references](INDEX.md).
