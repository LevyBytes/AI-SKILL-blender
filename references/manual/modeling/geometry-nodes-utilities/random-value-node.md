# Random Value Node

## Random Value Node

Outputs white-noise values as Float, Integer, Vector, or Boolean fields.

**Inputs**

Min
Lower bound for sampling (Float, Integer, Vector only).

Max
Upper bound for sampling (Float, Integer, Vector only).

Probability
True probability for Boolean output (Boolean only).

ID
Seed ID. Defaults to the ID Node's value—the `id` attribute if present, otherwise the index.

Tip: By default, a unique value is generated per index.
To get a single value for the whole geometry, connect a constant (e.g., Integer Node) to ID.

Seed
Field to produce a different sequence even for identical ID inputs.

**Properties**

Data Type

Float: Outputs a Float field.

Integer: Outputs an Integer field.

Vector: Outputs a Vector field.

Boolean: Outputs a Boolean field.

**Outputs**

Value
Random field values.

[Related references](INDEX.md).
