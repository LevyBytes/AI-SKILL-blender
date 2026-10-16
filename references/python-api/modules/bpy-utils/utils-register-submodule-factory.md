# bpy.utils: bpy.utils. register_submodule_factory ( module_name , submodule_names )

bpy.utils. register_submodule_factory ( module_name , submodule_names ) 

Convenience helper that builds register and unregister functions
which simply import submodules
and call their register & unregister functions.

Note

Modules register in the order listed
and unregister in the reverse order.

Parameters :

- module_name ( str ) – The module name, typically __name__ .

- submodule_names ( list [ str ] ) – List of submodule names to load and unload.

Returns :

register and unregister functions.

Return type :

tuple[Callable[[], None], Callable[[], None]]

[Related references](INDEX.md).
