# Add-on Tutorial: python, import bpy

```python
import bpy
from bpy import context

scene = context.scene
cursor = scene.cursor.location
obj = context.active_object

# Use a fixed value for now, eventually make this user adjustable
total = 10

# Add 'total' objects into the scene
for i in range(total):
    obj_new = obj.copy()
    scene.collection.objects.link(obj_new)

    # Now place the object in between the cursor
    # and the active object based on 'i'
    factor = i / total
    obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
```
Run this with the active object and cursor spaced apart to see the result. The location math works because both are 3D mathutils.Vector instances — a convenient class from the mathutils module that lets vectors multiply by numbers and matrices; mathutils.Vector also offers handy helpers (angle between vectors, cross and dot products) and mathutils.geometry adds more (Bézier interpolation, ray-triangle intersection), useful for later. Write the add-on — first convert the script as-is:
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

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor.location
        obj = context.active_object

        total = 10

        for i in range(total):
            obj_new = obj.copy()
            scene.collection.objects.link(obj_new)

            factor = i / total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ObjectCursorArray)

def unregister():
    bpy.utils.unregister_class(ObjectCursorArray)

if __name__ == "__main__":
    register()
```
Everything here was covered earlier; the two obvious gaps are the hard-coded total of 10 and the inconvenience of reaching the operator only through Operator Search, both fixed next. Operator property: tool settings use property types such as int, float, vector, color, Boolean, and string, handled differently from ordinary Python attributes because Blender displays them in the UI, stores them in keymaps, and keeps them for reuse — so although it feels Pythonic, you're defining tool settings loaded into and accessed by Blender outside Python. To replace the literal 10, use an operator property from the bpy.props module, added to the class body:
```python
# moved assignment from execute() to the body of the class...
total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

# and this is accessed on the class
# instance within the execute() function as...
self.total
```
Blender treats bpy.props specially at registration so they appear as buttons, and many arguments can set limits, change the default, and add a tooltip.

See bpy.props.IntProperty(); this tutorial doesn't detail other property types, but that link has more advanced examples. Menu item: add-ons can extend existing Python-defined panels, headers, and menus — here we add to an existing menu. To find a menu's identifier, enable Python Tooltips in the preferences, then hover over the menu item to see it. The method is to append a draw function into an existing class:
```python
def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.append(menu_func)
```
(see bpy.types.Menu for extending menus). Keymap: add-ons get their own keymaps so they don't disturb Blender's built-in ones. Below, a new Object Mode bpy.types.KeyMap is created and a bpy.types.KeyMapItem referencing our operator is added with Shift-Ctrl-T as the shortcut:

[Related references](INDEX.md).
