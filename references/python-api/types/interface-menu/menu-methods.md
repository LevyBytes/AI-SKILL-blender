# bpy.types.Menu: methods

classmethod poll ( context )

When this method yields a non-null result, the menu is allowed to be drawn

Return type :

bool
draw ( context )

Lay out the menu's interface widgets within its UI layout
classmethod append ( draw_func )

Add a draw function onto the end of this menu; it receives the same arguments the menu's own draw function does
classmethod draw_collapsible ( context , layout )
draw_preset ( _context )

Set the following on your subclass:
- preset_operator (string)
- preset_subdir (string)

Optionally:
- preset_add_operator (string)
- preset_extensions (set of strings)
- preset_operator_defaults (dict of keyword args)
classmethod is_extended ( )
path_menu ( searchpaths , operator , * , props_default = None , prop_filepath = 'filepath' , filter_ext = None , filter_path = None , display_name = None , add_operator = None , add_operator_props = None , translate = True )

Populate a menu from a list of paths.

Parameters :

- searchpaths ( Sequence [ str ] ) – Paths to scan.

- operator ( str ) – The operator id to use with each file.

- prop_filepath ( str ) – Optional operator filepath property (defaults to "filepath").

- props_default ( dict [ str , Any ] | None ) – Properties to assign to each operator.

- filter_ext ( Callable [ [ str ] , bool ] | None ) – Optional callback that takes the file extensions.

Return false to drop the file from the listing.

- display_name ( Callable [ [ str ] , str ] | None ) – Optional callback that takes the full path, returns the name to display.
classmethod prepend ( draw_func )

Add a draw function onto the front of this menu; it receives the same arguments the menu's own draw function does
classmethod remove ( draw_func )

Detach a draw function that was previously attached to this menu.
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

[Related references](INDEX.md).
