# bpy.utils: bpy.utils. extension_path_user ( package , * , path = '' , create = False )

bpy.utils. extension_path_user ( package , * , path = '' , create = False ) 

Give back a user-writable directory tied to an extension.

Note

This gives every extension its own user directory for storing files.

Storing files in the extension's own location is unsuitable, since that location
is wiped on each upgrade and users may lack write access
to the repository (usually a "System" repository).

Parameters :

- package ( str ) – The __package__ of the extension.

- path ( str ) – Optional subdirectory.

- create ( bool ) – Treat the path as a directory and create it if its not existing.

Returns :

a path.

Return type :

str

[Related references](INDEX.md).
