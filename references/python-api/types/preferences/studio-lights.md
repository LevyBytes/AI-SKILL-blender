# bpy.types.StudioLights

load ( path , type )

Load studiolight from file

Parameters :

- path ( str ) – File Path, File path where the studio light file can be found (never None)

- type ( Literal [ 'STUDIO' , 'WORLD' , 'MATCAP' ] ) – Type, The type for the new studio light

Returns :

Newly created StudioLight

Return type :

StudioLight
new ( path )

Create studiolight from default lighting

Parameters :

path ( str ) – Path, Path to the file that will contain the lighting info (without extension) (never None)

Returns :

Newly created StudioLight

Return type :

StudioLight
remove ( studio_light )

Remove a studio light

Parameters :

studio_light (StudioLight) – The studio light to remove (never None)
refresh ( )

Refresh Studio Lights from disk
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
| Preferences.studio_lights | |
## StudioLights(bpy_prop_collection)

### StudioLights(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types. StudioLights ( bpy_prop_collection )

A group of studio lights.

[Related references](INDEX.md).
