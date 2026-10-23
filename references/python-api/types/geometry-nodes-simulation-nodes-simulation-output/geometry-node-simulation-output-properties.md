# bpy.types.GeometryNodeSimulationOutput: properties

## GeometryNodeSimulationOutput(GeometryNode)

### GeometryNodeSimulationOutput(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSimulationOutput ( GeometryNode ) 

Emits data out of the simulation zone.
active_index 

Where the active item sits in the list (in [0, inf], default 0)

Type :

int
active_item 

The list position of the currently active item

Type :

SimulationStateItem
state_items 

(default None, readonly)

Type :

NodeGeometrySimulationOutputItems[SimulationStateItem]

[Related references](INDEX.md).
