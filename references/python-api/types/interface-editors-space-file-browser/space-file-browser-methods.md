# bpy.types.SpaceFileBrowser: methods

## SpaceFileBrowser(Space)

### SpaceFileBrowser(Space)

base classes — bpy_struct, Space
class bpy.types. SpaceFileBrowser ( Space )

The space data for the file browser
activate_asset_by_id ( id_to_activate , * , deferred = False )

Make active and select the asset entry standing for the given ID

Parameters :

- id_to_activate (ID) – id_to_activate

- deferred ( bool ) – Whether the ID becomes active right away (false) or once the file browser has refreshed (true) (optional)
activate_file_by_relative_path ( * , relative_path = '' )

Make a file active and add it to the selection, keyed by its path relative to the current File Browser directory

Parameters :

relative_path ( str ) – relative_path, (optional, never None)
deselect_all ( )

Clear the selection of all files
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

[Related references](INDEX.md).
