# bpy.types.UI_UL_list

classmethod sort_items_by_name ( items , propname = 'name' ) 

Re-order items using their names (case-insensitive).
propname is the name of the string property to use for sorting.
return a list mapping org_idx -> new_idx,
or an empty list if no sorting has been done.

static sort_items_helper ( sort_data , key , reverse = False ) 

Common sorting utility. Returns a neworder list mapping org_idx -> new_idx.
sort_data must be an (unordered) list of tuples [(org_idx, …), (org_idx, …), …].
key must be the same kind of callable you would use for sorted() builtin function.
reverse will reverse the sorting!
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
| bpy_struct.id_data UIList.bl_idname UIList.list_id UIList.layout_type UIList.use_filter_show UIList.filter_name | UIList.use_filter_invert UIList.use_filter_sort_alpha UIList.use_filter_sort_reverse UIList.use_filter_sort_lock UIList.bitflag_filter_item UIList.bitflag_item_never_show |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module | bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values UIList.bl_system_properties_get UIList.draw_item UIList.draw_filter UIList.filter_items UIList.append UIList.is_extended UIList.prepend UIList.remove UIList.bl_rna_get_subclass UIList.bl_rna_get_subclass_py |
## `UI_UL`_list(UIList)

### `UI_UL`_list(UIList) 

base classes: bpy_struct, UIList

class bpy.types. `UI_UL`_list ( UIList ) 

static filter_items_by_name ( pattern , bitflag , items , propname = 'name' , flags = None , reverse = False ) 

Set `FILTER_ITEM` for items which name matches filter_name one (case-insensitive).
pattern is the filtering pattern.
propname is the name of the string property to use for filtering.
flags must be a list of integers the same length as items, or None!
return a list of flags (based on given flags if not None),
or an empty list if no flags were given and no filtering has been done.

[Related references](INDEX.md).
