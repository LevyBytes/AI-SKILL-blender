# bpy.types.Menu: Basic Menu Example

### Basic Menu Example

A minimal menu is shown below. What sets a menu apart from a panel is that it has to be invoked from a header, a panel, or some other menu rather than standing on its own.

The `CATEGORY_MT_name` form in `Menu.bl_idname` follows the standard naming pattern Blender expects for menus.

Note

Before a menu subclass can be referenced inside Blender, it has to be registered first.

Note

For menus, `UILayout.operator_context` defaults to `'EXEC_REGION_WIN'` instead of `'INVOKE_REGION_WIN'` (see Execution Context). Should an operator need to gather its inputs through `Operator.invoke`, you must assign that context yourself. Once a menu is embedded in something like a panel or a header, it picks up whatever execution context those elements use.

```python
import bpy

class BasicMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_select_test"
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
        layout.operator("object.select_random", text="Random")

bpy.utils.register_class(BasicMenu)

# Test call to display immediately.
bpy.ops.wm.call_menu(name="OBJECT_MT_select_test")
```

[Related references](INDEX.md).
