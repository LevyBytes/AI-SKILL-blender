# bpy.types.SpacePreferences: properties

## SpacePreferences(Space)

### SpacePreferences(Space)

base classes — bpy_struct, Space
class bpy.types. SpacePreferences ( Space )

The space data for the Blender preferences
filter_text

The term used to filter the UI (default “”, never None)

Type :

str
filter_type

Which method drives the filtering (default 'NAME' )

- NAME
Name – Filter based on the operator name.

- KEY
Key-Binding – Filter based on key bindings.

Type :

Literal[‘NAME’, ‘KEY’]
search_filter

The string used for live search filtering (default “”, never None)

Type :

str
show_region_ui

(default False)

Type :

bool
tab_search_results

Whether each visible tab turned up a search result (default False, readonly)

Type :

bool

[Related references](INDEX.md).
