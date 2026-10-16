# bpy.types.SpaceConsole: properties

## SpaceConsole(Space)

### SpaceConsole(Space)

base classes — bpy_struct, Space
class bpy.types. SpaceConsole ( Space )

The interactive Python console
font_size

Size of the font used to render the text (in [1, 256], default 0)

Type :

int
history

The history of commands (default None, readonly)

Type :

bpy_prop_collection[ConsoleLine]
language

Language used by the command line prompt (default “”, never None)

Type :

str
prompt

The command line prompt (default “”, never None)

Type :

str
scrollback

Output produced by commands (default None, readonly)

Type :

bpy_prop_collection[ConsoleLine]
select_end

(in [0, inf], default 0)

Type :

int
select_start

(in [0, inf], default 0)

Type :

int

[Related references](INDEX.md).
