# bpy.ops.anim.channels_bake

bpy.ops.anim. channels_bake ( * , use_scene_range = True , range = (0, 0) , step = 1.0 , remove_outside_range = False , interpolation_type = 'BEZIER' , bake_modifiers = True )

Generate keys matching the present F-Curve shape across chosen channels.

Parameters :

- use_scene_range ( bool ) – Use Scene Range, If enabled, the scene start and end frame will be used to determine the bake range (optional)

- range ( Sequence [ int ] ) – Frame Range, The custom range in which to create new keys. Only used when not using the scene range (array of 2 items, in [-inf, inf], optional)

- step ( float ) – Frame Step, At which interval to add keys (in [0.01, inf], optional)

- remove_outside_range ( bool ) – Remove Outside Range, Removes keys outside the given range, leaving only the newly baked (optional)

- interpolation_type ( Literal [ 'BEZIER' , 'LIN' , 'CONST' ] ) – Interpolation Type, Choose the interpolation type with which new keys will be added (optional)

- BEZIER
Bézier – New keys will be Bézier.

- LIN
Linear – New keys will be linear.

- CONST
Constant – New keys will be constant.

- bake_modifiers ( bool ) – Bake Modifiers, Bake Modifiers into keyframes and delete them after (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
