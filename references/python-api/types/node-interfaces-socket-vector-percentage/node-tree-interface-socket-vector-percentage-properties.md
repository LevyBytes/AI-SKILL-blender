# bpy.types.NodeTreeInterfaceSocketVectorPercentage: properties

## NodeTreeInterfaceSocketVectorPercentage(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorPercentage(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorPercentage ( NodeTreeInterfaceSocket ) 

A node socket that passes a 3D vector
default_value 

The value relied on when the socket is not hooked up (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

How many parts the vector socket contains (in [2, 4], default 0)

Type :

int
max_value 

Largest figure permitted (in [-inf, inf], default 0.0)

Type :

float
min_value 

Smallest figure permitted (in [-inf, inf], default 0.0)

Type :

float
subtype 

The subtype set on the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
