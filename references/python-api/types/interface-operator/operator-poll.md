# bpy.types.Operator: poll, poll_message_set

classmethod poll ( context ) 

Check whether the operator is allowed to run

Parameters :

context (Context) – (never None)

Return type :

bool
classmethod poll_message_set ( message , * args ) 

Define the message displayed in the tool-tip when poll fails.

Should message be callable, any extra user-supplied positional arguments are forwarded to the message function.

Parameters :

- message ( str | Callable [ ... , str | None ] ) – The message or a function that returns the message.

- args ( Any ) – A sequence of arguments to pass to message , if it’s a callable, otherwise argument is not available.

[Related references](INDEX.md).
