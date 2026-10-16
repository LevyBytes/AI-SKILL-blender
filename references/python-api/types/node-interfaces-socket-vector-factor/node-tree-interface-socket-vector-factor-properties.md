# bpy.types.NodeTreeInterfaceSocketVectorFactor: properties

## NodeTreeInterfaceSocketVectorFactor(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorFactor(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorFactor ( NodeTreeInterfaceSocket ) 

A node socket that transports a 3D vector
default_value 

The reading taken from the socket whenever it has no link (array of 3 items, in [0, 1], default (0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

How many entries make up the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Top of the allowed range (in [-inf, inf], default 0.0)

Type :

float
min_value 

Bottom of the allowed range (in [-inf, inf], default 0.0)

Type :

float
subtype 

Which subtype is attached to the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
