# bpy.ops.wm.tool_set_by_brush_type

bpy.ops.wm. tool_set_by_brush_type ( * , brush_type = '' , space_type = 'EMPTY' ) 

Identify the fitting tool for this brush category then turn it on

Parameters :

- brush_type ( str ) – Brush Type, Category identifier for the appropriate tool will be discovered (optional, never None)

- space_type ( Literal [ 'EMPTY' , '`VIEW_3D`' , '`IMAGE_EDITOR`' , '`NODE_EDITOR`' , '`SEQUENCE_EDITOR`' , '`CLIP_EDITOR`' , '`DOPESHEET_EDITOR`' , '`GRAPH_EDITOR`' , '`NLA_EDITOR`' , '`TEXT_EDITOR`' , 'CONSOLE' , 'INFO' , 'TOPBAR' , 'STATUSBAR' , 'OUTLINER' , 'PROPERTIES' , '`FILE_BROWSER`' , 'SPREADSHEET' , 'PREFERENCES' ] ) – Type, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:2439

[Related references](INDEX.md).
