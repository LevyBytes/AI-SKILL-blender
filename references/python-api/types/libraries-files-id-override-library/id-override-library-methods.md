# bpy.types.IDOverrideLibrary: methods

operations_update ( )

Rebuild the override's list of operations from the differences between this override ID and its reference.
reset ( * , do_hierarchy = True , set_system_override = False )

Bring this override back in line with its linked reference ID.

Parameters :

- do_hierarchy ( bool ) – Reset this override's dependencies too so they line up with their own reference linked IDs (optional)

- set_system_override ( bool ) – Demote every user-editable override into a non-editable system override (optional)
destroy ( * , do_hierarchy = True )

Delete this override ID and send everything that referenced it back to the linked reference ID.

Parameters :

do_hierarchy ( bool ) – Delete this override's dependencies too and point their usages back at their reference linked IDs (optional)
resync ( scene , * , view_layer = None , residual_storage = None , do_hierarchy_enforce = False , do_whole_hierarchy = False )

Re-synchronize the data-block and its sub-hierarchy, or the entire hierarchy when asked.

Parameters :

- scene (Scene) – Scene the operation runs in, used for contextual matters such as keeping the active object active and making sure every overridden object stays instantiated (never None)

- view_layer (ViewLayer) – View layer the operation runs in, used like the scene argument; when omitted the scene's collection stands in for it (optional)

- residual_storage (Collection) – Collection that catches objects no longer instantiated in any other collection (a garbage bin, created on demand when none is supplied) (optional)

- do_hierarchy_enforce ( bool ) – Force the dependency hierarchy among data-blocks back into line with the reference linked hierarchy (WARNING: any ID pointers you deliberately overrode get reset to their defaults) (optional)

- do_whole_hierarchy ( bool ) – Resync the entire hierarchy that contains this data-block, not just its own sub-hierarchy (optional)

Returns :

Success, Whether the resync process was successful or not

Return type :

bool
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
| ID.override_library | |

[Related references](INDEX.md).
