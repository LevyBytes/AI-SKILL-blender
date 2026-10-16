# Vertex Weight Proximity Modifier

## Vertex Weight Proximity Modifier

The Vertex Weight Proximity Modifier sets weights in a vertex group according to distances between the object (or specific vertices) and another target object (or its surfaces).

Warning: This modifier enforces weight clamping to 0.0–1.0 range; all values fall outside are clipped to the boundary.

Note: This documentation covers Vertex Weight Proximity for Grease Pencil objects. See the general Vertex Weight Proximity Modifier for other object types.

Vertex Group: Target group to affect. Invert: Reverses the weight influence of the vertex group. Target Object: Source object from which distances are measured. Lowest: Distance at which weight becomes 0.0. Highest: Distance at which weight becomes 1.0. Minimum: Threshold weight value. Multiply Weights: Multiplies computed weights with existing values.

Influence: See Influence Filters.

[Related references](INDEX.md).
