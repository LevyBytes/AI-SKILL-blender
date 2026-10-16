# bpy.app.translations: bpy.app.translations. pgettext_data ( msgid , msgctxt = None )

bpy.app.translations. pgettext_data ( msgid , msgctxt = None )

Get a translation for msgid when data-object name translations are active.

Note

See pgettext() notes.

Parameters :

- msgid ( str ) – The text to translate.

- msgctxt ( str | None ) – The context for the translation (defaults to `BLT_I18NCONTEXT_DEFAULT`).

Returns :

The translated version (or msgid if unavailable).

Return type :

str

[Related references](INDEX.md).
