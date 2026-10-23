# bpy.types.ViewLayer: methods

## ViewLayer(bpy_struct)

### ViewLayer(bpy_struct)

base class: bpy_struct
class bpy.types. ViewLayer ( bpy_struct )

View layer
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
bl_system_properties_get ( * , do_create = False )

DEBUG ONLY. Low-level entry point to runtime-defined RNA storage, meant purely for tests and debugging. Steer clear of it in normal scripts, and never assume what it returns is writable.

Parameters :

do_create ( bool ) – Ensure that system properties are created if they do not exist yet (optional)

Returns :

The root container for system properties, or None when none are stored yet on this data and creation was not asked for

Return type :

PropertyGroup
classmethod update_render_passes ( )

Re-fetch the set of enabled render passes from the render engine
update ( )

Refresh data flagged for update following earlier access to data or operators
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

| Members | Members |
| --- | --- |
| bpy.context.view_layer Context.view_layer Depsgraph.view_layer Depsgraph.view_layer_eval ID.override_hierarchy_create IDOverrideLibrary.resync LayerCollection.has_selected_objects Object.hide_get Object.hide_set Object.holdout_get Object.indirect_only_get | Object.select_get Object.select_set Object.visible_get RenderEngine.register_pass RenderEngine.update_render_passes Scene.statistics Scene.view_layers ViewLayers.new ViewLayers.remove Window.view_layer |

[Related references](INDEX.md).
