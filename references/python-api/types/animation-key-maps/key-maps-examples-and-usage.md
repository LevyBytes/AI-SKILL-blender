# bpy.types.KeyMaps: overview

class bpy.types. KeyMaps ( bpy_prop_collection ) 

The collection that holds keymaps
## KeyMaps(bpy_prop_collection)

### KeyMaps(bpy_prop_collection)
### Add-on Keymap Registration 

The snippet below demonstrates registering a custom shortcut from an add-on.
Such keymaps live under keyconfigs.addon and get torn down on unregister.

Keep each (keymap, keymap_item) pair around so cleanup is reliable, since the same keymap may be shared by several add-ons.

Note

The Keymap Preferences let users override an add-on's shortcuts.
An add-on's keymaps show up below the editors they apply to, where they
can be tweaked or switched off without touching the add-on's source.

Confine add-on changes to keyconfigs.addon and leave the user's own keymaps alone,
because the add-on's entries are only defaults that a user is free to override.
Editing user keymaps directly works against whatever the user has configured.

Warning

An add-on may extend an already-existing modal keymap, but Python
cannot be used to build a brand-new one. Pass modal=True to point at
an existing modal keymap, for instance the “Knife Tool Modal Map”.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.types.KeyMaps.html#add-on-keymap-registration).

base classes: bpy_prop, bpy_prop_collection

[Related references](INDEX.md).
