import bpy
import pxr.Gf as Gf
import pxr.Sdf as Sdf
import pxr.UsdShade as UsdShade

def on_export(export_context):
    """ Include the Blender filepath in the root layer custom data.
    """

    stage = export_context.get_stage()

    if stage is None:
        return False
    data = bpy.data
    if data is None:
        return False

    # Set the custom data.
    rootLayer = stage.GetRootLayer()
    customData = rootLayer.customLayerData
    customData["blenderFilepath"] = data.filepath
    rootLayer.customLayerData = customData

    return True

def on_material_export(export_context, bl_material, usd_material):
    """ Create a simple MaterialX shader on the exported material.
    """

    stage = export_context.get_stage()

    # Create a MaterialX standard surface shader
    mtl_path = usd_material.GetPrim().GetPath()
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("mtlxstandard_surface"))
    shader.CreateIdAttr("ND_standard_surface_surfaceshader")

    # Connect the shader.  MaterialX materials use "mtlx" renderContext
    usd_material.CreateSurfaceOutput("mtlx").ConnectToSource(shader.ConnectableAPI(), "out")

    # Set the color to the Blender material's viewport display color.
    col = bl_material.diffuse_color
    shader.CreateInput("base_color", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(col[0], col[1], col[2]))

    return True
