# bpy.types.UIList: properties

bitflag_filter_item

The value of the reserved bitflag ‘`FILTER_ITEM`’ (in filter_flags values) (in [0, inf], default 0, readonly)

Type :

int
bitflag_item_never_show

Skip the item from displaying in the list (in [0, inf], default 0, readonly)

Type :

int
bl_idname

If this is set, the uilist gets a custom ID, otherwise it takes the name of the class used to define the uilist (for example, if the class name is “`OBJECT_UL`_vgroups”, and bl_idname is not set by the script, then bl_idname = “`OBJECT_UL`_vgroups”) (default “”, never None)

Type :

str
filter_name

Only show items matching this name (use ‘*’ as wildcard) (default “”, never None)

Type :

str
layout_type

(default 'DEFAULT' , readonly)

Type :

Literal[Uilist Layout Type Items]
list_id

Identifier of the list, if any was passed to the “list_id” parameter of “template_list()” (default “”, readonly, never None)

Type :

str
use_filter_invert

Invert filtering (show hidden items, and vice versa) (default False)

Type :

bool
use_filter_show

Show filtering options (default False)

Type :

bool
use_filter_sort_alpha

Sort items by their name (default False)

Type :

bool
use_filter_sort_lock

Lock the order of shown items (user cannot change it) (default False)

Type :

bool
use_filter_sort_reverse

Reverse the order of shown items (default False)

Type :

bool

[Related references](INDEX.md).
