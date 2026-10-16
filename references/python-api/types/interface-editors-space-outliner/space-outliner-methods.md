# bpy.types.SpaceOutliner: methods

## SpaceOutliner(Space)

### SpaceOutliner(Space)

base classes — bpy_struct, Space
class bpy.types. SpaceOutliner ( Space )

The space data for the Outliner
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

The matching RNA type, or the default if none is found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default ( type | None ) – Value returned if nothing matches.

Returns :

The matching class, or the default if none is found.

Return type :

type
classmethod draw_handler_add ( callback , args , region_type , draw_type )

Register a fresh draw handler on this kind of space.
Whenever the named region of that space type is redrawn, the handler runs.
Note: for the moment, every argument here is positional-only.

Parameters :

- callback ( Callable [ ... , Any ] ) – A function invoked at region draw time.
It is handed the arguments listed below, and any value it hands back gets thrown away.

- args ( tuple [ Any , ... ] ) – Arguments handed to the callback.

- region_type ( str ) – The region type the callback draws in; usually WINDOW . (bpy.types.Region.type)

- draw_type ( str ) – Usually `POST_PIXEL` for 2D drawing and `POST_VIEW` for 3D drawing. In some cases `PRE_VIEW` can be used. BACKDROP can be used for backdrops in the node editor.

Returns :

A handler reference you can remove afterward.

Return type :

object
classmethod draw_handler_remove ( handler , region_type )

Detach a draw handler that had been registered earlier.

Parameters :

- handler ( object ) – The draw handler to take off.

- region_type ( str ) – The region type that handler was attached to.
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data Space.type | Space.show_locked_time Space.show_region_header |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert | bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Space.bl_rna_get_subclass Space.bl_rna_get_subclass_py Space.draw_handler_add Space.draw_handler_remove |

[Related references](INDEX.md).
