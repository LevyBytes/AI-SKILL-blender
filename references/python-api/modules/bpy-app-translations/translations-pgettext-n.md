# bpy.app.translations: bpy.app.translations. pgettext_n ( msgid , msgctxt = None )

bpy.app.translations. pgettext_n ( msgid , msgctxt = None )

Extract msgid into translation files as a candidate for translation. No actual translation occurs; it only marks the string.

Note

See pgettext() notes.

Parameters :

- msgid ( str ) – The string to extract for translation.

- msgctxt ( str | None ) – The context for the translation (defaults to `BLT_I18NCONTEXT_DEFAULT`).

Returns :

The initial string unchanged.

Return type :

str

[Related references](INDEX.md).
