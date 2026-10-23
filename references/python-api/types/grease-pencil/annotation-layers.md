# bpy.types.AnnotationLayers

active_index

Index of active annotation layer (in [0, inf], default 0)

Type :

int
active_note

Note/Layer to add annotation strokes to (default 'DEFAULT' )

Type :

Literal['DEFAULT']
new ( name , * , set_active = True )

Instantiate a new annotation layer.

Parameters :

- name ( str ) – Name, Name of the layer (never None)

- set_active ( bool ) – Set Active, Set the newly created layer to the active layer (optional)

Returns :

The newly created layer

Return type :

AnnotationLayer
remove ( layer )

Delete a annotation layer.

Parameters :

layer (AnnotationLayer) – The layer to remove (never None)
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
| Annotation.layers | |
## AnnotationLayers(bpy_prop_collection)

Container of annotation layers.

base classes: bpy_prop, bpy_prop_collection
class bpy.types. AnnotationLayers ( bpy_prop_collection )

Collection of annotation layer objects.

[Related references](INDEX.md).
