# White Noise Texture Node

## White Noise Texture Node

The White Noise Texture node returns a random number from an input Seed — a number, or a 2D/3D/4D vector per the Dimensions property — ranging from zero to one. Inputs (dynamic, appearing as needed): Vector (the seed in 2D, 3D, and 4D) and W (the seed in 1D and 4D). Properties: Dimensions — 1D (W is the seed), 2D (the Vector's X and Y), 3D (the Vector), or 4D (both Vector and W). Outputs: Value (a random value) and Color (a random color). Notes: the slightest seed difference gives completely different output, so poor precision can matter a lot — mitigate by eliminating a problematic constant seed value (choose a lower dimension or multiply it by zero), adding an arbitrary value to the seed (issues often arise only at boundaries like unit boundaries), or taking the seed's absolute value (since computing has signed zeros, this unifies zero). Example: generate cell noise using the Snap vector operation with the White Noise node.

### White Noise Texture Node

This node hands back a random number off an input Seed. What form that seed takes — a plain number, or a 2D, 3D, or 4D vector — follows from the Dimensions property. Whatever comes back falls somewhere from zero up to one.

### Inputs

Which inputs appear is dynamic: they show up only as the node properties call for them.

Vector
Vector used as seed in 2D, 3D, and 4D dimensions.

W
Value used as seed in 1D and 4D dimensions.

### Properties

Dimensions
Which space the noise is evaluated in.

1D :

The W input is used as seed.

2D :

The X and Y components of the Vector input are used as seed.

3D :

The Vector input is used as seed.

4D :

Both the Vector input and the W input are used as seed.

### Outputs

Value
Output random value.

Color
Output random color.

### Notes

The tiniest change in seed values yields a completely different output, so poor precision can hit the result hard. Usually you can ease this by:

- Getting rid of the seed value causing trouble. Where it stays constant, drop a dimension or multiply it out by zero.

- Tacking some arbitrary number onto the seed. The trouble can show up only at particular boundaries, unit boundaries among them, so a throwaway offset often clears it.

- Folding the seed through an absolute value. Computing lets zero be signed either way, and an absolute value collapses both signed zeros into a single one.

| Precision issue due to signed zeros on the Z axis. | Mitigating the issue by eliminating the Z axis. |
| --- | --- |
| Mitigating the issue by adding an arbitrary value. | Mitigating the issue by taking the absolute value. |

### Examples

Generating cell noise using the Snap vector operation and the White Noise node.

[Related references](INDEX.md).
