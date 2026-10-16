# bpy.types.NodeTreeInterfaceSocketFloatFactor: properties

## NodeTreeInterfaceSocketFloatFactor(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketFloatFactor(NodeTreeInterfaceSocket)

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketFloatFactor ( NodeTreeInterfaceSocket )

A node socket that carries a floating-point number
default_value

Value fed in while the socket stays unlinked (in [0, 1], default 1.0)

Type :

float
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
