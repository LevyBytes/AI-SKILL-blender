# bpy.types.UILayout: column, column_flow

column ( * , align = False , heading = '' , heading_ctxt = '' , translate = True ) 

Sub-layout. Items placed in this sublayout are placed under each other in a column.

Parameters :

- align ( bool ) – Align buttons to each other (optional)

- heading ( str ) – Heading, Label to insert into the layout for this sub-layout (optional, never None)

- heading_ctxt ( str ) – Override automatic translation context of the given heading (optional, never None)

- translate ( bool ) – Translate the given heading, when UI translation is enabled (optional)

Returns :

Sub-layout to put items in

Return type :

UILayout
column_flow ( * , columns = 0 , align = False ) 

column_flow

Parameters :

- columns ( int ) – Number of columns, 0 is automatic (in [0, inf], optional)

- align ( bool ) – Align buttons to each other (optional)

Returns :

Sub-layout to put items in

Return type :

UILayout

[Related references](INDEX.md).
