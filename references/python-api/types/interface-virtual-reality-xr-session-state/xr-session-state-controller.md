# bpy.types.XrSessionState: controller_pose_actions_set, controller_grip_location_get, controller_grip_rotation_get, controller_aim_location_get, controller_aim_rotation_get

classmethod controller_pose_actions_set ( context , action_set , grip_action , aim_action ) 

Choose the actions that drive the VR controller poses

Parameters :

- context (Context) – (never None)

- action_set ( str ) – Action Set, Action set name (never None)

- grip_action ( str ) – Grip Action, Name of the action representing the controller grips (never None)

- aim_action ( str ) – Aim Action, Name of the action representing the controller aims (never None)

Returns :

Result

Return type :

bool
classmethod controller_grip_location_get ( context , index ) 

Read the most recent world-space controller grip location

Parameters :

- context (Context) – (never None)

- index ( int ) – Index, Controller index (in [0, 255])

Returns :

Location, Controller grip location (array of 3 items, in [-inf, inf], never None)

Return type :

mathutils.Vector
classmethod controller_grip_rotation_get ( context , index ) 

Read the most recent world-space controller grip rotation (quaternion)

Parameters :

- context (Context) – (never None)

- index ( int ) – Index, Controller index (in [0, 255])

Returns :

Rotation, Controller grip quaternion rotation (array of 4 items, in [-inf, inf], never None)

Return type :

mathutils.Quaternion
classmethod controller_aim_location_get ( context , index ) 

Read the most recent world-space controller aim location

Parameters :

- context (Context) – (never None)

- index ( int ) – Index, Controller index (in [0, 255])

Returns :

Location, Controller aim location (array of 3 items, in [-inf, inf], never None)

Return type :

mathutils.Vector
classmethod controller_aim_rotation_get ( context , index ) 

Read the most recent world-space controller aim rotation (quaternion)

Parameters :

- context (Context) – (never None)

- index ( int ) – Index, Controller index (in [0, 255])

Returns :

Rotation, Controller aim quaternion rotation (array of 4 items, in [-inf, inf], never None)

Return type :

mathutils.Quaternion

[Related references](INDEX.md).
