# bpy.types.Menu: properties

bl_description

(default "")

Type :

str
bl_idname

When set, this gives the menu an explicit ID; leave it unset and the menu inherits the defining class's name instead (so a class named "`OBJECT_MT`_hello" with no script-assigned bl_idname ends up with bl_idname = "`OBJECT_MT`_hello") (default "", never None)

Type :

str
bl_label

The menu label (default "", never None)

Type :

str
bl_options

Options for this menu type (default set())

- `SEARCH_ON_KEY_PRESS`
Search on Key Press – Open a menu search when a key pressed while the menu is open.

Type :

set[Literal[‘`SEARCH_ON_KEY_PRESS`’]]
bl_owner_id

(default "", never None)

Type :

str
bl_translation_context

(default "*", never None)

Type :

str
layout

Defines the structure of the menu in the UI (readonly)

Type :

UILayout

[Related references](INDEX.md).
