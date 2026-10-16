# bpy.types.NodeTreeInterfaceSocketVectorDirection2D: properties

## NodeTreeInterfaceSocketVectorDirection2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorDirection2D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorDirection2D ( NodeTreeInterfaceSocket ) 

A node socket holding a 3D vector
default_value 

Fallback fed in when the socket has no incoming link (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Component count of the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Highest permitted value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Lowest permitted value (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype assigned to the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
