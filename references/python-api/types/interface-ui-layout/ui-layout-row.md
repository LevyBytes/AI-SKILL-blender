# bpy.types.UILayout: row

row ( * , align = False , heading = '' , heading_ctxt = '' , translate = True ) 

Sub-layout. Items placed in this sublayout are placed next to each other in a row.

Parameters :

- align ( bool ) – Align buttons to each other (optional)

- heading ( str ) – Heading, Label to insert into the layout for this sub-layout (optional, never None)

- heading_ctxt ( str ) – Override automatic translation context of the given heading (optional, never None)

- translate ( bool ) – Translate the given heading, when UI translation is enabled (optional)

Returns :

Sub-layout to put items in

Return type :

UILayout

[Related references](INDEX.md).
