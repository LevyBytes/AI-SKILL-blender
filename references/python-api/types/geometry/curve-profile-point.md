# bpy.types.CurveProfilePoint

handle_type_1

How the path interpolates here (default 'FREE' )

Type :

Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
handle_type_2

How the path interpolates here (default 'FREE' )

Type :

Literal['AUTO', 'VECTOR', 'FREE', 'ALIGN']
location

The point's X and Y position on the path (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
select

Whether the path point is currently selected (default False)

Type :

bool
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

- default ( type | None ) – The value to return when not found.

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
| CurveProfile.points CurveProfile.segments | CurveProfilePoints.add CurveProfilePoints.remove |
## CurveProfilePoint(bpy_struct)

### CurveProfilePoint(bpy_struct)

base class: bpy_struct
class bpy.types. CurveProfilePoint ( bpy_struct )

A point that helps define a profile path.

[Related references](INDEX.md).
