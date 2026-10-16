# bpy.types.UILayout: grid_flow

grid_flow ( * , row_major = False , columns = 0 , even_columns = False , even_rows = False , align = False ) 

grid_flow

Parameters :

- row_major ( bool ) – Fill row by row, instead of column by column (optional)

- columns ( int ) – Number of columns, positive are absolute fixed numbers, 0 is automatic, negative are automatic multiple numbers along major axis (e.g. -2 will only produce 2, 4, 6 etc. columns for row major layout, and 2, 4, 6 etc. rows for column major layout). (in [-inf, inf], optional)

- even_columns ( bool ) – All columns will have the same width (optional)

- even_rows ( bool ) – All rows will have the same height (optional)

- align ( bool ) – Align buttons to each other (optional)

Returns :

Sub-layout to put items in

Return type :

UILayout

[Related references](INDEX.md).
