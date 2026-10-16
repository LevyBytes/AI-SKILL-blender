# bpy_extras.anim_utils

## bpy_extras submodule (bpy_extras.anim_utils)

### bpy_extras submodule (bpy_extras.anim_utils)
bpy_extras.anim_utils. bake_action ( obj , * , action , frames , bake_options ) 

Parameters :

- obj (bpy.types.Object) – Object to bake.

- action (bpy.types.Action | None) – An action to bake the data into, or None for a new action
to be created.

- frames ( Iterable [ int ] ) – Frames to bake.

- bake_options ( anim_utils.BakeOptions ) – Options for baking.

Returns :

Action or None.

Return type :

bpy.types.Action | None
bpy_extras.anim_utils. bake_action_objects ( object_action_pairs , * , frames , bake_options ) 

A wrapper around bake_action_objects_iter() that accepts frames and returns the result.

Parameters :

- object_action_pairs (Sequence[tuple[bpy.types.Object, bpy.types.Action | None]]) – Sequence of object action tuples,
action is the destination for the baked data. When None a new action will be created.

- frames ( Iterable [ int ] ) – Frames to bake.

- bake_options ( anim_utils.BakeOptions ) – Options for baking.

Returns :

A sequence of Action or None types (aligned with object_action_pairs )

Return type :

Sequence[bpy.types.Action]
bpy_extras.anim_utils. bake_action_iter ( obj , * , action , bake_options ) 

A coroutine that bakes the action for one object.

Parameters :

- obj (bpy.types.Object) – Object to bake.

- action (bpy.types.Action | None) – An action to bake the data into, or None for a new action
to be created.

- bake_options ( anim_utils.BakeOptions ) – Options for baking.

Returns :

an action or None

Return type :

bpy.types.Action | None
bpy_extras.anim_utils. bake_action_objects_iter ( object_action_pairs , bake_options ) 

A coroutine that bakes actions across several objects.

Parameters :

- object_action_pairs (Sequence[tuple[bpy.types.Object, bpy.types.Action | None]]) – Sequence of object action tuples,
action is the destination for the baked data. When None a new action will be created.

- bake_options ( anim_utils.BakeOptions ) – Options for baking.

Returns :

A generator yielding None per frame, and at the end
yielding a tuple of actions (aligned with object_action_pairs ).

Return type :

Generator

[Related references](INDEX.md).
