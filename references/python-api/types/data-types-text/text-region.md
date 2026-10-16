# bpy.types.Text: region_as_string, region_from_string

region_as_string ( * , range = None )

Parameters :

range ( tuple [ tuple [ int , int ] , tuple [ int , int ] ] | None ) – The region of text to be returned, defaulting to the selection when no range is passed.
Each int pair represents a line and column: ((start_line, start_column), (end_line, end_column))
The values match Python’s slicing logic (negative values count backwards from the end, the end value is not inclusive).

Returns :

The specified region as a string.

Return type :

str
region_from_string ( body , / , * , range = None )

Parameters :

- body ( str ) – The text to be inserted.

- range ( tuple [ tuple [ int , int ] , tuple [ int , int ] ] | None ) – The region of text to be returned, defaulting to the selection when no range is passed.
Each int pair represents a line and column: ((start_line, start_column), (end_line, end_column))
The values match Python’s slicing logic (negative values count backwards from the end, the end value is not inclusive).

[Related references](INDEX.md).
