# freestyle.types.Operators: static chain ( it , pred , modifier )

static chain ( it , pred , modifier ) 

static chain ( it , pred )

Assembles a collection of chains out of the present set of ViewEdges. Each ViewEdge in the current list seeds a fresh chain. The chaining operator then walks the ViewMap's ViewEdges with the iterator the user provides. Since it uses only the increment operator, the walk runs in a single direction.

Parameters :

- it (ViewEdgeIterator) – An iterator covering the ViewMap's ViewEdges; it
holds the chaining rule.

- pred (UnaryPredicate1D) – A ViewEdge predicate giving the
stopping condition.

- modifier (UnaryFunction1DVoid) – A function accepting a ViewEdge that adjusts
the state of the ViewEdge being processed; bumping the timestamp is the
classic example of such a modifier. Omit this argument and the time stamp is
handled for you automatically.

[Related references](INDEX.md).
