# bpy.types.SpaceTextEditor: methods

## SpaceTextEditor(Space)

### SpaceTextEditor(Space)

base classes: bpy_struct, Space
class bpy.types. SpaceTextEditor ( Space )

Data for the text editor space
is_syntax_highlight_supported ( )

Reports True when the editor can syntax-highlight the active text data-block

Return type :

bool
region_location_from_cursor ( line , column )

Work out the region position for a given line together with its column offset

Parameters :

- line ( int ) – Line, Line index (in [-inf, inf])

- column ( int ) – Column, Column index (in [-inf, inf])

Returns :

Region coordinates (array of 2 items, in [-1, inf])

Return type :

bpy_prop_array[int]
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

[Related references](INDEX.md).
