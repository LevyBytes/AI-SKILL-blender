# Closure: Input Items, Output Items, Outputs, Usage, Using External Values, Example

### Input Items

List of input sockets
A row appears for each socket the closure declares; double-click one to rename it.

Add Item
Attach a fresh input socket to the closure.

Remove Item
Drop the input socket you have selected.

Type
Picks the data type of the chosen socket (e.g. Float, Vector, Geometry, Object, Bundle). For value types a default-value control turns up, taking effect whenever the socket is left unlinked.

Shape
Picks the data structure that socket conveys, such as a Single value, Field , or Grid . Its choice governs the way data gets computed and routed onward through the graph. See Socket Shape for more information.

### Output Items

Available when the closure's output zone is selected.

List of output sockets
A row appears for each socket the closure output declares; double-click to rename.

Add Item
Attach a fresh output socket to the closure.

Remove Item
Drop the output socket you have selected.

Type
Picks the data type of the chosen socket (e.g. Float, Vector, Geometry, Object, Bundle). For value types a default-value control turns up, taking effect whenever the socket is left unlinked.

Shape
Picks the data structure that socket conveys, such as a Single value, Field , or Grid . Its choice governs the way data gets computed and routed onward through the graph. See Socket Shape for more information.

### Outputs

A closure declares outputs that hand values back to the node tree it runs in. To make one, drag a socket from within the zone onto the empty socket at the closure's output, or place sockets manually from the node's properties.

### Usage

Closures hold reusable logic you can inject into another node tree. They show up most in procedural systems where part of the behaviour should stay user-defined.

Common scenarios:

- Spelling out a bespoke scatter rule for some terrain builder.

- Laying out, procedurally, how instances get spread or altered.

- Supplying tunable mappings, field lookups, or transform rules.

### Using External Values

Values living outside the zone can be captured by a closure. Once captured, a value rides along as part of the closure's definition and remains on hand even where the closure later runs in another context.

This lets outside parameters — think scale, density, colour — travel with the closure without your having to wire up dedicated input sockets, which leaves closures tidier and simpler to reuse from one node tree to the next.

Capturing an external input value inside a closure.

### Example

- Within some terrain-builder group, replace whatever logic spreads the trees with an
Evaluate Closure node.

- Surface that closure input out on the group's own interface.

- Over in the main tree, build a Closure Zone and hook it to that input.

- Within the zone itself, spell out the tree-placement behaviour you are after.

Once the builder evaluates the closure, your zone's custom spread takes over from the stock behaviour.

A Closure Zone defining a custom distribution pattern for tree scattering.

[Related references](INDEX.md).
