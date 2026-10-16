# bpy.types.FileHandler: properties

bl_export_operator

Operator able to export files whose extensions are listed in bl_file_extensions (default “”, never None)

Type :

str
bl_file_extensions

A string listing the file extensions the file handler accepts; each one should begin with a “.” and be split apart by “;”.
For Example: ".blend;.ble"

(default “”, never None)

Type :

str
bl_idname

When set, gives the file handler a custom ID; otherwise it inherits the name of the class that defines it (so if the class is called “`OBJECT_FH`_hello” and the script leaves bl_idname unset, then bl_idname becomes “`OBJECT_FH`_hello”) (default “”, never None)

Type :

str
bl_import_operator

Operator able to import files whose extensions are listed in bl_file_extensions (default “”, never None)

Type :

str
bl_label

The label shown for the file handler (default “”, never None)

Type :

str

[Related references](INDEX.md).
