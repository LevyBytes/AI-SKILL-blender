# bpy.app.translations: bpy.app.translations. pgettext ( msgid , msgctxt = None )

bpy.app.translations. pgettext ( msgid , msgctxt = None )

Attempt to retrieve a translated version of the supplied msgid using an optional context.

Note

The parameter order (msgid first, then optional msgctxt) differs from standard gettext, enabling single-argument calls (context falls back to `BLT_I18NCONTEXT_DEFAULT`).

Note

Generally avoid this in production add-ons—Blender's core handles translations internally. Exception: strings with format specifiers (like "File: %r"); prefer pgettext_iface()/pgettext_tip() for those.

Note

Returns msgid unchanged when i18n is disabled in the Blender build.

Parameters :

- msgid ( str ) – The text to translate.

- msgctxt ( str | None ) – The context for the translation (defaults to `BLT_I18NCONTEXT_DEFAULT`).

Returns :

The translated version (or msgid if unavailable).

Return type :

str

[Related references](INDEX.md).
