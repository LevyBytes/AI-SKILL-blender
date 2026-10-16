# bpy.types.Operator: bl_cursor_pending, bl_description, bl_idname, bl_label, bl_options, bl_translation_context, bl_undo_group, bl_property

bl_cursor_pending 

Cursor shown while the user is being asked to pick a spot to fire the operator (when bl_options carries `DEPENDS_ON_CURSOR`) (default 'DEFAULT' )

Type :

Literal[Window Cursor Items]
bl_description 

(default “”, never None)

Type :

str
bl_idname 

(default “”, never None)

Type :

str
bl_label 

(default “”, never None)

Type :

str
bl_options 

Options for this operator type (default set())

Type :

set[Literal[Operator Type Flag Items]]
bl_translation_context 

(default “Operator”, never None)

Type :

str
bl_undo_group 

(default “”, never None)

Type :

str
bl_property 

The name of the property treated as this operator's primary one. At present it only picks the default property used when an operator is expanded into a menu.

Type :

str

[Related references](INDEX.md).
