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

```python
bl_info = {
    "name": "Cursor Array",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}

    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor.location
        obj = context.active_object

        for i in range(self.total):
            obj_new = obj.copy()
            scene.collection.objects.link(obj_new)

            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either,
    # so we have to check this to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'T', 'PRESS', ctrl=True, shift=True)
        kmi.properties.total = 4
        addon_keymaps.append((km, kmi))

def unregister():
    # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
```
Run it (or save and install it through Preferences) and it appears in the Object menu; after picking it, choose how many cube instances to create. Running the script directly several times re-adds the menu each time — harmless, and add-ons enabled through Preferences won't register twice. Conclusions: add-ons neatly package functionality for improving your own workflow or for sharing utilities, and although Python has limits within Blender, a great deal is achievable without touching its C/C++ code; the tutorial's example is small but shows the API used for common tasks you can build on. Further reading: Blender ships commented templates in the Text editor's header (a good place to find example code), plus the Blender/Python API Overview, "How to Think Like a Computer Scientist," the Blender Development pages, and the Blender Developer Forum.

## See also

- [Quickstart](../../../python-api/guides/quickstart/INDEX.md)

[Related references](INDEX.md).
