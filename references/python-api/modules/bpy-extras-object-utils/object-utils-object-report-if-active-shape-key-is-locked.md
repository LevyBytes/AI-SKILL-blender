# bpy_extras.object_utils: bpy_extras.object_utils. object_report_if_active_shape_key_is_locked ( obj , operator )

bpy_extras.object_utils. object_report_if_active_shape_key_is_locked ( obj , operator ) 

Tests whether the given object's active shape key is locked and reports an error when it is.

When the object carries no shape keys there is nothing to lock, so the function returns False.

Parameters :

- obj (bpy.types.Object) – Object to check.

- operator (bpy.types.Operator | None) – Currently running operator to report the error through. Use None to suppress emitting the message.

Returns :

True if the shape key was locked.

Return type :

bool

[Related references](INDEX.md).
