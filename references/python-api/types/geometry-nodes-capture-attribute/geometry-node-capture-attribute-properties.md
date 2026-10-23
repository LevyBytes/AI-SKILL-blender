# bpy.types.GeometryNodeCaptureAttribute: properties

## GeometryNodeCaptureAttribute(GeometryNode)

### GeometryNodeCaptureAttribute(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCaptureAttribute ( GeometryNode )

Saves a field's result on a geometry and exposes the data through a node socket. Lets you retain or interpolate data while the geometry changes, for instance positions captured before deformation.
active_index

Index of the active item (in [0, inf], default 0)

Type :

int
active_item

Index of the active item

Type :

RepeatItem
capture_items

(default None, readonly)

Type :

NodeGeometryCaptureAttributeItems[NodeGeometryCaptureAttributeItem]
domain

The domain the data is kept in (default 'POINT' )

Type :

Literal[Attribute Domain Items]

[Related references](INDEX.md).
