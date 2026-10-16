# bpy.types.Driver

expression

The expression evaluated for a Scripted Expression (default “”, never None)

Type :

str
is_simple_expression

The scripted expression is simple enough to run without the full Python interpreter (default False, readonly)

Type :

bool
is_valid

A past evaluation of the driver failed, so it ought to be passed over (default True)

Type :

bool
type

Which kind of driver this is (default 'AVERAGE' )

Type :

Literal[‘AVERAGE’, ‘SUM’, ‘SCRIPTED’, ‘MIN’, ‘MAX’]
use_self

Expose a ‘self’ entry in the namespace so drivers can readily point at the data they’re changing — object, bone, and the like (default False)

Type :

bool
variables

The properties feeding values into this driver (default None, readonly)

Type :

ChannelDriverVariables[DriverVariable]
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| FCurve.driver | |
## Driver(bpy_struct)

### Driver(bpy_struct)

base class — bpy_struct
class bpy.types. Driver ( bpy_struct )

Sets a property’s value by deriving it from an outside value

[Related references](INDEX.md).
