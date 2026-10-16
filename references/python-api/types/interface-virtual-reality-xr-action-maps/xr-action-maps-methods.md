# bpy.types.XrActionMaps: methods

classmethod new ( xr_session_state , name , replace_existing ) 

new

Parameters :

- xr_session_state (XrSessionState) – XR Session State, (never None)

- name ( str ) – Name, (never None)

- replace_existing ( bool ) – Replace Existing, Swap out any actionmap that already carries this name

Returns :

Action Map, Added action map

Return type :

XrActionMap
classmethod new_from_actionmap ( xr_session_state , actionmap ) 

new_from_actionmap

Parameters :

- xr_session_state (XrSessionState) – XR Session State, (never None)

- actionmap (XrActionMap) – Action Map, An action map to copy as a template (never None)

Returns :

Action Map, Added action map

Return type :

XrActionMap
classmethod remove ( xr_session_state , actionmap ) 

remove

Parameters :

- xr_session_state (XrSessionState) – XR Session State, (never None)

- actionmap (XrActionMap) – Action Map, Removed action map (never None)
classmethod find ( xr_session_state , name ) 

find

Parameters :

- xr_session_state (XrSessionState) – XR Session State, (never None)

- name ( str ) – Name, (never None)

Returns :

Action Map, The action map with the given name

Return type :

XrActionMap
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
