# bpy.ops.paint.mask_flood_fill

bpy.ops.paint. mask_flood_fill ( * , mode = 'VALUE' , value = 0.0 ) 

Replenish the comprehensive mask with a provided quantity, or invert its quantities

Parameters :

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
