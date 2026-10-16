# Vector Curves Node

## Vector Curves Node

The Vector Curves node maps an input vector's components through a curve — use it to slow things down or speed them up from the original scene. Inputs: Factor (in the shader context, an extra property controlling how much the node influences the output vector) and Vector (standard vector input). Properties: Channel (X, Y, Z) and Curve (see the Curve widget). Output: Vector (standard vector output).

Maps input vector components to a curve. Use this curve node to slow things down or speed them up from the original scene.

Inputs:
- Factor (shader context only): Modulates influence strength on output
- Vector: Standard vector input

Properties:
Channel: X, Y, Z
Curve: See Curve widget for control details

Outputs:
- Vector: Standard vector output

### Vector Curves Node

This node applies a curve mapping to vector values, permitting fine-tuning of magnitude changes.

Apply this curve operation to decelerate or accelerate changes relative to source values.

### Inputs

In the shader context the node also has an additional Factor property.

Factor
Determines the intensity of the node's effect on the final output.

Vector
Standard vector input.

### Properties

Channel
X, Y, Z

Curve
For the curve controls see: Curve widget.

### Outputs

Vector
Standard vector output.

[Related references](INDEX.md).
