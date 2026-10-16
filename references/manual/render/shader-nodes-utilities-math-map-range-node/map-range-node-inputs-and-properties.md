# Map Range Node: Inputs, Properties, Outputs, Examples

## Map Range Node

The Map Range node remaps a value from one range to a target range. Inputs: Value/Vector (the input to remap); From Min and From Max (the source range's bounds); To Min and To Max (the target range's bounds); and Steps (the number of allowed values between To Min and To Max in Stepped Linear interpolation — higher being smoother, lower progressively quantizing the input). Properties: Data Type (Float or Vector, updating the sockets to match) and Interpolation Type — Linear, Stepped Linear, Smooth Step (smooth Hermite edge interpolation), or Smoother Step (smoother Hermite edge interpolation) — plus Clamp (clamp the output to the target range). Output: Result/Vector (the remapped value). Example: the Noise Texture node outputs [0, 1], and Map Range can remap it to [-1, 1].

### Map Range Node

Remap a value from one range to another.

### Inputs

**Value/Vector**
Input to remap.

**From Min**
Source range lower.

**From Max**
Source range upper.

**To Min**
Target range lower.

**To Max**
Target range upper.

**Steps**
Quantization steps for Stepped Linear.
Higher: smoother; lower: more quantization.

### Properties

**Data Type**
Float or Vector (updates sockets).

**Interpolation Type**

- **Linear:** Linear transition.
- **Stepped Linear:** Stepped transition via Steps.
- **Smooth Step:** Hermite edge smoothing.
- **Smoother Step:** Enhanced Hermite smoothing.

**Clamp**
Cap output to target range.

### Outputs

**Result/Vector**
Remapped output.

### Examples

Noise Texture yields [0, 1].
Map Range remaps to [-1, 1].

Map Range example.

### Map Range Node

Feed the Map Range node a value and it rescales that value from its source span onto a target span.

### Inputs

Value/Vector
Whatever value or vector you are feeding in for remapping.

From Min
Bottom end of the source span.

From Max
Top end of the source span.

To Min
Bottom end of the destination span.

To Max
Top end of the destination span.

Steps
How many values are allowed between To Min and To Max under Stepped Linear interpolation. Raise it for smoother interpolation; lower it and the input quantizes more and more.

[Related references](INDEX.md).
