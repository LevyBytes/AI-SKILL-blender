# bpy.ops.object.quick_explode

bpy.ops.object. quick_explode ( * , style = 'EXPLODE' , amount = 100 , frame_duration = 50 , frame_start = 1 , frame_end = 10 , velocity = 1.0 , fade = True ) 

Detonate chosen objects into fragments

Parameters :

- style ( Literal [ 'EXPLODE' , 'BLEND' ] ) – Explode Style, (optional)

- amount ( int ) – Number of Pieces, (in [2, 10000], optional)

- frame_duration ( int ) – Duration, (in [1, 300000], optional)

- frame_start ( int ) – Start Frame, (in [1, 300000], optional)

- frame_end ( int ) – End Frame, (in [1, 300000], optional)

- velocity ( float ) – Outwards Velocity, (in [0, 300000], optional)

- fade ( bool ) – Fade, Dim the fragments progressively (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object_quick_effects.py:273

[Related references](INDEX.md).
