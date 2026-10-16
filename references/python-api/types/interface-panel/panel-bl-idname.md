# bpy.types.Panel: bl_idname

bl_idname

When provided, gives the panel an explicit ID; left unset, the panel inherits the defining class name. So a class named “`OBJECT_PT`_hello” with no script-assigned bl_idname ends up with bl_idname = “`OBJECT_PT`_hello”. (default “”, never None)

Type :

str

[Related references](INDEX.md).
