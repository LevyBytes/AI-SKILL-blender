# bpy.ops.wm.tool_set_by_index

bpy.ops.wm. tool_set_by_index ( * , index = 0 , cycle = False , expand = True , as_fallback = False , space_type = 'EMPTY' ) 

Activate the instrument by its slot number (to be used with shortcuts)

Parameters :

- index ( int ) – Index in Toolbar, (in [-inf, inf], optional)

- cycle ( bool ) – Cycle, Switch among tools in this set (optional)

- expand ( bool ) – expand, Allow tool subdivisions (optional)

- as_fallback ( bool ) – Set Fallback, Make the secondary tool active rather than principal (optional)

- space_type ( Literal [ 'EMPTY' , '`VIEW_3D`' , '`IMAGE_EDITOR`' , '`NODE_EDITOR`' , '`SEQUENCE_EDITOR`' , '`CLIP_EDITOR`' , '`DOPESHEET_EDITOR`' , '`GRAPH_EDITOR`' , '`NLA_EDITOR`' , '`TEXT_EDITOR`' , 'CONSOLE' , 'INFO' , 'TOPBAR' , 'STATUSBAR' , 'OUTLINER' , 'PROPERTIES' , '`FILE_BROWSER`' , 'SPREADSHEET' , 'PREFERENCES' ] ) – Type, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:2398

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:2398

[Related references](INDEX.md).
