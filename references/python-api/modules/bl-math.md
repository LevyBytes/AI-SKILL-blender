# bl_math

## Additional Math Functions (bl_math)

### Additional Math Functions (bl_math) 

Miscellaneous math utilities module.
bl_math. clamp ( value , min = 0 , max = 1 ) 

Constrains a float value within a min/max range. To avoid
confusion, any call must use either one or all three arguments.

Parameters :

- value ( float ) – The numeric value to constrain.

- min ( float ) – The minimum value, defaults to 0.

- max ( float ) – The maximum value, defaults to 1.

Returns :

The clamped value.

Return type :

float
bl_math. lerp ( from_value , to_value , factor ) 

Smoothly interpolates between two float values using a blend factor.

Parameters :

- from_value ( float ) – Starting point when factor is 0.

- to_value ( float ) – Ending point when factor is 1.

- factor ( float ) – The blend weight, normally in [0.0, 1.0].

Returns :

The interpolated value.

Return type :

float
bl_math. smoothstep ( from_value , to_value , value ) 

Computes a smooth transition between 0 and 1 using the specified boundary values.
At positions outside this range, the result clamps to the nearest boundary value.

Parameters :

- from_value ( float ) – Lower boundary where output is 0.

- to_value ( float ) – Upper boundary where output is 1.

- value ( float ) – Position for interpolation.

Returns :

The interpolated value in [0.0, 1.0].

Return type :

float

[Related references](INDEX.md).
