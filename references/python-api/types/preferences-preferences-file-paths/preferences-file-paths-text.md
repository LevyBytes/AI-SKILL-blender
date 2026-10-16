# bpy.types.PreferencesFilePaths: text_editor, text_editor_args

text_editor

Command that launches the text editor, given as a full path or a command on $PATH.
Leave blank to fall back to the internal editor

(default “”, never None)

Type :

str
text_editor_args

Sets the exact argument layout the text editor uses when opening files. The available expansions are:

$filepath The file's absolute path.
$line Which line to jump to (Optional).
$column Which column, counted from the line's start, to jump to (Optional).
$line0 & column0 start at zero.
Example: -f $filepath -l $line -c $column

(default “”, never None)

Type :

str

[Related references](INDEX.md).
