# bpy.types.XrSessionState: action_set_create, action_create, action_binding_create, action_state_get

classmethod action_set_create ( context , actionmap ) 

Create a VR action set

Parameters :

- context (Context) – (never None)

- actionmap (XrActionMap) – (never None)

Returns :

Result

Return type :

bool
classmethod action_create ( context , actionmap , actionmap_item ) 

Create a VR action

Parameters :

- context (Context) – (never None)

- actionmap (XrActionMap) – (never None)

- actionmap_item (XrActionMapItem) – (never None)

Returns :

Result

Return type :

bool
classmethod action_binding_create ( context , actionmap , actionmap_item , actionmap_binding ) 

Create a VR action binding

Parameters :

- context (Context) – (never None)

- actionmap (XrActionMap) – (never None)

- actionmap_item (XrActionMapItem) – (never None)

- actionmap_binding (XrActionMapBinding) – (never None)

Returns :

Result

Return type :

bool
classmethod action_state_get ( context , action_set_name , action_name , user_path ) 

Read the current state of a VR action

Parameters :

- context (Context) – (never None)

- action_set_name ( str ) – Action Set, Action set name (never None)

- action_name ( str ) – Action, Action name (never None)

- user_path ( str ) – User Path, OpenXR user path (never None)

Returns :

Action State, Current state of the VR action. Second float value is only set for 2D vector type actions. (array of 2 items, in [-inf, inf], never None)

Return type :

bpy_prop_array[float]

[Related references](INDEX.md).
