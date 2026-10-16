# bpy_extras.io_utils.ImportHelper

class bpy_extras.io_utils. ImportHelper
check ( _context ) 

Confirm the axis conversion settings are valid.

Returns :

True when a property was updated.

Return type :

bool
invoke ( context , _event ) 

Open the file selector for import.

Parameters :

context (bpy.types.Context) – The context.

Returns :

The operator return value.

Return type :

set[str]
invoke_popup ( context , confirm_text = '' ) 

Bring up a popup confirmation dialog when a filepath is already set;
otherwise drop back to the file selector.

Parameters :

- context (bpy.types.Context) – The context.

- confirm_text ( str ) – Label for the confirm button,
defaults to the operator label.

Returns :

The operator return value.

Return type :

set[str]

[Related references](INDEX.md).
