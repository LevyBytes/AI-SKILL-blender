# bpy.ops.sculpt.mask_from_cavity

bpy.ops.sculpt. mask_from_cavity ( * , mix_mode = 'MIX' , mix_factor = 1.0 , settings_source = 'OPERATOR' , factor = 0.5 , blur_steps = 2 , use_curve = False , invert = False )

Form a mask based on the curvature characteristic of the geometry

Parameters :

- mix_mode ( Literal [ 'MIX' , 'MULTIPLY' , 'DIVIDE' , 'ADD' , 'SUBTRACT' ] ) – Mode, Blend approach (optional)

- mix_factor ( float ) – Mix Factor, (in [0, 5], optional)

- settings_source ( Literal [ 'OPERATOR' , 'BRUSH' , 'SCENE' ] ) – Settings, Source for parameter values (optional)

- OPERATOR
Operator – Use settings from operator properties.

- BRUSH
Brush – Use settings from brush.

- SCENE
Scene – Use settings from scene.

- factor ( float ) – Factor, The intensity of the cavity mask (in [0, 5], optional)

- blur_steps ( int ) – Blur, How often the cavity mask is softened (in [0, 25], optional)

- use_curve ( bool ) – Custom Curve, (optional)

- invert ( bool ) – Cavity (Inverted), (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
