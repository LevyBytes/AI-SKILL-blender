# bpy.types.Macro: properties

bl_cursor_pending

Cursor shown while waiting for the user to pick a location that triggers the operator (applies when bl_options has `DEPENDS_ON_CURSOR` set) (default 'DEFAULT' )

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

Flags configuring this operator type (default set())

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
has_reports

Whether the operator produced any reports — warnings and errors — on its last run (default False, readonly)

Type :

bool
name

(default “”, readonly, never None)

Type :

str
properties

(readonly, never None)

Type :

OperatorProperties

[Related references](INDEX.md).
