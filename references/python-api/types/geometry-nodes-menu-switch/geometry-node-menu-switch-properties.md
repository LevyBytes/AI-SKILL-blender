# bpy.types.GeometryNodeMenuSwitch: properties

## GeometryNodeMenuSwitch(GeometryNode)

### GeometryNodeMenuSwitch(GeometryNode) 

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMenuSwitch ( GeometryNode ) 

Pick among several inputs by referencing their names.
active_index 

Position of the currently selected item (in [0, inf], default 0)

Type :

int
active_item 

Active item

Type :

NodeEnumItem
data_type 

(default 'GEOMETRY' )

Type :

Literal[Node Socket Data Type Items]
enum_definition 

Reaching the enum definition straight from the node is now supported; this remains only so older setups keep working. (readonly)

Type :

Node
enum_items 

(default None, readonly)

Type :

NodeMenuSwitchItems[NodeEnumItem]

[Related references](INDEX.md).
