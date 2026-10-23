# bpy.types.Operator: Enum Search Popup

### Enum Search Popup 

When you want an operator to ask the user to pick an entry from a search field, reach for bpy.types.Operator.invoke_search_popup .

```python
import bpy
from bpy.props import EnumProperty

class SearchEnumOperator(bpy.types.Operator):
    bl_idname = "object.search_enum_operator"
    bl_label = "Search Enum Operator"
    bl_property = "my_search"

    my_search: EnumProperty(
        name="My Search",
        items=(
            ('FOO', "Foo", ""),
            ('BAR', "Bar", ""),
            ('BAZ', "Baz", ""),
        ),
    )

    def execute(self, context):
        self.report({'INFO'}, "Selected:" + self.my_search)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.invoke_search_popup(self)
        return {'RUNNING_MODAL'}

### Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(SearchEnumOperator.bl_idname, text="Search Enum Operator")

### Register and add to the object menu (required to also use F3 search "Search Enum Operator" for quick access).
bpy.utils.register_class(SearchEnumOperator)
bpy.types.VIEW3D_MT_object.append(menu_func)

### Test call.
bpy.ops.object.search_enum_operator('INVOKE_DEFAULT')
```

base class: bpy_struct

[Related references](INDEX.md).
