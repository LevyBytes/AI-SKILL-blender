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

```python
### In this example keymap registration functions are only split out for clarity,
### so skipping keymap registration in background mode doesn't interfere with other registration logic.

import bpy

### Store (keymap, keymap_item) for cleanup on unregister.
addon_keymaps = []

def register_keymaps():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc is None:
        return  # Can be None in background mode.

    ### Target the 3D View; name must match Blender's built-in keymap exactly.
    km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')

    ### Bind Shift+Alt+K to frame selected objects.
    kmi = km.keymap_items.new(
        idname="view3d.view_selected",
        type='K',
        value='PRESS',
        shift=True,
        alt=True,
    )
    kmi.properties.use_all_regions = True

    addon_keymaps.append((km, kmi))

def unregister_keymaps():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

def register():
    register_keymaps()

def unregister():
    unregister_keymaps()

if __name__ == "__main__":
    register()
```

base classes — bpy_prop, bpy_prop_collection

[Related references](INDEX.md).
