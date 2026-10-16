# bpy.types.NodeTreeInterfaceSocketIntFactor: properties

## NodeTreeInterfaceSocketIntFactor(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketIntFactor(NodeTreeInterfaceSocket)

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketIntFactor ( NodeTreeInterfaceSocket )

A node socket that carries an integer value
default_value

Value fed in while the socket stays unlinked (in [0, inf], default 0)

Type :

int
max_value

Upper bound on the value (in [-inf, inf], default 0)

Type :

int
min_value

Lower bound on the value (in [-inf, inf], default 0)

Type :

int
subtype

Variant tag applied to the default value (default 'DEFAULT' )

Type :

Literal[‘DEFAULT’]

[Related references](INDEX.md).
