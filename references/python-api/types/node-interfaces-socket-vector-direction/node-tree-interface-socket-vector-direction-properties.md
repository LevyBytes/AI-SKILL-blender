# bpy.types.NodeTreeInterfaceSocketVectorDirection: properties

## NodeTreeInterfaceSocketVectorDirection(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorDirection(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorDirection ( NodeTreeInterfaceSocket ) 

A node socket carrying a 3D vector
default_value 

Value supplied to the socket while nothing is wired into it (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

How many components the vector socket exposes (in [2, 4], default 0)

Type :

int
max_value 

Upper bound on the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Lower bound on the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

Which subtype the default value carries (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
