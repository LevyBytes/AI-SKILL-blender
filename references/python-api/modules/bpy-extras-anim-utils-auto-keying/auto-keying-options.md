# bpy_extras.anim_utils.AutoKeying: classmethod options ( * , keytype = '' , use_loc = True , use_rot = True , use_scale = True , force_autokey = False )

classmethod options ( * , keytype = '' , use_loc = True , use_rot = True , use_scale = True , force_autokey = False ) 

Context manager that adjusts several keyframing options.

Parameters :

- keytype ( str ) – The key type to use.

- use_loc ( bool ) – Key location channels.

- use_rot ( bool ) – Key rotation channels.

- use_scale ( bool ) – Key scale channels.

- force_autokey ( bool ) – Allow use without the user activating auto-keying.

Returns :

A context manager that resets the options on exit.

Return type :

Iterator[None]

static get_4d_rotlock ( bone ) 

Fetch the lock status of the 4D rotation.

Parameters :

bone (bpy.types.PoseBone) – The pose bone to check.

Returns :

Lock status for W, X, Y, Z rotation channels.

Return type :

list[bool]

[Related references](INDEX.md).
