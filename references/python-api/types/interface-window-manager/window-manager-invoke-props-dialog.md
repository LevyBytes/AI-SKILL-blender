# bpy.types.WindowManager: classmethod invoke_props_dialog ( operator , * , width = 300 , title = '' , confirm_text = '' , cancel_default = False , text_ctxt = '' , translate = True )

classmethod invoke_props_dialog ( operator , * , width = 300 , title = '' , confirm_text = '' , cancel_default = False , text_ctxt = '' , translate = True )

Operator dialog (non-autoexec popup) invoke (show operator properties and only execute it on click on OK button)

Parameters :

- operator (Operator) – Operator to call

- width ( int ) – Width of the popup (in [0, inf], optional)

- title ( str ) – Title, Optional text to show as title of the popup (optional, never None)

- confirm_text ( str ) – Confirm Text, Optional text to show instead to the default "OK" confirmation button text (optional, never None)

- cancel_default ( bool ) – cancel_default, (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

Returns :

result

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
