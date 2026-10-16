# bpy.types.NodeTreeInterfaceSocketVectorTranslation: properties

## NodeTreeInterfaceSocketVectorTranslation(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorTranslation(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorTranslation ( NodeTreeInterfaceSocket ) 

A 3D vector socket used by a node
default_value 

The value the socket adopts while left unconnected (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
dimensions 

How many components belong to the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Most the value can be (in [-inf, inf], default 0.0)

Type :

float
min_value 

Least the value can be (in [-inf, inf], default 0.0)

Type :

float
subtype 

Subtype recorded for the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
