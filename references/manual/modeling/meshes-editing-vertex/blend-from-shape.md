# Blend from Shape

## Blend from Shape

### Blend from Shape

Reference

Mode:

Edit Mode

Menu:

Vertex → Blend from Shape

Shifts selected vertices toward their stored position in a specific Shape Key.
Helpful for refining geometry by borrowing deformations from a shape key.

### Options

Shape
Which shape key to reference.

Blend
How much to apply the shape (like the shape key's Value).
0 leaves unchanged; 1 makes vertices exactly match the key.

Add
When off, each vertex interpolates between its current spot and the shape key's absolute position.

When on, Blender finds the difference between the shape key positions and its Relative To shape key, then adds that difference (scaled by Blend) to the vertex.

[Related references](INDEX.md).
