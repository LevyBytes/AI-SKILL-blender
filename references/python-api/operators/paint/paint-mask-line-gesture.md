# bpy.ops.paint.mask_line_gesture

bpy.ops.paint. mask_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , use_front_faces_only = False , use_limit_to_segment = False , mode = 'VALUE' , value = 1.0 ) 

Mask to singular flank of a progression specified by the cursor

Parameters :

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Pointer styling to utilize through the dynamic activity (in [0, inf], optional)

- use_front_faces_only ( bool ) – Front Faces Only, Modify merely faces addressing toward the observation (optional)

- use_limit_to_segment ( bool ) – Limit to Segment, Employ the motion activity exclusively to the zone that stays enclosed within the progression devoid of magnifying its consequence to the full progression (optional)

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
