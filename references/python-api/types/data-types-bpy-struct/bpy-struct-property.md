# bpy.types.bpy_struct: property_overridable_library_set, property_unset

property_overridable_library_set ( property , overridable , / )

Marks a property as overridable or not (custom properties only!).

Parameters :

- property ( str ) – Property name.

- overridable ( bool ) – Overridable status to set.

Returns :

True when the overridable status of the property was successfully set.

Return type :

bool
property_unset ( property , / )

Clears a property so it reverts to its default value.

Parameters :

property ( str ) – Property name.

[Related references](INDEX.md).
