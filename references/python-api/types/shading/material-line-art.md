# bpy.types.MaterialLineArt

intersection_priority

The intersection line is assigned to whichever object has the higher intersection priority value (in [0, 255], default 0)

Type :

int
mat_occlusion

Faces with this material act as though they carry the set number of layers for occlusion (in [0, 255], default 1)

Type :

int
use_intersection_priority_override

Override the intersection priority value of the object and collection (default False)

Type :

bool
use_material_mask

Filter occluded strokes out using material masks (default False)

Type :

bool
use_material_mask_bits

(array of 8 items, default (False, False, False, False, False, False, False, False))

Type :

bpy_prop_array[bool]
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
| Material.lineart | |
## MaterialLineArt(bpy_struct)

### MaterialLineArt(bpy_struct)

base class — bpy_struct
class bpy.types. MaterialLineArt ( bpy_struct )

[Related references](INDEX.md).
