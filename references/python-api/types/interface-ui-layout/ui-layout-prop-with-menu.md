# bpy.types.UILayout: prop_with_menu ( data , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , icon_only = False , menu )

prop_with_menu ( data , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , icon_only = False , menu )

prop_with_menu

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- icon_only ( bool ) – Draw only icons in tabs, no text (optional)

- menu ( str ) – Identifier of the menu (never None)

[Related references](INDEX.md).
