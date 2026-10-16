# bpy.types.ArrayModifier: fit_length, fit_type

fit_length

Length to fit array within (in [0, inf], default 0.0)

Type :

float
fit_type

Array length calculation method (default '`FIXED_COUNT`' )

- `FIXED_COUNT`
Fixed Count – Duplicate the object a certain number of times.

- `FIT_LENGTH`
Fit Length – Duplicate the object as many times as fits in a certain length.

- `FIT_CURVE`
Fit Curve – Fit the duplicated objects to a curve.

Type :

Literal['`FIXED_COUNT`', '`FIT_LENGTH`', '`FIT_CURVE`']

[Related references](INDEX.md).
