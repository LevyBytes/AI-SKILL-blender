# bpy.types.GeometryNodeViewer: properties

## GeometryNodeViewer(GeometryNode)

### GeometryNodeViewer(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeViewer ( GeometryNode )

Sends the connected data to the Spreadsheet Editor so it can be inspected.
active_index

Where the active item sits in the list (in [0, inf], default 0)

Type :

int
active_item

Type :

NodeGeometryViewerItem
domain

The domain over which fields get evaluated (default 'POINT' )

Type :

Literal[Attribute Domain With Auto Items]
ui_shortcut

(in [-32768, 32767], default 0)

Type :

int
viewer_items

(default None, readonly)

Type :

NodeGeometryViewerItems[NodeGeometryViewerItem]

[Related references](INDEX.md).
