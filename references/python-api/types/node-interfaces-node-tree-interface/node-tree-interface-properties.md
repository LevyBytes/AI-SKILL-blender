# bpy.types.NodeTreeInterface: properties

## NodeTreeInterface(bpy_struct)

### NodeTreeInterface(bpy_struct) 

base class: bpy_struct
class bpy.types. NodeTreeInterface ( bpy_struct ) 

The set of sockets and UI panels that a node group declares.
active 

Active item

Type :

NodeTreeInterfaceItem
active_index 

Position of the currently active item (in [0, inf], default 0)

Type :

int
items_tree 

Every entry held in the node interface (default None, readonly)

Type :

bpy_prop_collection[NodeTreeInterfaceItem]

[Related references](INDEX.md).
