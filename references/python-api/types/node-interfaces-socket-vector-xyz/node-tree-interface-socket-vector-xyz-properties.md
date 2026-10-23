# bpy.types.NodeTreeInterfaceSocketVectorXYZ: properties

## NodeTreeInterfaceSocketVectorXYZ(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorXYZ(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorXYZ ( NodeTreeInterfaceSocket ) 

A node socket that handles a 3D vector
default_value 

Value the socket assumes when no wire reaches it (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

The vector socket's component count (in [2, 4], default 0)

Type :

int
max_value 

How high the value may go (in [-inf, inf], default 0.0)

Type :

float
min_value 

How low the value may go (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype recorded against the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
