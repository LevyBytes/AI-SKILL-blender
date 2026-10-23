# bpy.types.NodeTreeInterfaceSocketVectorDirection4D: properties

## NodeTreeInterfaceSocketVectorDirection4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorDirection4D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorDirection4D ( NodeTreeInterfaceSocket ) 

A node socket for a 3D vector
default_value 

Default that applies whenever the socket is left unconnected (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Number of vector components the socket has (in [2, 4], default 0)

Type :

int
max_value 

The largest value allowed (in [-inf, inf], default 0.0)

Type :

float
min_value 

The smallest value allowed (in [-inf, inf], default 0.0)

Type :

float
subtype 

Default value's subtype (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
