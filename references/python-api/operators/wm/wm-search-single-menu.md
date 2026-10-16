# bpy.ops.wm.search_single_menu

bpy.ops.wm. search_single_menu ( * , menu_idname = '' , initial_query = '' )

Displays a popup to search within a specific menu in current context

Parameters :

- menu_idname ( str ) – Menu Name, Menu to search in (optional, never None)

- initial_query ( str ) – Initial Query, Query to insert into the search box (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.wm.search_single_menu(*, menu_idname='', initial_query='')

Pops up a search for a menu in the current context.
Parameters:
- menu_idname ( str ) – Menu Name, Menu to search in (optional, never None)
- initial_query ( str ) – Initial Query, Query to insert into the search box (optional, never None)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
