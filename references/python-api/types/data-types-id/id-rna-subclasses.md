# bpy.types.ID: bl_system_properties_get, bl_rna_get_subclass, bl_rna_get_subclass_py

bl_system_properties_get ( * , do_create = False )

DEBUG ONLY. A back door into runtime-defined RNA storage meant purely for tests and debugging. Steer clear of it in normal scripts, and never count on the contents being writable.

Parameters :

do_create ( bool ) – Ensure that system properties are created if they do not exist yet (optional)

Returns :

The root container for system properties, or None when this data holds none yet and you did not ask for them to be created

Return type :

PropertyGroup
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
