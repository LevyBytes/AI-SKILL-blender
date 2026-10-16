# bpy.types.NodeTreeInterfaceSocketVectorXYZ4D: properties

## NodeTreeInterfaceSocketVectorXYZ4D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorXYZ4D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorXYZ4D ( NodeTreeInterfaceSocket ) 

A 3D vector socket that a node provides
default_value 

Value supplied to the socket whenever it lacks a connection (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Amount of components in the vector socket (in [2, 4], default 0)

Type :

int
max_value 

The value's ceiling (in [-inf, inf], default 0.0)

Type :

float
min_value 

The value's floor (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype recorded for the default (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
