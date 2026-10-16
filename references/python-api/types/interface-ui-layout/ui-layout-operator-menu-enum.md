# bpy.types.UILayout: operator_menu_enum ( operator , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' )

operator_menu_enum ( operator , property , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' )

operator_menu_enum

Parameters :

- operator ( str ) – Identifier of the operator (never None)

- property ( str ) – Identifier of property in operator (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

Returns :

Operator properties to fill in

Return type :

OperatorProperties

[Related references](INDEX.md).
