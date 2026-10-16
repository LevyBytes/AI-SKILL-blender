# bpy.types.RigidBodyWorld: methods

convex_sweep_test ( object , start , end )

Sweep test convex rigidbody against the current rigidbody world

Parameters :

- object (Object) – Rigidbody object with a convex collision shape (never None)

- start (mathutils.Vector) – (array of 3 items, in [-inf, inf])

- end (mathutils.Vector) – (array of 3 items, in [-inf, inf])

Returns :

object_location , The hit location of this sweep test, mathutils.Vector

hitpoint , The hit location of this sweep test, mathutils.Vector

normal , The face normal at the sweep test hit location, mathutils.Vector

has_hit , If the function has found collision point, value is 1, otherwise 0, int

Return type :

tuple[mathutils.Vector, mathutils.Vector, mathutils.Vector, int]
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
| Scene.rigidbody_world | |

[Related references](INDEX.md).
