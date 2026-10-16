# bpy.types.NodeTreeInterfaceSocket: default_attribute_name, default_input

default_attribute_name 

Name applied to the attribute by default once a geometry nodes modifier drives the node group (default “”, never None)

Type :

str
default_input 

Source for the value when nothing is wired in. Needs “Hide Value”. (default 'VALUE' )

- VALUE
Default Value – The node socket’s default value.

- INDEX
Index – The index from the context.

- `ID_OR_INDEX`
ID or Index – The “id” attribute if available, otherwise the index.

- NORMAL
Normal – The geometry’s normal direction.

- POSITION
Position – The position from the context.

- `INSTANCE_TRANSFORM`
Instance Transform – Transformation of each instance from the geometry context.

- `HANDLE_LEFT`
Left Handle – The left Bézier control point handle from the context.

- `HANDLE_RIGHT`
Right Handle – The right Bézier control point handle from the context.

Type :

Literal[‘VALUE’, ‘INDEX’, ‘`ID_OR_INDEX`’, ‘NORMAL’, ‘POSITION’, ‘`INSTANCE_TRANSFORM`’, ‘`HANDLE_LEFT`’, ‘`HANDLE_RIGHT`’]

[Related references](INDEX.md).
