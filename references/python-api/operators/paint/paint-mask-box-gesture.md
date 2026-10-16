# bpy.ops.paint.mask_box_gesture

bpy.ops.paint. mask_box_gesture ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , use_front_faces_only = False , mode = 'VALUE' , value = 1.0 ) 

Mask throughout a rectangular area specified by the cursor

Parameters :

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

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
