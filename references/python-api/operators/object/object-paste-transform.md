# bpy.ops.object.paste_transform

bpy.ops.object. paste_transform ( * , method = 'CURRENT' , bake_step = 0 , use_mirror = False , mirror_axis_loc = 'x' , mirror_axis_rot = 'z' , use_relative = False ) 

Transfer the stored translation/rotation/scale matrix from the clipboard to the active pose bone or object. Uses global-space transformation data

Parameters :

- method ( Literal [ 'CURRENT' , '`EXISTING_KEYS`' , 'BAKE' ] ) – Paste Method, Overwrite immediate values, marked animation frames, or produce new animation frames (optional)

- CURRENT
Current Transform – Overwrite the now-active values only, respecting auto-keying if enabled.

- `EXISTING_KEYS`
Selected Keys – Overwrite marked animation frames, potentially creating new frames on those times.

- BAKE
Bake on Key Range – Overwrite all frames between the first and last marked key, creating animation frames if required.

- bake_step ( int ) – Frame Step, Only applies to baking; step=1 adds a frame per tick, step=2 every other tick (in [1, inf], optional)

- use_mirror ( bool ) – Mirror Transform, When pasting, invert the transform relative to an anchor object or bone (optional)

- mirror_axis_loc ( Literal [ 'x' , 'y' , 'z' ] ) – Location Axis, Which spatial axis to flip for position (optional)

- mirror_axis_rot ( Literal [ 'x' , 'y' , 'z' ] ) – Rotation Axis, Which spatial axis to flip for orientation (optional)

- use_relative ( bool ) – Use Relative Paste, When pasting, treat the matrix as relative to another object (configured in the interface) (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/copy_global_transform.py:325

[Related references](INDEX.md).
