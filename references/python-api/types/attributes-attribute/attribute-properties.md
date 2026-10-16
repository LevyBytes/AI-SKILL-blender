# bpy.types.Attribute: properties

data_type

Type of data stored in attribute (default 'FLOAT' , readonly)

Type :

Literal[Attribute Type Items]
domain

Domain of the Attribute (default 'POINT' , readonly)

Type :

Literal[Attribute Domain Items]
is_internal

The attribute is meant for internal use by Blender (default False, readonly)

Type :

bool
is_required

Whether the attribute can be removed or renamed (default False, readonly)

Type :

bool
name

Name of the Attribute (default "", never None)

Type :

str
storage_type

Method used to store the data (default 'ARRAY' , readonly)

Type :

Literal[Attr Storage Type Items]

[Related references](INDEX.md).
