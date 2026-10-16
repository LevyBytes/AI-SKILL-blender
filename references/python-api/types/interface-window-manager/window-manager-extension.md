# bpy.types.WindowManager: extension_repo_filter, extension_search, extension_show_panel_available, extension_show_panel_installed, extension_tags, extension_type, extension_use_filter

extension_repo_filter

Filter extensions by repository

Type :

str
extension_search

Filter by extension name, author & category (default "", never None)

Type :

str
extension_show_panel_available

Show the available extensions panel (default True)

Type :

bool
extension_show_panel_installed

Show the installed extensions panel (default True)

Type :

bool
extension_tags

(default None, readonly)

Type :

bpy_prop_collection[ BlExtDummyGroup ]
extension_type

Show extensions by type (default 'ADDON' )

- ALL
All – Show all extension types.

- ADDON
Add-ons – Only show add-ons.

- THEME
Themes – Only show themes.

Type :

Literal['ALL', 'ADDON', 'THEME']
extension_use_filter

Filter Extensions by Tags & Repository (default False)

Type :

bool

[Related references](INDEX.md).
