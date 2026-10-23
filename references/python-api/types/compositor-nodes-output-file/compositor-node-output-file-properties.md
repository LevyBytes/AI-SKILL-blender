# bpy.types.CompositorNodeOutputFile: properties

## CompositorNodeOutputFile(CompositorNode)

### CompositorNodeOutputFile(CompositorNode)

base classes: bpy_struct, Node, NodeInternal, CompositorNode
class bpy.types. CompositorNodeOutputFile ( CompositorNode )

Saves the incoming image out to a file on disk.
active_item_index

Position of the currently active item in the list (in [0, inf], default 0)

Type :

int
directory

Folder that the rendered image is saved into (default “”, never None, blend relative // prefix supported, Supports template expressions)

Type :

str
file_name

Stem used for the filename; depending on the node settings, extra details may be appended to what ends up on disk (default “”, never None, Supports template expressions)

Type :

str
file_output_items

(default None, readonly)

Type :

NodeCompositorFileOutputItems[NodeCompositorFileOutputItem]
format

(readonly)

Type :

ImageFormatSettings
save_as_render

When writing a byte image, also run the render portion of the display transform (default False)

Type :

bool

[Related references](INDEX.md).
