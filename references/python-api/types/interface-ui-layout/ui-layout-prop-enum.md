# bpy.types.UILayout: prop_enum ( data , property , value , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' )

prop_enum ( data , property , value , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' )

prop_enum

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- value ( str ) – Enum property value (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

[Related references](INDEX.md).
