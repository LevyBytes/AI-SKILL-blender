# bpy.types.NodeTreeInterfaceSocketVectorVelocity: properties

## NodeTreeInterfaceSocketVectorVelocity(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorVelocity(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorVelocity ( NodeTreeInterfaceSocket ) 

A node socket conveying a 3D vector value
default_value 

The value pulled in when the socket has nothing connected (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Count of the vector socket's components (in [2, 4], default 0)

Type :

int
max_value 

Greatest allowed magnitude (in [-inf, inf], default 0.0)

Type :

float
min_value 

Smallest allowed magnitude (in [-inf, inf], default 0.0)

Type :

float
subtype 

The subtype noted on the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
