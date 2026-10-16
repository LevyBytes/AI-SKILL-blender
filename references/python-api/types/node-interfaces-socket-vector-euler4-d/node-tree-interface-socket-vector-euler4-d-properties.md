# bpy.types.NodeTreeInterfaceSocketVectorEuler4D: properties

## NodeTreeInterfaceSocketVectorEuler4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorEuler4D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorEuler4D ( NodeTreeInterfaceSocket ) 

A 3D vector socket belonging to a node
default_value 

The value applied while the socket sits unconnected (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion
dimensions 

Tally of components held by the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Cap on the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Base limit on the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

The default value's subtype label (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
