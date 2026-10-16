# bpy_extras.anim_utils.AutoKeying: classmethod keyframe_channels ( target , options , data_path , group , locks )

classmethod keyframe_channels ( target , options , data_path , group , locks ) 

Keyframe the channels while skipping ones that are locked.

Parameters :

- target (bpy.types.Object | bpy.types.PoseBone) – The object or pose bone to keyframe.

- options ( set [ str ] ) – Keyframing options.

- data_path ( str ) – The data path to keyframe.

- group ( str ) – The group name for the keyframes.

- locks ( Iterable [ bool ] ) – Per-channel lock status.

[Related references](INDEX.md).
