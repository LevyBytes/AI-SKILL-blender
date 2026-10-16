# bpy.types.PoseBone: bl_system_properties_get, bl_rna_get_subclass, bl_rna_get_subclass_py

bl_system_properties_get ( * , do_create = False )

DEBUG ONLY. A back door into runtime-defined RNA data storage meant only for tests and debugging. Leave it alone in normal scripting, and never count on its contents being writable

Parameters :

do_create ( bool ) – Force the system properties into existence when they are not present (optional)

Returns :

The root container holding the system properties, or None when none are stored on this data yet and creating them was not asked for

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
