import pxr.UsdShade as UsdShade

def material_import_poll(import_context, usd_material):
    """
    Return True if the given USD material can be converted.
    Return False otherwise.
    """
    # We can convert MaterialX.
    surf_output = usd_material.GetSurfaceOutput("mtlx")
    return bool(surf_output)

def on_material_import(import_context, bl_material, usd_material):
    """
    Import a simple mtlx material.  Just handle the base_color input
    of a ND_standard_surface_surfaceshader.
    """

    # We must confirm that we can handle this material.
    surf_output = usd_material.GetSurfaceOutput("mtlx")
    if not surf_output:
        return False

    if not surf_output.HasConnectedSource():
        return False

    # Get the connected surface output source.
    source = surf_output.GetConnectedSource()
    # Get the shader prim from the source
    shader = UsdShade.Shader(source[0])
    shader_id = shader.GetShaderId()
    if shader_id != "ND_standard_surface_surfaceshader":
        return False

    color_attr = shader.GetInput("base_color")
    if color_attr is None:
        return False

    # Create the node tree
    nodes = bl_material.node_tree.nodes
    output = nodes.new(type="ShaderNodeOutputMaterial")
    bsdf = nodes.new(type="ShaderNodeBsdfPrincipled")
    bsdf.location[0] -= 1.5 * bsdf.width
    bl_material.node_tree.links.new(output.inputs["Surface"], bsdf.outputs["BSDF"])
    bsdf_base_color_input = bsdf.inputs['Base Color']

    # Try to set the default color value.
    # Get the authored default value
    color = color_attr.Get()

    if color is None:
        return False

    bsdf_base_color_input.default_value = (color[0], color[1], color[2], 1)

    return True
