# bpy.ops.nla.bake

bpy.ops.nla. bake ( * , frame_start = 1 , frame_end = 250 , step = 1 , only_selected = True , visual_keying = False , clear_constraints = False , clear_parents = False , use_current_action = False , clean_curves = False , bake_types = {'POSE'} , channel_types = {'BBONE', 'LOCATION', 'PROPS', 'ROTATION', 'SCALE'} ) 

Cook every chosen thing's position/scaling/turn shifts into an action

Parameters :

- frame_start ( int ) – Start Frame, Where to begin cooking (in [0, 300000], optional)

- frame_end ( int ) – End Frame, Where to finish cooking (in [1, 300000], optional)

- step ( int ) – Frame Step, How many frames to skip when cooking each step (in [1, 120], optional)

- only_selected ( bool ) – Only Selected Bones, Mark only chosen bone portions (Pose cooking only) (optional)

- visual_keying ( bool ) – Visual Keying, Key based on final shifts (with rules used) (optional)

- clear_constraints ( bool ) – Clear Local Constraints, Strip all rules from cooked object/bones. For sound cooking enable visual marking (optional)

- clear_parents ( bool ) – Clear Parents, Cook shift onto the object then strip parents (objects only) (optional)

- use_current_action ( bool ) – Overwrite Current Action, Cook shifts into the focal action, not a fresh one (for cooking only part of bones in a frame) (optional)

- clean_curves ( bool ) – Clean Curves, After cooking curves, erase unneeded marks (optional)

- bake_types ( set [ Literal [ 'POSE' , 'OBJECT' ] ] ) – Bake Data, What shift types to cook (optional)

- POSE
Pose – Cook bone shifts.

- OBJECT
Object – Cook thing shifts.

- channel_types ( set [ Literal [ 'LOCATION' , 'ROTATION' , 'SCALE' , 'BBONE' , 'PROPS' ] ] ) – Channels, What channels to cook (optional)

- LOCATION
Location – Cook place channels.

- ROTATION
Rotation – Cook turn channels.

- SCALE
Scale – Cook sizing channels.

- BBONE
B-Bone – Cook B-Bone channels.

- PROPS
Custom Properties – Cook special traits.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/anim.py:274

[Related references](INDEX.md).
