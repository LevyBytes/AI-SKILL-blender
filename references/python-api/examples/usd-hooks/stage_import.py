import bpy
import textwrap
import pxr.Usd as Usd
import pxr.Sdf as Sdf

def on_import(import_context):
    """Inspect the imported stage & objects to set some custom data
    """

    ###########################################################
    # Store some USD metadata on each imported data-block.
    ###########################################################
    prim_map = import_context.get_prim_map()

    # Store prim path as a string on each data-block created.
    for prim_path, data_blocks in prim_map.items():

        # Type hints for prim map.
        prim_path: Sdf.Path
        data_blocks: list[bpy.types.ID]

        # Loop over mapped data-blocks to store some metadata.
        for data_block in data_blocks:
            data_block["prim_path"] = str(prim_path)

    ###########################################################
    # Create a text object to display the stage's custom data.
    ###########################################################
    stage = import_context.get_stage()

    if stage is None:
        return False

    # Get the custom data.
    rootLayer = stage.GetRootLayer()
    customData = rootLayer.customLayerData

    # Create a text object to display the stage path
    # and custom data dictionary entries.

    bpy.ops.object.text_add()
    ob = bpy.context.view_layer.objects.active

    if (ob is None) or (ob.data is None):
        return False

    ob.name = "layer_data"
    ob.data.name = "layer_data"

    # The stage root path is the first line.
    text = rootLayer.realPath

    # Append key/value strings, enforcing text wrapping.
    for item in customData.items():
        print(item)
        text += '\n'
        line = str(item[0]) + ': ' + str(item[1])
        text += textwrap.fill(line, width=80)

    ob.data.body = text

    return True
