# bpy.types.Text: select_end_character, select_end_line, select_end_line_index

select_end_character

Position one character past the selection’s end, on the line where the selection finishes (in [0, inf], default 0)

Type :

int
select_end_line

End line of selection (readonly, never None)

Type :

TextLine
select_end_line_index

Index of last TextLine in selection (in [-inf, inf], default 0)

Type :

int

[Related references](INDEX.md).
