# bpy.types.NodeTreeInterfaceSocketVectorPercentage2D: properties

## NodeTreeInterfaceSocketVectorPercentage2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorPercentage2D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorPercentage2D ( NodeTreeInterfaceSocket ) 

A 3D vector socket on a node
default_value 

Value used by the socket while it remains unwired (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

Component total of the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Upper extreme of the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Lower extreme of the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype applied to the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
