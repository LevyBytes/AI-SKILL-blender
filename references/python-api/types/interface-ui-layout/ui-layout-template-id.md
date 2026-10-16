# bpy.types.UILayout: template_ID ( data , property , * , new = '' , open = '' , unlink = '' , filter = 'ALL' , live_icon = False , text = '' , text_ctxt = '' , translate = True )

template_ID ( data , property , * , new = '' , open = '' , unlink = '' , filter = 'ALL' , live_icon = False , text = '' , text_ctxt = '' , translate = True )

template_ID

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- new ( str ) – Operator identifier to create a new ID block (optional, never None)

- open ( str ) – Operator identifier to open a file for creating a new ID block (optional, never None)

- unlink ( str ) – Operator identifier to unlink the ID block (optional, never None)

- filter ( Literal [ 'ALL' , 'AVAILABLE' ] ) – Optionally limit the items which can be selected (optional)

- live_icon ( bool ) – Show preview instead of fixed icon (optional)

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

[Related references](INDEX.md).
