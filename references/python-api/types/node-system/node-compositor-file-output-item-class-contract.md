# bpy.types.NodeCompositorFileOutputItem - class-contract, Inherited Properties, Inherited Functions, References

color

The color shown for this socket type within the node editor (array of 4 items, in [0, inf], default (0.0, 0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
format

(readonly)

Type :

ImageFormatSettings
name

(default “”, never None)

Type :

str
override_node_format

Save this file with its own format rather than the node's format (default False)

Type :

bool
save_as_render

When writing a byte image, run the render portion of the display transform first (default False)

Type :

bool
socket_type

(default 'FLOAT' )

Type :

Literal[Node Socket Data Type Items]
vector_socket_dimensions

How many dimensions the vector socket has (in [2, 4], default 0)

Type :

int
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
| CompositorNodeOutputFile.file_output_items NodeCompositorFileOutputItems.new | NodeCompositorFileOutputItems.remove |

[Related references](INDEX.md).
