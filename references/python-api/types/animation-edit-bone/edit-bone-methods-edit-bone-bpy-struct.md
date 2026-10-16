# bpy.types.EditBone: methods — EditBone(bpy_struct), EditBone(bpy_struct), Inherited Properties, Inherited Functions

## EditBone(bpy_struct)

### EditBone(bpy_struct)

base class — bpy_struct
class bpy.types. EditBone ( bpy_struct )

A bone as it appears while editing an armature data-block
bl_system_properties_get ( * , do_create = False )

DEBUG ONLY. A low-level way into the RNA data storage defined at runtime, meant strictly for tests and debugging. Steer clear of it in ordinary scripts, and never count on its contents being writable

Parameters :

do_create ( bool ) – Create the system properties if none exist so far (optional)

Returns :

The root container for system properties, or None when this data holds none yet and you didn’t ask for them to be created

Return type :

PropertyGroup
align_roll ( vector )

Set the bone’s local-space roll so its Z axis lines up with the supplied vector

Parameters :

vector (mathutils.Vector) – Vector, (array of 3 items, in [-inf, inf])
align_orientation ( other )

Line this bone up with another by shifting its tail and setting its roll;
the other bone’s length plays no part.
parent_index ( parent_test )

Equivalent to ‘bone in other_bone.parent_recursive’
but without building a list along the way.
transform ( matrix , * , scale = True , roll = True )

Transform the bone’s head, tail, roll and envelope
(the envelope only when the matrix carries a scale component).

Parameters :

- matrix (mathutils.Matrix) – 3x3 or 4x4 transformation matrix.

- scale ( bool ) – Scale the bone envelope by the matrix.

- roll ( bool ) – Correct the roll to point in the same relative
direction to the head and tail.
translate ( vec )

A convenience for adding vec to this bone’s head and tail.
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

[Related references](INDEX.md).
