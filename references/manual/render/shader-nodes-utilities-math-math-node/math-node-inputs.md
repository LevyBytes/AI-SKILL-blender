# Math Node: Inputs

## Math Node

The Math node performs math operations. Inputs (dynamic — some appear only for certain operations, e.g. Addend only for Multiply Add): Value (trigonometric functions read it as radians), Addend, Base, Exponent, Epsilon, Distance, Min, Max, Increment, Scale, Degrees, and Radians. Properties: Operation, grouped as — Functions: Add (the sum), Subtract (the difference), Multiply (the product), Divide (the first over the second, division by zero giving zero), Multiply Add (the product of the two values plus Addend), Power (Base to the Exponent), Logarithm (the log of the value to a given Base), Square Root, Inverse Square Root (one over the square root), Absolute (the value without its sign, making negatives positive), and Exponent (Euler's number to the value's power). Comparison: Minimum, Maximum, Less Than (1.0 if the first value is smaller, else 0.0), Greater Than (1.0 if the first is larger, else 0.0), Sign (1.0 for positives, -1.0 for negatives, 0.0 for zero), Compare (1.0 if the two values' difference is at most Epsilon), Smooth Minimum, and Smooth Maximum. Rounding: Round (to the nearest integer, up at 0.5), Floor (down), Ceil (up), Truncate (the integer part), Fraction (the fractional part), Truncated Modulo (the remainder of the first divided by the second), Floored Modulo (the positive remainder), Wrap (a value between Min and Max from the absolute difference between the input and the nearest integer multiple of Max below it), Snap (down to the nearest integer multiple of Increment), and Ping-pong (bouncing between 0.0 and Scale as the input rises). Trigonometric: Sine, Cosine, Tangent, Arcsine, Arccosine, Arctangent, Arctan2 (the inverse tangent of the first value over the second, in radians), Hyperbolic Sine, Hyperbolic Cosine, and Hyperbolic Tangent. Conversion: To Radians and To Degrees. Plus Clamp (limit the output to 0.0-1.0; see Clamp). Output: Value (the numerical result). Examples — Manual Z-Mask: a cube ~10 units from the camera (top Render Layers) and a plane covering the left half ~7 units away (bottom Render Layers) both pass through Map Value nodes multiplying depth by 0.05 and clamping to [0.0, 1.0] for display as color; the Minimum node picks the smaller depth per pixel (the plane on the left since it's closer, the cube on the right), while the Maximum node picks the larger (the cube on the left, the infinitely-far background on the right). Using sine to pulsate: a Time node outputs a linear 0-to-1 over 101 frames, so at frame 25 the value is 0.25, which times 2×pi (6.28) becomes 1.0 via Sine since sin(2×pi/4) = sin(pi/2) = +1.0; since sine outputs -1.0 to 1.0, a Map Value node rescales to 0.0-1.0 (add 1, then multiply by 0.5) and the default Color Ramp shows it as grayscale (medium gray for 0.0, black for -1.0, white for 1.0) — animate it for a smooth cyclic gray sequence, usable to fade an alpha channel, push a scene in/out of focus via Z, or pulse a color channel.

Brightening (scaling) a channel: a Math (Multiply) node raises the luminance channel (Y) to brighten the image — use a Map Value node with min() and max() turned on to keep the output within valid values, and with this approach a logarithmic function can make a high-dynamic-range image; for this particular case, a Brightness/Contrast node may give simpler brightness control.

The Math Node carries out math operations.

Inputs: the node's inputs are dynamic, with some appearing only for certain operations; the Addend input, for instance, shows only for Multiply Add.
Value: an input value; trigonometric functions read it as radians.
Addend: an input addend.
Base: an input base.
Exponent: an input exponent.
Epsilon: an input epsilon.
Distance: an input distance.
Min: an input minimum.
Max: an input maximum.
Increment: an input increment.
Scale: an input scale.
Degrees: input degrees.
Radians: input radians.

Properties:
Operation: the math operator applied to the inputs.
  Functions: Add (the two values' sum), Subtract (their difference), Multiply (their product), Divide (the first over the second; dividing by zero gives zero), Multiply Add (the product of the two plus Addend), Power (Base raised to Exponent), Logarithm (the log of the value to the given Base), Square Root (the value's square root), Inverse Square Root (one over the square root), Absolute (the value with its sign dropped, turning negatives positive), Exponent (Euler's number raised to the value).
  Comparison: Minimum (the smaller input), Maximum (the larger input), Less Than (1.0 when the first is below the second, else 0.0), Greater Than (1.0 when the first exceeds the second, else 0.0), Sign (positives give 1.0, negatives -1.0, and 0.0 gives 0.0), Compare (1.0 when the two values differ by at most Epsilon), Smooth Minimum, Smooth Maximum.
  Rounding: Round (rounds entrywise to the nearest integer, up at a 0.5 fraction), Floor (rounds down to the nearest integer), Ceil (rounds up to the nearest integer), Truncate (the value's integer part), Fraction (the value's fractional part), Truncated Modulo (the remainder of the first over the second), Floored Modulo (a division's positive remainder), Wrap (a value between Min and Max from the absolute gap between the value and the nearest integer multiple of Max below it), Snap (rounds down to the nearest integer multiple of Increment), Ping-pong (bounces between 0.0 and Scale as the value rises).
  Trigonometric: Sine, Cosine, Tangent, Arcsine, Arccosine, Arctangent (each of the input value), Arctan2 (the inverse tangent of the first over the second, in radians), Hyperbolic Sine, Hyperbolic Cosine, Hyperbolic Tangent (each of the input value).
  Conversion: To Radians (degrees to radians), To Degrees (radians to degrees).
Clamp: limits the output to 0.0–1.0; see Clamp.

Outputs:
Value: the numerical result.

### Math Node

Numerical operations.

### Inputs

Dynamic; some only appear for certain operations.
Example: Addend for Multiply Add.

**Value**
Input (radians for trig).

**Addend**
Input for Multiply Add.

**Base**
Input for Power/Logarithm.

**Exponent**
Input for Power.

**Epsilon**
Threshold for Compare.

**Distance**
Input for distance ops.

**Min**
Lower bound.

**Max**
Upper bound.

**Increment**
Input for Snap.

**Scale**
Input for Ping-pong.

**Degrees**
Input for conversion.

**Radians**
Input for conversion.

[Related references](INDEX.md).
