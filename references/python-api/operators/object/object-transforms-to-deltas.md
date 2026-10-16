# bpy.ops.object.transforms_to_deltas

bpy.ops.object. transforms_to_deltas ( * , mode = 'ALL' , reset_values = True ) 

Shift ordinary item movements to differential movements, existing differential movements stay in place too

Parameters :

- mode ( Literal [ 'ALL' , 'LOC' , 'ROT' , 'SCALE' ] ) – Mode, What kinds of movements to shift (optional)

- ALL
All Transforms – Shift spot, orientation, and sizing movements.

- LOC
Location – Shift spot movements exclusively.

- ROT
Rotation – Shift orientation movements exclusively.

- SCALE
Scale – Shift sizing movements exclusively.

- reset_values ( bool ) – Reset Values, Discharge movement values following shifting to deltas (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object.py:777

[Related references](INDEX.md).
