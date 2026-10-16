# bpy.types.KeyMaps: new

new ( name , * , space_type = 'EMPTY' , region_type = 'WINDOW' , modal = False , tool = False ) 

Make sure the keymap is present. The matching one for the given name, space type, and region type is returned, and a new keymap is created only if none already exists.

Parameters :

- name ( str ) – Name, (never None)

- space_type (Literal[Space Type Items]) – Space Type, (optional)

- region_type (Literal[Region Type Items]) – Region Type, (optional)

- modal ( bool ) – Modal, Keymap for modal operators. Modal keymaps are not supported for KeyConfigs.addons . (optional)

- tool ( bool ) – Tool, Keymap for active tools (optional)

Returns :

Key Map, Added key map

Return type :

KeyMap

[Related references](INDEX.md).
