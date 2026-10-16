# bpy.ops.wm.tool_set_by_id

bpy.ops.wm. tool_set_by_id ( * , name = '' , cycle = False , as_fallback = False , space_type = 'EMPTY' ) 

Pick the tool based on label (to be used with input maps)

Parameters :

- name ( str ) – Identifier, Code reference of the tool (optional, never None)

- cycle ( bool ) – Cycle, Switch among instruments in this collection (optional)

- as_fallback ( bool ) – Set Fallback, Establish the alternate tool rather than the main tool (optional)

- space_type ( Literal [ 'EMPTY' , '`VIEW_3D`' , '`IMAGE_EDITOR`' , '`NODE_EDITOR`' , '`SEQUENCE_EDITOR`' , '`CLIP_EDITOR`' , '`DOPESHEET_EDITOR`' , '`GRAPH_EDITOR`' , '`NLA_EDITOR`' , '`TEXT_EDITOR`' , 'CONSOLE' , 'INFO' , 'TOPBAR' , 'STATUSBAR' , 'OUTLINER' , 'PROPERTIES' , '`FILE_BROWSER`' , 'SPREADSHEET' , 'PREFERENCES' ] ) – Type, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/wm.py:2348

[Related references](INDEX.md).
