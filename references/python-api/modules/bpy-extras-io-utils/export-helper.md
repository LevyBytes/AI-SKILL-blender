# bpy_extras.io_utils.ExportHelper

class bpy_extras.io_utils. ExportHelper
check ( _context ) 

Confirm the filepath and axis conversion settings are valid.

Returns :

True when a property was updated.

Return type :

bool
invoke ( context , _event ) 

Open the file selector for export, seeding a default filepath
from the name of the current blend file.

Parameters :

context (bpy.types.Context) – The context.

Returns :

The operator return value.

Return type :

set[str]

[Related references](INDEX.md).
