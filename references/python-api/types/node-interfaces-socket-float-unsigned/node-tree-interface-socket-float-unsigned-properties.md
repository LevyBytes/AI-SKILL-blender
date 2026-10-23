# bpy.types.NodeTreeInterfaceSocketFloatUnsigned: properties

## NodeTreeInterfaceSocketFloatUnsigned(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketFloatUnsigned(NodeTreeInterfaceSocket)

base classes: bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketFloatUnsigned ( NodeTreeInterfaceSocket )

A node socket that carries a floating-point number
default_value

Value fed in while the socket stays unlinked (in [0, inf], default 0.0)

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
