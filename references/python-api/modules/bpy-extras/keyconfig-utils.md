# bpy_extras.keyconfig_utils

## bpy_extras submodule (bpy_extras.keyconfig_utils)

### bpy_extras submodule (bpy_extras.keyconfig_utils)
bpy_extras.keyconfig_utils. addon_keymap_register ( keymap_data ) 

Register a batch of keymaps for add-ons from a list of keymaps.

For examples of the format used here, look at 'blender_default.py'.

Parameters :

keymap_data ( list [ tuple [ str , dict [ str , Any ] , dict [ str , Any ] ] ] ) – A list of keymap definitions to register.
bpy_extras.keyconfig_utils. addon_keymap_unregister ( keymap_data ) 

Remove a batch of add-on keymaps.

Parameters :

keymap_data ( list [ tuple [ str , dict [ str , Any ] , dict [ str , Any ] ] ] ) – A list of keymap definitions to unregister.
bpy_extras.keyconfig_utils. keyconfig_test ( kc ) 

Check a key configuration for duplicated key-map item assignments.

Parameters :

kc (bpy.types.KeyConfig) – The key configuration to test.

Returns :

True if any duplicates were found.

Return type :

bool

[Related references](INDEX.md).
