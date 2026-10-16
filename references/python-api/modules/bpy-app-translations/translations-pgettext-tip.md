# bpy.app.translations: bpy.app.translations. pgettext_tip ( msgid , msgctxt = None )

bpy.app.translations. pgettext_tip ( msgid , msgctxt = None )

Retrieve a translation for msgid when tooltip translations are enabled.

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
