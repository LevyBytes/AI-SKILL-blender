# Vertex Weight Mix Modifier: Options

### Options

The Vertex Weight Mix modifier panel.

Vertex Group A, B

- A : The vertex group that gets affected.

- B : The second vertex group folded into the affected one.
Leave it blank when you only mean to mix in a flat value.

Invert Weights A/B
Flips the vertex group's influence.

Default Weight A, B

- A : The weight handed by default to every vertex outside the given vertex group.

- B : The weight handed by default to every vertex outside the given second vertex group.

Vertex Set
Picks which vertices get affected.

All :

Hits every vertex, paying no mind to what the vertex groups hold.

Vertex Group A :

Hits only the vertices belonging to the affected vertex group.

Vertex Group B :

Hits only the vertices belonging to the second vertex group.

Vertex Group A or B :

Hits only the vertices belonging to at least one of the two vertex groups.

Vertex Group A and B :

Hits only the vertices belonging to both vertex groups.

Important

With All vertices , Vertices from group B or Vertices from one group in play,
some vertices may end up added to the affected vertex group.

Mix Mode
Sets how the affected group's weights are reshaped by the other group's weights.

Replace :

Overwrites the affected weights with the second group's weights.

Add :

Tacks Group B's values onto Group A's.

Subtract :

Takes Group B's values away from Group A's.

Multiply :

Multiplies Group A's values by Group B's.

Divide :

Divides Group A's values by Group B's.

Difference :

Takes the smaller of the two values from the larger.

Average :

Sums the two values and halves the result.

Minimum :

Keeps whichever weight is smaller out of VGroup A's and VGroup B's.

Maximum :

Keeps whichever weight is larger out of VGroup A's and VGroup B's.

Normalize Weights
Rescales the vertex group's weights so their relative spacing holds
while the lowest and highest values stretch across the full 0 - 1 range.

[Related references](INDEX.md).
