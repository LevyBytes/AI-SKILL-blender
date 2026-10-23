# bpy.types.SpaceSequenceEditor: methods

## SpaceSequenceEditor(Space)

### SpaceSequenceEditor(Space)

base classes: bpy_struct, Space
class bpy.types. SpaceSequenceEditor ( Space )

Data for the sequence editor space
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

Either the matching RNA type, or the default when there is no match.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default ( type | None ) – Value returned if nothing matches.

Returns :

Either the matching class, or the default when there is no match.

Return type :

type
classmethod draw_handler_add ( callback , args , region_type , draw_type )

Register a fresh draw handler on this space type. The handler runs each time the named region of the
space type is redrawn. Keep in mind that, for the moment, every argument is positional only.

Parameters :

- callback ( Callable [ ... , Any ] ) – Function invoked while the region is being drawn.
The supplied arguments are passed to it, and whatever it returns is discarded.

- args ( tuple [ Any , ... ] ) – Arguments handed to the callback.

- region_type ( str ) – Which region type the callback renders into; typically WINDOW . (bpy.types.Region.type)

- draw_type ( str ) – Generally `POST_PIXEL` for 2D and `POST_VIEW` for 3D; `PRE_VIEW` occasionally applies, and BACKDROP serves node-editor backdrops.

Returns :

A handler you can later remove.

Return type :

object
classmethod draw_handler_remove ( handler , region_type )

Detach a draw handler that had been registered earlier.

Parameters :

- handler ( object ) – The draw handler to detach.

- region_type ( str ) – Region type to which the callback had been attached.
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data Space.type | Space.show_locked_time Space.show_region_header |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert | bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Space.bl_rna_get_subclass Space.bl_rna_get_subclass_py Space.draw_handler_add Space.draw_handler_remove |

[Related references](INDEX.md).
