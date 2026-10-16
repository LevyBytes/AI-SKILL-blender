import bpy
from .group_list import MESH_UL_vgroups_slow
from .panel import UIListPanelExample2

def register():
    bpy.utils.register_class(MESH_UL_vgroups_slow)
    bpy.utils.register_class(UIListPanelExample2)


def unregister():
    bpy.utils.unregister_class(UIListPanelExample2)
    bpy.utils.unregister_class(MESH_UL_vgroups_slow)


if __name__ == "__main__":
    register()
