# bpy.types.SpaceNodeOverlay: properties

## SpaceNodeOverlay(bpy_struct)

### SpaceNodeOverlay(bpy_struct)

base class — bpy_struct
class bpy.types. SpaceNodeOverlay ( bpy_struct )

Configuration for the overlays drawn in the Node Editor
preview_shape

Which shape the node previews take (default 'FLAT' )

- FLAT
Flat – Use the default flat previews.

- 3D
3D – Use the material preview scene for the node previews.

Type :

Literal[‘FLAT’, ‘3D’]
show_context_path

Draw breadcrumbs showing the editor's context (default True)

Type :

bool
show_named_attributes

Indicate when nodes make use of named attributes (default True)

Type :

bool
show_overlays

Draw overlays such as colored or dashed wires (default True)

Type :

bool
show_previews

Draw a node's preview when that node is toggled on (default False)

Type :

bool
show_reroute_auto_labels

Label reroute nodes from the label of the reroute nodes they connect to (default False)

Type :

bool
show_timing

Draw how long each node took to run last time (default False)

Type :

bool
show_wire_color

Tint node links according to the sockets they connect (default True)

Type :

bool

[Related references](INDEX.md).
