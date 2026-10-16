bl_info = {
    "name": "USD Hook Example",
    "blender": (4, 4, 0),
}

import bpy
import bpy.types
import textwrap

# Make `pxr` module available, for running as `bpy` PIP package.
bpy.utils.expose_bundled_modules()

from .exports import on_export, on_material_export
from .stage_import import on_import
from .material_import import material_import_poll, on_material_import

class USDHookExample(bpy.types.USDHook):
    """Example implementation of USD IO hooks"""
    bl_idname = "usd_hook_example"
    bl_label = "Example"
    on_export = staticmethod(on_export)
    on_material_export = staticmethod(on_material_export)
    on_import = staticmethod(on_import)
    material_import_poll = staticmethod(material_import_poll)
    on_material_import = staticmethod(on_material_import)

def register():
    bpy.utils.register_class(USDHookExample)


def unregister():
    bpy.utils.unregister_class(USDHookExample)


if __name__ == "__main__":
    register()
