# bpy.types.bpy_struct: is_property_set ( property , / , * , ghost = True )

is_property_set ( property , / , * , ghost = True )

Reports whether a property has been set; handy for inspecting operator properties.

Parameters :

- property ( str ) – Property name.

- ghost ( bool ) – Used for operators that re-run with previous settings.
In this case the property is not marked as set,
yet the value from the previous execution is used.

In rare cases you may want to set this option to false.

Returns :

True when the property has been set.

Return type :

bool

Note

Run-time properties keep their values as custom-properties.

The check here is whether that backing data exists, which is what makes the property count as set .

Operators commonly compute a value for properties
the caller never explicitly assigned
(the caller being a key-binding, menu item, or Python script, for instance).

When operators run more than once, prior-execution values get reused.

For instance, subdividing a mesh with a smooth value of 1.0 keeps reusing
that figure on later subdivision calls, unless you invoke the operator with
a different value for that property.

Declaring the property with the `SKIP_SAVE` option turns this behavior off (see: bpy.props).

The ghost argument lets you detect how a previous-execution value is being treated.

- When true: The property is considered unset even if the value from a previous call is used.

- When false: The existence of any values causes is_property_set to return true.

While this argument should typically be omitted, there are times when
it's important to know if a value is anything besides the default.

For example, the previous value may have been scaled by the scene's unit scale.
In this case scaling the value multiple times would cause problems, so the ghost argument should be false.

[Related references](INDEX.md).
