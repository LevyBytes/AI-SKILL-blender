# bpy.types.FModifierFunctionGenerator: properties

## FModifierFunctionGenerator(FModifier)

### FModifierFunctionGenerator(FModifier)

base classes — bpy_struct, FModifier
class bpy.types. FModifierFunctionGenerator ( FModifier )

Produces values from one of the built-in functions.
amplitude

Multiplier that sets the peak and trough values (in [-inf, inf], default 1.0)

Type :

float
function_type

Which built-in function to apply (default 'SIN' )

- SIN
Sine.

- COS
Cosine.

- TAN
Tangent.

- SQRT
Square Root.

- LN
Natural Logarithm.

- SINC
Normalized Sine – sin(x) / x.

Type :

Literal[‘SIN’, ‘COS’, ‘TAN’, ‘SQRT’, ‘LN’, ‘SINC’]
phase_multiplier

Multiplier that sets how fast the function runs (in [-inf, inf], default 1.0)

Type :

float
phase_offset

Fixed amount by which the function's time input is shifted (in [-inf, inf], default 0.0)

Type :

float
use_additive

Adds this modifier's output onto the existing values rather than replacing them (default False)

Type :

bool
value_offset

Fixed amount by which the output values are shifted (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
