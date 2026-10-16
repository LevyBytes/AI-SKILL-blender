# bpy.ops.object.quick_fur

bpy.ops.object. quick_fur ( * , density = 'MEDIUM' , length = 0.1 , radius = 0.001 , view_percentage = 1.0 , apply_hair_guides = True , use_noise = True , use_frizz = True ) 

Build a hair/fur system on chosen objects

Parameters :

- density ( Literal [ 'LOW' , 'MEDIUM' , 'HIGH' ] ) – Density, (optional)

- length ( float ) – Length, (in [0.001, 100], optional)

- radius ( float ) – Hair Radius, (in [0, 10], optional)

- view_percentage ( float ) – View Percentage, (in [0, 1], optional)

- apply_hair_guides ( bool ) – Apply Hair Guides, (optional)

- use_noise ( bool ) – Noise, (optional)

- use_frizz ( bool ) – Frizz, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object_quick_effects.py:92

[Related references](INDEX.md).
