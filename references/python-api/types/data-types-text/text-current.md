# bpy.types.Text: current_character, current_line, current_line_index

current_character

Position of the caret’s character on the active line, doubling as the selection’s starting character when a selection is present (in [0, inf], default 0)

Type :

int
current_line

Current line, and start line of selection if one exists (readonly, never None)

Type :

TextLine
current_line_index

Index of current TextLine in TextLine collection (in [-inf, inf], default 0)

Type :

int

[Related references](INDEX.md).
