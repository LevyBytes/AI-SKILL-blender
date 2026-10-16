# bpy.types.GeometryNodeRepeatOutput: properties

## GeometryNodeRepeatOutput(GeometryNode)

### GeometryNodeRepeatOutput(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeRepeatOutput ( GeometryNode )
active_index

Position of the item currently active (in [0, inf], default 0)

Type :

int
active_item

Position of the item currently active

Type :

RepeatItem
inspection_index

The iteration number read by inspection tools such as the viewer node or socket inspection (in [-inf, inf], default 0)

Type :

int
repeat_items

(default None, readonly)

Type :

NodeGeometryRepeatOutputItems[RepeatItem]

[Related references](INDEX.md).
