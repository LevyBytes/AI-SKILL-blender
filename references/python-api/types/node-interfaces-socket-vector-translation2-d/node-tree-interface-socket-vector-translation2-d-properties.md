# bpy.types.NodeTreeInterfaceSocketVectorTranslation2D: properties

## NodeTreeInterfaceSocketVectorTranslation2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorTranslation2D(NodeTreeInterfaceSocket) 

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorTranslation2D ( NodeTreeInterfaceSocket ) 

A node socket holding a 3D vector value
default_value 

Value the socket supplies absent any incoming connection (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
dimensions 

The component count for the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Maximum bound of the value (in [-inf, inf], default 0.0)

Type :

float
min_value 

Minimum bound of the value (in [-inf, inf], default 0.0)

Type :

float
subtype 

The default value's subtype designation (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
