# bpy.types.UILayout: template_list ( listtype_name , list_id , dataptr , propname , active_dataptr , active_propname , * , item_dyntip_propname = '' , rows = 5 , maxrows = 5 , type = 'DEFAULT' , columns = 9 , sort_reverse = False , sort_lock = False )

template_list ( listtype_name , list_id , dataptr , propname , active_dataptr , active_propname , * , item_dyntip_propname = '' , rows = 5 , maxrows = 5 , type = 'DEFAULT' , columns = 9 , sort_reverse = False , sort_lock = False )

Item. A list control for showing collections of data such as vertex groups.

Parameters :

- listtype_name ( str ) – Identifier of the list type to use (never None)

- list_id ( str ) – Identifier of this list widget. Necessary to tell apart different list widgets. Mandatory when using default “`UI_UL`_list” class. If this not an empty string, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is “`OBJECT_UL`_vgroups”, and list_id is not set by the script, then bl_idname = “`OBJECT_UL`_vgroups”) (never None)

- dataptr (AnyType) – Data from which to take the Collection property

- propname ( str ) – Identifier of the Collection property in data (never None)

- active_dataptr (AnyType) – Data from which to take the integer property, index of the active item (never None)

- active_propname ( str ) – Identifier of the integer property in active_data, index of the active item (never None)

- item_dyntip_propname ( str ) – Identifier of a string property in items, to use as tooltip content (optional, never None)

- rows ( int ) – Default and minimum number of rows to display (in [0, inf], optional)

- maxrows ( int ) – Default maximum number of rows to display (in [0, inf], optional)

- type (Literal[Uilist Layout Type Items]) – Type, Type of layout to use (optional)

- columns ( int ) – Number of items to display per row, for GRID layout (in [0, inf], optional)

- sort_reverse ( bool ) – Display items in reverse order by default (optional)

- sort_lock ( bool ) – Lock display order to default value (optional)

[Related references](INDEX.md).
