# Add-on Tutorial: python, bl_info = {

## Add-on Tutorial

Add-on tutorial. Intended audience: technical artists or developers learning to extend Blender, assuming Python basics. Prerequisites: be comfortable in Blender, know how to run a script in the Text editor, understand Python's primitive types (integer, Boolean, string, list, tuple, dictionary, set), be familiar with modules, and have a basic grasp of classes. Suggested reading: parts of "Dive Into Python" (sections 1, 2, 3, 4, 7) and the Blender API Quickstart. To catch Python errors while scripting, run Blender from a terminal (see Use The Terminal), and consider enabling Developer Extras in the preferences. Documentation links worth keeping open: the Blender API Overview (detailed but helpful), the bpy.context reference (the items your script can act on), and bpy.types.Operator (since the tutorial defines operators). What is an add-on? Simply a Python module with a few extra requirements so Blender can list it with useful information. The simplest possible add-on:
```python
bl_info = {
    "name": "My Test Add-on",
    "blender": (2, 80, 0),
    "category": "Object",
}
def register():
    print("Hello World")
def unregister():
    print("Goodbye World")
```
Here bl_info is a dictionary of metadata (title, version, author, and the minimum Blender version — older versions hide the add-on); register runs only when the add-on is enabled, so the module can load without activating; and unregister undoes whatever register set up, running when the add-on is disabled. This example does nothing Blender-specific (it never imports bpy), illustrating that an add-on's base requirements are minimal — an add-on typically registers operators, panels, and menu items, but any script can do that from the Text editor or console, since that capability comes from the bpy module, not from being an add-on; an add-on is just a tidy way to package a module for easy reuse. Running this in the Text editor prints nothing — install it through Preferences to see the messages when enabling and disabling. Your first add-on: the example above is illustrative but does little. The next one integrates a script using an Operator, the usual way to define a tool reached from menus, buttons, and shortcuts; it simply moves every object in the scene. Write the script — add this to the Text editor:
```python
import bpy

scene = bpy.context.scene
for obj in scene.objects:
    obj.location.x += 1.0
```
Click Run Script and every object in the active scene shifts 1.0 unit. Write the add-on (simple) — move that body into an operator's execute() function:
```python
bl_info = {
    "name": "Move X Axis",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.move_x"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move X by One"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

def register():
    bpy.utils.register_class(ObjectMoveX)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

if __name__ == "__main__":
    register()
```
bl_info is split across lines purely as a style convention for easy editing. Note that execute() uses the context argument passed to it rather than bpy.context.scene — usually identical, but operators may receive a custom context, so prefer the passed-in one. Paste it into the Text editor and run it, which executes the script and calls register immediately; running won't move anything, though, so trigger the registered operator: open the Operator Search menu, type "Move X by One" (the bl_label), and press Return, and the objects move as before. Keep this open for the install step. Install the add-on: once it's in the Text editor, you'll want to install it so it can be enabled in Preferences and load on startup.

Even though this add-on is a test, the install steps are worth knowing. First save the Text-editor text to disk, obeying Python module naming rules and ending in .py; then install it as you would a downloaded add-on via Preferences ‣ Add-ons ‣ Install…, selecting the file. The add-on then appears in the list; tick its checkbox to enable it (press Save as Default to keep it enabled on restart), and run the operator as before. Enabling runs the add-on's register() function and disabling runs unregister(). The destination depends on your Blender configuration — the source and destination paths print to the console on install — and you can also find add-on locations from the Python Console:
```python
import addon_utils
print(addon_utils.paths())
```
(see Directory Layout for more). Your second add-on focuses on object instancing — making linked copies of an object, similar to the Array modifier. Write the script, starting simple before turning it into an add-on:
```python
import bpy
from bpy import context

# Get the current scene
scene = context.scene
# Get the 3D cursor location
cursor = scene.cursor.location
# Get the active object (assume we have one)
obj = context.active_object
# Now make a copy of the object
obj_new = obj.copy()
# The new object has to be added to a collection in the scene
scene.collection.objects.link(obj_new)
# Now we can place the object
obj_new.location = cursor
```
Run it on the default Cube, clicking first to move the 3D cursor so the duplicate appears there; entering Edit Mode to change the Cube then changes all copies too — these are Linked Duplicates. Next, loop it to build a row of objects spanning from the active object to the cursor:

[Related references](INDEX.md).
