# bpy.utils: bpy.utils. register_cli_command ( id , execute )

bpy.utils. register_cli_command ( id , execute ) 

Add a command that can be reached through the ( -c / --command ) command-line argument.

Parameters :

- id ( str ) – The command identifier (must pass an str.isidentifier check).

Should that id already exist, Blender warns and leaves the command unreachable, guarding against firing the wrong one by mistake.

- execute ( Callable [ [ list [ str ] ] , int ] ) – Callback, taking a single list of strings and returns an int.
Its arguments come from every command-line token that trails the command id.
A return of 0 means success and 1 means failure, though the os module's specific error codes are usable too.

Returns :

The command handle which can be passed to unregister_cli_command().

The implementation relies on Python's capsule type, but treat the result purely as an opaque token for later unregistering.

Return type :

Any

Custom Commands

Through registered commands you can readily surface command-line
features as commands invoked via ( -c / --command ).

[Related references](INDEX.md).
