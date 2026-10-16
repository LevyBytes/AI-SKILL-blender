# bpy.ops.paint.mask_lasso_gesture

bpy.ops.paint. mask_lasso_gesture ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , use_front_faces_only = False , mode = 'VALUE' , value = 1.0 ) 

Mask throughout a contour specified by the cursor

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Choosing delays behind cursor and adheres to a uniformer trajectory (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Increased quantities yield a uniformer stroke (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Reduced gap from preceding spot prior to choosing persists (in [10, 200], optional)

- use_front_faces_only ( bool ) – Front Faces Only, Modify merely faces addressing toward the observation (optional)

- mode ( Literal [ 'VALUE' , '`VALUE_INVERSE`' , 'INVERT' ] ) – Mode, (optional)

- VALUE
Value – Fix mask to the profundity indicated by the 'value' attribute.

- `VALUE_INVERSE`
Value Inverted – Fix mask to the profundity indicated by the flipped 'value' attribute.

- INVERT
Invert – Reverse the mask.

- value ( float ) – Value, Mask profundity to utilize whenever manner is 'Value'; naught implies no concealment and unity is absolutely concealed (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
