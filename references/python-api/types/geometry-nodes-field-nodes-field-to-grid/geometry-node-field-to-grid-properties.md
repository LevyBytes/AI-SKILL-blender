# bpy.types.GeometryNodeFieldToGrid: properties

## GeometryNodeFieldToGrid(GeometryNode)

### GeometryNodeFieldToGrid(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeFieldToGrid ( GeometryNode ) 

Build fresh grids by sampling new values over the topology of an existing volume grid
active_index 

Index of the active item (in [0, inf], default 0)

Type :

int
active_item 

Index of the active item

Type :

RepeatItem
data_type 

Data type for topology grid (default 'FLOAT' )

Type :

Literal[Node Socket Data Type Items]
grid_items 

(default None, readonly)

Type :

GeometryNodeFieldToGridItems[GeometryNodeFieldToGridItem]

[Related references](INDEX.md).
