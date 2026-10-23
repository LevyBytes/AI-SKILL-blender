# bpy.types.Header

bl_idname

Set this to give the header a custom ID; leave it unset and the defining class name is used instead. So with a class named "`OBJECT_HT`_hello" and no bl_idname in the script, bl_idname = "`OBJECT_HT`_hello" (default "", never None)

Type :

str
bl_region_type

The region where the header is going to be used in (defaults to header region) (default 'HEADER' )

Type :

Literal[Region Type Items]
bl_space_type

The space where the header is going to be used in (default 'EMPTY' )

Type :

Literal[Space Type Items]
layout

Structure of the header in the UI (readonly)

Type :

UILayout
draw ( context )

Draw UI elements into the header UI layout
classmethod append ( draw_func )

Append a draw function to this menu,
takes the same arguments as the menus draw function
classmethod is_extended ( )
classmethod prepend ( draw_func )

Prepend a draw function to this menu, takes the same arguments as
the menus draw function
classmethod remove ( draw_func )

Remove a draw function that has been added to this menu.
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
## Header(bpy_struct)

### Header(bpy_struct)

base class: bpy_struct
class bpy.types. Header ( bpy_struct )

Holds the UI widgets that make up an editor's header bar.

[Related references](INDEX.md).
