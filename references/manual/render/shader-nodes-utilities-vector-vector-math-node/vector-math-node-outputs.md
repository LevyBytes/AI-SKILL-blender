# Vector Math Node: Outputs

Absolute :

The entrywise absolute value of A.

Power :

The entrywise power operation where the Base raised to the power of Exponent.

Sign :

Extracts the sign. Positive values output 1.0, negative values output -1.0, and 0.0 outputs 0.0.

Minimum :

The entrywise minimum of A and B.

Maximum :

The entrywise maximum of A and B.

Round :

Rounds each component to the nearest integer, rounding upward when the fractional part is 0.5.

Floor :

Rounds each component downward to the nearest integer.

Ceil :

Rounds each component upward to the nearest integer.

Fraction :

Returns the fractional component of each value.

Modulo :

The entrywise remainder of A divided by B.

Wrap :

The entrywise output of a value between Min and Max based on the absolute difference between the input value and the nearest integer multiple of Max less than the value.

Snap :

The result of rounding A to the largest integer multiple of B less than or equal A.

Sine :

The entrywise sine of A.

Cosine :

The entrywise cosine of A.

Tangent :

The entrywise tangent of A.

### Outputs

The output of the node is dynamic. It is either a vector or a scalar depending on the operator. For instance, the Length operator has a scalar output while the Add operator has a vector output.

Vector
Output vector.

Value
Output value.

[Related references](INDEX.md).
