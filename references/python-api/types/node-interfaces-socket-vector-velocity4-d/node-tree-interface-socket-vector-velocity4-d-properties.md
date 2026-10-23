# bpy.types.NodeTreeInterfaceSocketVectorVelocity4D: properties

## NodeTreeInterfaceSocketVectorVelocity4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorVelocity4D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorVelocity4D ( NodeTreeInterfaceSocket ) 

A socket for a 3D vector on a node
default_value 

Value drawn upon while the socket stays unconnected (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

The total components on the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Upper limit of the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Lower limit of the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

The default's subtype identifier (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
