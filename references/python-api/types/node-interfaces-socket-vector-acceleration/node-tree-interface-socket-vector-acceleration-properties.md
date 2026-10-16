# bpy.types.NodeTreeInterfaceSocketVectorAcceleration: properties

## NodeTreeInterfaceSocketVectorAcceleration(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorAcceleration(NodeTreeInterfaceSocket)

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorAcceleration ( NodeTreeInterfaceSocket )

A node socket holding a 3D vector
default_value

Value fed in while the socket stays unlinked (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions

Component count of the vector socket (in [2, 4], default 0)

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

Variant tag applied to the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
