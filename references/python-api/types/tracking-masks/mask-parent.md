# bpy.types.MaskParent

id

ID-block that the masking element is parented to, or one of its properties

Type :

ID
id_type

Which kind of ID-block may be used (default 'MOVIECLIP' )

Type :

Literal[‘MOVIECLIP’]
parent

Name of the parent object inside the chosen data-block that drives the parenting (default “”, never None)

Type :

str
sub_parent

Name of the parent sub-object inside the chosen data-block that drives the parenting (default “”, never None)

Type :

str
type

Parent Type (default '`POINT_TRACK`' )

Type :

Literal[‘`POINT_TRACK`’, ‘`PLANE_TRACK`’]
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
| MaskSplinePoint.parent | |
## MaskParent(bpy_struct)

### MaskParent(bpy_struct)

base class — bpy_struct
class bpy.types. MaskParent ( bpy_struct )

Settings that parent a masking element.

[Related references](INDEX.md).
