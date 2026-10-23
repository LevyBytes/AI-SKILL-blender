# bpy.types.NodeTreeInterfaceSocketVectorTranslation4D: properties

## NodeTreeInterfaceSocketVectorTranslation4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorTranslation4D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorTranslation4D ( NodeTreeInterfaceSocket ) 

A node's 3D vector socket
default_value 

The figure the socket uses while nothing is plugged in (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Component quantity of the vector socket (in [2, 4], default 0)

Type :

int
max_value 

The value's upper bound (in [-inf, inf], default 0.0)

Type :

float
min_value 

The value's lower bound (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype kept for the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
