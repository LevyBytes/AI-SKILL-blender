# bpy.types.WindowManager: addon_filter, addon_search, addon_support, addon_tags

addon_filter

Filter add-ons by category

Type :

str
addon_search

Filter by add-on name, author & category (default "", never None)

Type :

str
addon_support

Display support level (default { 'COMMUNITY' , 'OFFICIAL' })

- OFFICIAL
Official – Officially supported.

- COMMUNITY
Community – Maintained by community developers.

Type :

set[Literal['OFFICIAL', 'COMMUNITY']]
addon_tags

(default None, readonly)

Type :

bpy_prop_collection[ BlExtDummyGroup ]

[Related references](INDEX.md).
