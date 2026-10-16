# bpy.types.NodeTreeInterfaceSocketVectorEuler: properties

## NodeTreeInterfaceSocketVectorEuler(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorEuler(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorEuler ( NodeTreeInterfaceSocket ) 

A socket on a node that carries a 3D vector
default_value 

Standby value the socket uses when nothing connects to it (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
dimensions 

Count of components in the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Ceiling for the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Floor for the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

The subtype tag on the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
