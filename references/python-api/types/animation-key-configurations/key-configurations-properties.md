# bpy.types.KeyConfigurations: properties

## KeyConfigurations(bpy_prop_collection)

### KeyConfigurations(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types. KeyConfigurations ( bpy_prop_collection )

A collection of KeyConfigs.
active

The active key configuration (preset)

Type :

KeyConfig
addon

A key configuration add-ons can extend, merged into the active configuration as events are handled (readonly)

Type :

KeyConfig
default

The built-in default key configuration (readonly)

Type :

KeyConfig
user

The final key configuration, blending keymaps from the active and add-on configurations and open to user edits (readonly)

Type :

KeyConfig

[Related references](INDEX.md).
