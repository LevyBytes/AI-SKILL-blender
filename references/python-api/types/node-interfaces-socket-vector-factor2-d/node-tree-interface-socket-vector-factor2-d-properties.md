# bpy.types.NodeTreeInterfaceSocketVectorFactor2D: properties

## NodeTreeInterfaceSocketVectorFactor2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorFactor2D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorFactor2D ( NodeTreeInterfaceSocket ) 

A 3D-vector socket attached to a node
default_value 

Substitute value for the socket while it stays disconnected (array of 2 items, in [0, 1], default (0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

The number of components the vector socket carries (in [2, 4], default 0)

Type :

int
max_value 

Greatest value it may take (in [-inf, inf], default 0.0)

Type :

float
min_value 

Least value it may take (in [-inf, inf], default 0.0)

Type :

float
subtype 

Default's assigned subtype (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
