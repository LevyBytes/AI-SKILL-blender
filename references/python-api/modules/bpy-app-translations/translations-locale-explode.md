# bpy.app.translations: bpy.app.translations. locale_explode ( locale )

bpy.app.translations. locale_explode ( locale )

Breaks down an ISO locale code into its individual parts and all intermediate combinations.

```pycon
>>> bpy.app.translations.locale_explode("sr_RS@latin")
("sr", "RS", "latin", "sr_RS", "sr@latin")
```

For incomplete locale codes, absent elements appear as None.

Parameters :

locale ( str ) – The ISO locale string to break down.

Returns :

A tuple (language, country, variant, language_country, language@variant) .

Return type :

tuple[str | None, str | None, str | None, str | None, str | None]

[Related references](INDEX.md).
