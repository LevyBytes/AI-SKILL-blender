# bpy.types.XrSessionState: haptic_action_apply, haptic_action_stop

classmethod haptic_action_apply ( context , action_set_name , action_name , user_path , duration , frequency , amplitude ) 

Trigger a VR haptic action

Parameters :

- context (Context) – (never None)

- action_set_name ( str ) – Action Set, Action set name (never None)

- action_name ( str ) – Action, Action name (never None)

- user_path ( str ) – User Path, Optional OpenXR user path. If not set, the action will be applied to all paths. (never None)

- duration ( float ) – Duration, Haptic duration in seconds. 0.0 is the minimum supported duration. (in [0, inf])

- frequency ( float ) – Frequency, Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime’s default frequency. (in [0, inf])

- amplitude ( float ) – Amplitude, Haptic amplitude, ranging from 0.0 to 1.0 (in [0, 1])

Returns :

Result

Return type :

bool
classmethod haptic_action_stop ( context , action_set_name , action_name , user_path ) 

Halt a VR haptic action

Parameters :

- context (Context) – (never None)

- action_set_name ( str ) – Action Set, Action set name (never None)

- action_name ( str ) – Action, Action name (never None)

- user_path ( str ) – User Path, Optional OpenXR user path. If not set, the action will be stopped for all paths. (never None)

[Related references](INDEX.md).
