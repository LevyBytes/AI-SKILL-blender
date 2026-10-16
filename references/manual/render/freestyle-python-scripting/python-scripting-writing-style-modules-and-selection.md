# Python Scripting: Writing Style Modules, Selection, Chaining, Splitting, Sorting

## Python Scripting

Python Scripting — Programmable Style Modules

The Python Scripting mode provides full scriptable line stylization. Styling operations are Python scripts called style modules. A style module receives a view map (detected feature edges) and outputs stylized strokes.

A style module chains five basic operators: selection, chaining, splitting, sorting, and stroke creation. Selection identifies a subset based on predicates. Chaining processes selected edges using predicates and functions to construct chains. Splitting and sorting refine chains. Stroke creation applies stroke shaders to build output strokes.

Python style modules are text data-blocks within blend-files. External modules load in the Text Editor first. A style module stack selector allows choosing from loaded modules.

Blender supplies Python style modules serving as starting references. Consult the Freestyle Python API in the Blender Python API reference for complete style module details.

| Description | Description |
| --- | --- |
| By T.K. using the Python Scripting mode (blend-file, CC0). | By T.K. using the Python Scripting mode (blend-file, CC0). |

### Writing Style Modules

A style module stylizes Freestyle line output. Input is a view map (set of feature edges); output is stylized strokes. A style module forms a pipeline of operations transforming input edges into output strokes.

Five operation types exist (with corresponding operator functions):

- Selection Operators.select()
- Chaining Operators.chain(), Operators.bidirectional_chain()
- Splitting Operators.sequential_split(), Operators.recursive_split()
- Sorting Operators.sort()
- Stroke creation Operators.create()

The input view map contains ViewEdge objects. Selection identifies ViewEdges of interest using predicates. Chaining constructs Chains by joining ViewEdges per user predicates and functions. Chains undergo further refinement via splitting and sorting. Finally, stroke creation transforms chains into strokes via stroke shaders.

ViewEdges, Chains, and Strokes constitute one-dimensional (1D) elements. A 1D element is a polyline of connected straight lines. Polyline vertices are called 0D elements.

All operators work on active 1D element sets. Initial active set contains input view map ViewEdges. Operators update the active set.

### Selection

Selection examines every active set element, retaining only those matching a predicate. Operators.select() takes a unary predicate operating on any Interface1D representing a 1D element. Example:

Operators.select(QuantitativeInvisibilityUP1D(0))

This selects visible ViewEdges (quantitative invisibility equals 0). Selection limits styling to a fraction of active 1D elements.

QuantitativeInvisibilityUP1D is a predicate class, and Operators.select() receives an instance. The predicate evaluation invokes the __call__ method. Operators.select() takes a functor taking Interface0D arguments. Freestyle Python API employs functors extensively for predicates and functions.

### Chaining

Chaining operators work on active ViewEdge sets, determining future stroke topology. Chaining implements an iterator traversing the ViewMap graph along ViewEdges. The iterator sets a chaining rule dictating the next ViewEdge at a given vertex. Several iterators ship with Freestyle Python API; custom ones inherit ViewEdgeIterator. Chaining operators take a UnaryPredicate on Interface1D as stopping criteria. Chaining halts when reaching a ViewEdge satisfying this predicate.

Chaining is unidirectional Operators.chain() or bidirectional Operators.bidirectional_chain(). Bidirectional chaining propagates in both directions from the starting edge.

Example bidirectional chaining:

Operators.bidirectional_chain(
ChainSilhouetteIterator(),
NotUP1D(QuantitativeInvisibilityUP1D(0)),
)

This uses ChainSilhouetteIterator for chaining and stops at invisible ViewEdges.

Chaining processes active ViewEdges sequentially. Previously sorted ViewEdges via Operators.sort() can control this order. It starts a chain with the first ViewEdge. Processed ViewEdges are marked (timestamp modification) to avoid reprocessing. When chaining hits a stopping predicate, the chain ends. A new chain begins from the first unmarked ViewEdge. This repeats until all unmarked ViewEdges finish processing. Post-chaining, the active set contains the new Chains.

Python Scripting — Splitting, Sorting, and Stroke Creation (continued)

### Splitting

Splitting refines Chain topology. Operators.sequentialSplit() parses the Chain at arbitrary resolution, evaluating a unary predicate at each point. When satisfied, the chain splits. Sequential splitting results become the new active set.

Operators.sequentialSplit(TrueUP0D(), 2)

This splits the chain every 2 units. An advanced version uses two predicates: one for new chain start, another for end. This produces disjoint or overlapping chains if predicates differ.

Operators.recursiveSplit() evaluates a function on 0D elements at given resolution, finding the maximum value point. The Chain splits there and repeats recursively on each segment until stopping conditions are met.

func = Curvature2DAngleF0D()
Operators.recursive_split(func, NotUP1D(HigherLengthUP1D(5)), 5)

This recursively splits Chains at highest 2D curvature points, with 5-unit resolution. Chains under 5 units avoid further splitting.

### Sorting

Operators.sort() arranges active 1D element stacking. It takes a binary predicate as a "smaller than" operator.

Operators.sort(Length2DBP1D())

This sorts Interface1D objects by ascending 2D length. Sorting pairs well with causal density. Causal density evaluates image density during rendering. To remove strokes when local density exceeds limits, control drawing order. Use sorting to draw "important" lines first.

[Related references](INDEX.md).
