# bpy.types.Struct: properties

## Struct(bpy_struct)

### Struct(bpy_struct)

base class: bpy_struct
class bpy.types. Struct ( bpy_struct )

The RNA definition of a structure.
base

Struct definition this is derived from (readonly)

Type :

Struct
description

Description of the Struct’s purpose (default “”, readonly, never None)

Type :

str
functions

(default None, readonly)

Type :

bpy_prop_collection[Function]
identifier

Unique name used in the code and scripting (default “”, readonly, never None)

Type :

str
name

Human readable name (default “”, readonly, never None)

Type :

str
name_property

Property that gives the name of the struct (readonly)

Type :

StringProperty
nested

Struct in which this struct is always nested, and to which it logically belongs (readonly)

Type :

Struct
properties

Properties in the struct (default None, readonly)

Type :

bpy_prop_collection[Property]
property_tags

Tags that properties can use to influence behavior (default None, readonly)

Type :

bpy_prop_collection[EnumPropertyItem]
translation_context

Translation context of the struct’s name (default “”, readonly, never None)

Type :

str

[Related references](INDEX.md).
