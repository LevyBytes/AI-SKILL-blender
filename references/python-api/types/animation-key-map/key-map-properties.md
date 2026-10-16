# bpy.types.KeyMap: properties

## KeyMap(bpy_struct)

### KeyMap(bpy_struct) 

base class — bpy_struct
class bpy.types. KeyMap ( bpy_struct ) 

Holds an input setup together with its keymaps
bl_owner_id 

Owner used internally (default “”, never None)

Type :

str
is_modal 

Marks the keymap as one that converts modal events for an operator (default False, readonly)

Type :

bool
is_user_modified 

Set when the user has authored this keymap (default False)

Type :

bool
keymap_items 

The entries of the keymap, each tying an operator to an input event (default None, readonly)

Type :

KeyMapItems[KeyMapItem]
modal_event_values 

Exposes the event values available to items of this modal keymap (#KeyMapItem.propvalue), intended for API introspection (default None, readonly)

Type :

bpy_prop_collection[EnumPropertyItem]
name 

The key map's name (default “”, readonly, never None)

Type :

str
region_type 

If set, the region type this keymap belongs to (default 'WINDOW' , readonly)

Type :

Literal[Region Type Items]
show_expanded_children 

Whether children are unfolded in the interface (default False)

Type :

bool
show_expanded_items 

Whether the entry is unfolded in the interface (default False)

Type :

bool
space_type 

If set, the space type this keymap belongs to (default 'EMPTY' , readonly)

Type :

Literal[Space Type Items]

[Related references](INDEX.md).
