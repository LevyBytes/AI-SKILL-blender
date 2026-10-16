import bpy

# Minimal code to use above UIList...
class UIListPanelExample2(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UIList Example 2 Panel"
    bl_idname = "OBJECT_PT_ui_list_example_2"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # `template_list` now takes two new arguments.
        # The first one is the identifier of the registered UIList to use (if you want only the default list,
        # with no custom draw code, use "UI_UL_list").
        layout.template_list("MESH_UL_vgroups_slow", "", obj, "vertex_groups", obj.vertex_groups, "active_index")
