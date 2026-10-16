# bpy.types.UILayout: template_path_builder ( data , property , root , * , text = '' , text_ctxt = '' , translate = True )

template_path_builder ( data , property , root , * , text = '' , text_ctxt = '' , translate = True )

template_path_builder

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- root (ID) – ID-block from which path is evaluated from

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

[Related references](INDEX.md).
