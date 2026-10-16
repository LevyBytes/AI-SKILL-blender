# bpy.types.FCurve: update, update_autoflags

update ( )

Ensure keyframes are sorted in chronological order and handles are set correctly
update_autoflags ( data )

Refresh the FCurve flags that are derived automatically from the property it drives (for instance, the integer/discrete flags raised when that property is not a float)

Parameters :

data (AnyType) – Data, Data containing the property controlled by given FCurve (never None)

[Related references](INDEX.md).
