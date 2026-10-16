# Quickstart: Types, Native Types

```python
import bpy

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")

def register():
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    register()
```

To run the script:

- Start Blender and switch to the Scripting workspace.

- Click the New button in the text editor to create a new text data-block.

- Copy the code from above and paste it into the text editor.

- Click on the Run Script button.

To view the results:

- Select the default cube.

- Click on the Object properties icon in the buttons panel (far right; appears as a tiny cube).

- Scroll down to see a panel named "Hello World Panel".

- Changing the object name also updates Hello World Panel's name: field.

Notice how the rows are arranged and how the label and properties get laid out by the code.

See also

bpy.types.Panel

### Types

Blender brings its own collection of Python types into play while also relying on Python's built-in ones. You can divide Blender's Python API into three buckets.

### Native Types

In the trivial cases, dressing up a bare number or string as a custom type would only get in the way, so what you get back is just an everyday native value.

- Blender float, int, boolean -> float, int, boolean

- Blender enumerator -> string

```pycon
>>> C.object.rotation_mode = '`AXIS_ANGLE`'
```

- Blender enumerator (multiple) -> set of strings

[Related references](INDEX.md).
