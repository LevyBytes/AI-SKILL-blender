# freestyle.types.Operators: static bidirectional_chain ( it , pred )

static bidirectional_chain ( it , pred ) 

static bidirectional_chain ( it )

Assembles a collection of chains out of the present set of ViewEdges. Any ViewEdge in the current list may seed a fresh chain. The chaining operator then walks the ViewMap's ViewEdges with the iterator the user provides. Since it uses both the increment and decrement operators, the walk runs in both directions. The operator relies on a ChainingIterator that carries the chaining rules; that iterator is what can be configured to chain only selected edges or to avoid revisiting a ViewEdge during chaining. Every time a ViewEdge joins a chain its chaining time stamp goes up, which lets you tally how many chains a given ViewEdge belongs to.

Parameters :

- it (ChainingIterator) – A ChainingIterator covering the ViewMap's ViewEdges; it
holds the chaining rule.

- pred (UnaryPredicate1D) – A ViewEdge predicate giving the stopping condition.
You can leave it out: when the iterator definition already bakes in the stopping
criterion, no separate one is needed here.

[Related references](INDEX.md).
