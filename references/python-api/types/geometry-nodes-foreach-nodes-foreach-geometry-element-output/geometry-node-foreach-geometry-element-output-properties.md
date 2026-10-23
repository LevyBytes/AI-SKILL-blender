# bpy.types.GeometryNodeForeachGeometryElementOutput: properties

## GeometryNodeForeachGeometryElementOutput(GeometryNode)

### GeometryNodeForeachGeometryElementOutput(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeForeachGeometryElementOutput ( GeometryNode )
active_generation_index 

Index of the active item (in [0, inf], default 0)

Type :

int
active_input_index 

Index of the active item (in [0, inf], default 0)

Type :

int
active_main_index 

Index of the active item (in [0, inf], default 0)

Type :

int
domain 

The geometry domain that the loop runs across (default 'POINT' )

Type :

Literal[Attribute Domain Items]
generation_items 

(default None, readonly)

Type :

NodeGeometryForeachGeometryElementGenerationItems[ForeachGeometryElementGenerationItem]
input_items 

(default None, readonly)

Type :

NodeGeometryForeachGeometryElementInputItems[ForeachGeometryElementInputItem]
inspection_index 

The iteration index referenced by inspection tools such as the viewer node or socket inspection (in [-inf, inf], default 0)

Type :

int
main_items 

(default None, readonly)

Type :

NodeGeometryForeachGeometryElementMainItems[ForeachGeometryElementMainItem]

[Related references](INDEX.md).
