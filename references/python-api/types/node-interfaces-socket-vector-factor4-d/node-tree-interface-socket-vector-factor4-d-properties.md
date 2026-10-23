# bpy.types.NodeTreeInterfaceSocketVectorFactor4D: properties

## NodeTreeInterfaceSocketVectorFactor4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorFactor4D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorFactor4D ( NodeTreeInterfaceSocket ) 

A node socket conveying a 3D vector
default_value 

Value the socket falls back on with no connection present (array of 4 items, in [0, 1], default (0.0, 0.0, 0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

Number of elements in the vector socket (in [2, 4], default 0)

Type :

int
max_value 

The maximum it is permitted to reach (in [-inf, inf], default 0.0)

Type :

float
min_value 

The minimum it is permitted to reach (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype tied to the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
