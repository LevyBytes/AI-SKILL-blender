# bpy.types.NodeTreeInterfaceSocketVectorEuler2D: properties

## NodeTreeInterfaceSocketVectorEuler2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorEuler2D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorEuler2D ( NodeTreeInterfaceSocket ) 

A node's socket that conveys a 3D vector
default_value 

What the socket reads when it is wired to nothing (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

bpy_prop_array[float]
dimensions 

Quantity of components on the vector socket (in [2, 4], default 0)

Type :

int
max_value 

The value's maximum (in [-inf, inf], default 0.0)

Type :

float
min_value 

The value's minimum (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype carried by the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
