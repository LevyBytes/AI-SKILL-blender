# Vertex Weight Edit Modifier: Influence, Example

### Influence

The three Vertex Weight modifiers all share these settings.

Global Influence
The modifier's influence taken as a whole
(0.0 leaves the vertex group's weights as they were, 1.0 is the standard influence).

Important

Influence acts on weights only; setting it to 0.0 won't stop vertices from being
added to or removed from the vertex group.

On top of that, per-vertex fine control is available through either a vertex group or a texture
(the two being mutually exclusive). Their per-vertex values get multiplied by the Global Influence .

For the full reference, see common masking options.

### Example

What follows shows a range of effects produced with the Vertex Weight Edit modifier
(paired with the Vertex Weight Proximity modifier)
to build the weights that drive the Displace modifier.

| Concave-type mapping curve. |
| --- |
| No mapping curve (linear). |
| Convex-type mapping curve. |

Vertices with a computed weight below 0.1 removed from the vertex group.

The blend-file,
`TEST_2` scene.

[Related references](INDEX.md).
