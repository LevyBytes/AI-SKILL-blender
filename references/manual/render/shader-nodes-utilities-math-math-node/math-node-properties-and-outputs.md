# Math Node: Properties, Outputs

### Properties

**Operation**

**Functions**

- **Add:** Sum.
- **Subtract:** Difference.
- **Multiply:** Product.
- **Divide:** First ÷ second (zero yields zero).
- **Multiply Add:** (First × second) + Addend.
- **Power:** Base ^ Exponent.
- **Logarithm:** log_Base(Value).
- **Square Root:** √Value.
- **Inverse Square Root:** 1 / √Value.
- **Absolute:** Magnitude.
- **Exponent:** e ^ Value.

**Comparison**

- **Minimum:** Smallest input.
- **Maximum:** Largest inputs.
- **Less Than:** 1.0 if first < second; 0.0 otherwise.
- **Greater Than:** 1.0 if first > second; 0.0 otherwise.
- **Sign:** Extract sign (+1.0 positive, -1.0 negative, 0.0 zero).
- **Compare:** 1.0 if difference <= Epsilon; 0.0 otherwise.
- **Smooth Minimum:** Smooth minimum transition.
- **Smooth Maximum:** Smooth maximum transition.

**Rounding**

- **Round:** Nearest integer (round 0.5 up).
- **Floor:** Round toward negative infinity.
- **Ceil:** Round toward positive infinity.
- **Truncate:** Integer part only.
- **Fraction:** Fractional part only.
- **Truncated Modulo:** First % second (truncated).
- **Floored Modulo:** Positive remainder.
- **Wrap:** Value between Min and Max via offset.
- **Snap:** Round down to nearest Increment multiple.
- **Ping-pong:** Bounce [0, Scale] as input increases.

**Trigonometric**

- **Sine:** sin(Value).
- **Cosine:** cos(Value).
- **Tangent:** tan(Value).
- **Arcsine:** arcsin(Value).
- **Arccosine:** arccos(Value).
- **Arctangent:** arctan(Value).
- **Arctan2:** arctan(first / second) in radians.
- **Hyperbolic Sine:** sinh(Value).
- **Hyperbolic Cosine:** cosh(Value).
- **Hyperbolic Tangent:** tanh(Value).

**Conversion**

- **To Radians:** degrees → radians.
- **To Degrees:** radians → degrees.

**Clamp**
Limit output to [0.0, 1.0].

### Outputs

**Value**
Numeric output.

[Related references](INDEX.md).
