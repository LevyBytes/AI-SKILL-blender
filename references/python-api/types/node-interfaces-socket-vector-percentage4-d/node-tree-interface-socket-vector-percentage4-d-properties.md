# bpy.types.NodeTreeInterfaceSocketVectorPercentage4D: properties

## NodeTreeInterfaceSocketVectorPercentage4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorPercentage4D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorPercentage4D ( NodeTreeInterfaceSocket ) 

A socket carrying a 3D vector for a node
default_value 

What feeds in when no link reaches the socket (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

Number of components present on the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Highest figure it may hold (in [-inf, inf], default 0.0)

Type :

float
min_value 

Lowest figure it may hold (in [-inf, inf], default 0.0)

Type :

float
subtype 

The subtype marking the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
