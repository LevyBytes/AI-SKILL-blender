# bpy.types.UILayout: operator ( operator , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , emboss = True , depress = False , icon_value = 0 , search_weight = 0.0 )

operator ( operator , * , text = '' , text_ctxt = '' , translate = True , icon = 'NONE' , emboss = True , depress = False , icon_value = 0 , search_weight = 0.0 )

Item. Adds a button to the layout that triggers an Operator when clicked.

Parameters :

- operator ( str ) – Identifier of the operator (never None)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- icon (Literal[Icon Items]) – Icon, Override automatic icon of the item (optional)

- emboss ( bool ) – Draw the button itself, not just the icon/text (optional)

- depress ( bool ) – Draw pressed in (optional)

- icon_value ( int ) – Icon Value, Override automatic icon of the item (in [0, inf], optional)

- search_weight ( float ) – Search Weight, Influences the sorting when using menu-seach (in [-inf, inf], optional)

Returns :

Operator properties to fill in

Return type :

OperatorProperties

[Related references](INDEX.md).
