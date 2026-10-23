# bpy.types.GeometryNodeBake: properties

## GeometryNodeBake(GeometryNode)

### GeometryNodeBake(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeBake ( GeometryNode )

Stores the incoming data so it stays available without being recalculated.
active_index

Index of the active item (in [0, inf], default 0)

Type :

int
active_item

Index of the active item

Type :

RepeatItem
bake_items

(default None, readonly)

Type :

NodeGeometryBakeItems[NodeGeometryBakeItem]

[Related references](INDEX.md).
