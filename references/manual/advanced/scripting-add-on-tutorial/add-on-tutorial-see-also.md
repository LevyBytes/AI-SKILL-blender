# Add-on Tutorial: See also

```python
# store keymaps here to access after registration
addon_keymaps = []

def register():
    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'T', 'PRESS', ctrl=True, shift=True)
    kmi.properties.total = 4
    addon_keymaps.append((km, kmi))

def unregister():
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
```
Note the keymap item can set total to a value different from the operator's default, letting several keys reach the same operator with different settings. Shift-Ctrl-T isn't a Blender default, but since you can't guarantee add-ons won't overwrite each other's keymaps, take care that your keys don't clash with important Blender functionality (see also the "is key free" add-on). For API docs see bpy.types.KeyMaps.new(), bpy.types.KeyMap, bpy.types.KeyMapItems.new(), and bpy.types.KeyMapItem. Bringing it all together:

The complete program is in the [upstream source](https://docs.blender.org/manual/en/5.1/advanced/scripting/addon_tutorial.html#bringing-it-all-together).
Run it (or save and install it through Preferences) and it appears in the Object menu; after picking it, choose how many cube instances to create. Running the script directly several times re-adds the menu each time — harmless, and add-ons enabled through Preferences won't register twice. Conclusions: add-ons neatly package functionality for improving your own workflow or for sharing utilities, and although Python has limits within Blender, a great deal is achievable without touching its C/C++ code; the tutorial's example is small but shows the API used for common tasks you can build on. Further reading: Blender ships commented templates in the Text editor's header (a good place to find example code), plus the Blender/Python API Overview, "How to Think Like a Computer Scientist," the Blender Development pages, and the Blender Developer Forum.

## See also

- [Quickstart](../../../python-api/guides/quickstart/INDEX.md)

[Related references](INDEX.md).
