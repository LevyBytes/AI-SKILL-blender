# bpy.types.NodeTreeInterfaceSocketVectorVelocity2D: properties

## NodeTreeInterfaceSocketVectorVelocity2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorVelocity2D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorVelocity2D ( NodeTreeInterfaceSocket ) 

A 3D vector socket living on a node
default_value 

The standby value while the socket carries no link (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
dimensions 

How many components the socket's vector spans (in [2, 4], default 0)

Type :

int
max_value 

The largest value supported (in [-inf, inf], default 0.0)

Type :

float
min_value 

The smallest value supported (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype stamped on the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
