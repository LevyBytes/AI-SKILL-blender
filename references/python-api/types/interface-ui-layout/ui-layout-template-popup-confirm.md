# bpy.types.UILayout: template_popup_confirm ( operator , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , cancel_text = '' , cancel_default = False )

template_popup_confirm ( operator , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , cancel_text = '' , cancel_default = False )

Adds confirm and cancel buttons to a popup; clicking either one dismisses the popup.

Parameters :

- operator ( str ) – Identifier of the operator (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- cancel_text ( str ) – Optional text to use for the cancel, not shown when an empty string (optional, never None)

- cancel_default ( bool ) – Cancel button by default (optional)

Returns :

Operator properties to fill in

Return type :

OperatorProperties

[Related references](INDEX.md).
