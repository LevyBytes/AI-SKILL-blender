# bpy.types.MeshDeformModifier

invert_vertex_group

Invert vertex group influence (default False)

Type :

bool
is_bound

Whether geometry has been bound to control cage (default False, readonly)

Type :

bool
object

Mesh object to deform with

Type :

Object
precision

The grid size for binding (in [2, 10], default 5)

Type :

int
use_dynamic_bind

Recompute binding dynamically on top of other deformers (slower and more memory consuming) (default False)

Type :

bool
vertex_group

Vertex group name (default "", never None)

Type :

str
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
| bpy_struct.id_data Modifier.name Modifier.type Modifier.show_viewport Modifier.show_render Modifier.show_in_editmode Modifier.show_on_cage | Modifier.show_expanded Modifier.is_active Modifier.use_pin_to_last Modifier.is_override_data Modifier.use_apply_on_spline Modifier.execution_time Modifier.persistent_uid |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Modifier.bl_rna_get_subclass Modifier.bl_rna_get_subclass_py |
## MeshDeformModifier(Modifier)

### MeshDeformModifier(Modifier)

base classes: bpy_struct, Modifier
class bpy.types. MeshDeformModifier ( Modifier )

Mesh deformation modifier to deform with other meshes

[Related references](INDEX.md).
