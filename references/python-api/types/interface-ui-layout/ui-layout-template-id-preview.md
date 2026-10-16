# bpy.types.UILayout: template_ID_preview ( data , property , * , new = '' , open = '' , unlink = '' , rows = 0 , cols = 0 , filter = 'ALL' , hide_buttons = False )

template_ID_preview ( data , property , * , new = '' , open = '' , unlink = '' , rows = 0 , cols = 0 , filter = 'ALL' , hide_buttons = False )

template_ID_preview

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- new ( str ) – Operator identifier to create a new ID block (optional, never None)

- open ( str ) – Operator identifier to open a file for creating a new ID block (optional, never None)

- unlink ( str ) – Operator identifier to unlink the ID block (optional, never None)

- rows ( int ) – Number of thumbnail preview rows to display, (in [0, inf], optional)

- cols ( int ) – Number of thumbnail preview columns to display, (in [0, inf], optional)

- filter ( Literal [ 'ALL' , 'AVAILABLE' ] ) – Optionally limit the items which can be selected (optional)

- hide_buttons ( bool ) – Show only list, no buttons (optional)

[Related references](INDEX.md).
