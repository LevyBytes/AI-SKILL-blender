# Vector Math Node: Inputs (dynamic, available based on operation), Operations

## Vector Math Node

The Vector Math node applies the chosen math operation to the input vectors. Inputs (dynamic — some appear only for certain operations, e.g. Scale only for the Scale operator): Vector A, Vector B, and Scale s. Properties: Operation — Add (A + B), Subtract (A - B), Multiply (the entrywise product of A and B), Divide (the entrywise division of A by B, division by zero giving zero), Multiply Add (the entrywise A × B + C), Cross Product (the cross product of A and B), Project (the projection of A onto B), Reflect (the reflection of A about the normal B, which needn't be normalized), Refract (for incident vector A, surface normal B, and an index-of-refraction ratio, the refraction vector R), Faceforward (orient A to point away from a surface B by its normal C, computing (dot(B, C) < 0) ? A : -A), Dot Product (Ax·Bx + Ay·By + Az·Bz), Distance (between A and B), Length (the length of A, √(Ax² + Ay² + Az²)), Scale (A times the scalar Scale), Normalize (A scaled to length 1 in the same direction, or (0, 0, 0) if A is (0, 0, 0)), Absolute (the entrywise absolute value of A), Power (the entrywise Base to the Exponent), Sign (1.0 for positives, -1.0 for negatives, 0.0 for zero), Minimum and Maximum (the entrywise min/max of A and B), Round (entrywise to the nearest integer, up at 0.5), Floor (entrywise down), Ceil (entrywise up), Fraction (the entrywise fractional part), Modulo (the entrywise modulo of A by B), Wrap (entrywise, a value between Min and Max from the absolute difference between the input and the nearest integer multiple of Max below it), Snap (A down to the largest integer multiple of B at most A), Sine, Cosine, and Tangent (entrywise). Outputs (dynamic — a vector or a scalar by operator, e.g. Length is scalar, Add is vector): Vector (the output vector) and Value (the output value).

Performs selected mathematical operations on two input vectors to produce the computed result.

Inputs (dynamic, available based on operation):
- Vector: A = (Ax, Ay, Az)
- Vector: B = (Bx, By, Bz)
- Scale: s

Operations:

Add: Sum of A and B.
(Ax+Bx, Ay+By, Az+Bz)

Subtract: Difference of A and B.
(Ax-Bx, Ay-By, Az-Bz)

Multiply: Element-wise product of A and B.
(Ax·Bx, Ay·By, Az·Bz)

Divide: Element-wise division of A by B. Division by zero = zero.
(Ax/Bx, Ay/By, Az/Bz)

Multiply Add: Element-wise combination of multiply and addition.
A × B + C

Cross Product: Cross product of A and B.
(Ay·Bz - Az·By, Az·Bx - Ax·Bz, Ax·By - Ay·Bx)

Project: Projection of A onto B

Reflect: A's reflection relative to normal B (B normalization not required)

Refract: Refraction vector R given incident vector A, surface normal B, and IOR ratio

Faceforward: Orients vector A to point away from surface B with normal C.
Computes (dot(B, C) < 0) ? A : -A

Dot Product: Dot product of A and B.
Ax·Bx + Ay·By + Az·Bz

Distance: Distance between A and B

Length: Magnitude of A.
√(Ax² + Ay² + Az²)

Scale: Multiply A by scalar input.
(s·Ax, s·Ay, s·Az)

Normalize: Unit vector in direction of A, with length 1. If A is (0, 0, 0), output is (0, 0, 0)

Absolute: Element-wise absolute value of A

Power: Base raised to Exponent power, element-wise

Sign: Extracts sign: positive → 1.0, negative → -1.0, zero → 0.0

Minimum: Element-wise minimum of A and B

Maximum: Element-wise maximum of A and B

Round: Rounds element-wise to nearest integer; 0.5 fractions round upward

Floor: Rounds element-wise down to nearest integer

Ceil: Rounds element-wise up to nearest integer

Fraction: Returns fractional part, element-wise

Modulo: Element-wise modulo of A by B

Wrap: Element-wise output between Min and Max based on absolute difference to nearest multiple of Max less than value

Snap: Rounds A to largest integer multiple of B that is ≤ A

Sine: Element-wise Sine of A

Cosine: Element-wise Cosine of A

Tangent: Element-wise Tangent of A

Properties:
Operation: The vector math operator to apply

Outputs (dynamic, vector or scalar depending on operator):
- Vector: Output vector
- Value: Output scalar

[Related references](INDEX.md).
