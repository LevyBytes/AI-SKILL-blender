# bpy.types.UILayout: template_action ( id , * , new = '' , unlink = '' , text = '' , text_ctxt = '' , translate = True )

template_action ( id , * , new = '' , unlink = '' , text = '' , text_ctxt = '' , translate = True )

template_action

Parameters :

- id (ID) – The data-block for which to select an Action (never None)

- new ( str ) – Operator identifier to create a new ID block (optional, never None)

- unlink ( str ) – Operator identifier to unlink the ID block (optional, never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

[Related references](INDEX.md).
