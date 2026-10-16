# bpy.types.WorkSpaceTool: setup

setup ( idname , * , cursor = 'DEFAULT' , keymap = '' , gizmo_group = '' , brush_type = '' , data_block = '' , operator = '' , index = 0 , options = set() , idname_fallback = '' , keymap_fallback = '' ) 

Configure the tool's settings

Parameters :

- idname ( str ) – Identifier, (never None)

- cursor (Literal[Window Cursor Items]) – cursor, (optional)

- keymap ( str ) – Key Map, (optional, never None)

- gizmo_group ( str ) – Gizmo Group, (optional, never None)

- brush_type ( str ) – Brush Type, Confine this tool to one kind of brush (optional)

- data_block ( str ) – Data Block, (optional, never None)

- operator ( str ) – Operator, (optional, never None)

- index ( int ) – Index, (in [-inf, inf], optional)

- options ( set [ Literal [ '`KEYMAP_FALLBACK`' , '`USE_BRUSHES`' ] ] ) – Tool Options, (optional)

- `KEYMAP_FALLBACK`
Fallback.

- `USE_BRUSHES`
Uses Brushes – Allow this tool to use brushes via the asset system.

- idname_fallback ( str ) – Fallback Identifier, (optional, never None)

- keymap_fallback ( str ) – Fallback Key Map, (optional, never None)

[Related references](INDEX.md).
