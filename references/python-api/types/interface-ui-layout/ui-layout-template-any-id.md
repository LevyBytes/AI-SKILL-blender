# bpy.types.UILayout: template_any_ID ( data , property , type_property , * , text = '' , text_ctxt = '' , translate = True )

template_any_ID ( data , property , type_property , * , text = '' , text_ctxt = '' , translate = True )

template_any_ID

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- type_property ( str ) – Identifier of property in data giving the type of the ID-blocks to use (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

[Related references](INDEX.md).
