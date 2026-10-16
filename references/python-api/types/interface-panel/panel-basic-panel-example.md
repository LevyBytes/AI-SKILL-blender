# bpy.types.Panel: Basic Panel Example

### Basic Panel Example

A minimal panel that renders into the object properties area is shown below.

Observe the `CATEGORY_PT_name` value given to Panel.bl_idname — Blender expects panel IDs to follow that naming pattern.

Note

Blender only recognizes Panel subclasses once they have been registered.

```python
import bpy

class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_hello_world"
    bl_label = "Hello World"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        self.layout.label(text="Hello World")

bpy.utils.register_class(HelloWorldPanel)
```

[Related references](INDEX.md).
