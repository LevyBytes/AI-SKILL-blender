# bpy.types.WindowManager: classmethod invoke_confirm ( operator , event , * , title = '' , message = '' , confirm_text = '' , icon = 'NONE' , text_ctxt = '' , translate = True )

classmethod invoke_confirm ( operator , event , * , title = '' , message = '' , confirm_text = '' , icon = 'NONE' , text_ctxt = '' , translate = True )

Operator confirmation popup (only to let user confirm the execution, no operator properties shown)

Parameters :

- operator (Operator) – Operator to call

- event (Event) – Event

- title ( str ) – Title, Optional text to show as title of the popup (optional, never None)

- message ( str ) – Message, Optional first line of content text (optional, never None)

- confirm_text ( str ) – Confirm Text, Optional text to show instead to the default "OK" confirmation button text (optional, never None)

- icon ( Literal [ 'NONE' , 'WARNING' , 'QUESTION' , 'ERROR' , 'INFO' ] ) – Icon, Optional icon displayed in the dialog (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

Returns :

result

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
