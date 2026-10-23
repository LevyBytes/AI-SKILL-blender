# bpy.types.VolumeRender

clipping

Threshold below which voxels count as empty so rendering can be optimized (in [0, 1], default 0.001)

Type :

float
precision

Choose the precision of the volume data. Smaller settings save memory but lose detail. (default 'HALF' )

- FULL
Full – Store every value as a 32-bit float.

- HALF
Half – Store every value as a 16-bit float.

- VARIABLE
Variable – Quantize using a variable number of bits.

Type :

Literal['FULL', 'HALF', 'VARIABLE']
space

Choose whether volume density and step size are measured in object or world space (default 'OBJECT' )

- OBJECT
Object – Hold opacity and detail steady no matter the object's scale.

- WORLD
World – Measure the step size and density in world space.

Type :

Literal['OBJECT', 'WORLD']
step_size

Spacing between volume samples. Smaller values capture more detail but cost performance. A value of zero lets Blender derive the step size from voxel size. (in [0, inf], default 0.0)

Type :

float
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
| Volume.render | |
## VolumeRender(bpy_struct)

### VolumeRender(bpy_struct)

base class: bpy_struct
class bpy.types. VolumeRender ( bpy_struct )

Render settings for a volume object.

[Related references](INDEX.md).
