# bpy.types.NodeTreeInterfaceSocketVectorXYZ2D: properties

## NodeTreeInterfaceSocketVectorXYZ2D(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketVectorXYZ2D(NodeTreeInterfaceSocket) 

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketVectorXYZ2D ( NodeTreeInterfaceSocket ) 

A node socket transporting a 3D vector
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
default_value 

The value applied to the socket without an incoming link (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
dimensions 

Number of components carried by the vector socket (in [2, 4], default 0)

Type :

int
max_value 

Topmost value allowed (in [-inf, inf], default 0.0)

Type :

float
min_value 

Bottommost value allowed (in [-inf, inf], default 0.0)

Type :

float
subtype 

The subtype label of the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
