# bpy.types.Particle: methods

## Particle(bpy_struct)

### Particle(bpy_struct)

base class: bpy_struct
class bpy.types. Particle ( bpy_struct )

A single particle belonging to a particle system
uv_on_emitter ( modifier )

Look up the UV coordinates of a particle on an evaluated mesh.

Parameters :

modifier (ParticleSystemModifier) – Particle modifier from an evaluated object (never None)

Returns :

uv, (array of 2 items, in [-inf, inf])

Return type :

mathutils.Vector
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
| ParticleHairKey.co_object ParticleHairKey.co_object_set ParticleSystem.mcol_on_emitter | ParticleSystem.particles ParticleSystem.uv_on_emitter |

[Related references](INDEX.md).
